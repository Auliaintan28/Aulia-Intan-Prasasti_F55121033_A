import time
import sys
import itertools

graph = {
    'a': {'b': 12, 'c': 10, 'g': 12},
    'b': {'a': 12, 'c': 8, 'd': 12},
    'c': {'a': 10, 'b': 8, 'd': 11, 'e': 3, 'g': 9},
    'd': {'b': 12, 'c': 11, 'e': 11, 'f': 10},
    'e': {'c': 3, 'd': 11, 'f': 6, 'g': 7},
    'f': {'d': 10, 'e': 6, 'g': 9},
    'g': {'a': 12, 'c': 9, 'e': 7, 'f': 9}
}

def tsp():
    start_time = time.time()

    nodes = list(graph.keys())
    shortest_path = None
    shortest_distance = sys.maxsize

    for permutation in itertools.permutations(nodes):
        distance = 0
        for i in range(len(permutation) - 1):
            source = permutation[i]
            destination = permutation[i + 1]
            if destination in graph[source]:
                distance += graph[source][destination]
            else:
                distance = sys.maxsize
                break

        if distance < shortest_distance:
            shortest_distance = distance
            shortest_path = permutation

        print(f'Iterasi: {permutation}, Jarak: {distance}')

    end_time = time.time()
    execution_time = end_time - start_time

    print(f'\nWaktu Komputasi: {execution_time} detik')
    print(f'\nHasil Akhir: {shortest_path}')

def dijkstra():
    start_time = time.time()

    start_node = 'a'
    distances = {node: sys.maxsize for node in graph}
    distances[start_node] = 0
    unvisited_nodes = set(graph.keys())

    while unvisited_nodes:
        current_node = min(unvisited_nodes, key=lambda node: distances[node])

        for neighbor, distance in graph[current_node].items():
            new_distance = distances[current_node] + distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

        unvisited_nodes.remove(current_node)
        print(f'Node: {current_node}, Distances: {distances}')

    end_time = time.time()
    execution_time = end_time - start_time

    print(f'\nWaktu Komputasi: {execution_time} detik')
    print(f'\nHasil Akhir (Shortest Path): {distances}')

def main():
    while True:
        print("Pilih Algoritma")
        print("1. TSP")
        print("2. Djikstra")
        print("3. Keluar dari Program")
        choice = int(input("Masukkan Pilihan Anda (1, 2, 3): "))

        if choice == 1:
            print("======TSP=====")
            tsp()
        elif choice == 2:
            print("======DJIKSTRA======")
            dijkstra()
        elif choice == 3:
            print("Terima Kasih..")
            break
        else:
            print("Pilihan Tidak Valid")

        continue_choice = input("Lanjutkan? (y/n): ")
        if continue_choice.lower() != "y":
            print("Terima Kasih..")
            break

if __name__ == '__main__':
    main()
