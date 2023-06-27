import time

def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    end_time = time.time()
    execution_time = end_time - start_time

    return arr, execution_time


def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    end_time = time.time()
    execution_time = end_time - start_time

    return arr, execution_time


def print_iterations(arr):
    print("Iterasi:")
    print("5 Iterasi Pertama:")
    for i in range(5):
        print(arr[i], end=" ")
    print("\n5 Iterasi Terakhir:")
    for i in range(len(arr) - 5, len(arr)):
        print(arr[i], end=" ")
    print()


def print_before_after(arr, sorted_arr):
    print("Sebelum Pengurutan:", arr)
    print("Sesudah Pengurutan:", sorted_arr)


def analyze_algorithm():
    arr = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7,
           26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21,
           17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59,
           40, 7, 41, 81]

    while True:
        print("Pilih Algoritma")
        print("1. Bubble Sort")
        print("2. Insertion Sort")
        print("3. Keluar dari Program")
        choice = int(input("Masukkan Pilihan Anda (1, 2, 3): "))

        if choice == 1:
            sorted_arr, execution_time = bubble_sort(arr.copy())
            print("\nBUBBLE SORT")
            print_iterations(sorted_arr)
            print_before_after(arr, sorted_arr)
            print("Waktu Komputasi Pengurutan:", execution_time, "detik")
        elif choice == 2:
            sorted_arr, execution_time = insertion_sort(arr.copy())
            print("\nINSERTION SORT")
            print_iterations(sorted_arr)
            print_before_after(arr, sorted_arr)
            print("Waktu Komputasi Pengurutan:", execution_time, "detik")
        elif choice == 3:
            print("Terima Kasih..")
            break
        else:
            print("Pilihan Tidak Valid")

        continue_choice = input("Lanjutkan? (y/n): ")
        if continue_choice.lower() != "y":
            print("Terima Kasih..")
            break


analyze_algorithm()