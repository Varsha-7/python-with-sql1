import mysql.connector as connector

con=connector.connect(host='localhost',
                       port='3306',
                       user='root',
                       password='Chakkara@7',
                       database='pythontest1')
print(con)

class DBHelper:
    def _init_(self):
         self.con = connector.connect(host='localhost',
                       port='3306',
                       user='root',
                       password='Chakkara@7',
                       database='pythontest1')
                        
         query='create table if not exists user(userId int primary key, userName varchar(200))'

         cur = self.con.cursor()
         cur.execute(query)
         print("created")

    def insert_user(self,userid,username):
        query="insert into user(userId,userName)
        values({},'{}','{}')".format(userid,username)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to db")    
    def update_user(self,userId,newName):
        query="update user set userName='{}' where userId ={}".format(newName,userId)
        print(query)     
        
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")   
           
 
helper=DBHelper()
helper.insert_user(12,"Amruth")
helper.update_user(12,"ankith")

