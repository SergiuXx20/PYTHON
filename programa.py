usuario = "Sergio"
clave = "1234"
admin = "root"
claveadmin = "4321"


nombreusuario = input("Escribe tu nombre de usuario: ")
claveusuario = input("Escribe tu clave: ")

while ((nombreusuario != usuario) and (claveusuario != clave)):
    print("Acceso denegado")
    nombreusuario = input("Escribe tu nombre de usuario: ")
    claveusuario = input("Escribe tu clave: ")

if ((nombreusuario == usuario) and (claveusuario == clave)): 
    eligio = input("""
                   _Acceso concedido_
                    
                    1- Modo root
                    2- Opcion vacia 2
                    3- Opcion vacia 3

                    Escoja una opcion:
                    """)
                
if eligio == "1":
    print("BIENVENIDO AL MODO ROOT")
    nombreadmin = input("Escribe tu nombre de usuario: ")
    adminclave = input("Escribe tu clave: ")

    while ((nombreadmin != admin) and (adminclave != claveadmin)):
        print("Acceso denegado")
        print("Vuelva a intentarlo")
        nombreadmin = input("Escribe tu nombre de usuario: ")
        adminclave = input("Escribe tu clave: ")

    if ((nombreadmin == admin) and (adminclave == claveadmin)): 
        eligioadmin = input("""
                   _Acceso concedido_
                    
                    1 Opcion vacia 1
                    2 Opcion vacia 2
                    3 Opcion vacia 3
                    4 Opcion vacia 4

                    Escoja una opcion:
                    """)

    if eligioadmin == "1":
                    print("Vacio 1")
                
    if eligioadmin == "2":
                    print("Vacio 1")

    if eligioadmin == "3":
                    print("Vacio 1")
                
    if eligioadmin == "4":
                print("Vacio 1")
    
    else:
        print("Opcion no existente, vuelva a intentarlo")
    

if eligio == "2":
    print("Escogiste la opcion 2")

if eligio == "3":
    print("Escogiste la opcion 3")

else:
    print("Opcion no existente, vuelva a intentarlo")


  





    





