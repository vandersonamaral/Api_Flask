import sqlite3

DATABASE = 'funcionario.db'
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

# Criar tabela se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS Funcionarios (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    setor TEXT,
    idade INTEGER
)
""")

# Inserir dados na tabela
cursor.execute('INSERT INTO Funcionarios (nome, idade,setor) VALUES (?, ?)', ('Pedro', 19,"Gerente"))
cursor.execute('INSERT INTO Funcionarios (nome, idade,setor) VALUES (?, ?)', ('Lucas', 29, "Escravo"))

# Confirmar as mudanças
conn.commit()

# Selecionar e imprimir dados da tabela
cursor.execute('SELECT * FROM Funcionarios')
for row in cursor.fetchall():
    print(row)

# Fechar conexão
conn.close()
