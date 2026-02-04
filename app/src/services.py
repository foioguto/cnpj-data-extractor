import httpx
import re
from typing import Dict, Any
from .models import EmpresaResponse

class CNPJService:
    BASE_URL = "https://brasilapi.com.br/api/cnpj/v1"

    @staticmethod
    def _clean_cnpj(cnpj_raw: str) -> str:
        """Removes non-numeric characters."""
        return re.sub(r'\D', '', cnpj_raw)

    def fetch_company_data(self, cnpj: str) -> Dict[str, Any]:
        cleaned_cnpj = self._clean_cnpj(cnpj)
        
        # Using context manager for safe connection closing
        with httpx.Client(timeout=10.0) as client:
            try:
                response = client.get(f"{self.BASE_URL}/{cleaned_cnpj}")
                response.raise_for_status() # Raises error for 4xx or 5xx
                
                # Validates with Pydantic and dumps to dict for Excel writing
                return EmpresaResponse(**response.json()).model_dump()
                
            except httpx.HTTPStatusError as e:
                # Returns error details to be written in Excel instead of crashing
                return {
                    "razao_social": f"API ERROR: {e.response.status_code}",
                    "descricao_situacao_cadastral": "Failed Request",
                    "uf": "-"
                }
            except Exception as e:
                return {
                    "razao_social": f"SYSTEM ERROR: {str(e)}",
                    "descricao_situacao_cadastral": "Critical Failure",
                    "uf": "-"
                }
