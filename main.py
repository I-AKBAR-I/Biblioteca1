from user_management import UserManager
from catalog_management import CatalogManager
from loan_management import LoanManager
from reporting import ReportManager

def main():
    user_manager = UserManager()
    catalog_manager = CatalogManager()
    loan_manager = LoanManager(user_manager, catalog_manager)
    report_manager = ReportManager(user_manager, catalog_manager, loan_manager)
    
    while True:
        print("\nSistema de Gestión de Préstamos de Biblioteca")
        print("1. Gestión de Usuarios")
        print("2. Gestión de Catálogo")
        print("3. Gestión de Préstamos y Devoluciones")
        print("4. Generación de Reportes")
        print("5. Salir")

        choice = input("Seleccione una opción: ")

        if choice == '1':
            user_manager.manage_users()
        elif choice == '2':
            catalog_manager.manage_catalog()
        elif choice == '3':
            loan_manager.manage_loans()
        elif choice == '4':
            report_manager.generate_reports()
        elif choice == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
