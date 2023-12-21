import datetime
import time
import os

os.system('cls')

def banner():
    print("""
   |================================================================================================|
   |                                   ┏┓  ┓         ┓                                              |
   |                                   ┗┓┏┓┃┏┓┏┳┓┏┓╋┏┫┏┓╋┏┓┏┓┏┓                                     |
   |                                   ┗┛┗ ┗┗┻┛┗┗┗┻┗┗┻┗┻┗┗┻┛┗┗┫                                     |
   |                                                          ┛                                     |
   |================================================================================================|
   |db   dD db      d888888b d8b   db d888888b db   dD      .d8888. d88888b db   db  .d8b.  d888888b|
   |88 ,8P' 88        `88'   888o  88   `88'   88 ,8P'      88'  YP 88'     88   88 d8' `8b `~~88~~'|
   |88,8P   88         88    88V8o 88    88    88,8P        `8bo.   88ooooo 88ooo88 88ooo88    88   |
   |88`8b   88         88    88 V8o88    88    88`8b          `Y8b. 88~~~~~ 88~~~88 88~~~88    88   |
   |88 `88. 88booo.   .88.   88  V888   .88.   88 `88.      db   8D 88.     88   88 88   88    88   |
   |YP   YD Y88888P Y888888P VP   V8P Y888888P YP   YD      `8888Y' Y88888P YP   YP YP   YP    YP   |
   --------------------------------------------------------------------------------------------------""")
    
class Pasien:
    def __init__(self, tipe, nama, kelamin, tanggal_lahir, alamat, nomor_telepon, gejala):
        self.tipe = tipe
        self.nama = nama
        self.kelamin = kelamin
        self.tanggal_lahir = tanggal_lahir
        self.alamat = alamat
        self.nomor_telepon = nomor_telepon
        self.gejala = gejala

    def hitung_usia(self):
        today = datetime.date.today()
        tanggal_lahir = datetime.datetime.strptime(self.tanggal_lahir, "%Y-%m-%d").date()
        usia = today.year - tanggal_lahir.year - ((today.month, today.day) < (tanggal_lahir.month, tanggal_lahir.day))
        return usia
    
    def antrian(self):
        now = datetime.datetime.now()
        noantrian = now.strftime("%y/%m/%d, %H:%M %p")
        return noantrian

    def searchbyname(daftar_pasien, nama_target):
        for pasien in daftar_pasien:
            if pasien.nama == nama_target:
                return pasien
        return None
    
    def searchbynotelpon(daftar_pasien, notelp_target):
        for pasien in daftar_pasien:
            if pasien.nomor_telepon == notelp_target:
                return pasien
        return None
    
class AplikasiKesehatan:
    def __init__(self):
        self.daftar_pasien = []

    def tambah_pasien(self, pasien):
        self.daftar_pasien.append(pasien)

    def tampilkan_pasien(self):
        i=0
        print("""
   |================================================================================================|
   |                                   ┳┓┏┓┏┓┏┳┓┏┓┳┓  ┏┓┏┓┏┓┳┏┓┳┓                                   |
   |                                   ┃┃┣┫┣  ┃ ┣┫┣┫  ┃┃┣┫┗┓┃┣ ┃┃                                   |
   |                                   ┻┛┛┗┻  ┻ ┛┗┛┗  ┣┛┛┗┗┛┻┗┛┛┗                                   |
   |================================================================================================|""")
        for pasien in self.daftar_pasien:
            print()
            print(f"   Tgl. Pendaftaran : {pasien.antrian()}")
            print(f"   No. Antrian      : {i+1}")
            print(f"   Tipe Pasien      : {pasien.tipe}")
            print(f"   Nama             : {pasien.nama}")
            print(f"   Jenis Kelamin    : {pasien.kelamin}")
            print(f"   Usia             : {pasien.hitung_usia()} tahun")
            print(f"   Alamat           : {pasien.alamat}")
            print(f"   Nomor Telepon    : {pasien.nomor_telepon}")
            print(f"   Keluhan Pasien   : {pasien.gejala}")
            i=i+1
        print("                                                       Silakan menunggu Nomor Antrian anda dipanggil.")
        print("   ==================================================================================================")

