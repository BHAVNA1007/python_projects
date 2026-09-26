from database.connection import Database

class UserDao:

    def delete_user_by_id(self, user_id):
        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = 'delete from users where user_id = %s'

        cursor.execute(query, (user_id,))
        delete_count = cursor.rowcount

        conn.commit()

        if delete_count>0:
            print(f"{user_id} : deleted successfully")

        else:
            print("user not found")

        cursor.close()
        conn.close()

        return delete_count    



    def update_user_by_id(self, user_name, user_id):
        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query ='update users set name = %s  where user_id = %s'
        cursor.execute(query, (user_name, user_id,))

        update_count = cursor.rowcount
        conn.commit()

        if update_count > 0:
            print(f"{user_name}: user name updated successfully")

        else:
            print("user not found")

        cursor.close()
        conn.close()
        return update_count
            
    def get_user_by_id(self, user_id):
        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = 'select * from users where user_id = %s'
        cursor.execute(query, (user_id,))

        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row

    def login_user(self, email, password):
        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query ="select * from users where email = %s  AND password = %s"
        cursor.execute(query, (email, password))
        rows = cursor.fetchone() 

        cursor.close()
        conn.close()
        return rows


    def save_user(self, user):
        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = 'insert into users (name, email, password) values(%s, %s, %s)'
        data = (user.name, user.email, user.password)

        cursor.execute(query, data)

        conn.commit()
        cursor.close()
        conn.close()
        print("user saved successfully")
