import rpyc
from constRPYC import *

class Client:
    conn = rpyc.connect(SERVER, PORT) # Conectar ao servidor
    print(conn.root.exposed_value()) # Imprimir a lista atual
    
    # Adicionar um elemento na lista
    conn.root.exposed_append(5)
    conn.root.exposed_append(6)
    print(conn.root.exposed_value()) # Imprimir a lista atualizada
    
    # Pesquisar um elemento na lista
    search_element = 5
    if search_element in conn.root.exposed_value():
        print(f"O elemento {search_element} está na lista")
    else:
        print(f"O elemento {search_element} não está na lista")
    
    # Remover um elemento da lista
    remove_element = 5
    if remove_element in conn.root.exposed_value():
        conn.root.exposed_remove(remove_element)
        print(f"O elemento {remove_element} foi removido da lista")
    else:
        print(f"O elemento {remove_element} não está na lista")
    print(conn.root.exposed_value()) # Imprimir a lista atualizada
    
    # Inserir um elemento na lista em uma posição específica
    insert_element = 10
    insert_index = 1
    conn.root.exposed_insert(insert_index, insert_element)
    print(f"O elemento {insert_element} foi inserido na posição {insert_index}")
    print(conn.root.exposed_value()) # Imprimir a lista atualizada
    
    # Ordenar a lista em ordem crescente
    conn.root.exposed_sort()
    print("A lista foi ordenada em ordem crescente")
    print(conn.root.exposed_value()) # Imprimir a lista ordenada
