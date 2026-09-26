from dao.user_dao import UserDao

class UserService:

    def delete_user_by_id(self, user_id):
        user_dao = UserDao()
        delete_count = user_dao.delete_user_by_id(user_id)
        return delete_count

    def update_user_by_id(self, user_name,  user_id):
        user_dao = UserDao()
        update_count = user_dao.update_user_by_id(user_name, user_id)
        return update_count


    def get_user_by_id(self, user_id):
        user_dao = UserDao()
        row = user_dao.get_user_by_id(user_id)
        return row

    def login_user(self, email, password):
        user_dao = UserDao()
        row = user_dao.login_user(email, password)
        return row
    
    def save_user(self, user):
        user_dao = UserDao()
        user_dao.save_user(user) 