def hitung_volume_tabung(diameter, tinggi):
    pi = 3.14
    jari_jari = diameter / 2
    volume_tabung = pi * jari_jari**2 * tinggi
    return volume_tabung
def hitung_volume_kubus(sisi):
    volume_kubus = sisi**3
    return volume_kubus
def hitung_volume_balok(panjang,lebar,tinggi):
    volume_balok = panjang * lebar*tinggi
    return volume_balok

print("==================== KALKULATOR CERDAS ====================")
print("Pilihlah bangun yang ingin anda hitung (inputan angka saja) :")
print("1. Tabung")
print("2. Kubus")
print("3. Balok")

pilihan = int(input(">> "))

if pilihan == 1:
    diameter = int(input("Masukkan diameter (cm) : "))
    tinggi = int(input("Masukkan tinggi (cm) : "))
    volume_tabung = hitung_volume_tabung(diameter, tinggi)
    print("Volume tabung adalah", volume_tabung, "cm³")
elif pilihan == 2:
    sisi = int(input("Masukkan sisi (cm) : "))
    volume_kubus = hitung_volume_kubus(sisi)
    print("Volume kubus adalah", volume_kubus, "cm³")
elif pilihan == 3:
    panjang = int(input(' masukan panjang (cm) : '))
    lebar = int(input(' masukan lebar (cm) : '))
    tinggi = int(input(' masukan tinggi (cm) : '))
    volume_balok =hitung_volume_balok(panjang,lebar,tinggi)
    print("Volume balok adalah", volume_balok, "cm³")
else:
    print('DATA YANG ANDA MASUKAN TIDAK VALID')