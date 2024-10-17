mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]

def remove_duplicates(items_list):
    filtered_list = list(set(items_list))
    print("La lista sin duplicados es: ", filtered_list)
    return filtered_list


def sorted_ascending(items_list):
    items_list.sort(reverse=True)
    print("La lista ordenada de mayor a menor es: ", items_list)


def run():
    print("La lista original es: ", mi_lista)
    unique_items_list = remove_duplicates(mi_lista)
    sorted_ascending(unique_items_list)


if __name__ == "__main__":
    run()