# Dasar-Dasar Python 2

Sebelumnya, kita telah belajar tipe data umum seperti `string`, `integer`, `float`, `tuple`, `list`, dan `dict`, mengeluarkan output dengan `print`, membuat fungsi, dll.

Sekarang, kita akan mempelajari banyak hal seperti `for`-loop, `while`-loop, dan `import`.

## Fundamental 6 - Looping

Mari kita kenalan dengan `for`-loop. `for`-loop adalah perulangan yang mengambil satu demi satu data yang tersedia.

```python
banyak_angka = [10, 9, 8, 7, 6, 5]

for angka in banyak_angka:
    print(angka) # 10 9 8 7 6 5
```

Cara ini lebih baik daripada materi sebelumnya dimana kita mengekstrak satu demi satu data dan dipisah dengan variabel.

Dan dalam penggunaan for-loop ini. Bagian pertama kita secara otomatis memecah data ke variabel `angka` dari banyak_angka.

Jadi, dari banyak data dipisah menjadi satu data yang nanti diproses lagi agar tidak melakukan repetisi.

<br>

## Fundamental 6.1 - While Loop

Nah, kita sudah menggunakan for-loop yang hanya mengikuti arus dari data `list`. Kita akan mengenal `while`-loop.

`while`-loop adalah salah satu perulangan dimana sebuah perulangan akan terus berjalan sampai suatu kondisi telah berakhir.

Kita akan membuat replika `for`-loop menggunakan `while`-loop.

```python
banyak_angka = [10, 9, 8, 7, 6, 5]
index = 0

while index < len(banyak_angka):
    print(banyak_angka[index]) # 10 9 8 7 6 5
    index += 1
```

**Fungsi baru**! `len` digunakan untuk menghitung berapa banyak data dari suatu kumpulan data, layaknya tadi. `len(banyak_data)` akan mengeluarkan nilai 6.
Fungsi `len` dapat digunakan pada `string` untuk menghitung berapa banyak huruf atau isi didalam suatu tulisan.

Yang pertama, kita mengkondisikan apakah index lebih kecil daripada ukuran dari banyak_angka? Jika iya, kita memprint angka dari index lalu menambahkan index dengan 1 dan ulangi. Jika tidak, selesai.

<br>

## Fundamental 7 - Import

Import adalah suatu cara untuk mengambil beberapa hal yang kita perlu tanpa kita harus membuatnya terlebih dahulu. Di python, ada banyak jenis _modul_ dan _paket_ yang bisa kita gunakan.

Kita akan mengimpor `b64encode`, dan `b64decode` melalui modul `base64`

```python
from base64 import b64encode, b64ddecode
```

Ini akan mengimpor 2 fungsi yang nantinya kita bisa gunakan nanti.

Cara lain agar kita mendapat keseluruhan isi modul adalah dengan berikut:

```python
import base64
```

Namun, kita hanya perlu menambah `base64.` sebelum kita menggunakan fungsi / isian yang ada seperti pada contoh ini:

```python
base64.b64encode
```

Namun, dengan `from`-import:

```python
from base64 import b64encode, b64decode
b64encode
```

Singkat kan? kita hanya mengambil sebagian fungsi saja.

Contoh menggunakan base64 encode dan decode:

```python
from base64 import b64encode, b64decode

nama = "Agus"

tak_jelas = b64encode(agus.encode('utf-8'))

menjadi_jelas = b64decode(tak_jelas).decode('utf-8')

print(nama == menjadi_jelas) # True
```

Pertama, kita mengimport, lalu membuat variabel nama dengan isi "Agus". Kita mengencode nama agus dengan pertama menjadikan tulisan agus menjadi dalam bentuk bita.
Setelah itu kita decode base64 tadi dengan fungsi `b64decode` lalu mendekode lagi agar bisa menjadi bentuk `string` atau tulisan.

**Heads up**! Kita mendapati tipe data baru, `bytes` sekaligus 1 metode untuk `string` dan 1 metode untuk `bytes`

`str.encode` akan mengubah suatu `string` menjadi tipe data `bytes` atau bita dan `bytes.decode` akan mengubah suatu `bytes` menjadi tipe data `string`.

Tipe data bytes itu berguna di masa depan nanti.

---

## Penutup

Sekian, pembelajaran singkat dari saya. Bila ada kesalahan saya memohon maaf sebesar-besarnya. Semoga kalian dapat memahami materi ini.

### Pengarang/Penulis

Dokumen ini diketik oleh [RimuEirnarn](https://github.com/RimuEirnarn). Kode sumber dari gambar, contoh, dll disimpan di [Repository](https://github.com/RimuEirnarn/lessons)

### Hak Cipta

Projek ini dilisensi dengan BSD-3-Clause.