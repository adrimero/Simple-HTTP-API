from repositories.user_repo import UserRepository
from schemas.user import UserCreateSchema
from pydantic import ValidationError
from models.user import User
import json

class UserService:
    def __init__(self):
        self.repo = UserRepository()

    def create_user(self, raw_data: dict) -> tuple[int, dict]:
        try:
            # Validacion de Input con Pydantic
            valid_data = UserCreateSchema(**raw_data)

            # Verificar reglas de negocio (ej: email duplicado)
            if User.objects( #type: ignore
                email = valid_data.email
            ).first():
                return 400, {"error": "The emails is alredy in use"}

            # Guardar en DB a travez del Repositorio
            user = self.repo.create(valid_data.model_dump())

            # Devolvemos el JSON en MongoEngine (parseado para limpiarlo)
            return 201, json.loads(user.to_json())

        except ValidationError as e:
            return 400, {"error": "Validation failed", "details": e.errors()}
        except Exception as e:
            return 500, {"error": "Internal server error", "details": str(e)}

    def get_users(self) -> tuple[int, list]:
        users = self.repo.get_all()
        return 200, json.loads(users.to_json())
