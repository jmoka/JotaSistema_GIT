import Conexao_BD_MySQL_localhost

def comando_DML(sql):
  Conexao_BD_MySQL_localhost.Metodos.metodo_coleta(sql)
  for x in Conexao_BD_MySQL_localhost.Metodos.metodo_coleta(sql).comite_resultado:
      print(x)


if __name__=="__main__":
    # Descrição das tabelas, comando "DESCRIBE NOME DA TABELA"
    # Mostrar as Tabelas do Banco de Dados, "SHOW TABLES"
    # Select  , Mostra o quem tem na tabela, "SELECT * FROM NOME DA TABELA"
    # clausula WHERE FILTAR , WHERE FILTRAR UM REGISTRO "SELECT * FROM NOME DA TABELA WHERE NOME DA COLUNA = DADO DESEJADO"
    # EXE: SELECT * FROM brasil WHERE nome=jose

    sql='''select * from brasil
    where nome='jose'; '''
    comando_DML(sql)



