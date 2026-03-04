import sqlite3
import pandas as pd

# 1. Conexão com o banco
conn = sqlite3.connect('web.db')

# 2. Criação do cursor para executar comandos SQL
c = conn.cursor()

# --- ESPAÇO PARA AS QUERYS DOS EXERCÍCIOS ---

c.execute('DROP TABLE estudantes')

c.execute('CREATE TABLE estudantes ([estudante_id] INTEGER PRIMARY KEY, [estudante_nome] TEXT, [curso] TEXT)')
c.execute('''INSERT INTO estudantes (estudante_id, estudante_nome, curso)
          VALUES
          (1, 'Miguel Remides', 'Sistemas de informação')
          ''')
c.execute("DELETE FROM estudantes")
c.execute('''INSERT INTO estudantes (estudante_id, estudante_nome, curso)
          VALUES
          (1, 'Miguel Remides', 'Sistemas de informação')
          ''')
conn.commit()
