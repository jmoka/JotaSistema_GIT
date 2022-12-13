import mysql.connector

class Conexao:
    def __init__(self, host, database, user, password, port):
        self.host=host
        self.database=database
        self.user=user
        self.password=password
        self.port=port

    def conexao(self):
        con = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port)
        print('CONECTADO')
        return con

host = 'localhost'
database = 'Aulas'
user = 'root'
password = "123456"
port = '3306'
conectar = Conexao(host, database, user, password, port)


if __name__ == "__main__":
  conectar.conexao()



