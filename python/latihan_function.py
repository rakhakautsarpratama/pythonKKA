# def hai():
#     print("hallo")
# hai() 
# print("Rakha")

# def data(nama,umur):
#     print("nama:", nama)
#     print("umur", umur)
# data("rakha", 16) 

# def tambah(a, b):
#     return a + b

# hasil = tambah(5, 3)
# print(hasil)

# def luas_persegi(s):
#     return s * s

# hasil = luas_persegi(4)
# print(hasil + 10)

# def hitung_gaji(gaji_pokok, bonus):
#     return gaji_pokok + bonus

# gaji_rakha = hitung_gaji(3000000, 500000)
# pajak = gaji_rakha *0.1

# print("gaji bersih:", gaji_rakha - pajak)

# def rata_rata(nilai1, nilai2, nilai3):
#     return (nilai1 + nilai2 + nilai3) / 3

# hasil = rata_rata(80, 90, 100)
# print("rata-rata nilai rakha:", hasil)

def login(username, password):
    if username == "admin" and password == "123":
        return "login berhasil"
    else:
        return"login gagal"
    
    print(login("admin", "123"))
    print(login("admin", "456"))