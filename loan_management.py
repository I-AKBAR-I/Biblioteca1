class LoanManager:
    def __init__(self, user_manager, catalog_manager):
        self.loans = []
        self.user_manager = user_manager
        self.catalog_manager = catalog_manager

    def manage_loans(self):
        while True:
            print("\nGestión de Préstamos y Devoluciones")
            print("1. Registrar Préstamo")
            print("2. Registrar Devolución")
            print("3. Volver")

            choice = input("Seleccione una opción: ")

            if choice == '1':
                self.register_loan()
            elif choice == '2':
                self.register_return()
            elif choice == '3':
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def register_loan(self):
        user_id = input("Ingrese identificación del usuario: ")
        user = next((u for u in self.user_manager.users if u['id'] == user_id), None)
        if not user:
            print("Usuario no encontrado.")
            return

        item_id = input("Ingrese ID del artículo: ")
        item = next((i for i in self.catalog_manager.catalog if i['id'] == item_id), None)
        if not item or item['copies'] <= 0:
            print("Artículo no disponible.")
            return

        loan = {
            'user_id': user_id,
            'item_id': item_id,
            'item_title': item['title'],
            'loan_date': input("Ingrese fecha de préstamo (dd/mm/yyyy): "),
            'return_date': input("Ingrese fecha de devolución estimada (dd/mm/yyyy): ")
        }

        item['copies'] -= 1
        self.loans.append(loan)
        print("Préstamo registrado con éxito.")

    def register_return(self):
        user_id = input("Ingrese identificación del usuario: ")
        item_id = input("Ingrese ID del artículo: ")

        loan = next((l for l in self.loans if l['user_id'] == user_id and l['item_id'] == item_id), None)
        if loan:
            self.loans.remove(loan)
            item = next((i for i in self.catalog_manager.catalog if i['id'] == item_id), None)
            if item:
                item['copies'] += 1
            print("Devolución registrada con éxito.")
        else:
            print("Préstamo no encontrado.")
