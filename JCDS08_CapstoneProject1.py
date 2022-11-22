data_barang = {
    'mnns01' : {'Kode' : 'MNNS01','Kat.': 'MNM', 'Nama Produk': 'Bear Brand Kaleng 189 ml', 'Produsen': 'NESTLE', 'Stok': 808, 'Satuan': 'kaleng', 'Harga': 10000},  
    'mnff01': {'Kode' : 'MNFF01','Kat.': 'MNM', 'Nama Produk': 'Bendera Kental Manis 370gr', 'Produsen':'FRISIAN', 'Stok': 700, 'Satuan': 'kaleng', 'Harga': 15000},
    'mkmy01' : {'Kode' : 'MKMY01', 'Kat.': 'MKN', 'Nama Produk': 'Roma Kelapa Original 300gr', 'Produsen':'MAYORA', 'Stok': 1204, 'Satuan': 'pcs', 'Harga': 20000},
    'mkmo01' : {'Kode' : 'MKMO01','Kat.': 'MKN', 'Nama Produk' : 'Oreo Cokelat Original 119.6gr', 'Produsen':'MONDELEZ', 'Stok': 1204, 'Satuan': 'pcs', 'Harga': 17000},
    'bmin01' : {'Kode' : 'BMIN01', 'Kat.': 'BMK', 'Nama Produk' : 'Indomie Goreng Original 85gr', 'Produsen':'INDOFOOD', 'Stok': 1000, 'Satuan': 'pcs', 'Harga': 3000}
    }

def print_header():
     print('\n Kode \t|Kat. \t|Nama Produk \t\t\t|Produsen \t|Stok (sat.) \t|Harga')
def print_data(key):
    print('{} \t|{} \t|{} \t|{} \t|{} {} \t|{}'.format(data_barang[key]['Kode'],data_barang[key]['Kat.'], data_barang[key]['Nama Produk'], data_barang[key]['Produsen'], data_barang[key]['Stok'], data_barang[key]['Satuan'], data_barang[key]['Harga']))
def print_input_salah():
    print("\nMenu Tidak Tersedia, Silakan Kembali ke Menu Awal")


#Menampilkan semua data
def default_data():
    if len(data_barang) == 0:
        print("Tidak Ada Data")
    else:
         print('='*100)
         print(' '*30+'DAFTAR BARANG')
         print('='*100)
         print_header()
         for key in data_barang.keys():
            print_data(key)

#Menu untuk menampilkan data        
def view_data_barang():
    while len(data_barang) == 0:
        print("Tidak Ada Data")
        break
    else:
        while True:
            pilih_menu_view = input('\n********** MENU BARANG ********** \n1. Lihat Semua Data Barang \n2. Lihat Berdasarkan Kategori Barang \n3. Cari berdasarkan Nama Produk \n4. Kembali ke Menu Utama \n \nPilih Menu: \n')

            if pilih_menu_view == '1':  #menampilkan semua data
                default_data()
                
            elif pilih_menu_view == '2': #menampilkan data berdasarkan Kategori Barang
                pilih_kategori = input('\n********** DAFTAR KATEGORI BARANG ********** \n1. Makanan \n2. Minuman \n3. Bahan Makanan \n4. Kembali Ke Menu Awal \nPilih Kategori Produk: \n')
                if pilih_kategori == '1': #menampilkan kategori makanan
                    print_header()
                    for key in data_barang.keys(): 
                        if data_barang[key]['Kat.']== 'MKN':
                            print_data(key)
                        else:
                            continue
                elif pilih_kategori == '2': #menampilkan kategori minuman
                    print_header()
                    for key in data_barang.keys(): 
                        if data_barang[key]['Kat.']== 'MNM':
                            print_data(key)
                elif pilih_kategori == '3': #menampilkan kategori bahan makanan
                    print_header()
                    for key in data_barang.keys(): 
                        if data_barang[key]['Kat.']== 'BMK':
                            print_data(key)
                elif pilih_kategori == '4': #kembali ke menu utama
                    break
                else:
                    print('\n-Kategori Tidak Tersedia-')
            
            #Menampilkan menu pencarian Nama Produk
            elif pilih_menu_view == '3':
                search = input('Masukkan Nama Produk: \n')
                print_header()
                for key in data_barang.keys():
                    if search.lower() in data_barang[key]['Nama Produk'].lower():
                        print_data(key)
                    else:
                        continue

            #kembali ke menu utama
            elif pilih_menu_view == '4':
                break
            else: 
                print_input_salah()
                break

