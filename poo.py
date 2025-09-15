import mysql.connector

conexao = mysql.connector.connect(

host = "Localhost",
username = "root",
password = "root",
database ="sistema"
)

cursor = conexao.cursor()


class User:
    def __init__(self,name: str,email : str,password: str) -> None:
        self.name = name
        self.email = email
        self.password = password

    def Register(self) ->None:
        query = ("INSERT INTO user (name,password,email) values (%s,%s,%s)")
        data = (self.name,self.password,self.email)
        cursor.execute('SELECT * from  user where email = %s',(self.email,))
        if cursor.fetchone():
            print('Ja existe esse email')
            return
        cursor.execute( 
            query,data
        )
        conexao.commit()
        print("User cadastrado com Sucesso!")
    
    def Login(self) -> bool:
        cursor.execute(
            "SELECT name FROM user WHERE email = %s AND password = %s",
            (self.email, self.password)
        )
        result = cursor.fetchone()
        if result:
            login_name = cursor.fetchone()
            print(f"Welcome, {login_name}")
            return True
        
        if not cursor.fetchone():
            print("Email or Password incorrect")
            return False

