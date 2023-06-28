import os
import CRUD as CRUD
import string

if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix":
            os.system("clear")
        case "nt":
            os.system("cls")

    print("=" * 30)
    print("  SELAMAT DATANG DI PRGORAM")
    print("    DATABASE PERPUSTAKAAN")
    print("=" * 30)

CRUD.init_console()

while True:
    os.system("clear")
    print("=" * 80)
    print(f"{'SELAMAT DATANG DI PROGRAM DATABASE PERPUSTAKAAN':^80}")
    print("=" * 80)
    print("")
    print(" " * 3, "1. Read Data")
    print(" " * 3, "2. Create Data")
    print(" " * 3, "3. Update Data")
    print(" " * 3, "4. Delete Data\n")

    user_option = input(" Masukkan Opsi : ")
    print("")

    match user_option:
        case "1":
            CRUD.read_console()
        case "2":
            CRUD.create_console()
        case "3":
            CRUD.update_console()
        case "4":
            CRUD.delete_console()
        case _:
            print("  Opsi tidak sesuai ")
            input("Tekan enter untuk melanjutkan...")
            continue

    is_done = input("  Apakah ingin Keluar dari Program? (y/n) ")
    if is_done == "y" or is_done == "Y":
        break

print("\n    Program berakhir terimakasih kakak\n")
