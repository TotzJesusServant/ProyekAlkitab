import json


def buat_struktur_teks_per_kitab(nama_file, struktur_alkitab):
    print("Masuk")
    f = open(nama_file, 'r')
    teks = f.read()
    f.close()
    
    struktur_teks_per_kitab = {}
    for kitab in struktur_alkitab:
        #print(kitab)
        pasal = 1
        struktur_teks_per_kitab[kitab] = {}
        print(kitab+str(pasal))
        index_mulai_kitab = teks.find(kitab+" "+str(pasal))
        if  list(struktur_alkitab.keys()).index(kitab) < 66:
            print('true')
            index_akhir_kitab = teks.find(kitab+" "+str(pasal + 1))
        else:
            index_akhir_kitab = len(teks)
        print(teks[index_mulai_kitab:index_akhir_kitab])
        struktur_teks_per_kitab[kitab]["Isi"] = teks[index_mulai_kitab:index_akhir_kitab]
    return struktur_teks_per_kitab

def simpan_ke_json(data, nama_file):
    with open("C:\\Users\\Totz Tech\\Documents\\Code\\teks_per_kitab.json", 'w') as file:
        json.dump(data, file, indent=4)
    print("Done")

# Baca file teks Alkitab
# Data struktur Alkitab (dalam bentuk yang Anda sebutkan)

