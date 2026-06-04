# nilai = float(input("masukkan nilai: "))

# if nilai >100:
#         print("ngarang")
# elif nilai == 100:
#         print("jenius")
# elif nilai >= 90:
#         print("pintar")
# elif nilai >= 80:
#         print("hebat")
# elif nilai >= 70:
#         print("boleh")
# elif nilai >= 60:
#         print ("dikit lagi")
# else:
#         print("dungu")

BB = float (input("masukan berat badan anda:"))
TB = float (input("masukan tinggi badan anda:"))
TB = TB/100
imt = BB / TB**2
print(f"BB: {BB}, TB: {TB}, IMT:{round}")
