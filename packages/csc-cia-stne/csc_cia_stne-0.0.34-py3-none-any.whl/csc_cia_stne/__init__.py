import os
from dotenv import load_dotenv
from .logger_json import get_logger as get_logger_json
from .logger_rich import get_logger as get_logger_rich
from .karavela import Karavela
from .servicenow import ServiceNow
from .stne_admin import StoneAdmin
from .bc_sta import BC_STA
from .bc_correios import BC_Correios
from .gcp_bigquery import BigQuery
from .email import Email
from .provio import Provio

# Define os itens disponíveis para importação
__all__ = [
    "Karavela",
    "BigQuery",
    "BC_Correios",
    "BC_STA",
    "StoneAdmin",
    "ServiceNow",
    "Util",
    "logger",
    "Provio",
    "Email"
]

_diretorio_inicial = os.getcwd()
_caminho_env = os.path.join(_diretorio_inicial, ".env")

# Carrega .env
load_dotenv(_caminho_env)
logger = None  # Inicializa como None

def _running_in_container():

    if os.environ.get("KUBERNETES_SERVICE_HOST") or os.path.exists("/.dockerenv"):
        
        return True
    
    try:
    
        with open("/proc/1/cgroup", "rt") as file:
    
            for line in file:
    
                if "docker" in line or "kubepods" in line:
    
                    return True
    
    except FileNotFoundError as e:
    
        return False
    
    return False
    
def logger():
    
    if os.getenv('ambiente_de_execucao') is not None and os.getenv('ambiente_de_execucao') == "karavela":
        
        return get_logger_json()
    
    elif _running_in_container():
        
        return get_logger_json()
    
    else:
        
        return get_logger_rich()
