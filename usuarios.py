import json
datos = {}
while True:    
    a = input("Ingrese usuario: ")
    b = input("Ingrese contraseña: ")
    def carga_datos(datos):
        datos[a] = b    
    def mostrar_datos(datos):
        mostrar = input("Mostrar dato? si/no:".lower())
        if mostrar == 'si':
            print(f"{datos}")        
            for a , b in datos.items():
                print(f"Usuario: {a}", f"\tContraseña: {b}")    
    def login(datos):
        buscar = input("Login? si/no:".lower())        
        while buscar == 'si':
            u = input("Ingrese su usuario: ")
            if u in datos.keys():
                c = input("Ingrese su contraseña: ")
                if c == datos[u]:
                    print(f"Hola {a}, que bueno verte de nuevo!!!")
                    break            
                else:
                    print("Contraseña incorrecta!!!")
                    salir = input("Salir? si/no: ")
                    if salir == 'si':
                        print("Chauuu!")
                    break                     
            else:
                print("Usuario no encontrado!!")
                salir = input("Salir? si/no: ")
                if salir == 'si':
                    print("Chauuu!")                                
                with open("datos_guardados.json", "w") as file:
                    json.dump(datos, file, indent=4)
    carga_datos(datos)
    mostrar_datos(datos)
    login(datos)




