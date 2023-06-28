from . import Operasi
import os


def read_console():
    data_file = Operasi.read()
    index_label = "No"
    judul_label = "Judul"
    penulis_label = "Penulis"
    tahun_label = "Tahun"

    # Header
    os.system("clear")
    print("\n" + "=" * 103)
    print(
        f"|  {index_label}   | {judul_label:^40} | {penulis_label:^40} | {tahun_label:^5} |"
    )
    print("-" * 103)
    # Data
    for index, data in enumerate(data_file):
        data_break = data.split(",")
        if len(data_break) >= 5:
            pk = data_break[0].strip()
            date_add = data_break[1].strip()
            penulis = data_break[2].strip()
            judul = data_break[3].strip()
            tahun = data_break[4].strip()

            index_str = str(index + 1).ljust(2)[:2]
            judul = judul.ljust(40)[:40]
            penulis = penulis.ljust(40)[:40]
            tahun = tahun.ljust(4)[:4]

            print(f"|   {index_str}  | {judul} | {penulis} | {tahun}  |")

    # Footer
    print("=" * 103 + "\n")


def create_console():
    print("=" * 46)
    print("   Masukan Data Buku yang ingin ditambahkan!")
    print("=" * 46)

    print()
    penulis = input("   Penulis : ")
    while not penulis.strip():
        print("   Penulis tidak boleh kosong. Mohon masukan kata!")
        penulis = input("   Penulis : ")

    judul = input("   Judul   : ")
    while not judul.strip():
        print("   Judul tidak boleh kosong. Mohon masukkan kata!")
        judul = input("   Judul   : ")

    while True:
        try:
            tahun = int(input("   Tahun   : "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus berupa Angka! Silahkan ulangi lagi!")
        except:
            print("Tahun harus berupa Angka! Silahkan ulangi lagi!")

    Operasi.create(tahun, judul, penulis)
    print()
    print(" Yeayy... Data Berhasil Ditambahkan!\n")
    stop = input(" Tekan ENTER untuk melihat data...")
    read_console()


def update_console():
    read_console()
    while True:
        print("=" * 52)
        print("   Silahkan Masukan Nomor Buku yang ingin diubah!")
        print("=" * 52)

        no_buku = input("    Nomor buku : ")
        while not no_buku.isdigit():
            print(
                "\n    Nomor buku hanya boleh berisi angka.\n    Mohon masukkan nomor buku yang valid.\n"
            )
            no_buku = input("    Nomor buku: ")

        no_buku = int(no_buku)

        data_buku = Operasi.read(index=no_buku)
        if data_buku:
            break
        else:
            print("Nomor tidak ada! Mohon masukan no yang sesuai!")

    data_break = data_buku.split(",")
    pk = data_break[0]
    date_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]

    while True:
        print("=" * 52)
        print("Silahkan pilih data yang ingin anda ubah!")
        print(f"1. Judul   : {judul:.40}")
        print(f"2. Penulis : {penulis:.40}")
        print(f"3. Tahun   : {tahun:.4}")

        user_option = input("Pilih data 1-3 : ")
        print("=" * 52)

        match (user_option):
            case "1":
                judul = input("Judul   : ")

            case "2":
                penulis = input("Penulis   : ")

            case "3":
                while True:
                    try:
                        tahun = int(input("Tahun   : "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("Tahun harus berupa Angka! Silahkan ulangi lagi!")
                    except:
                        print("Tahun harus berupa Angka! Silahkan ulangi lagi!")

            case _:
                print("Data tidak ada yang cocok! hanya 1 -3 saja")

        print("\n" + "=" * 52)
        print("Data sudah di ubah!")
        print(f"1. Judul   : {judul:.40}")
        print(f"2. Penulis : {penulis:.40}")
        print(f"3. Tahun   : {tahun:.4}")

        is_done = input("Apakah Data sudah Sesuai? (y/n) ")
        if is_done == "y" or is_done == "Y":
            break
    Operasi.update(no_buku, pk, date_add, tahun, judul, penulis)


def delete_console():
    read_console()
    while True:
        no_buku = int(input("Nomor buku: "))
        print("Silahkan pilih No Buku yang ingin dihapus!")
        data_buku = Operasi.read(index=no_buku)
        if data_buku:
            data_break = data_buku.split(",")
            pk = data_break[0]
            date_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]
            print("\n" + "=" * 80)
            print("Data yang ingin Anda hapus!")

            print(f"1. Judul   : {judul:.40}")
            print(f"2. Penulis : {penulis:.40}")
            print(f"3. Tahun   : {tahun:.4}")
            is_done = input("Apakah data sudah sesuai? (y/n) ")
            if is_done == "y" or is_done == "Y":
                Operasi.delete(no_buku)
                break

        else:
            print("Nomor tidak ada! Mohon masukkan nomor yang sesuai!")

    print("Data berhasil dihapus!")
