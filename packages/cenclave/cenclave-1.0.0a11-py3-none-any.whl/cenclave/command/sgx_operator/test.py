"""cenclave.command.sgx_operator.test module."""

import os
import subprocess
import sys
from pathlib import Path

from cenclave.command.helpers import get_client_docker, get_running_app_container
from cenclave.core.bootstrap import is_waiting_for_secrets
from cenclave.core.conf import AppConf, AppConfParsingOption
from cenclave.core.sgx_docker import SgxDockerConfig
from cenclave.error import AppContainerBadState
from cenclave.log import LOGGER as LOG


def add_subparser(subparsers):
    """Define the subcommand."""
    parser = subparsers.add_parser("test", help="Test a deployed web app")

    parser.add_argument(
        "name",
        type=str,
        help="the name of the application",
    )

    parser.add_argument(
        "--test",
        type=Path,
        required=True,
        help="the path of the test directory extracted from the tarball package",
    )

    parser.add_argument(
        "--config",
        type=Path,
        required=True,
        help="the conf path extracted from the tarball package",
    )

    parser.set_defaults(func=run)


def run(args) -> None:
    """Run the subcommand."""
    client = get_client_docker()
    container = get_running_app_container(client, args.name)

    docker = SgxDockerConfig.load(container.attrs, container.labels)

    if is_waiting_for_secrets(f"https://{docker.host}:{docker.port}"):
        raise AppContainerBadState(
            "Your application is waiting for secrets and can't be tested right now."
        )

    code_config = AppConf.load(args.config, option=AppConfParsingOption.SkipCloud)

    for package in code_config.tests_requirements:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    try:
        env = dict(os.environ)

        if "TEST_REMOTE_URL" not in os.environ:
            env["TEST_REMOTE_URL"] = f"https://{docker.host}:{docker.port}"

        subprocess.check_call(
            [sys.executable, "-m", code_config.tests_cmd],
            cwd=args.test,
            env=env,
        )

        LOG.info("Tests successful")
    except subprocess.CalledProcessError:
        LOG.error("Tests failed!")
