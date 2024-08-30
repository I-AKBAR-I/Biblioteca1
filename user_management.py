class UserManager:
    def __init__(self):
        self.users = []

    def manage_users(self):
        while True:
            print("\nGestión de Usuarios")
            print("1. Registrar Usuario")
            print("2. Listar Usuarios")
            print("3. Volver")

            choice = input("Seleccione una opción: ")

            if choice == '1':
                self.register_user()
            elif choice == '2':
                self.list_users()
            elif choice == '3':
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def register_user(self):
        user = {}
        user['id'] = input("Ingrese identificación única: ")
        user['Nombre'] = input("Ingrese nombre completo: ")
        user['Direccio'] = input("Ingrese dirección: ")
        user['Telefono'] = input("Ingrese número celular: ")
        user['Correo'] = input("Ingrese correo electrónico: ")
        user['dob'] = input("Ingrese fecha de nacimiento (dd/mm/yyyy): ")
        user['Ocupacion'] = input("Ingrese ocupación o centro de estudios: ")

        if any(u['id'] == user['id'] for u in self.users):
            print("Error: La identificación ya existe.")
        else:
            self.users.append(user)
            print("Usuario registrado con éxito.")

    def list_users(self):
        if not self.users:
            print("No hay usuarios registrados.")
        else:
            for idx, user in enumerate(self.users, start=1):
                print(f"\nUsuario {idx}:")
                for key, value in user.items():
                    print(f"{key}: {value}")
                print("-" * 40)

