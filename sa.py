def cari_nilai_minimum_bruteForce(arr):
    min_index = 0
    for i in range(1, len(arr)):
        change_min_Index = False
        if arr[i] < arr[min_index]:
            change_min_Index = True
            min_index = i
        print("Iterasi ke-" + str(i) + ": " + "arr[" + str(i) + "] < arr[" + str(min_index) + "]: " + str(change_min_Index ) + ", Nilai minimum sekarang ada di array indeks ke-" + str(min_index))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Nilai minimum ada di array dengan indeks ke-" + str(min_index) + " dengan nilai: " + str(arr[min_index]))

def cari_nilai_minimum_DNQ(arr, low, high, indent=""):
    if high - low <= 1:
        if arr[high] < arr[low]:
            print(indent[:len(indent)-2] + "┣━" + listToString(arr[low:high+1]), "min: " + str(arr[high]))
            return arr[high]
        else:
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
    teks = "input.txt"
    arr_str = []
    arr_int = []
    data_file = open(teks, 'r')
    teks = data_file.readline().replace("\n", "")
    while teks != "":
        data = teks.split()
        teks = data_file.readline().replace("\n", "")
        arr_str.append(data)
        for i in arr_str :
            for n in i :
                arr_int.append(int(n))
    data_file.close()
    minimum, maximum = 0, -1
    # array initialization
    # arr = [6, 2, 3, 5, 1, 2]

    print("Pencarian menggunakan Divide & Conquer")
    minimum = cari_nilai_minimum_DNQ(arr_int, 0, len(arr_int)-1, "  ┃ ")
    print("  ┗The minimum number in the array is:", minimum)

    print("\nPencarian menggunakan Brute Force")
    cari_nilai_minimum_bruteForce(arr_int)