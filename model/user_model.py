import mysql.connector
import json
class user_model():
    def __init__(self):
       try:
    #connection establishment
        self.con= mysql.connector.connect(host="localhost",user="root",password="WJ28@krhps",database="flask_t")
        self.con.autocommit=True
        self.cur=self.con.cursor(dictionary=True)
        print("connection successful")
       except:
          print("some error")

    def user_gets(self):
        #query execution code
        self.cur.execute("SELECT * FROM users")
        result=self.cur.fetchall()
        if len(result)>0:
           return {"payload":result}
        else:
           return "No Data Found"
        
    def user_get(self, id):
        #query execution code
        self.cur.execute(f"SELECT * FROM users WHERE id={id}")
        result=self.cur.fetchone()
        if len(result)>0:
           return {"payload":result}
        else:
           return "No Data Found"
        
        
    
    def user_add(self, data):
        #query execution code
        self.cur.execute(f"INSERT INTO users(name, phone, email, role) VALUES('{data['name']}', '{data['name']}', '{data['email']}', '{data['role']}')")
        return "User created successfully"
    

    def user_update(self, data):
        #query execution code
        self.cur.execute(f"UPDATE users SET name='{data['name']}', phone='{data['phone']}', email='{data['email']}', role='{data['role']}' WHERE id={data['id']}")
        if self.cur.rowcount>0:
            return "User updated  successfully"
        else:
           return "Nothing to update "
        


    def user_delete(self, id):
        #query execution code
        self.cur.execute(f"DELETE FROM users WHERE id={id}")
        if self.cur.rowcount>0:
            return "User Deleted successfully"
        else:
           return "Nothing to Delete "