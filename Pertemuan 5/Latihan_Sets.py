# membuat sebuah set dengan tipe data integer
student_id = {2021071001, 2021071002, 2021071003, 2021071004, 2021071005}
print('ID Mahasiswa:', student_id)

# membuat sebuah set dengan tipe data string
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Huruf Vokal:', vowel_letters)

# membuat sebuah set dengan tipe data campuran
mixed_set = {'Halo', 404, -2, 'Selamat tinggal'}
print('Set dengan tipe data campuran:', mixed_set)

# Menambahkan elemen ke dalam set
student_id.add(2021071006)
print('Setelah menambahkan elemen baru:', student_id)

# Menghapus elemen dari set
student_id.remove(2021071003)
print('Setelah menghapus elemen:', student_id)

# Operasi matematika pada set
even_numbers = {2, 4, 6, 8, 10}
odd_numbers = {1, 3, 5, 7, 9}

# Gabungan (union) dari dua set
all_numbers = even_numbers.union(odd_numbers)
print('Gabungan dari dua set:', all_numbers)

# Irisan (intersection) dari dua set
common_numbers = even_numbers.intersection(odd_numbers)
print('Irisan dari dua set:', common_numbers)

# Selisih (difference) antara dua set
difference_numbers = even_numbers.difference(odd_numbers)
print('Selisih antara dua set:', difference_numbers)

# Menghapus semua elemen dari set
mixed_set.clear()
print('Setelah menghapus semua elemen:', mixed_set)
