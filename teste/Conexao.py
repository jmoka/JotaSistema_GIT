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



class Metodos:
  def __init__(self,sql,conexao,cursor, execucao, comite_resultado, fechar):
    self.setSql(sql)
    self.setConexao(conexao)
    self.setCursor(cursor)
    self.setExecucao(execucao)
    self.setComite_resultado(comite_resultado)
    self.setFechar(fechar)

#==========================================================

  def setSql(self,sql):
    self.sql=sql

  def setConexao(self, conexao):
      self.conexao= conexao

  def setCursor(self, cursor):
      self.cursor = cursor

  def setExecucao(self, execucao):
      self.execuxao = execucao

  def setComite_resultado(self, comite_resultado):
      self.comite_resultado = comite_resultado

  def setFechar(self, fechar):
      self.fechar = fechar

#==============================================

  def getSql(self):
    return self.sql

  def getConexao(self):
      return self.conexao

  def getCursor(self):
      return self.cursor

  def getExecucao(self):
      return self.execuxao

  def getComite_resultado(self):
      return self.comite_resultado

  def getFechar(self):
      return self.fechar
#================================================================

  def metodo_conexao(sql):
      conexao = conectar.conexao()
      cursor = conexao.cursor()
      execucao = cursor.execute(sql)
      comite_resultado = conexao.commit()
      fechar = conexao.close()
      metodos = Metodos(sql, conexao, cursor, execucao, comite_resultado, fechar)
      return metodos

  def metodo_coleta(sql):
      conexao = conectar.conexao()
      cursor = conexao.cursor()
      execucao = cursor.execute(sql)
      comite_resultado = cursor.fetchall()
      fechar = conexao.close()
      metodos = Metodos(sql, conexao, cursor, execucao, comite_resultado, fechar)
      return metodos


host = 'localhost'
database = 'Aulas'
user = 'root'
password = "123456"
port = '3306'
conectar = Conexao(host, database, user, password, port)



