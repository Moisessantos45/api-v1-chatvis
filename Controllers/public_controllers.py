import os
import json
from fastapi.responses import JSONResponse, FileResponse
from Utils.generte_uudi import generate_id
from Utils.procesar_files import procesar_files
from Utils.deletesFiles import deleteFile
from Utils.create_csv import create_csv
from Services.processs_word import process_messages


async def processFiles(files, id):
    list_files = []
    dir_upload = f"uploads/{id}"
    uploads_dir = os.path.join(os.path.dirname(__file__), "../", dir_upload)
    os.makedirs(uploads_dir, exist_ok=True)

    for file in files:
        new_file_name = (
            file.filename.replace("Chat de WhatsApp con ", "")
            .replace(".txt", "")
            .replace(" ", "_")
        )
        fileName = f"{new_file_name}__" + generate_id() + ".txt"
        file_path = os.path.join(uploads_dir, fileName)
        list_files.append(file_path)
        with open(file_path, "wb") as f:
            f.write(await file.read())
    return list_files


def get_data_json(id):

    dir_upload = f"uploads/{id}"
    uploads_dir = os.path.join(os.path.dirname(__file__), "../", dir_upload)
    try:
        objetos_json = []

        for files in os.listdir(uploads_dir):
            if files.endswith(".json"):
                path = os.path.join(uploads_dir, files)

                with open(path, "r", encoding="utf-8") as archivo:
                    contenido_json = json.load(archivo)

                objectJson = {"path": files, "data": contenido_json}

                objetos_json.append(objectJson)
        return JSONResponse(
            content={"data": objetos_json},
            status_code=200,
        )
    except Exception as e:
        return JSONResponse(
            content={"message": "Error al obtener el archivo json"},
            status_code=500,
        )


async def post_data(id, files):
    try:
        file_path = await processFiles(files, id)
        list_files = []
        for file_path in file_path:
            procesesDta = procesar_files(file_path)
            list_files.append(procesesDta)
            deleteFile(file_path)

        return JSONResponse(
            content={"data": list_files},
            status_code=200,
        )
    except Exception as e:
        return JSONResponse(
            content={"message": "Error al procesar los archivos"},
            status_code=500,
        )


def create_to_wordCloud(id, file_path):
    try:
        carpeta_uploads = os.path.join(os.path.dirname(__file__), "../uploads", id)
        print(carpeta_uploads)
        ruta_completa = os.path.join(carpeta_uploads, file_path)

        word_keys = process_messages(ruta_completa)

        return JSONResponse(
            content={"data": word_keys},
            status_code=200,
        )
    except Exception as e:
        return JSONResponse(
            content={"message": "Error al crear el archivo wordCloud"},
            status_code=500,
        )


def create_json_to_csv(id,file_path):
    try:
        carpeta_uploads = os.path.join(os.path.dirname(__file__), "../uploads",id)
        # print(carpeta_uploads)
        ruta_completa = os.path.join(carpeta_uploads, file_path)
        path_csv = create_csv(ruta_completa, file_path)
        
        return FileResponse(path_csv, media_type="text/csv")
    except Exception as e:
        return JSONResponse(
            content={"message": "Error al crear el archivo csv"},
            status_code=500,
        )
