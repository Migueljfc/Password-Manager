
import sqlite3

MATER_PASSWORD = "1234"
senha = input("Enter the master password: ")
if senha != MATER_PASSWORD:
    print("ERROR:Invalid password!")
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
    print("| 1-> Enter new password        |")
    print("| 2-> List saved services       |")
    print("| 3-> Recover a password        |")
    print("| 4-> Delete user               |")
    print("| 5-> Update password           |")
    print("| 6-> Delete all users          |")
    print("| 0-> Exit                      |")
    print("|_______________________________|")

def show_services():
    cursor.execute('''
        SELECT service FROM users;
        ''')
    if cursor.rowcount == 0:
        print("Empty")
    else:
        for service in cursor.fetchall():
            print(service)

def insert_password(service,username,password):
    cursor.execute(f'''
        INSERT INTO users(service,username,password) 
        VALUES ('{service}','{username}','{password}')
    ''')
    conn.commit()

def get_password(service):
    cursor.execute(f'''
        SELECT username,password FROM users
        WHERE service = '{service}'
    ''')
    if cursor.rowcount == 0:
        print("Service not found, please register it first.")
    else:
        for user in cursor.fetchall():
            print(user)

def del_user(username):
    cursor.execute(f'''
        DELETE FROM users WHERE username = '{username}'
    ''')
    if cursor.rowcount == 0:
        print("User not found!")
    else:
        print("Deleted")
    conn.commit()

def edit(username,password,service):
    cursor.execute(f'''
        UPDATE users SET password = '{password}' WHERE username = '{username}' AND service = '{service}'
    ''')
    if cursor.rowcount == 0:
        print('User not found')
    else :
        print("Success")
    conn.commit()
def del_all():
    cursor.execute('''
        DELETE FROM USERS 
    ''')
    print("Deleted")
    conn.commit()


while True:
    menu()
    op = input("Option-> ")
    if op not in['0','1','2','3','4','5','6']:
        print("Invalid Option")
        continue
    if op == '0' :
        break
    if op == '1':
        service = input('What\'s the name of the service ? ')
        username = input('What\'s the user\'s name? ')
        password = input('What\'s your password?')
        insert_password(service, username, password)
    if op == '2':
        show_services()
    if op == '3':
        service = input('What service do you want the password for ?  ')
        get_password(service)
    if op == '4':
        username = input('What\'s the user\'s name? ')
        del_user(username)
    if op == '5':
        username = input('What\'s the user\'s name ? ')
        service = input ('What\'s the service ? ')
        password = input('What is the new password ?')
        edit(username,password,service)
    if op == '6':
        del_all()

conn.close()