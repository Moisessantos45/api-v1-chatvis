# API ChatVis v1

Api para el procesamiento de los chats de whatsApp. 

## Caracteristicas
    * Subida de archivos.
    * Procesamiento de multiples archivos ala vez.
    * Funcionalida de creacion de jsons de los archivos subidos.
    * Implementacion desde cero el codigo para separar cada mensaje en `fecha`, `nombre`, `hora`, `mensaje` ademas ajustar el formato de la fecha.
    * Analisis avanzado de los chats haciendo uso de .`fecha`, `nombre`, `hora`, `mensaje` ademas ajustar el formato de la fecha.
    * Analisis avanzado de los mensajes con `nltk`.
    * Creacion de csv.
    * La API esta creada con fastApi.

## Instalación
* Para clonar el repositorio ejecuta

```console
git clone https://github.com/Moisessantos45/graficador-chatvis-frontend.git
```
* Para trabajar con la nueva version
```console
git checkout version-2
```

* Debes tener instalado pyhton en tu equipo para poder hacer uso de la API.
* Una vez clonado el repositorio ejeucta sel siguiente comando para instalar el entorno virtaul esta es la formas ma recomendada.

```console
pip install virtualenv
```

# Crear el entorno vitual ejecuta el siguiente comando.
```console
virtualenv name
```
* Cambia el name por el nombre que desees.

# Para hacer uso de tu entorno virtual.
    * Visual studio normalmente detecta tu entorno virtual asi que te preguntara si deseas hacer del que acabas de crear.
    * Si no los detecta puedes ir al apartado de menus de vsc en ver luego en paleta de comandos se mostrar un panel donde deberas escribir `python: select interpreter` seguido de esto se mostrara los entornos virtuales de tu equipo nosotros seleccionaremos el que concide el que creamos o bien el que diga recomendado.
### Para trabajar en tu entorno virtual en tu terminal deberas de ejecutar el siguiente comando.
```console
    .\name\Scripts\activate
```
    Sustituye el name por el nombre que asignaste al entorno virtaul.

# Ejecutar tu API
```console
uvicorn main:app --reload
```

## Configuaracion de cors
Por defecto vite crea el puerto `5173` pero este puede cambiar si tienes definido un puerto.
    * Puedes agregar mas puertos dependiendo el uso.
    * Si no conoces el puerto puedes agregar un * entre comillas dobles esto permitira todas las conexiones.

```python
app = FastAPI()
origns = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origns,
    allow_credentials=True,
    allow_methods=[
        "GET",
        "POST",
    ],
    allow_headers=["*"],
)
```

## Ejemplo de Uso de la API
```python

# Esta ruta se encarga de buscar los jsons creados buscando por el id del usuario 
@public_router.get("/get-data/{id}")
async def getDataJson(id: str):
    return get_data_json(id)

# Esta ruta se encarga de recibir la ruta de un archivo json y convertirlo a csv
# Recibe el dato por query
# Retorna el archivo creado
@public_router.get("/download/")
async def getData(path: str):
    return create_json_to_csv(path)

# Esta ruta encarga de crear un wordcloud a partir de un archivo json
# Recibe el dato por query la cual es el path del archivo
# la respuesta que regresa son las palabras mas comunes que se encontraron
@public_router.get("/create-wordCloud/")
async def getData(path: str):
    return create_to_wordCloud(path)

# Esta ruta se encarga de recibir un archivo y convertirlo a json
# La respuesta que regresa es un array de objetos donde cada objeto tiene dos propiedades el path del archivo json que se creo y data que contiene un arrays con todos los mensajes del chat que se subio.
@public_router.post("/upload")
async def postData(files: List[UploadFile] = File(...)):
    return await post_data(files)
```