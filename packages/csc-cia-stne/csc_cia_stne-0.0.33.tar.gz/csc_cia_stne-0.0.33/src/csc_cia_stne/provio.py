import logging
import requests
from requests.auth import HTTPBasicAuth
from pydantic import BaseModel, Field, ValidationError

# Validadores
class ProvioModel(BaseModel):
    username: str = Field(..., strip_whitespace=True, min_length=1)
    password: str = Field(..., strip_whitespace=True, min_length=1)

class ExportarRelatorioParams(BaseModel):
    ano: int = Field(..., gt=2015, description="O ano deve ser maior que 2015")
    mes: int = Field(..., ge=1, le=12, description="O mês deve estar entre 1 e 12")

# Classe provio
class Provio:
    
    def __init__(self,username:str,password:str):
        
        # Validação usando Pydantic
        data = ProvioModel(username=username, password=password)

        self.api_url = "https://provio.apps.stone.com.br/api/reports"
        self.auth = HTTPBasicAuth(data.username, data.password)

    def exportar_relatorio_geral(self, ano:int, mes:int):
        
        # Validação dos parâmetros
        params = ExportarRelatorioParams(ano=ano, mes=mes)
        periodo = f"{params.ano}-{params.mes:02d}"
        skip = 0
        todos_os_dados = []  # Lista para armazenar todos os resultados
        requisicao = 0
        try:
            
            while True:
            
                url = f"{self.api_url}/general/{periodo}/{skip}"
                response = requests.get(url=url, auth=self.auth)

                if response.status_code == 200:
            
                    dados = response.json()

                    # Verifica se há itens na resposta
                    if not dados:  # Se a resposta for vazia, interrompa o loop
            
                        break

                    # Adiciona os dados recebidos à lista total
                    todos_os_dados.extend(dados)

                    # Incrementa o skip para buscar a próxima página
                    skip += 500
                    requisicao += 1
                    logging.info(f"Exportando relatório: Requisição #{str(requisicao).zfill(3)} - {len(todos_os_dados)} registros exportados")
            
                else:
            
                    return {"success": False, "error": f"{response.status_code} - {response.text}"}

            return {"success": True, "error": None, "report": todos_os_dados}

        except Exception as e:
            
            return {"success": False, "error": str(e)}
