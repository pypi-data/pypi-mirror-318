from pydantic_settings import BaseSettings

class CommonConfigs(BaseSettings):
    service_name: str
    service_port: int
    service_id: str
    service_hostname: str = '127.0.0.1'
    service_host: str

    consul_host: str = '127.0.0.1'
    consul_port: int = 8888

#     db
    POSTGRES_HOST: str
    POSTGRES_USER: str
    POSTGRES_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DB_ALEMBIC_URL: str

    @property
    def database_url(self):
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


configs = CommonConfigs()