from pydantic_settings import BaseSettings

class Conf(BaseSettings):
    DB_URL: str

    class Config:
        env_file = "backend/.env"

conf = Conf()