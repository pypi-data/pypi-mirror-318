"""cenclave.core.test_docker module."""

from pathlib import Path
from typing import ClassVar, Dict, List, Optional, Tuple

from pydantic import BaseModel


class TestDockerConfig(BaseModel):
    """Definition of a running test docker configuration."""

    port: int
    code: Path
    application: str
    sealed_secrets: Optional[Path]
    secrets: Optional[Path]
    simu_enclave_sk: Optional[Path]

    secret_mountpoint: ClassVar[str] = "/root/.cache/cenclave/secrets.json"
    sealed_secrets_mountpoint: ClassVar[str] = (
        "/root/.cache/cenclave/sealed_secrets.json"
    )
    enclave_sk_mountpoint: ClassVar[str] = "/key/enclave.key"

    code_mountpoint: ClassVar[str] = "/app"
    entrypoint: ClassVar[str] = "cenclave-test"

    def cmd(self) -> List[str]:
        """Serialize the docker command args."""
        return ["--application", self.application, "--debug"]

    def ports(self) -> Dict[str, Tuple[str, str]]:
        """Define the docker ports."""
        return {f"{self.port}/tcp": ("127.0.0.1", str(self.port))}

    def volumes(self) -> Dict[str, Dict[str, str]]:
        """Define the docker volumes."""
        v = {
            f"{self.code.resolve()}": {
                "bind": TestDockerConfig.code_mountpoint,
                "mode": "rw",
            },
        }

        if self.secrets:
            v[f"{self.secrets.resolve()}"] = {
                "bind": TestDockerConfig.secret_mountpoint,
                "mode": "rw",
            }

        if self.sealed_secrets:
            v[f"{self.sealed_secrets.resolve()}"] = {
                "bind": TestDockerConfig.sealed_secrets_mountpoint,
                "mode": "rw",
            }

        if self.simu_enclave_sk:
            v[f"{self.simu_enclave_sk.resolve()}"] = {
                "bind": TestDockerConfig.enclave_sk_mountpoint,
                "mode": "rw",
            }

        return v