bible_structure = {
    "Genesis": {
        "jumlah_pasal": 50,
        "jumlah_ayat_per_pasal": [31, 25, 24, 26, 32, 22, 24, 22, 29, 32, 32, 20, 18, 24, 21, 16, 27, 33, 38, 18, 34, 24, 20, 67, 34, 35, 46, 22, 35, 43, 55, 32, 20, 31, 29, 43, 36, 30, 23, 23, 57, 38, 34, 34, 28, 34, 31, 22, 33, 26]
    },
    "Exodus": {
        "jumlah_pasal": 40,
        "jumlah_ayat_per_pasal": [22, 25, 22, 31, 23, 30, 29, 28, 35, 29, 10, 51, 22, 31, 27, 36, 16, 27, 25, 26, 36, 31, 33, 18, 40, 37, 21, 43, 46, 38, 18, 35, 23, 35, 35, 38, 29, 31, 43, 38]
    },
    "Leviticus": {
        "jumlah_pasal": 27,
        "jumlah_ayat_per_pasal": [17, 16, 17, 35, 19, 30, 38, 36, 24, 20, 47, 8, 59, 57, 33, 34, 16, 30, 37, 27, 24, 33, 44, 23, 55, 46, 34]
    },
    "Numbers": {
        "jumlah_pasal": 36,
        "jumlah_ayat_per_pasal": [54, 34, 51, 49, 31, 27, 89, 26, 23, 36, 35, 16, 33, 45, 41, 50, 13, 32, 22, 29, 35, 41, 30, 25, 18, 65, 23, 31, 40, 16, 54, 42, 56, 29, 34, 13]
    },
    "Deuteronomy": {
        "jumlah_pasal": 34,
        "jumlah_ayat_per_pasal": [46, 37, 29, 49, 33, 25, 26, 20, 29, 22, 32, 32, 18, 29, 23, 22, 20, 22, 21, 20, 23, 30, 25, 22, 19, 19, 26, 68, 29, 20, 30, 52, 12]
    },
    "Joshua": {
        "jumlah_pasal": 24,
        "jumlah_ayat_per_pasal": [18, 24, 17, 24, 15, 27, 26, 35, 27, 43, 23, 24, 33, 15, 63, 10, 18, 28, 51, 9, 45, 34, 16, 33]
    },
    "Judges": {
        "jumlah_pasal": 21,
        "jumlah_ayat_per_pasal": [36, 23, 31, 24, 31, 40, 25, 35, 57, 18, 40, 15, 25, 20, 20, 31, 13, 31, 30, 48, 25]
    },
    "Ruth": {
        "jumlah_pasal": 4,
        "jumlah_ayat_per_pasal": [22, 23, 18, 22]
    },
    "1 Samuel": {
        "jumlah_pasal": 31,
        "jumlah_ayat_per_pasal": [28, 36, 21, 22, 12, 21, 17, 22, 27, 27, 15, 25, 23, 52, 35, 23, 58, 30, 24, 42, 16, 23, 28, 23, 44, 25, 12, 25, 11, 31, 13]
    },
    "2 Samuel": {
        "jumlah_pasal": 24,
        "jumlah_ayat_per_pasal": [27, 32, 39, 12, 25, 23, 29, 18, 13, 19, 27, 31, 39, 33, 37, 23, 29, 33, 43, 26, 22, 51, 39, 25]
    },
    "1 Kings": {
        "jumlah_pasal": 22,
        "jumlah_ayat_per_pasal": [53, 46, 28, 34, 18, 38, 51, 66, 28, 29, 43, 33, 34, 31, 34, 34, 24, 46, 21, 43, 29, 54]
    },
    "2 Kings": {
        "jumlah_pasal": 25,
        "jumlah_ayat_per_pasal": [18, 25, 27, 44, 27, 33, 20, 29, 37, 36, 21, 21, 25, 29, 38, 20, 41, 37, 37, 21, 26, 20, 37, 20, 30]
    },
    "1 Chronicles": {
        "jumlah_pasal": 29,
        "jumlah_ayat_per_pasal": [54, 55, 24, 43, 41, 66, 40, 40, 44, 14, 47, 40, 14, 17, 29, 43, 27, 17, 19, 8, 30, 19, 32, 31, 31, 32, 34, 21, 30]
    },
    "2 Chronicles": {
        "jumlah_pasal": 36,
        "jumlah_ayat_per_pasal": [17, 18, 17, 22, 14, 42, 22, 18, 31, 19, 23, 16, 22, 15, 19, 14, 19, 34, 11, 37, 20, 12, 21, 27, 28, 23, 9, 27, 36, 27, 21, 33, 25, 33, 27, 23]
    },
    "Ezra": {
        "jumlah_pasal": 10,
        "jumlah_ayat_per_pasal": [11, 70, 13, 24, 17, 22, 28, 36, 15, 44]
    },
    "Nehemiah": {
        "jumlah_pasal": 13,
        "jumlah_ayat_per_pasal": [11, 20, 32, 23, 19, 19, 73, 18, 38, 39, 36, 47, 31]
    },
    "Esther": {
        "jumlah_pasal": 10,
        "jumlah_ayat_per_pasal": [22, 23, 15, 17, 14, 14, 10, 17, 32, 3]
    },
    "Job": {
        "jumlah_pasal": 42,
        "jumlah_ayat_per_pasal": [22, 13, 26, 21, 27, 30, 21, 22, 35, 22, 20, 25, 28, 22, 35, 22, 16, 21, 29, 29, 34, 30, 17, 25, 6, 14, 23, 28, 25, 31, 40, 22, 33, 37, 16, 33, 24, 41, 30, 32, 26, 17]
    },
    "Psalms": {
        "jumlah_pasal": 150,
        "jumlah_ayat_per_pasal": [6, 12, 8, 9, 13, 11, 18, 10, 21, 18, 7, 9, 6, 7, 5, 11, 15, 51, 15, 10, 14, 32, 6, 10, 22, 12, 14, 9, 11, 13, 25, 11, 22, 23, 28, 13, 40, 23, 14, 18, 14, 12, 5, 27, 18, 12, 10, 14, 32, 16, 10, 13, 21, 23, 6, 10, 12, 8, 9, 11, 32, 22, 14, 9, 11, 12, 24, 12, 11, 8, 12, 15, 6, 11, 12, 14, 9, 6, 7, 8, 19, 16, 8, 18, 7, 8, 9, 4, 8, 5, 6, 5, 6, 8, 8, 3, 18, 3, 3, 21, 26, 9, 8, 24, 13, 10, 7, 12, 15, 21, 10, 20, 14, 9, 6]
    },
    "Proverbs": {
        "jumlah_pasal": 31,
        "jumlah_ayat_per_pasal": [33, 22, 35, 27, 23, 35, 27, 36, 18, 32, 31, 28, 25, 35, 33, 33, 28, 24, 29, 30, 31, 29, 35, 34, 28, 28, 27, 28, 27, 33, 31]
    },
    "Ecclesiastes": {
        "jumlah_pasal": 12,
        "jumlah_ayat_per_pasal": [18, 26, 22, 16, 20, 12, 29, 17, 18, 20, 10, 14]
    },
    "Song of Solomon": {
        "jumlah_pasal": 8,
        "jumlah_ayat_per_pasal": [17, 17, 11, 16, 16, 13, 13, 14]
    },
    "Isaiah": {
        "jumlah_pasal": 66,
        "jumlah_ayat_per_pasal": [31, 22, 26, 6, 30, 13, 25, 23, 20, 34, 16, 6, 22, 32, 9, 14, 12, 14, 7, 25, 6, 17, 25, 18, 23, 12, 21, 13, 29, 24, 33, 9, 20, 24, 17, 10, 22, 38, 22, 8, 31, 29, 25, 28, 28, 25, 13, 15, 22, 26, 11, 23, 15, 12, 17, 13, 12, 21, 14, 21, 22, 11, 12, 19, 12, 25, 24]
    },
    "Jeremiah": {
        "jumlah_pasal": 52,
        "jumlah_ayat_per_pasal": [19, 37, 25, 31, 31, 30, 34, 23, 25, 25, 23, 17, 27, 22, 21, 21, 27, 23, 15, 18, 14, 30, 40, 10, 38, 24, 22, 17, 32, 24, 40, 44, 26, 22, 19, 32, 21, 28, 18, 16, 18, 22, 13, 30, 5, 28, 7, 47, 39, 46, 64, 34]
    },
    "Lamentations": {
        "jumlah_pasal": 5,
        "jumlah_ayat_per_pasal": [22, 22, 66, 22, 22]
    },
    "Ezekiel": {
        "jumlah_pasal": 48,
        "jumlah_ayat_per_pasal": [28, 10, 27, 17, 17, 14, 27, 18, 11, 22, 25, 28, 23, 23, 8, 63, 24, 32, 14, 49, 32, 31, 49, 27, 17, 21, 36, 26, 21, 26, 18, 32, 33, 31, 15, 38, 28, 23, 29, 49, 26, 20, 27, 31, 25, 24, 23, 35]
    },
    "Daniel": {
        "jumlah_pasal": 12,
        "jumlah_ayat_per_pasal": [21, 49, 30, 37, 31, 28, 28, 27, 27, 21, 45, 13]
    },
    "Hosea": {
        "jumlah_pasal": 14,
        "jumlah_ayat_per_pasal": [11, 23, 5, 19, 15, 11, 16, 14, 17, 15, 12, 14, 16, 9]
    },
    "Joel": {
        "jumlah_pasal": 3,
        "jumlah_ayat_per_pasal": [20, 32, 21]
    },
    "Amos": {
        "jumlah_pasal": 9,
        "jumlah_ayat_per_pasal": [15, 16, 15, 13, 27, 14, 17, 14, 15]
    },
    "Obadiah": {
        "jumlah_pasal": 1,
        "jumlah_ayat_per_pasal": [21]
    },
    "Jonah": {
        "jumlah_pasal": 4,
        "jumlah_ayat_per_pasal": [17, 10, 10, 11]
    },
    "Micah": {
        "jumlah_pasal": 7,
        "jumlah_ayat_per_pasal": [16, 13, 12, 13, 15, 16, 20]
    },
    "Nahum": {
        "jumlah_pasal": 3,
        "jumlah_ayat_per_pasal": [15, 13, 19]
    },
    "Habakkuk": {
        "jumlah_pasal": 3,
        "jumlah_ayat_per_pasal": [17, 20, 19]
    },
    "Zephaniah": {
        "jumlah_pasal": 3,
        "jumlah_ayat_per_pasal": [18, 15, 20]
    },
    "Haggai": {
        "jumlah_pasal": 2,
        "jumlah_ayat_per_pasal": [15, 23]
    },
    "Zechariah": {
        "jumlah_pasal": 14,
        "jumlah_ayat_per_pasal": [21, 13, 10, 14, 11, 15, 14, 23, 17, 12, 17, 14, 9, 21]
    },
    "Malachi": {
        "jumlah_pasal": 4,
        "jumlah_ayat_per_pasal": [14, 17, 18, 6]
    },
    "Matthew": {
        "jumlah_pasal": 28,
        "jumlah_ayat_per_pasal": [25, 23, 17, 25, 48, 34, 29, 34, 38, 42, 30, 50, 58, 36, 39, 28, 27, 35, 30, 34, 46, 46, 39, 51, 46, 75, 66, 20]
    },
    "Mark": {
        "jumlah_pasal": 16,
        "jumlah_ayat_per_pasal": [45, 28, 35, 41, 43, 56, 37, 38, 50, 52, 33, 44, 37, 72, 47, 20]
    },
    "Luke": {
        "jumlah_pasal": 24,
        "jumlah_ayat_per_pasal": [80, 52, 38, 44, 39, 49, 50, 56, 62, 42, 54, 59, 35, 35, 32, 31, 37, 43, 48, 47, 38, 71, 56, 53]
    },
    "John": {
        "jumlah_pasal": 21,
        "jumlah_ayat_per_pasal": [51, 25, 36, 54, 47, 71, 53, 59, 41, 42, 57, 50, 38, 31, 27, 33, 26, 40, 42, 31, 25]
    },
    "Acts": {
        "jumlah_pasal": 28,
        "jumlah_ayat_per_pasal": [26, 47, 26, 37, 42, 15, 60, 40, 43, 48, 30, 25, 52, 28, 41, 40, 34, 28, 40, 38, 40, 30, 35, 27, 27, 32, 44]
    },
    "Romans": {
        "jumlah_pasal": 16,
        "jumlah_ayat_per_pasal": [32, 29, 31, 25, 21, 23, 25, 39, 33, 21, 36, 21, 14, 23, 33, 27]
    },
    "1 Corinthians": {
        "jumlah_pasal": 16,
        "jumlah_ayat_per_pasal": [31, 16, 23, 21, 13, 20, 40, 13, 27, 33, 34, 31, 13, 40, 58, 24]
    },
    "2 Corinthians": {
        "jumlah_pasal": 13,
        "jumlah_ayat_per_pasal": [24, 17, 18, 18, 21, 18, 16, 24, 15, 18, 33, 21, 14]
    },
    "Galatians": {
        "jumlah_pasal": 6,
        "jumlah_ayat_per_pasal": [24, 21, 29, 31, 26, 18]
    },
    "Ephesians": {
        "jumlah_pasal": 6,
        "jumlah_ayat_per_pasal": [23, 22, 21, 32, 33, 24]
    },
    "Philippians": {
        "jumlah_pasal": 4,
        "jumlah_ayat_per_pasal": [30, 30, 21, 23]
    },
    "Colossians": {
        "jumlah_pasal": 4,
        "jumlah_ayat_per_pasal": [29, 23, 25, 18]
    },
    "1 Thessalonians": {
        "jumlah_pasal": 5,
        "jumlah_ayat_per_pasal": [10, 20, 13, 18, 28]
    },
    "2 Thessalonians": {
        "jumlah_pasal": 3,
        "jumlah_ayat_per_pasal": [12, 17, 18]
    },
    "1 Timothy": {
        "jumlah_pasal": 6,
        "jumlah_ayat_per_pasal": [20, 15, 16, 16, 25, 21]
    },
    "2 Timothy": {
        "jumlah_pasal": 4,
        "jumlah_ayat_per_pasal": [18, 26, 17, 22]
    },
    "Titus": {
        "jumlah_pasal": 3,
        "jumlah_ayat_per_pasal": [16, 15, 15]
    },
    "Philemon": {
        "jumlah_pasal": 1,
        "jumlah_ayat_per_pasal": [25]
    },
    "Hebrews": {
        "jumlah_pasal": 13,
        "jumlah_ayat_per_pasal": [14, 18, 19, 16, 14, 20, 28, 13, 28, 39, 40, 29, 25]
    },
    "James": {
        "jumlah_pasal": 5,
        "jumlah_ayat_per_pasal": [27, 26, 18, 17, 20]
    },
    "1 Peter": {
        "jumlah_pasal": 5,
        "jumlah_ayat_per_pasal": [25, 25, 22, 19, 14]
    },
    "2 Peter": {
        "jumlah_pasal": 3,
        "jumlah_ayat_per_pasal": [21, 22, 18]
    },
    "1 John": {
        "jumlah_pasal": 5,
        "jumlah_ayat_per_pasal": [10, 29, 24, 21, 21]
    },
    "2 John": {
        "jumlah_pasal": 1,
        "jumlah_ayat_per_pasal": [13]
    },
    "3 John": {
        "jumlah_pasal": 1,
        "jumlah_ayat_per_pasal": [14]
    },
    "Jude": {
        "jumlah_pasal": 1,
        "jumlah_ayat_per_pasal": [25]
    },
    "Revelation": {
        "jumlah_pasal": 22,
        "jumlah_ayat_per_pasal": [20, 29, 22, 11, 14, 17, 17, 13, 21, 11, 19, 17, 18, 20, 8, 21, 18, 24, 21, 15, 27, 21]
    }
}
namafile = "%alkitab%"

# Buat struktur teks per kitab
struktur_teks_per_kitab = buat_struktur_teks_per_kitab("C:\\Users\\Totz Tech\\Documents\\Code\\alkitab.txt", bible_structure)

# Simpan ke file JSON
simpan_ke_json(struktur_teks_per_kitab, 'teks_per_kitab.json')
