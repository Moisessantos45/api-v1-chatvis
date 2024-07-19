import os


def deleteFile(path):
    try:
        os.remove(path)
    except FileNotFoundError:
        pass
    except Exception as e:
        return {"error": str(e)}
