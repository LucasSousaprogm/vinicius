import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "sistema"
)

cursor = conexao.cursor()


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        

    def cadastrar(self, cursor, conexao):
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (self.email,))
        if cursor.fetchone():
            print("Já existe um usuário com este e-mail.")
            return

        cursor.execute(
        "INSERT INTO usuarios (nome, email, senha) values (%s, %s, %s)",
        ({self.nome}, {self.email}, {self.senha})
        )
    
        conexao.commit()
        print(f"{self.nome} cadastrado com sucesso. ")

    def login(self, cursor):
        cursor.execute(
            "SELECT nome FROM usuarios WHERE email = %s AND senha = %s",
            (self.email, self.senha)
        )

        resultado = cursor.fetchone()
        if resultado:
            nome_real = resultado[0]
            print(f"Bem-vindo(a), {nome_real}")
            return True
        else:
            print("E-mail ou senha incorreta")
            return False
        

while True: 
    print("/n === Menu ===")
    print("1 - Cadastrar usuario")
    print("2 - Fazer lgin")
    print("3 - Sair")
    opcao = input ("Escolha uma opcao: ")

    if opcao == "1":
        nome = input("Nome: ")
        email = input("E-mail: ")
        senha = input("Senha: ")
        usuario = input("Usuario: ")
        usuario.cadastrar(cursor, conexao)
    elif opcao == "2":
        email = input("Senha: ")
        senha = input("Senha: ")
        usuario = usuario("",email,senha)
        usuario.login(cursor)
    elif opcao == "3":
        cursor.close
    else:
        print("Insira uma opcao valida")

