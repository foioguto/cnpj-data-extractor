from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    file_name: str
    cnpj_column: str
    start_row: int
    fields_map: list[str]
    columns: list[int]


config = Config(
    file_name="dados.xlsx",

    cnpj_column="A",

    start_row=2,

    fields_map = ["razao_social", "descricao_situacao_cadastral", "uf"],

    columns = [1, 1, 1, 1]
)