def main():
    aplikasi = AplikasiKesehatan()

    while True:
        print()
        banner()
        print("   1. Tambah Pasien")
        print("   2. Tampilkan Daftar Pasien")
        print("   3. Cari Data Pasien")
        print("   4. Keluar")

        pilihan = input("   Pilih menu (1/2/3/4): ")

        if pilihan == "1":
            os.system('cls')
            banner()
            print("   1. Pasien Baru")
            print("   2. Pasien Lama")

            type = input("   Pasien (1/2) : ")

            if type == "1":
                tipe = "Pasien Baru"
                nama = input("\n   Nama : ")
                time.sleep(1)
                kelamin = input("   Jenis Kelamin [L/P] : ")
                time.sleep(1)
                tanggal_lahir = input("   Tanggal Lahir (YYYY-MM-DD) : ")
                time.sleep(1)
                alamat = input("   Alamat : ")
                time.sleep(1)
                nomor_telepon = input("   Nomor Telepon (+62) : ")
                time.sleep(1)
                gejala = input("   Keluhan : ")
                time.sleep(1)

                pasien_baru = Pasien(tipe, nama, kelamin, tanggal_lahir, alamat, nomor_telepon, gejala)
                aplikasi.tambah_pasien(pasien_baru)
                print("\n   Pasien berhasil ditambahkan.")
                time.sleep(1)
                os.system('cls')

            elif type == "2":
                tipe = "Pasien Lama"
                nama = input("\n   Nama : ")
                time.sleep(1)
                kelamin = input("   Jenis Kelamin [L/P] : ")
                time.sleep(1)
                tanggal_lahir = input("   Tanggal Lahir (YYYY-MM-DD) : ")
                time.sleep(1)
                alamat = input("   Alamat : ")
                time.sleep(1)
                nomor_telepon = input("   Nomor Telepon (+62) : ")
                time.sleep(1)
                gejala = input("   Keluhan : ")
                time.sleep(1)

                pasien_baru = Pasien(tipe, nama, kelamin, tanggal_lahir, alamat, nomor_telepon, gejala)
                aplikasi.tambah_pasien(pasien_baru)
                print("\n   Pasien berhasil ditambahkan.")
                time.sleep(1)
                os.system('cls')

            else:
                os.system('cls')
                banner()
                print("   Pilihan tidak valid. Silakan pilih kembali.")
                time.sleep(1)
                os.system('cls')

        elif pilihan == "2":
            os.system('cls')
            print("   Memproses Data, Harap Tunggu Beberapa Detik.")
            time.sleep(3)
            os.system('cls')
            aplikasi.tampilkan_pasien()
            input("\n   Press Any Key For Back To Main Menu.")
            os.system('cls')

        elif pilihan == "3":
            os.system('cls')
            time.sleep(1)
            banner()
            print("   1. Cari Berdasarkan Nama.")
            print("   2. Cari Berdasarkan No. Telpon.")

            searchby = input("   Pilih opsi (1/2) : ")

            if searchby == "1":
                time.sleep(1)
                os.system('cls')
                banner()
                nama_target = input("   Masukan Nama Pasien Yang Ingin Dicari : ")
                hasil_cari_nama = Pasien.searchbyname(aplikasi.daftar_pasien, nama_target)

                if hasil_cari_nama:
                    os.system('cls')
                    print("   Mencari Data Pasien... Harap Bersabar.")
                    time.sleep(3)
                    os.system('cls')
                    banner()
                    print()
                    print("\n   Pasien Ditemukan")
                    print(f"   Tgl. Pendaftaran : {hasil_cari_nama.antrian()}")
                    print(f"   No. Antrian      : {aplikasi.daftar_pasien.index(hasil_cari_nama) + 1}")
                    print(f"   Tipe Pasien      : {hasil_cari_nama.tipe}")
                    print(f"   Nama             : {hasil_cari_nama.nama}")
                    print(f"   Jenis Kelamin    : {hasil_cari_nama.kelamin}")
                    print(f"   Usia             : {hasil_cari_nama.hitung_usia()} tahun")
                    print(f"   Alamat           : {hasil_cari_nama.alamat}")
                    print(f"   Nomor Telepon    : {hasil_cari_nama.nomor_telepon}")
                    print(f"   Keluhan Pasien   : {hasil_cari_nama.gejala}")
                else:
                    os.system('cls')
                    print("   Mencari Data Pasien... Harap Bersabar.")
                    time.sleep(3)
                    os.system('cls')
                    banner()
                    print("\n   Pasien Tidak Ditemukan.")
                input("\n   Press Any Key For Back To Main Menu.")
                os.system('cls')

            elif searchby == "2":
                time.sleep(1)
                os.system('cls')
                banner()
                notelp_target = input("   Masukan Nomor Telpon Target (+62) : ")
                hasil_cari_notelp = Pasien.searchbynotelpon(aplikasi.daftar_pasien, notelp_target)

                if hasil_cari_notelp:
                    os.system('cls')
                    print("   Mencari Data Pasien... Harap Bersabar.")
                    time.sleep(3)
                    os.system('cls')
                    banner()
                    print()
                    print("\n   Pasien Ditemukan")
                    print(f"   Tgl. Pendaftaran : {hasil_cari_notelp.antrian()}")
                    print(f"   No. Antrian      : {aplikasi.daftar_pasien.index(hasil_cari_notelp) + 1}")
                    print(f"   Tipe Pasien      : {hasil_cari_notelp.tipe}")
                    print(f"   Nama             : {hasil_cari_notelp.nama}")
                    print(f"   Jenis Kelamin    : {hasil_cari_notelp.kelamin}")
                    print(f"   Usia             : {hasil_cari_notelp.hitung_usia()} tahun")
                    print(f"   Alamat           : {hasil_cari_notelp.alamat}")
                    print(f"   Nomor Telepon    : {hasil_cari_notelp.nomor_telepon}")
                    print(f"   Keluhan Pasien   : {hasil_cari_notelp.gejala}")
                else:
                    os.system('cls')
                    print("   Mencari Data Pasien... Harap Bersabar")
                    time.sleep(3)
                    os.system('cls')
                    banner()
                    print("\n   Pasien Tidak Ditemukan.")
                input("\n   Press Any Key For Back To Main Menu.")
                os.system('cls')
            
            else:
                os.system('cls')
                banner()
                print("   Pilihan tidak valid. Silakan pilih kembali.")
                time.sleep(1)
                os.system('cls')

        elif pilihan == "4":
            os.system('cls')
            print("Terima kasih! Keluar dari aplikasi.")
            break

        else:
            os.system('cls')
            banner()
            print("   Pilihan tidak valid. Silakan pilih kembali.")
            time.sleep(1)
            os.system('cls')

if __name__ == "__main__":
    main()