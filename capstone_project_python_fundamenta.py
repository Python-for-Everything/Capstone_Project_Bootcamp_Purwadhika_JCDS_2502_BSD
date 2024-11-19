# Aplikasi Manajemen Perangkat Keras Jaringan Dengan Fitur Pencarian

# Penyimpanan Data

daftar_perangkat = {
   0: {"firewall": "Cisco ASA", "Qty": 2, "Harga": 1000000.00},
   1: {"firewall": "Fortigate", "Qty": 2, "Harga": 500000000},
   2: {"firewall": "Check Point", "Qty": 2, "Harga": 1000000000},
   3: {"firewall": "Sophos XG Firewall", "Qty": 2, "Harga": 1000000.00},
   4: {"firewall": "Paloalto Networks", "Qty": 2, "Harga": 2000000000},
   5: {"firewall": "Juniper SRX", "Qty": 2, "Harga": 1000000000},
   6: {"router": "Cisco ISR", "Qty": 2, "Harga": 1000000000},
   7: {"router": "Fortinet Switch", "Qty": 2, "Harga": 1000000000},
   8: {"router": "Juniper MX", "Qty": 2, "Harga": 1000000000},
   9: {"wifi_controller": "Cisco WLC", "Qty": 2, "Harga": 2000000000},
   10: {"wifi_controller": "Fortinet WLC", "Qty": 2, "Harga": 1000000000},
   11: {"access_point": "Cisco Aironet", "Qty": 2, "Harga": 2000000000},
   12: {"access_point": "Aruba Controller", "Qty": 2, "Harga": 2000000000},
   13: {"load_balancer": "Cisco Nexus Load Balancer", "Qty": 2, "Harga": 2000000000},
   14: {"load_balancer": "F5", "Qty": 2, "Harga": 2000000000},
   15: {"vpn_gateway": "Cisco AnyConnect", "Qty": 2, "Harga": 2000000000},
   16: {"vpn_gateway": "Fortigate VPN", "Qty": 2, "Harga": 1000000000},
   17: {"vpn_gateway": "Sophos XG Firewall", "Qty": 2, "Harga": 2000000000},
   18: {"ids_ips": "Cisco Firepower", "Qty": 2, "Harga": 2000000000},
   19: {"ids_ips": "Fortigate IPS", "Qty": 2, "Harga": 2000000000},
   20: {"utm_appliance": "Cisco Meraki", "Qty": 2, "Harga": 2000000000},
   21: {"utm_appliance": "Fortigate UTM", "Qty": 2, "Harga": 2000000000},
   22: {"utm_appliance": "CheckPoint UTM", "Qty": 2, "Harga": 2000000000},
   23: {"utm_appliance": "Sophos XG UTM", "Qty": 2, "Harga": 2000000000},
}

# Fungsi Tampilkan Menu Utama dan Jalankan Pilihan
def menu_utama():
   while True:
       print("\nMenu Utama - Manajemen Perangkat Keras Jaringan")
       print("1. Lihat Perangkat")
       print("2. Tambah Perangkat")
       print("3. Perbaharui Perangkat")
       print("4. Hapus Perangkat")
       print("5. Cari Perangkat")
       print("6. Keluar")

       pilihan = input("Pilih Opsi: ")
       if pilihan == "1":
           menu_baca_perangkat()
       elif pilihan == "2":
           menu_tambah_perangkat()
       elif pilihan == "3":
           menu_perbarui_perangkat()
       elif pilihan == "4":
           menu_hapus_perangkat()
       elif pilihan == "5":
           menu_cari_perangkat()
       elif pilihan == "6":
           print("Keluar Program")
           break
       else:
           print("Pilihan Opsi Tidak Valid. Silahkan Pilih Opsi 1 - 6")

# Fungsi Menu Untuk Baca Perangkat
def menu_baca_perangkat():
   if not daftar_perangkat:
       print("Data Yang Anda Cari Tidak Ada.")
       return

   print("\nMenu Baca Perangkat")
   print("1. Tampilkan Semua Daftar Perangkat Jaringan")
   print("2. Kembali Ke Menu Utama")

   pilihan = input("Pilih Opsi 1 atau 2: ")
   if pilihan == "1":
       tampilkan_semua_perangkat()
   elif pilihan == "2":
       return
   else:
       print("Opsi Tidak Valid. Kembali Ke Menu Utama.")

# Fungsi Menu Tampilkan Semua Perangkat
def tampilkan_semua_perangkat():
   print("\nSemua Data Perangkat Jaringan: ")
   for key, item in daftar_perangkat.items():
       print(f"ID: {key}")
       for detail, value in item.items():
           print(f" {detail}: {value}")
       print() # Tambahkan baris kosong untuk setiap perangkat

