import Metodos

def criarTabela():

    sql = '''CREATE TABLE linda
            (  id  character varying(10), 
               nome VARCHAR(255), 
               cpf int, 
               email  VARCHAR(100) 
        )'''
    print('Tabela criada com Sucesso')
    return Metodos.metodo(sql)


if __name__ == "__main__":
    criarTabela()
