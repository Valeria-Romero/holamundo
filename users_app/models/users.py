from users_app.config.mysqlconnection import connectToMySQL


class User:

    def __init__(self, data):
        #data = {"id": "1", "first_name":"Elena", "last_name":"De Troya", "email": "elena@cd.com", "created_at":"0000-00-00", "updated_at":"0000-00-00"}
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.create_at = data['create_at']
        self.update_at = data['update_at']

    @classmethod
    def guardar(cls, formulario):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
        result = connectToMySQL('crud').query_db(query, formulario)
        return result

    @classmethod
    def muestra_usuarios(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('crud').query_db(query)

        users = []
        for u in results:
            instacia_usuario = cls(u)
            users.append(instacia_usuario)
        return users
    
    @classmethod
    def borrar(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s"
        result = connectToMySQL('crud').query_db(query, data)
        return result




