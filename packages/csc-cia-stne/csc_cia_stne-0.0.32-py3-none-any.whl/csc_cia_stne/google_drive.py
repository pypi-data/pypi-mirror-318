import os, time, logging, json
from .karavela import Karavela
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError
from io import BytesIO
from googleapiclient.discovery import build
from google.oauth2 import service_account
from .utilitarios.validations.GoogleDriveValidator import InitParamsValidator, CreateFolderValidator, ListFolderValidator
from pydantic import ValidationError



class GoogleDrive():
    
    """
        Classe responsável por gerenciar operações no Google Drive, como upload de arquivos, criação de pastas
        e listagem de conteúdo. Utiliza a API do Google Drive para realizar essas operações.

        Args:
            key (str): Chave de autenticação para acessar a API do Google Drive.
    """
    
    def __init__(self, key, with_subject : str, scopes : list = ["https://www.googleapis.com/auth/drive"], version : str = "v3"):
        """
            Inicializa a classe GoogleDrive e autentica o serviço usando a chave fornecida.

            Args:
                key (str): Chave de autenticação do Google Drive.
        """
        try:
            InitParamsValidator(key=key, with_subject=with_subject, scopes=scopes)
        except ValidationError as e:
            raise ValueError("Erro na validação dos dados de input da inicialização da instância:", e.errors())

        self.__token = json.loads(Karavela.get_secret(key))
        self.version = version
        self.scopes = scopes
        self.__auth = self.__autentica(with_subject)
        self.page_size = 1000
        self.service = self.create_service()

    def timer_decorator(func):
        """
            Classe reponsável por calcular qualquer execução que ela seja chamada.        
        """
        def wrapper(*args, **kwargs):
            inicio = time.time()
            resultado = func(*args, **kwargs)
            fim = time.time()
            logging.debug(f"Tempo de execução de {func.__name__}: {fim - inicio:.2f} segundos")
            return resultado
        return wrapper
    
    def create_service(self):
        """
            Cria um serviço para a plataforma Google especificada.

            Args:
                platform (str): O nome da plataforma Google para a qual o serviço será criado (por exemplo, 'drive', 'sheets').

            Returns:
                googleapiclient.discovery.Resource: Serviço do Google para a plataforma especificada.
                bool: Retorna False se houver um erro ao criar o serviço.
        """
        try:
            
            cred = build(f"drive", f"{self.version}", credentials=self.__auth)
            logging.debug(f"Serviço do Google drive criado")
            return cred
        except Exception as e:
            logging.debug(f"Erro ao criar o serviço do Google drive: Error: {e}")
            return False
    
    def __autentica(self, with_subject : str):
        """
            Autentica o serviço do Google utilizando um token e escopos fornecidos.

            Args:
                token (dict): As credenciais de autenticação.
                scopes (list): A lista de escopos para o acesso aos serviços do Google.

            Returns:
                google.oauth2.service_account.Credentials: Objeto de credenciais autenticado.
                bool: Retorna False em caso de erro.
        """

        try:
            credentials = service_account.Credentials.from_service_account_info(self.__token, scopes=self.scopes)
            delegated_credencial = credentials.with_subject(with_subject)
            return delegated_credencial

        except Exception as e:
            logging.debug(f"Erro ao tentar autenticar. Verifique o erro: {e}")
            return False

    @timer_decorator
    def upload(self, folder_id: str, name: str, file_path: str, mimetype: str):
        """
            Faz o upload de um arquivo para o Google Drive em uma pasta especificada.

            Args:
                folder_id (str): ID da pasta no Google Drive onde o arquivo será armazenado.
                name (str): Nome do arquivo que será carregado.
                file_path (str): Caminho completo do arquivo no sistema local.
                mimetype (str): Tipo MIME do arquivo a ser carregado.

            Returns:
                dict: Informações sobre o arquivo carregado, incluindo o ID do arquivo.
                None: Caso o caminho do arquivo não seja encontrado.
        """
        file_metadata = {"name": name, "parents": [folder_id]}
        if not os.path.exists(file_path):
            logging.debug(f"Pasta {file_path} não encontrada")           
            return {"success" : False, "result" : None, "error" : "Diretório ou arquivo não encontrado"}
        
        try:
            logging.debug(f"Realizando o upload do arquivo")
            media = MediaFileUpload(file_path, mimetype=mimetype, resumable=True)
            file = (
                self.service.files()
                .create(body=file_metadata, media_body=media, fields="id", supportsAllDrives=True)
                .execute()
            )

            logging.debug(f"Upload realizado com sucesso")
            return {"success" : True, "result" : file}
        except Exception as e:
            logging.debug(f"Erro ao realizar o upload do arquivo {name} no google drive. Erro: {e}")
            return {"success" : False, "result" : None, "error" : str(e)}
   
    def create_folder(self, name: str, parent_folder_id: str):
        """
            Cria uma pasta no Google Drive dentro de uma pasta existente.

            Args:
                name (str): Nome da pasta a ser criada.
                parent_folder_id (int): ID da pasta pai onde a nova pasta será criada.

            Returns:
                str: ID da pasta criada.
        """
        try:
            CreateFolderValidator(name=name, parent_folder_id=parent_folder_id)
        except ValidationError as e:
            raise ValueError("Erro na validação dos dados de input da inicialização da instância:", e.errors())
            
        try:
            folder_metadata = {
                "name": name,
                "parents": [parent_folder_id],
                "mimeType": "application/vnd.google-apps.folder",
            }
            folder = (
                self.service.files().create(body=folder_metadata, fields="id", supportsAllDrives=True).execute()
            )
            return {"success" : True, "result": folder}
        except Exception as e:
            logging.debug(f"Não foi possível criar a pasta {name}")
            return {"success" : False, "result": None, "error" : str(e)}
    
    def list(self, query: str = "", spaces: str = "drive", fields: str = "nextPageToken, files(id, name)"):
        """
            Lista os arquivos e pastas no Google Drive com base nos critérios fornecidos.

            Args:
                query (str, optional): Critério de busca para os arquivos ou pastas no Google Drive. 
                                    Consulte https://developers.google.com/drive/api/v3/ref-search-terms.
                                    Defaults to "".
                spaces (str, optional): Especifica os locais de armazenamento a serem consultados. Pode ser 'drive', 
                                        'appDataFolder', ou 'photos'. Defaults to 'drive'.
                fields (str, optional): Campos a serem retornados na resposta. Consulte a documentação para os campos disponíveis.
                                        Defaults to "nextPageToken, files(id, name)".

            Returns:
                dict: Dicionário contendo o resultado da busca.
        """
        try:
            ListFolderValidator(query=query, fields=fields, spaces=spaces)
        except ValidationError as e:
            raise ValueError("Erro na validação dos dados de input da lista:", e.errors())
        try: 
            results = (
                self.service.files()
                .list(q=query,
                      spaces=spaces,
                      pageSize=self.page_size,
                      fields=fields,
                      supportsAllDrives=True,
                      includeItemsFromAllDrives=True)
                .execute()
            )
            return {"success" : True, "result" : results}
        except HttpError as hr:
            logging.debug(f"Ocorreu um de http. Erro: {hr}")
            return {"success" : False, "result" : None, "error" : str(hr)}
    
    @timer_decorator
    def get_file(self, file : str, ):
        """
            Obtém o conteúdo de um arquivo armazenado no Google Drive.

            Esta função acessa o Google Drive usando a API e lê os dados do arquivo especificado, retornando-os como um objeto binário de memória (`BytesIO`).

            Parâmetros:
                - file (str): Dicionário contendo informações do arquivo no Google Drive, incluindo as chaves:
                    - `"name"`: Nome do arquivo.
                    - `"id"`: ID do arquivo.

            Retorna:
                - BytesIO: Objeto em memória contendo os dados do arquivo.
                - None: Caso ocorra um erro ao tentar abrir ou ler o arquivo.

            Logs:
                - Registra mensagens indicando o início e o término da leitura do arquivo.
                - Em caso de falha, registra o erro ocorrido.

            Exceções:
                - Qualquer erro durante o processo será capturado e registrado no log. A função retornará `None` nesses casos.

            Dependências:
                - A função assume a existência de um atributo `self.service` configurado para interagir com a API do Google Drive.
        """
        try:
            # file_metadata = self.service.files().get(fileId=file_id, fields="name, mimeType").execute()
            logging.debug(f"Lendo o arquivo {file.get("name")}")
            request = self.service.files().get_media(fileId=file.get("id"))
            file_data = BytesIO(request.execute())
            logging.debug("Leitura do arquivo finalizada")

            return {"success" : True, "result" : file_data}
    
        except Exception as e:
            logging.debug(f"Erro ao tentar abrir o arquivo. Erro {e}")
            return {"success" : False, "result" : None}

        

