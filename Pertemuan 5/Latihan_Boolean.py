# Penggunaan pada Struktur Pemilihan (if-else)
x = 5
y = 10
is_greater = x > y
if is_greater:
    print("x lebih besar dari y")
else:
    print("x tidak lebih besar dari y")

# Penggunaan dalam Looping
is_running = True
while is_running:
    user_input = input("Masukkan 'stop' untuk menghentikan: ")
    if user_input.lower() == "stop":
        is_running = False
print("Program dihentikan")

# Penggunaan dalam Fungsi
def is_even(number):
    return number % 2 == 0

num = 10
if is_even(num):
    print(num, "adalah bilangan genap")
else:
    print(num, "adalah bilangan ganjil")

# Penggunaan dalam Penugasan Nilai
is_logged_in = False
username = "user123"
if username != "":
    is_logged_in = True
print("Status login:", is_logged_in)

# Penggunaan dalam Pemeriksaan Keanggotaan
available_colors = ["red", "green", "blue"]
selected_color = "yellow"
is_color_available = selected_color in available_colors
print("Apakah warna tersedia:", is_color_available)
