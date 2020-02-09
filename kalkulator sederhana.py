# MEMBUAT KALKULATOR SEDERHANA DENGAN PYTHON

# MENGGUNAKAN PENGULANGAN WHILE

while True:
# MEMBUAT FUNCTION
# FUNCTION PENAMBAHAN
    def tambah(a, b):
        return a + b
# FUNCTION PENGURANGAN
    def kurang(a, b):
        return a - b
# FUNCTION PERKALIAN
    def kali(a, b):
        return a * b
# FUNCTION PEMBAGIAN
    def bagi(a, b):
        return a / b

# PILIHAN OPERASI MATEMATIKA
    print('=' * 50)
    print('PILIHAN OPERASI MATEMATIKA')
    print('1. Penambahan')
    print('2. Pengurangan')
    print('3. Perkalian')
    print('4. Pembagian')
    print('=' * 50)

# MEMINTA USER UNTUK MENGINPUT PILIHAN DAN NILAI
    userInput = input('Masukan Pilihan Anda (1/2/3/4) : ')
    print('=' * 50)

    num1 = int(input('Masukan Nilai Pertama Anda : '))
    num2 = int(input('Masukan Nilai Kedua Anda : '))
    print('=' * 50)

# JIKA USER MENGINPUT 1/2/3/4, MAKA....
    if userInput == '1':
        print('Hasil Dari', num1, '+', num2, '=', tambah(num1, num2))
    elif userInput == '2':
        print('Hasil Dari', num1, '-', num2, '=', kurang(num1, num2))
    elif userInput == '3':
        print('Hasil Dari', num1, 'x', num2, '=', kali(num1, num2))
    elif userInput == '4':
        print('Hasil Dari', num1, ':', num2, '=', bagi(num1, num2))
    else:
        print('Pilihan Yang Anda Masukan Tidak Terdaftar Di List.')

    print('=' * 50)

# MEMINTA USER UNTUK MENGINPUT UNTUK MENGULANG KEMBALI ATAU TIDAKS
    userAgain = input('Ingin Lagi ? (y/n) : ')
    if userAgain == 'y':
        continue
    elif userAgain == 'n':
        print('=' * 50)
        print('Terima Kasih')
        break
    else:
        print('Maaf, Anda Memasukan Kata Kunci Yang Salah.')
        break
