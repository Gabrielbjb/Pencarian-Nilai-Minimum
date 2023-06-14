import time

def cari_nilai_minimum_bruteForce(arr):
    min_index = 0
    previous_min_index = min_index
    for i in range(1, len(arr)):
        change_min_Index = False
        if arr[i] < arr[min_index]:
            change_min_Index = True
            previous_min_index = min_index
            min_index = i
        print("Iterasi ke-" + str(i) + ": " + "arr[" + str(i) + "] < arr[" + str(previous_min_index) + "]: " + str(change_min_Index) + ", Nilai minimum sekarang ada di array indeks ke-" + str(min_index))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Nilai minimum ada di array dengan indeks ke-" + str(min_index) + " dengan nilai: " + str(arr[min_index]))

def cari_nilai_minimum_DNQ(arr, low, high, indent=""):
    if high - low == 1:
        if arr[high] < arr[low]:
            print(indent[:len(indent)-2] + "┣━" + listToString(arr[low:high+1]), "min: " + str(arr[high]))
            return arr[high]
        else:
            print(indent[:len(indent)-2] + "┣━" + listToString(arr[low:high+1]), "min: " + str(arr[low]))
            return arr[low]
    elif high - low == 0:
        print(indent[:len(indent)-2] + "┣━" + listToString(arr[low:high+1]), "min: " + str(arr[low]))
        return arr[low]
    else:
        print(indent[:len(indent)-2] + "┣━" + listToString(arr[low:high+1]))
        print(indent+ "  ┃ ")
        print(indent+ "  ┃ ")
        mid = (low + high) // 2
        min_kiri = cari_nilai_minimum_DNQ(arr, low, mid, indent + "  ┃ ")
        min_kanan = cari_nilai_minimum_DNQ(arr, mid + 1, high, indent + "  ┃ ")
        if min_kiri < min_kanan:
            print(indent+ "  ┃ ")
            print(indent + "  ┗━", "minimum:",min_kiri)
            print(indent)
            print(indent)
            return min_kiri
        else:
            print(indent+ "  ┃ ")
            print(indent + "  ┗━", "minimum:",min_kanan)
            print(indent)
            print(indent)
            return min_kanan

def listToString(s):
    x = "{ "
    for i in s:
        x += str(i)
        x += " "
    x += "}"
    return x

if __name__ == '__main__':
    # Pembacaan Input File
    teks = "input.txt" # Nama File .txt
    data_file = open(teks, 'r') # Open File dengan mode read 'r'
    arr_int = [] # Inisialisasi list untuk menampung nilai-nilai integer
    arr_str = data_file.read().split() # Inisialisasi list sementara untuk menampung string ketika membaca file
    for i in arr_str: # Looping untuk setiap elemen di array string
        if (i.isnumeric()): # Cek apakah elemen tersebut angka atau bukan
            arr_int.append(int(i)) # Jika angka, maka taruh ke array of integer
    data_file.close() # Close file kalau udah selesai
    
    # Jika panjang array of integer adalah 0 maka list adalah kosong
    if len(arr_int) < 1:
        print("Input Kosong")
    else:
        minimum = arr_int[0]
        print("Pencarian menggunakan Divide & Conquer")
        start1 = time.time()
        minimum = cari_nilai_minimum_DNQ(arr_int, 0, len(arr_int)-1, "  ┃ ")
        end1 = time.time()
        print("  ┗The minimum number in the array is:", minimum)
        print("Time:",(end1-start1) * 10**3, "ms")

        print("\nPencarian menggunakan Brute Force")
        start2 = time.time()
        cari_nilai_minimum_bruteForce(arr_int)
        end2 = time.time()
        print("Time:",(end2-start2) * 10**3, "ms")
