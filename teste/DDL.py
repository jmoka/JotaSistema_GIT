import Conexao_BD_MySQL_localhost

def comandoDDL(sql):
    Conexao_BD_MySQL_localhost.Metodos.metodo_conexao(sql)
    print('Ação Bem Sucedida!!')

def criarTabela():

    sql= '''CREATE TABLE brasi111l (
            id varchar(10) DEFAULT NULL,
            nome varchar(255) DEFAULT NULL,
            cpf int DEFAULT NULL,
            email varchar(100) DEFAULT NULL
    )'''
    comandoDDL(sql)

def inserirDadosTabela():
    # Inserir Dados nas Tabelas, "INSERT INTO NOME DA TABELA (COLUNA1,COLUNA2) VALUES (X,Y,G)
    sql=''' insert into jose1
           (id,nome,cpf,email) 
           VALUES 
           (23,"suely",564,"email@eail");'''
    comandoDDL(sql)
def selecionartabelas():
    sql= '''use aulas select * from brasil'''
    comandoDDL(sql)


if __name__ == "__main__":
    sql='''insert into brasil 
           (id,nome,cpf,email) 
           VALUES 
           (11,"sussely",56554,"emeeeeail@eail");'''

    selecionartabelas()
