from pydantic import BaseModel, Field
from typing import Optional

class EmpresaResponse(BaseModel):
    '''
    Docstring for EmpresaResponse

    the blueprint of the json received
    '''

    cnpj: str
    
    razao_social: str 
    
    nome_fantasia: Optional[str] = None 
    
    descricao_situacao_cadastral: str 
    
    uf: str
    