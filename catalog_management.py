class CatalogManager:
    def __init__(self):
        self.catalog = []

    def manage_catalog(self):
        while True:
            print("\nGestión de Catálogo")
            print("1. Agregar Artículo")
            print("2. Listar Catálogo")
            print("3. Volver")

            choice = input("Seleccione una opción: ")

            if choice == '1':
                self.add_item()
            elif choice == '2':
                self.list_catalog()
            elif choice == '3':
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def add_item(self):
        item = {}
        item['id'] = input("Ingrese ID del artículo (ISBN/ISSN): ")
        item['Titulo'] = input("Ingrese título completo: ")
        item['autor'] = input("Ingrese autor(es): ")
        item['Año'] = input("Ingrese año de publicación: ")
        item['Editorial'] = input("Ingrese editorial: ")
        item['keywords'] = input("Ingrese palabras clave: ")
        item['categoria'] = input("Ingrese categoría: ")
        item['copias'] = int(input("Ingrese cantidad de ejemplares disponibles: "))

        self.catalog.append(item)
        print("Artículo agregado con éxito.")

    def list_catalog(self):
        if not self.catalog:
            print("No hay artículos en el catálogo.")
        else:
            for idx, item in enumerate(self.catalog, start=1):
                print(f"\nArtículo {idx}:")
                for key, value in item.items():
                    print(f"{key}: {value}")
                print("-" * 40)
