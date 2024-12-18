import sqlite3

def get_connection():
    conn = sqlite3.connect('exemplo.db')
    return conn

def criar_funcionario(nome, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO funcionarios (nome, email) VALUES (?, ?)', (nome, email))
    conn.commit()
    conn.close()

def buscar_funcionarios():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM funcionarios')
    funcionarios = cursor.fetchall()
    conn.close()
    return funcionarios

def buscar_funcionario_por_id(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM funcionarios WHERE id = ?', (id,))
    funcionario = cursor.fetchone()
    conn.close()
    return funcionario

def atualizar_funcionario(id, nome, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE funcionarios SET nome = ?, email = ? WHERE id = ?', (nome, email, id))
    conn.commit()
    conn.close()

def deletar_funcionario(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM funcionarios WHERE id = ?', (id,))
    conn.commit()
    conn.close()

# Criação inicial da tabela (garantir que exista)
conn = get_connection()
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
''')
conn.commit()
conn.close()
