from fastapi import APIRouter, UploadFile, File
from typing import List
from Controllers.public_controllers import (
    post_data,
    create_json_to_csv,
    create_to_wordCloud,
    get_data_json,
)

public_router = APIRouter()


# Esta ruta se encarga de recibir un archivo y convertirlo a json
@public_router.post("/upload/{id}")
async def postData(id: str, files: List[UploadFile] = File(...)):
    return await post_data(id, files)

# Esta ruta se encarga de recibir un id y devolver el json correspondiente
@public_router.get("/get-data/{id}")
async def getDataJson(id: str):
    return get_data_json(id)


# este ruta se encarga de recibir la ruta de un archivo json y convertirlo a csv
# recibe el dato por query
@public_router.get("/download/")
async def getData(id:str,path: str):
    return create_json_to_csv(id,path)


# esta ruta encarga de crear un wordcloud a partir de un archivo json
# recibe el dato por query la cual es el path del archivo
@public_router.get("/create-wordCloud/")
async def getData(id:str,path: str):
    return create_to_wordCloud(id,path)
