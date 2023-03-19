import pymongo
client = pymongo.MongoClient("mongodb+srv://<username>:<password>@<cluster>.mongodb.net/?retryWrites=true&w=majority")
test = client.test

koleksi = test.koleksi

# --- Membuat data

koleksi.insert_one({
    "satu": 1,
    "dua": 2
})

# Ini akan membuat data dengan key-value pair "satu" -> 1, "dua" -> 2

# --- Memasukkan data

data_koleksi = koleksi.find({}, {'_id': False})

# Ini akan mencari SEMUA data-data di koleksi kita.
# Kalau ingin mendapatkan 1 data saja, kamu bisa menambahkan _one
# Setelah find seperti .find_one

koleksi_satu = koleksi.find_one({
    'satu': 1
})

# Ini akan mencari 1 data yang memiliki nilai 'satu' -> 1.

# --- Mengedit data

koleksi.update_one({
    'satu': 1
}, {
    '$set': {
        'tiga': 3
    }
})

# Ini akan mengubah 1 data yang memiliki nilai 'satu' -> 1
# dan mengeset 'tiga' -> 3

# --- Menghapus data

koleksi.delete_one({
    'satu': 1
})

# Ini akan menghapus 1 data yang memiliki nilai 'satu' -> 1
# Ingat, data yang dihapus tidak dapat dikembalikan lagi!
