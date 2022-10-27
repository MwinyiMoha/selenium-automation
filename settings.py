from pydantic import BaseSettings

class Settings(BaseSettings):

    base_url: str
    valid_email: str
    valid_password: str
    invalid_email: str
    invalid_password: str
    default_wait_time: int = 30
    ci_env: bool = True

    class Config:
        env_file = ".env"
