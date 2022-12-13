import Conexao_BD_MySQL_localhost

def metodo(sql):
  con=Conexao_BD_MySQL_localhost.conectar.conexao()
  cur = con.cursor()
  cur.execute(sql)
  con.commit()
  con.close()