#Menu untuk menambahkan data
def tambah_data_barang():
    while True:
        default_data()
        input_kode = input('\nMasukkan Kode Barang Baru:').upper()              #input kode
        new_input_kode = input_kode.replace('','')
        if new_input_kode.lower() not in data_barang.keys():
            print('\nSilakan Input Data Barang yang Ingin Ditambahkan\n')
            input_kategori_baru = input('Kategori \t: ').upper()                #input kategori
            input_nama_baru = input('Nama Produk \t: ')                         #input nama produk        
            while len(input_nama_baru) < 5:
                    print('\n!!! Nama Minimal 5 Karakter !!!')
                    input_nama_baru = input('Nama Produk \t: ')
            input_produsen_baru = input('Nama Produsen \t: ')                   #input nama produsen
            while True:
                try:
                    input_harga_baru = int(input('Harga \t\t: '))               #input harga produk
                    while input_harga_baru < 1:
                        print('\n!!! Harga tidak bisa kurang dari 1 !!!')
                        input_harga_baru = int(input('Harga \t\t: '))
                    break
                except:
                    print('\n!!! Silakan Masukkan Angka !!!')
            while True:
                try:
                    input_stok_baru = int(input('Stok \t\t: ' ))                #input stok produk
                    while input_stok_baru < 0:
                        print('\n!!! Stok tidak bisa kurang dari 0 !!!')
                        input_stok_baru = int(input('Stok \t\t: ' )) 
                    break
                except:
                    print('\n!!! Silakan Masukkan Angka !!!')
            input_satuan_baru = input('Satuan\t\t: ').lower()
            check = input(f'Apakah Yakin Ingin Menambahkan Data {input_kode} - {input_nama_baru} - {input_produsen_baru}, dengan harga {input_harga_baru} dan stok {input_stok_baru} {input_satuan_baru}? Yes/No\n')
            if check.lower() != 'yes':
                print('\n-Data tidak tersimpan-')
                break
            else:
                data_barang[input_kode]={'Kode' : input_kode, 'Kat.': input_kategori_baru, 'Nama Produk' : input_nama_baru, 'Produsen': input_produsen_baru, 'Stok': input_stok_baru, 'Satuan': input_satuan_baru, 'Harga': input_harga_baru}
                print('\n-Data Berhasil Ditambahkan-')
                break
        else:
            print('\n-Data Sudah Ada-')
            break

#Menu untuk mengubah data 
def ubah_data_barang():
        default_data()
        ubah_data = input('Masukkan Kode Barang yang Akan Diubah: \n')
        update_data = ubah_data.replace('','')
        while update_data.lower() in data_barang.keys():      
            pilih_update = input('\n********** PILIH DATA YANG AKAN DIUBAH ********** \n1. Nama Produk \n2. Jumlah Stok \n3. Harga \n4. Kembali Ke Menu Awal \nPilih Data yang Ingin Diubah: \n')
            if pilih_update == '1':                                             #update nama produk
                update_nama = input('\nMasukkan Nama Baru: \n')
                while len(update_nama) < 5:
                    print('\n!!! Nama Minimal 5 Karakter !!!')
                    update_nama = input('\nMasukkan Nama Baru: \n')
                check1 = input('Apakah Yakin Diubah? Yes/No \n')
                if check1.lower() != 'yes':
                    break
                else:
                    data_barang[update_data.lower()]['Nama Produk'] = update_nama
                    default_data()
                    break
            elif pilih_update == '2':                                           #update jumlah stok
                while True:
                    try:
                        update_stok = int(input('\nMasukkan Jumlah Stok Baru: \n'))
                        while update_stok < 0:
                            print('\n!!! Stok tidak bisa kurang dari 0 !!!')
                            update_stok = int(input('\nMasukkan Jumlah Stok Baru: \n'))
                        break
                    except:
                        print('\n!!! Silakan Masukkan Angka !!!') 
                check2 = input('Apakah Yakin Diubah? Yes/No \n')
                if check2.lower() != 'yes':
                    break
                else:
                    data_barang[update_data.lower()]['Stok'] = update_stok
                    default_data()
                break
            elif pilih_update == '3':                                           #update harga produk  
                while True:
                    try:
                        update_harga = int(input('\nMasukkan Harga Baru: \n'))
                        while update_harga < 1:
                            print('\n!!! Harga tidak bisa kurang dari 1 !!!')
                            update_harga = int(input('\nMasukkan Harga Baru: \n'))
                        break
                    except:
                        print('\n!!! Silakan Masukkan Angka !!!')
                check3 = input('Apakah Yakin Diubah? Yes/No \n')
                if check3.lower() != 'yes':
                    break
                else:
                    data_barang[update_data.lower()]['Harga'] = update_harga
                    default_data()
                break
            else: 
                print_input_salah()
                break

#Menu untuk menghapus data
def hapus_data_barang():
    default_data()
    delete_data = input('\nMasukkan Kode Barang yang Ingin Dihapus\n')
    new_delete_data = delete_data.replace('','')
    while new_delete_data.lower() not in data_barang.keys():
        print('\n-Tidak Ada Data-')
        break
    else:
        check4 = input('Apakah Anda Yakin Ingin Menghapus Data? Yes/No \n')
        while check4.lower() != 'yes':
            print('\n-Data Tidak Dihapus-')
            break
        else:
            del data_barang[new_delete_data.lower()]
            default_data()
            print('\n-Data Berhasil Dihapus-')


while True:
    pilih_menu = input('''
-------------------------------------------------------------------------------------------------------
++++ TOKO POJOK SOBARI ++++
-------------------------------------------------------------------------------------------------------
    MAIN MENU
1. View Data Barang
2. Tambah Data Barang
3. Ubah Data Barang
4. Hapus Data Barang
5. Keluar dari Program
Masukkan nomor menu yang akan dituju: \n''')

    if pilih_menu == '1':
        view_data_barang()
    elif pilih_menu == '2':
        tambah_data_barang()
    elif pilih_menu == '3':
        ubah_data_barang()
    elif pilih_menu == '4':
        hapus_data_barang()
    elif pilih_menu == '5':
        quit()
    else:
        print_input_salah()