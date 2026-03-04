#Exercício 2 - Inserção Múltipla e Tipos de Dados
import sqlite3
import pandas as pd

conn = sqlite3.connect('web.db')
c = conn.cursor()

c.execute('CREATE TABLE estoque ([item_id] INTEGER, [nome_item] TEXT, [quantidade] INTEGER)')
c.execute('''INSERT INTO estoque (item_id, nome_item, quantidade)
          VALUES
          (1, 'Teclado', 50),
          (2, 'Mouse', 100),
          (3, 'Monitor', 25)
          ''')
conn.commit()