# Fungsi Menu Tambah Perangkat
def menu_tambah_perangkat():
   print("\n--- Tambah Perangkat Jaringan Baru ---")
   try:
       id_perangkat = int(input("Masukkan ID Perangkat Jaringan Baru: "))
   except ValueError:
       print("ID Perangkat Harus Berupa Angka. ")
       return

   # Periksa Apakah ID Perangkat Sudah ada dalam daftar_perangkat
   if id_perangkat in daftar_perangkat:
       print("ID Perangkat Sudah Ada Dalam Inventaris. ")
       return

   # Minta Pengguna Memasukkan Informasi Perangkat Jaringan
   jenis_perangkat = input("Masukkan Jenis Perangkat (Misal: Firewall, Router, Access_Point, Wifi_Controller, "
                           "Load_Balancer, VPN_Gateway, IDS_IPS, UTM_Appliance): ").lower()
   nama_perangkat = input(f"Masukkan Nama {jenis_perangkat}: ")
   try:
       qty = int(input("Masukkan Jumlah Perangkat {Qty}: "))
   except ValueError:
       print("Jumlah Perangkat Harus Berupa Angka. ")
       return

   try:
       harga = float(input("Masukkan Harga Perangkat: "))
   except ValueError:
       print("Harga Perangkat Harus Berupa Angka. ")
       return

   # Tambahkan Perangkat Baru Ke Dictionary daftar_perangkat
   perangkat_baru = {
       jenis_perangkat: nama_perangkat,
       "Qty": qty,
       "Harga": harga
   }

   daftar_perangkat[id_perangkat] = perangkat_baru
   print("Perangkat Baru Berhasil diTambahkan ke Inventaris.")

# Fungsi Menu Perbaharui Perangkat
def menu_perbarui_perangkat():
   print("\n--- Perbaharui Perangkat ---")
   try:
       id_perangkat = int(input("Masukkan ID Perangkat Yang Ingin diPerbaharui: "))
   except ValueError:
       print("ID Perangkat Harus Berupa Angka. ")
       return

   perangkat = daftar_perangkat.get(id_perangkat)
   if not perangkat:
       print("Perangkat dengan ID Tersebut Tidak diTemukan. ")

   print(f"\nData Perangkat Saat Ini untuk ID {id_perangkat}: ")
   for detail, value in perangkat.items():
       print(f" {detail}: {value}")

   # Memperbaharui Detail Perangkat
   jenis_perangkat = input("Masukkan Jenis Perangkat Baru (kosongkan untuk Tidak Mengubah): ").lower()
   if jenis_perangkat:
       nama_perangkat = input("Masukkan Nama {Jenis Perangkat} Baru: ")
       perangkat.clear() # Menghapus item lama agar tidak terjadi duplikasi jenis perangkat
       perangkat[jenis_perangkat] = nama_perangkat

   try:
       qty = input("Masukkan Jumlah Perangkat Baru (Qty) (Kosongkan untuk Tidak Mengubah): ")
       if qty:
           perangkat["Qty"] = int(qty)
   except ValueError:
       print("Jumlah Perangkat harus Berupa Angka. ")
       return

   try:
       harga = input("Masukkan Harga Perangkat Baru (Kosongkan untuk Tidak Mengubah): ")
       if harga:
           perangkat["Harga"] = float(harga)
   except ValueError:
       print("Harga Perangkat Harus Berupa Angka. ")
       return

   print("Data Perangkat Berhasil diPerbaharui.")

# Fungsi Menu Hapus Perangkat
def menu_hapus_perangkat():
   print('\n--- Hapus Perangkat ---')
   try:
       id_perangkat = int(input("Masukkan ID Perangkat yang Ingin diHapus: "))
   except ValueError:
       print("ID Perangkat harus Berupa Angka.")

   if id_perangkat in daftar_perangkat:
       # Konfirmasi Hapus
       konfirmasi = input(f"Apakah Anda Yakin ingin Menghapus Perangkat dengan ID {id_perangkat}? (ya/tidak: ").lower()
       if konfirmasi == "ya":
           print("Perangkat Berhasil diHapus dari Inventaris.")
       else:
           print("Penghapusan diBatalkan.")
   else:
       print("Perangkat dengan ID Tersebut Tidak diTemukan.")

# Fungsi Menu Cari Perangkat
def menu_cari_perangkat():
   try:
       id_perangkat = int(input("Masukkan ID Perangkat yang ingin diCari: "))
   except ValueError:
       print("ID Perangkat Harus Berupa Angka.")
       return

   perangkat = daftar_perangkat.get(id_perangkat)
   if perangkat:
       print(f"\nPerangkat dengan ID {id_perangkat} ditemukan: ")
       for detail, value in perangkat.items():
           print(f" {detail}: {value}")
   else:
           print(f"Perangkat dengan ID {id_perangkat} tidak diTemukan.")

# Menjalankan Aplikasi
menu_utama()

