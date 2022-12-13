import main2

def show_tabelas(sql):
  main2.Metodos.metodo_coleta(sql)
  for x in main2.Metodos.metodo_coleta(sql).comite_resultado:
      print(x)

sql='Show tables'
show_tabelas(sql)
