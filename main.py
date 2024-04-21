class Chat:
    def __init__(self) -> None:
        self.name = None
        self.bio = None
        self.contacts = [
            {"name": "Franco",
             "number": "XXXXXXXX5"},

             {"name": "Francisco",
             "number": "XXXXXXXX4"},
        ]

    def main(self):
        while True:
            o = int(input("1)Perfil\n2)mensaje\n3)contacto\n4)Estado\n5)salir\nSeleccione opcion: "))

            match o:
                case 1:
                    self.profile()
                case 2:
                    self.message()
                case 3:
                    self.contact()
                case 4:
                    self.status()
                case 5:
                    print("Finalizando programa...\n")
                    break
                case _:
                    print("Comando erroneo...\n")
    
    # Definir, ver o modificar perfil
    def profile(self):
        # Si no tiene nombre lo define
        if self.name == None and self.bio == None:
            self.name = input("Ingrese su nombre: ")
            self.bio = input("Ingrese su biografia: ")
        # se ejecutan las opciones
        else:
            print(f'{"info".center(30,"-")}')
            print(f'Nombre: {self.name}\nBiografia: {self.bio}\n')
            o = int(input("1)modificar\n2)salir\nSeleccione opcion: "))

            match o:
                case 1:
                    print(f'{"info".center(30,"-")}')
                    print(f'Nombre: {self.name}\nBiografia: {self.bio}\n')
                    self.name = input("Ingrese su nombre: ")
                    self.bio = input("Ingrese su biografia: ")

                case 2:# salir al menu
                    pass
                case _:
                    print("Comando erroneo...\n")
    def message(self):
        # Hacer sistema de filtrado (quizas)
        contact = input("Contacto(1 para listar): ")
        if contact == "1":
            for i in self.contacts:
                print(f"Nombre: {i['name']}")
                print(f"Numero: {i['number']}")
            contact = input("Contacto: ")
            msg = input("Mensaje: ")
            print(f"Se ha enviado mensaje{msg} a {contact}\n")
        else:
            msg = input("Mensaje: ")
            print(f"Se ha enviado mensaje: {msg} a: {contact}\n")

    def contact(self):
        o = int(input("1)Agregar\n2)Modificar\n3)Salir\nEliga opcion: "))

        match o:
            case 1:
                name = input("Ingrese nombre:")
                number = input("Ingrese numero:")

                self.contacts.append({"name":name,"number":number})
                for i in self.contacts:
                    print(f"Nombre: {i['name']}")
                    print(f"Numero: {i['number']}")
            case 2:
                pass
            case 3:
                pass
            case _:
                print("Comando erroneo...\n")
            
    def status(self):
        o = int(input("1)Subir\n2)Ver3)Salir\nEliga opcion: "))


if __name__ == "__main__":
    chat = Chat()
    chat.main()