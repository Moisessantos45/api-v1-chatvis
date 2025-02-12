import re
import os
import json
from datetime import datetime

path = os.path.dirname(__file__)
dirP = "casoOne.txt"
pathFile = os.path.join(path, dirP)


def separar_cadena(cadena):

    patron_fecha_hora = (
        r"(\d{1,2}/\d{1,2}/\d{4})\s*(?:,)?\s*(\d{1,2}:\d{2}(?:\s*[ap]\.?\s*m\.?)?)"
    )

    match = re.search(patron_fecha_hora, cadena)
    if not match:
        return None

    fecha, hora = match.groups()

    resto = cadena[match.end() :].strip()

    if ":" in resto:
        nombre, mensaje = resto.split(":", 1)
    elif "-" in resto:
        nombre, mensaje = resto.split("-", 1)
    else:
        return None

    nombre = nombre.strip()
    mensaje = mensaje.strip()

    try:
        fecha_obj = datetime.strptime(fecha, "%d/%m/%Y")
        fecha = fecha_obj.strftime("%d/%m/%Y")
    except ValueError:
        pass

    if "a. m." in hora.lower() or "p. m." in hora.lower():
        hora = hora.lower().replace(".", "").replace(" ", "")
        if "am" in hora:
            hora = hora.replace("am", "a.m.")
        elif "pm" in hora:
            hora = hora.replace("pm", "p.m.")

    return {"fecha": fecha, "hora": hora, "nombre": nombre, "mensaje": mensaje}


def leer_mensajes_de_archivo(nombre_archivo):
    mensajes = []
    mensaje_actual = ""

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

        contenido = re.sub(r"\n{2,}", "\n", contenido)

        for linea in contenido.split("\n"):
            if re.match(r"\d{1,2}/\d{1,2}/\d{4}", linea):
                if mensaje_actual:
                    mensajes.append(mensaje_actual.strip())
                mensaje_actual = linea
            else:
                mensaje_actual += " " + linea.strip()

    if mensaje_actual:
        mensajes.append(mensaje_actual.strip())

    return mensajes


def procesar_mensajes(nombre_archivo):
    mensajes_raw = leer_mensajes_de_archivo(nombre_archivo)
    mensajes_procesados = []

    for mensaje in mensajes_raw:
        resultado = separar_cadena(mensaje)
        if resultado:
            mensajes_procesados.append(resultado)

    return mensajes_procesados


def procesar_files(pathFile):
    mensajes = procesar_mensajes(pathFile)
    dataMensaje = []

    for i, mensaje in enumerate(mensajes, 1):
        dataMensaje.append({"N": i, **mensaje})
    path_absoluta = os.path.abspath(pathFile)
    directorio = os.path.dirname(path_absoluta)

    nombre_archivo_original = os.path.splitext(os.path.basename(path_absoluta))[0]
    nombre_archivo_final = f"{nombre_archivo_original}.json"
    dir_archivo = os.path.join(directorio, nombre_archivo_final)

    with open(dir_archivo, "w", encoding="utf-8") as file: 
        json.dump(dataMensaje, file, indent=4)

    return {"path": nombre_archivo_final, "data": dataMensaje}
