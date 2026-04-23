from models.user import User

class UserRepository:
    def create(self, user_data: dict) -> User:
        user = User(**user_data)
        user.save()
        return user

    def get_all(self):
        return User.objects() #type: ignore

    def get_by_id(self, user_id: str):
        return User.objects( #type: ignore
            id = user_id
        ).first()
