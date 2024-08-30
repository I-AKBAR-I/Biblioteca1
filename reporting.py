class ReportManager:
    def __init__(self, user_manager, catalog_manager, loan_manager):
        self.user_manager = user_manager
        self.catalog_manager = catalog_manager
        self.loan_manager = loan_manager

    def generate_reports(self):
        while True:
            print("\nGeneración de Reportes")
            print("1. Reporte de Artículos más Prestados")
            print("2. Reporte de Usuarios Frecuentes")
            print("3. Reporte de Artículos Perdidos o Dañados")
            print("4. Reporte de Ingresos por Multas")
            print("5. Volver")

            choice = input("Seleccione una opción: ")

            if choice == '1':
                self.report_most_loaned_items()
            elif choice == '2':
                self.report_frequent_users()
            elif choice == '3':
                self.report_lost_damaged_items()
            elif choice == '4':
                self.report_fine_income()
            elif choice == '5':
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def report_most_loaned_items(self):
        # Implementación básica de ejemplo
        print("Reporte de Artículos más Prestados")

    def report_frequent_users(self):
        # Implementación básica de ejemplo
        print("Reporte de Usuarios Frecuentes")

    def report_lost_damaged_items(self):
        # Implementación básica de ejemplo
        print("Reporte de Artículos Perdidos o Dañados")

    def report_fine_income(self):
        # Implementación básica de ejemplo
        print("Reporte de Ingresos por Multas")
