from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()
@dataclass(frozen=True)
class Config:
    file_name: str
    cnpj_column: str
    start_row: int
    fields_map: list[str]
    columns: list[int]


def get_env_or_fail(key: str) -> str:
    value = os.getenv(key)
    if value is None:
        raise RuntimeError(f"Missing environment variable: {key}")
    return value


config = Config(
    file_name = get_env_or_fail('FILE_NAME'),

    cnpj_column = get_env_or_fail('CNPJ_COLUMN'),

    start_row = int(get_env_or_fail('START_ROW')),

    fields_map = get_env_or_fail('FIELDS_MAP').split(","),

    columns = [int(x) for x in get_env_or_fail('COLUMNS').split(",")]
)
