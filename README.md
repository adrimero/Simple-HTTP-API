# Simple HTTP API - Clean Architecture

Este proyecto es un servidor HTTP construido desde cero en Python, aplicando principios de arquitectura limpia.

## Arquitectura
- **Controller:** Manejo de rutas y parsing manual de HTTP.
- **Service:** Lógica de negocio y validación de esquemas (Pydantic).
- **Repository:** Abstracción de la base de datos.
- **Model:** Definición de documentos para MongoDB (MongoEngine).

## Tecnologías
- Python 3.x
- MongoDB & MongoEngine
- Pydantic (Validación)
