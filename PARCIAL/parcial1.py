import redis

r = redis.Redis(host='localhost', port=6379, db=0)


def register_item():
    item_name = input("Ingrese el nombre del artículo: ")
    item_quantity = input("Ingrese la cantidad del artículo: ")
    item_price = input("Ingrese el precio del artículo: ")

    r.hset(item_name, {'quantity': item_quantity, 'price': item_price})

    print("Item registered successfully.")


def search_item():
    item_name = input("Ingrese el nombre del artículo: ")

    item = r.hgetall(item_name)

    if item:
        print(f"Nombre: {item_name}")
        print(f"Cantidad: {item[b'quantity'].decode('utf-8')}")
        print(f"Precio: {item[b'price'].decode('utf-8')}")
    else:
        print("Artículo no encontrado.")


def edit_item():
    item_name = input("Ingrese el nombre del artículo: ")

    item = r.hgetall(item_name)

    if item:
        item_quantity = input("Ingrese la nueva cantidad: ")
        item_price = input("Ingrese el nuevo precio: ")

        r.hmset(item_name, {'quantity': item_quantity, 'price': item_price})

        print("Artículo editado exitosamente.")
    else:
        print("Artículo no encontrado.")


def delete_item():
    item_name = input("Ingrese el nombre del artículo: ")

    r.delete(item_name)

    print("Artículo eliminado exitosamente.")


while True:
    action = input("Ingrese una acción (registro, búsqueda, edición, eliminación, salida): ")

    if action == "registro":
        register_item()
    elif action == "búsqueda":
        search_item()
    elif action == "edición":
        edit_item()
    elif action == "eliminación":
        delete_item()
    elif action == "salida":
        break
    else:
        print("Acción inválida.")

