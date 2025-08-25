from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile 
from os import path

#Despues de descargar un token de Kaggle y colocarlo en:
# C:/Users/moscu/.kaggle/kaggle.json
#Verificamos lo anterior
dir_crede = path.expanduser("~")
#print(dir_crede)
dir_crede = path.join(dir_crede,".kaggle", "kaggle.json")
# print(dir_crede)
if not path.exists(dir_crede):
    raise FileNotFoundError("No se encontraron las credenciales de Kaggle")
#Inicializamos nuestro enlace con la API
api = KaggleApi()
api.authenticate()
print("Autenticado!")
#Verificamos nombres
name_dataset = "sheemazain/video-game-sales-by-sheema-zain"
#files = api.dataset_list_files(dataset).files
#for f in files:
#    print(f.name)
#Descargamos nuestro dataset con datos obtenidos de antemano
dir_actual = path.dirname(path.abspath(__file__))
api.dataset_download_file(
    dataset = name_dataset,# la URL despues de ".../datasets/"
    file_name = "vgsales (1).csv",#Nombre del archivo
    path = dir_actual #Direccion de este script
)

