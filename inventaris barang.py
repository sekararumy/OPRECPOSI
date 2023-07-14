### Pendaftaran dan Login ###
def login():
    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "admin123":
        print("Login berhasil!")
        return True
    else:
        print("Login gagal!")
        return False

def input_data():
    if login():
        nama = input("Masukkan nama lengkap: ")
        email = input("Masukkan e-mail: ")
        alamat = input("Masukkan alamat: ")
        username = input("Masukkan username: ")


        # Menyimpan data ke file atau database
        # Contoh disini hanya mencetak data yang diinputkan
        print("Data yang diinputkan:")
        print("Nama:", nama)
        print("Usia:", email)
        print("Alamat:", alamat)
        print

# Menjalankan program
input_data()