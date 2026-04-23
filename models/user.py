from mongoengine import Document, EmbeddedDocument, StringField, EmailField, EmbeddedDocumentField, ListField

#Objeto Embebido
class Address(EmbeddedDocument):
    street = StringField(required = True, max_length=100)
    city = StringField(required= True, max_length=50)
    zip_code = StringField(required= True, max_length=10)

#Objeto final
class User(Document):
    name = StringField(required= True, max_length= 50)
    email = EmailField(required= True, unique = True)
    password =  StringField(required= True)
    addresses = ListField(EmbeddedDocumentField(Address)) #Documento embebido

    meta = {
        "collection": "users"
    }
