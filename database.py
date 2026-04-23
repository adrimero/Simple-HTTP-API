from mongoengine import connect

def init_db():
    # Conexcion a MongoDB (Asegurate de tener MongoDB corriendo
    connect(
        db="simple_http_api",
        host = "localhost",
        port = 27017
    )
