import sys
from pathlib import Path
from functions import Dados, Rede

project_root = Path(__file__).resolve().parent

path_data = project_root / "data"
path_code = project_root / "code"

if str(path_code) not in sys.path:
    sys.path.append(str(path_code))

try:
    
    dados = Dados(path_data=path_data)
    df = dados.processa_dados(2023)
    
    rede_comercial = Rede(df=df)
    rede_comercial.constroi_rede()
    rede_comercial.calcula_estatisticas_rede(10, 10)
    rede_comercial.cria_subredes(10)
    
except ImportError as e:
    print(f"Erro ao importar módulos: {e}")
    print(f"Verifique se o caminho {path_code} contém o arquivo functions.py")
except Exception as e:
    print(f"Ocorreu um erro durante a execução: {e}")