# Exercício 3 - Prevenir o IntegrityError e tratar duplicidade
import sqlite3
import pandas as pd

conn = sqlite3.connect('web.db')
c = conn.cursor()

# Nota: Se rodarmos o INSERT abaixo, o Python disparará um IntegrityError 
# porque o product_id 4 seria duplicado na mesma instrução.

try:
    # Tentativa que falharia sem o tratamento adequado
    c.execute('''INSERT INTO products (product_id, product_name, price)
              VALUES
              (4, 'PS5', 1000),
              (4, 'XboxOne', 1500)
              ''')
except sqlite3.IntegrityError:
    print("Erro de integridade detectado: ID duplicado bloqueado pelo banco.")

# 2. Solução correta: Inserindo ou ignorando conflitos
# O comando INSERT OR IGNORE permite que o banco ignore registros que violem a PRIMARY KEY
c.execute('''INSERT OR IGNORE INTO products (product_id, product_name, price)
          VALUES
          (4, 'PS5', 1000),
          (4, 'XboxOne', 1500)
          ''')

# 3. Confirmação e encerramento
conn.commit()
conn.close()