from . import Database
from .Util import random_string
import time
import os


def create_first_data():
    penulis = input("Penulis : ")
    judul = input("Judul   : ")
    while True:
        try:
            tahun = int(input("Tahun   : "))
            if len(str(tahun)) == 4:
                break
            else:
                print("\nTahun harus berupa Angka! Silahkan ulangi lagi!\n")

        except:
            print("\nTahun harus berupa Angka! Silahkan ulangi lagi!\n")

    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H:%M:%S")
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis) :]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul) :]
    data["tahun"] = tahun

    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}"
    # print(data_str)

    try:
        with open(Database.DB_NAME, "w", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Gagal Booooskuh!! ")


def read(**kwargs):
    try:
        with open(Database.DB_NAME, "r") as file:
            content = file.readlines()
            jumlah_buku = len(content)
            if "index" in kwargs:
                index_buku = kwargs["index"] - 1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:
                    return content[index_buku]
            else:
                return content

    except:
        print("Membaca Database Error!")
        return False


def create(tahun, judul, penulis):
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H:%M:%S")
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis) :]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul) :]
    data["tahun"] = tahun

    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}"
    # print(data_str)
    try:
        with open(Database.DB_NAME, "a", encoding="utf-8") as file:
            file.write(data_str + "\n")
    except:
        print("Gagal menambahkan data ke file.")


def update(no_buku, pk, date_add, tahun, judul, penulis):
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = date_add
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis) :]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul) :]
    data["tahun"] = str(tahun)

    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}"

    panjang_data = len(data_str)

    try:
        with open(Database.DB_NAME, "r+", encoding="utf-8") as file:
            file.seek(panjang_data * (no_buku - 1))
            file.write(data_str)
    except:
        print("Gagal Mengupdate Data!")


def delete(no_buku):
    try:
        with open(Database.DB_NAME, "r") as file:
            counter = 0
            while True:
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_buku - 1:
                    pass
                else:
                    with open("data_temp.txt", "a", encoding="utf-8") as temp_file:
                        temp_file.write(content)

                counter += 1
    except:
        print("Databse Error")

    os.rename("data_temp.txt", Database.DB_NAME)
