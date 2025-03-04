from app import mongo, bcrypt
from bson import ObjectId

class User:
    @staticmethod
    def find_all():
        users = list(mongo.db.users.find())
        for user in users:
            user['_id'] = str(user['_id'])
        return users

    @staticmethod
    def find_by_id(user_id):
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        if user:
            user['_id'] = str(user['_id'])
        return user

    @staticmethod
    def create(name, email, password):
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = {
            "name": name,
            "email": email,
            "password": hashed_password
        }
        result = mongo.db.users.insert_one(user)
        return str(result.inserted_id)

    @staticmethod
    def update(user_id, data):
        if "password" in data:
            data["password"] = bcrypt.generate_password_hash(data["password"]).decode('utf-8')
        mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": data})

    @staticmethod
    def delete(user_id):
        mongo.db.users.delete_one({"_id": ObjectId(user_id)})

    @staticmethod
    def find_by_email(email):
        user = mongo.db.users.find_one({"email": email})
        if user:
            user['_id'] = str(user['_id'])
        return user
