# Materi 1 - Dasar-Dasar Python

## Pendahuluan

Menurut [Wikipedia](https://id.wikipedia.org/wiki/Python_(bahasa_pemrograman)), Python adalah bahasa pemrograman tujuan umum yang ditafsirkan, tingkat tinggi. Dibuat oleh Guido van Rossum dan pertama kali dirilis pada tahun 1991, filosofi desain Python menekankan keterbacaan kode dengan penggunaan spasi putih yang signifikan.

Singkatnya, Python adalah bahasa pemrograman tahun 1991 yang mudah untuk digunakan.

## Mengunduh dan Menginstall Python

Kita akan menggunakan Python3.11 dalam pembelajaran ini.

### Instalasi Windows

Kamu hanya perlu mengunduh Python [disini](https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe) dan jalankan saja aplikasinya.

### Instalasi Linux

Kamu perlu mengunduh kode sumber Python [disini](https://www.python.org/ftp/python/3.11.2/Python-3.11.2.tgz) dan ikuti panduan di file README.md

Apabila tidak terdapat cara, ikuti cara dibawah ini:

```bash
./configure
make
make test
sudo make altinstall
```

### Menjalankan Python

Di Windows, kita akan membuka cmd dan mengetik

```bash
py
```

atau linux dengan

```bash
python
```

Setidaknya, hasil keluaran yang kita inginkan seperti ini:

```
Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

## Fundamental Python

Karena Python adalah bahasa level tinggi dan penuh dengan bahasa inggris. Kita akan mempelajari hal-hal yang biasa digunakan di Python seperti `for`-loop, `while`-loop, fungsi, _lambda_, dll.

### Fundamental 1 - Halo Dunia!

Berikut adalah kode file python untuk mengeluarkan output "Hello, World!"

```python
print("Hello, World!")
```

Kode diatas hanya mengeluarkan output "Hello, World" dengan memanggil fungsi print, seperti printer, fungsi print bertugas untuk memberikan hasil visual pada pengguna akhir. Silahkan kalian coba dengan mengetik kode tersebut di _interpreter_ kalian

**Catatan**: Interpreter adalah perintah Python yang sebelumnya kita gunakan, di Windows CMD dengan perintah `py` dan `python` di Linux.

### Fundamental 2 - Variabel

Variabel adalah suatu data dengan simbol (huruf, angka, atau _) yang memiliki sebuah data lain seperti Angka, String/Tulisan, Bilangan asli, imajiner, dll.

Variabel juga seperti ember yang dapat menampung air. Kita dapat mengganti isinya dengan membuang terlebih dahulu atau mencampurkannya dengan hal lainnya.

Di matematika, variabel sering ditemui, seperti `n = 1`, `f = 40`, dll.

Dalam Python dan banyak bahasa lainnya juga mengikuti aturan variabel yang sama. Dan dengan begitu, mari kita mulai!

```python
nama = "Agus"
umur = 50
jenis_kelamin = "Pria"
status = "Presiden Korea Utara"
```

Di kode diatas, kita mambuat variabel nama dengan data "Agus", umur dengan nilai 50, jenis kelamin dengan "Pria", dan status dengan "Presiden Korea Utara".

Kita dapat menggunakan variabel setelah kita membuatnya. Berikut adalah contoh yang salah.

```python
print(nama)
nama = "Agus"
```

Ketika kamu mencobanya, pasti akan keluar tulisan seperti ini:

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'nama' is not defined
```

Itu karena kita terlambat membuat variabel nama. Mari kita susun kode tersebut dengan benar.

```python
nama = "Agus"
print(nama)
```

Nah, pasti yang keluar adalah Agus! Bagaimana? Sudah paham? Setelah ini kita akan melanjutkan pembelajaran kita ke Fundamental 3.

**Catatan**: Variabel dapat ditimpa/dibuat ulang atau juga digunakan sebagai data dari variabel lain

**Menimpa/Membuat lagi variabel**

```python
nama = "Agus"
nama = "Bambang"
```

**Menggunakan variabel sebagai nilai variabel lain**

```python
nama = "Agus"
nama_depan = nama
```

### Fundamental 3 - Tipe data variabel

Kita tadi membuat variabel-variabel dengan nilai dan bentuk yang berbeda, di bagian ini aku akan menjelaskan variabel tadi seperti `nama` dan `umur`. Serta tipe data lain yang mungkin akan berguna.

Di python, setidaknya ada beberapa tipe data seperti `string`, `integer`, `float`, `bytes`, `dict`, `tuple`, `list`, dan `set`.

Di pembelajaran ini, kita hanya akan membahas 3 tipe data saja, yaitu `string`, `integer`, dan `float`.

**Kode Snippet**

```python
nama = "Agus"
umur = 50
nilai = 99.52
```

Coba kalian berpikir sejenak... Apakah variabel tersebut mudah dipahami atau terasa familiar?

Jika sulit dipahami, Oke. Jadi, variabel `nama` kita buat dengan nilai "Agus" atau tulisan "Agus". Ini adalah contoh tipe data `string`.

Variabel berikutnya, `umur` kita buat dengan nilai 50. Ini adalah contoh tipe data `integer` atau bilangan bulat.

Variabel berikutnya `nilai` kita buat dengan nilai 99.52. Ini adalah contoh tipe data `float` atau bilangan asli.

### Fundamental 3.5 - Penamaan variabel yang benar.

Mungkin belum kujelaskan. Mari kita buat ini lebih detail lagi. Kita hanya boleh membuat variabel dengan aturan tertentu. Yaitu, hanya boleh dengan huruf, angka, dan _.

Berikut ini adalah contoh penamaan variabel yang salah:

```python
00nama = "Nama"
nama nya agus = "Agus"
```

Di baris pertama, `00nama` tidak sah karena angka mendahului huruf. Tetapi, variabel seperti `_00nama` tetap diperbolehkan.

### Fundamental 4 - Banyak data.

Kita tidak mungkin membuat banyak sekali variabel hanya untuk menyimpan data-data umum seperti nama, umur, dan nilai secara terpisah begitu saja (kecuali dengan alasan khusus).

Pertama, kita mulai dengan `list`. Apa itu `list`? `list` adalah tipe data Python dimana kita bisa memasukkan data-data sekaligus dalam 1 variabel menggunakan index.

Bayangkan `list` sebagai antrian-antrian orang yang berbelanja. Mereka mengantri secara teratur dan dinamis (mereka dapat meninggalkan tempat mereka atau ada orang lain ikut dalam antrian).

Kita membuat `list` dengan cara berikut:

```python
agus = ["Agus", 50, 99.51]
```

"Oke, kita udah buat nih, `list` dengan nama agus. Terus bagaimana kita bisa memprint data-data di dalam variabel agus?"

Karena kita berurusan dengan banyak data. Kita akan mengakses mereka berdasarkan index. Apa itu index? Pikirkan lagi orang di antrian. Orang yang paling depan adalah yang pertama. Karena index secara singkat adalah "posisi". Kita memulai posisi terdepan dengan angka 0.

Jadi untuk memanggil orang yang paling depan, kita hanya perlu angka 0. Berikut adalah cara untuk mendapatkan nama agus.

```python
agus = ["Agus", 50, 99.51]
nama = agus[0]
print(nama) # Agus
```

Ketika kita akan mencari setelah yang pertama, kita dapat menambahkan index dengan nilai 1, jadi 0 + 1 = 1. Mari kita coba.

```python
umur = agus[1]
print(umur) # 50
```

Kita coba lagi

```python
nilai = agus[2]
print(nilai) # 99.51
```

Kita secara konsisten mendapatkan nilai-nilai dari variabel agus dengan posisi (index) yang kita gunakan. Ingat, pertama adalah 0.

### Fundamental 4.1 - Tuple, temennya `list`

Tuple, beda dari `list` dimana kita bisa mengubahnya. Data-data di tuple tidak dapat dirubah setelah dibuat.

```python
agus = ("Agus", 50, 99.51)
```

Yang membedakan `tuple` dan `list` adalah `tuple` di definisikan dengan `()` dan `list` dengan `[]`

Cara kita mengakses data di tuple tetap sama dengan list, hanya dengan menggunakan index.

```python
nama = agus[0]
umur = agus[1]
nilai = agus[2]
print(nama, umur, nilai) # Agus 50 99.51
```

Nah, ini adalah perjalanan singkat kita dengan yang namanya `list` dan `tuple`. Kita akan bertemu lagi setelah kita membahas `fungsi`.

### Fundamental 4.2 - Dict/Dictionary. Paling beda dengan list.

Dict atau dictionary adalah tipe data python yang dibuat dengan cara yang berbeda. Kita menyebutnya dengan `key`-`value` pair. Atau kunci ke data. Simpelnya, `key` yang dimaksud ini mirip dengan `index` yang kita pelajari sebelumnya tetapi. `key` ini berbeda, karena dia bukan hanya nilai angka satu sampai seterusnya.

Berikut adalah contoh pembuatan `dict`:

```python
agus = {
    "nama": "Agus",
    "umur": 50, 
    "nilai": 99.51
}
```

Nah, disini. Key yang dimaksud itu seperti bagian kiri dari titik-dua (:) dan value yang di bagian kanan. Sama seperti saat membuat variabel tetapi kita harus menjadikan key sebagai data, dan value akan tetap menjadi data.

Berikut adalah contoh salah:

```python
agus = {
    nama: "Agus",
    umur: 50,
    nilai: 99.51
}
```

Kalau kita mendefinisikan key di dictionary dengan tulisan, maka kita harus mengubah key tersebut menjadi `string`.

"Bagaimana mengakses data dict?"

Caranya cukup mudah.

```python
agus = {
    "nama": "Agus",
    "umur": 50,
    "nilai": 99.51
}

print(agus['nama']) # Agus
```

Nah, karena kita sudah membuat key `nama`, kita hanya perlu mengaksesnya dengan string `"nama"` juga.

Layaknya juga dengan umur.

```python
print(agus['nama'], agus['umur'], agus['nilai']) # Agus 50 99.51
```

### Fundamental 5 - Fungsi

Di matematika, fungsi didefinisikan seperti `f(x) = x + 1`

Hanya saja, di python kita mendefinisikan fungsi dengan cara berikut:

```python
def fungsi(x):
    return x + 1
```

Kode diatas sama dengan fungsi matematika tadi, hanya saja nama fungsinya berbeda.

Pertama, kita melihat 2 kata `def`, dan `return`. Dua kata ini digunakan oleh python. `def` untuk mendefinisikan fungsi, dan `return` untuk mengeluarkan hasil fungsi agar kita bisa menggunakannya di masa depan nanti.

```python
def tambah_satu(x):
    return x + 1

satu = 1
dua = tambah_satu(1)
```

Kode diatas itu, pertama kita mendefinisikan fungsi `tambah_satu` dengan mengambil satu hal yang fungsi itu inginkan, yaitu variabel `x`. Kita tidak perlu membuat variabel x diluar definisi fungsi. Kita hanya perlu memasukkan data di dalam `()`. Ingat, kita sedang membuat fungsi. Kita tidak sedang membuat tuple.

Nah, karena fungsi tersebut hanya mengambil 1 permintaan saja. Kita bisa membuat fungsi yang mengambil 2 permintaan.

```python
def tambah(x, y):
    return x + y

satu = 1
dua = tambah(1, 1) # sama saja dengan 1 + 1
```

Fungsi `tambah` tersebut meminta 2 variabel agar diisi sehingga fungsi tersebut dapat berjalan. Kita mengisi x dengan nilai 1, dan y dengna nilai 2.

```python
print(tambah(2, 8))
```

Hasil dari kode diatas adalah 10 karena kita mengisi variabel x dengan nilai 2 dan mengisi variabel y dengan nilai 8. Jadinya, saat bagian `return` dilaksanakan. Kita sama saja melakukan `2 + 8` karena `x + y`

"Bisa gak kita isi variabel y sebelum x?"

Jawabannya adalah bisa! Tanpa basa-basi, aku akan menunjukkan kalian caranya memasukkan variabel secara spesifik.

```python
def tambah(x, y):
    return x + y

satu = tambah(y=1, x=0)
dua = tambah(x=0, y=2)
```

Nah, kita membuat variabel `satu` dengan menggunakan fungsi `tambah`, hanya saja ada sedikit perbedaan saja.

```python
satu = tambah(y=1, x=0)
```

Kita membuat variabel y dengan nilai 1 dan x dengan nilai 0 secara tidak berurutan.

Sebelumnya, kita mengisi variabel secara berurutan dengan memasukkan nilainya saja.

Jadinya, seperti contoh ini:

```python
tambah(5, 10)
tambah(y=10, x=5)
```

Adalah hal yang sama! Mengapa? Mari kita bedah sedikit.

Kita membuat fungsi `tambah` dengan meminta variabel `x` dan `y` namun kita meminta variabel `x` terlebih dahulu. Di baris kedua, kita memasukkan secara langsung variabel `y` dan `x`.

Nah, walau begitu. Terkadang bisa lho, terjadi kerusakan karena kita salah menggunakan kemampuan tersebut.

```python
tambah(y=50, 1)
```

Kode tersebut akan rusak, karena kita mendahului variabel `x`. Python akan kesusahan mencari maksud dari angka 1 yang kita berikan. Karenanya, kita wajib menuliskan tanpa langsung menunjuk variabel dengan suatu data. Ini adalah contoh yang benar:

```python
tambah(1, y=50)
```

Nah, karena pendefinisian tadi adalah `(x, y)`. Dari contoh tersebut, kita bisa menyimpulkan bahwa `(x=1, y=50)`

### Fundamental 5.1 - Banyak argumen/permintaan variabel.

Nah, karena kita telah membuat variabel yang menerima 2 argumen. Kita akan lanjut dengan sihir lain, ini disebut dengan metode, `*`, dan `**`.

```python
def tambahkan_semuanya(*angka):
    return sum(angka)

print(tambahkan_semuanya(1, 2, 3)) # 6 karena 1 + 2 + 3
```

Nah, di contoh diatas. Kita menggunakan satu `*`. Ini adalah cara bahwa kita akan mendapatkan data tanpa mendeklarasikan variabel seperti `tambah(x=5)`

Untuk kita dapat mendeklarasikan dengan variabel adalah dengan `**`.

Dan, apakah kalian tau? variabel `angka` dari `tambahkan_semuanya` itu adalah `tuple`?

Kita dapat mengakses data tuple seperti yang kita bahas sebelumnya. Di kasus ini dengan

```python
def tambahkan_semuanay(*angka):
    print(angka[0])
    return sum(angka)
```

Ini akan memprint data yang dikirimkan pertama ke fungsi. Dalam contoh tadi, `(1, 2, 3)`. Data pertama adalah `1`.

Berikutnya adalah `**`.

```python
def terima(**data):
    return data

print(terima(x=1, y=2))
```

Nah, di contoh atas tadi. Ketika kita menjalankan, kita akan mendapat data dictionary. Kita dapat mengakses suatu data dengan menggunakan key-nya

```python
def terima(**data):
    print(data['x'])
    return data

print(terima(x=1, y=2))
```

Kita akan mendapatkan pertama

```
1
{'x': 1, 'y': 2}
```

Nah, hasil kedua ini adalah data dictionary.

**Catatan**: Menggunakan `*`, membuat kita tidak dapat menggunakan `variabel=`

Dan `**`, membuat kita tidak dapat menggunakan `1, 2, 3`

Untuk menggabungkan hal-hal tersebut, kita hanya akan menggunakan cara berikut:

```python
def fungsi(*angka, **data):
    return angka, data
```

Ini akan menghasilkan/mengembalikan data tuple dan dictionary.

**Catatan**: Apapun yang ditaruh ke `*`, dan `**` bersifat opsional. Artinya mereka boleh tidak ada. Kita akan membahas perilaku variabel tidak dideklarasikan langsung di bagian berikutnya.

### Fundamental 5.2 - Argumen Opsional

Argumen Opsional adalah argumen yang boleh tidak ada karena kita sudah membuat pengganti ketika tidak ada.

```python
def tambah(x, y=2):
    return x + y

satu = tambah(-1) # -1 + 2
dua = tambah(x=0) # 0 + 2
```

Nah, di contoh diatas. Kita tidak memberikan data ke variabel y, karena fungsinya telah membuat cadangan ketika tidak diberikan. Sebelumnya, ketika tidak memberikan. Kita akan mendapati error dan kita dipaksa untuk memberikan data ke variabel yang kekurangan data.

```python
print(tambah(5, 5)) # 10
```

Kita bisa memasukkan data ke variabel `y` seperti contoh diatas.

### Fundamental 5.3 - Mendapatkan data kosong melalui **kwargs atau rusak.

Terkadang, suatu fungsi mengharapkan suatu variabel untuk ada tetapi lupa untuk memintanya atau memasukkannya sebagai keperluannya.

```python
def fungsi(**kwargs):
    print(kwargs['nama']) # rusak!

fungsi(umur=50)
```

Kode disebut akan rusak karena mencoba mendapatkan suatu data yang belum ada. Lantas, bagaimana kita mendapatkan data dari `**kwargs` tanpa merusak?

Mari kita berkenalan dengan `method` atau `metode`. Metode adalah suatu fungsi yang khusus untuk suatu data.

```python
def fungsi(**kwargs):
    print(kwargs.get('nama', "Agus"))


print(fungsi(umur=50)) # Agus
```

Nah, kita menggunakan `.get`. Disini, `.get` menerima 2 argumen, yaitu nama `key` dan `data` ketika key tidak ada di dictionary.

karena kita mengesetnya sebagai

```python
kwargs.get('nama', "Agus")
```

kita akan mendapatkan keluaran Agus!

```python
print(fungsi(nama="Bambang", umur=50)) # Bambang
```

Karena nama sekarang sudah ada. Metode `.get` hanya akan mengeluarkan data dengan kunci `nama` tanpa mengembalikan data bawaan/_default_

Sayangnya, tidak ada cara untuk mendapatkan data tertentu melalui `*`.

## Penutup

Sekian, pembelajaran singkat dari saya. Bila ada kesalahan saya memohon maaf sebesar-besarnya. Semoga kalian dapat memahami materi ini.

### Pengarang/Penulis

Dokumen ini diketik oleh [RimuEirnarn](https://github.com/RimuEirnarn). Kode sumber dari gambar, contoh, dll disimpan di [Repository](https://github.com/RimuEirnarn/lesson)

### Hak Cipta

Projek ini dilisensi dengan BSD-3-Clause.
