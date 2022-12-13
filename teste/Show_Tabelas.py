import main
import Conexao_BD_MySQL_localhost

def verificar_tabelas():
    sql = 'Show tables;'

    print(f'Essas São as Tabelas do Banco de Dados: {Conexao_BD_MySQL_localhost.database}')
    return Metodos.metodo1(sql)


if __name__=="__main__":
    verificar_tabelas()
