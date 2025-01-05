from typing import Optional

from pydantic_settings import BaseSettings

class CommonConfigs(BaseSettings):
    service_name: str = None
    service_port: int = None
    service_id: str = None
    service_hostname: str = '127.0.0.1'
    service_host: str = None

    consul_host: str = '127.0.0.1'
    consul_port: int = 8888

#     db
    POSTGRES_HOST: str = None
    POSTGRES_USER: str = None
    POSTGRES_PORT: int = None
    POSTGRES_PASSWORD: str = None
    POSTGRES_DB: str = None
    DB_ALEMBIC_URL: str = None

    @property
    def database_url(self) -> Optional[str]:
        """Construct the database URL if all required fields are present."""
        required_fields = [
            self.POSTGRES_USER,
            self.POSTGRES_PASSWORD,
            self.POSTGRES_HOST,
            self.POSTGRES_PORT,
            self.POSTGRES_DB
        ]
        if all(required_fields):
            return (
                f"postgresql+asyncpg://{self.POSTGRES_USER}:"
                f"{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:"
                f"{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
            )
        return None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


configs = CommonConfigs()