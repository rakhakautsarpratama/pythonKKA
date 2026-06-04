task = []

def tampilkan_menu():
    print("\n===== To Do List =====")
    print("1. Tambah tugas")
    print("2. Lihat tugas")
    print("3. Hapus tugas")
    print("4. Tandai tugas selesai")
    print("5. keluar")



def tambah_tugas():
    tugas = input("Masukan tugas: ")
    task.append({"nama": tugas, "selesai": False})
    print("Tugas berhasil ditambahkan")



def lihat_tugas():
    if len(task) == 0:
        print("Belum ada tugas")
        return
    
    print("\nDaftar tugas:")
    for i, tugas in enumerate(task, start=1):
        status = "✓" if tugas["selesai"] else "X"
        print(f"{i}. {tugas['nama']} [{status}]")


def hapus_tugas():
    lihat_tugas()

    if len(task) == 0:
        return 
    
    try:
        nomor = int(input("Masukkan nomor tugas yang akan dihapus: "))
        if 1 <= nomor <= len(task):
            task.pop(nomor - 1)
            print("Tugas berhasil dihapus!")
        else:
            print("Nomor tugas tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")
        


def tandai_selesai():
    lihat_tugas()

    if len(task) == 0:
        return

    try:
        nomor = int(input("Masukkan nomor tugas yang selesai: "))
        if 1 <= nomor <= len(task):
            task[nomor - 1]["selesai"] = True
            print("Tugas berhasil ditandai selesai!")
        else:
            print("Nomor tugas tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_tugas()
        elif pilihan == "2":
            lihat_tugas()
        elif pilihan == "3":
            hapus_tugas()
        elif pilihan == "4":
            tandai_selesai()
        elif pilihan == "5":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!")


main()