# -*- coding: utf-8 -*-
import sqlite3

MATER_PASSWORD = "1234"
senha = input("Insira a senha master:")
if senha != MATER_PASSWORD:
    print("ERRO:Senha inválida!")
    exit()

conn = sqlite3.connect('passwords.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
   service TEXT NOT NULL,
   username TEXT NOT NULL,
   password TEXT NOT NULL
);
''')

def menu():
    print(" _______________________________")
    print("|      Passwords Manager        |")
    print("|_______________________________|")
    print("| 1-> Inserir senha nova        |")
    print("| 2-> Listar serviços guardados |")
    print("| 3-> Recuperar uma senha       |")
    print("| 0-> Sair                      |")
    print("|_______________________________|")
def show_services():
    cursor.execute('''
        SELECT service FROM users;
        ''')
    for service in cursor.fetchall():
        print(service)

def insert_password(service,username,password):
    cursor.execute(f'''
        INSERT INTO users(service,username,password) 
        VALUES ('{service}','{username}','{password}')
    ''')
    conn.commit()

def get_password(service):
    pass  #falta acabar 

while True:
    menu()
    op = input("Opção->")
    if op not in['0','1','2','3']:
        print("Opção inválida")
        continue
    if op == '0' :
        break
    if op == '1':
        service = input('Qual o nome do serviço? ')
        username = input('Qual o nome do utilizador? ')
        password = input('Qual a sua password? ')
        insert_password(service, username, password)
    if op == '2':
        show_services()
    
conn.close()