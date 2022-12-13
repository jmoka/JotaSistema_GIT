import Conexao_BD_MySQL_localhost

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

  def metodo_conexao(self):
      self.conexao = Conexao_BD_MySQL_localhost.conectar.conexao()
      self.cursor = self.conexao.cursor()
      self.execuxao = self.cursor.execute(self.sql)
      self.comite = self.conexao.commit()
      self.fechar = self.conexao.close()

  def metodo_coleta(self):
      self.conexao = Conexao_BD_MySQL_localhost.conectar.conexao()
      self.cursor = self.conexao.cursor()
      self.execuxao = self.cursor.execute(self.sql)
      self.resultado = self.cursor.fetchall()
      self.fechar = self.conexao.close()


def estancia(sql):
   conexao = Conexao_BD_MySQL_localhost.conectar.conexao()
   cursor = conexao.cursor()
   execucao = cursor.execute(sql)
   comite_resultado = cursor.fetchall()
   fechar = conexao.close()
   metodos = Metodos(sql, conexao, cursor, execucao, comite_resultado, fechar)
   return metodos


