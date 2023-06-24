from cryptography.fernet import Fernet
import os.path as path

def key():
    key = Fernet.generate_key()
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)
    print('\n')
    print("Archivo generado con éxito!")

def ArchivoEncryptado():
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    fernet = Fernet(key)
    print('\n')
    n = input("Cual es el nombre del archivo Excel?: ")
    print('\n')
    x = n + '.xlsx'

    if path.exists(x):
        with open(x, 'rb') as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        with open('prueba.xlsx', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

        print('\n')
        print("Archivo Encryptado con éxito!")
    else:
        print("El archivo no existe.")
   
def ArchivoDescryptado():
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    print('\n')
    n = input("Cual es el nombre del archivo Excel?: ")
    print('\n')
    x = n + '.xlsx'

    if path.exists(x):
        with open(x, 'rb') as enc_file:
            encrypted = enc_file.read()
        
        decrypted = fernet.decrypt(encrypted)

        with open('prueba.xlsx', 'wb') as dec_file:
            dec_file.write(decrypted)

        print('\n')
        print("Archivo Descryptado con éxito!")
    else:
        ("El archivo no existe.")
        

def menu():
    while True:
        print('\n')
        print ("1. Generar Archivo 'key'.")
        print ("2. Encryptar Archivo.")
        print ("3. Desercyptar Archivo.")
        print ("4. Salir.")
        print('\n')

        entrada = input("Que desea hacer?: ")
        try:
            entrada = int(entrada)  
            if entrada == 1:
                key()
            elif entrada == 2:
                ArchivoEncryptado()
            elif entrada == 3:
                ArchivoDescryptado()
            else:
                exit()

        except ValueError:
            print('\n')
            print ("La entrada es incorrecta.")

menu()