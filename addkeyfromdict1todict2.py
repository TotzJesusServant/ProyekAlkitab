import json

# Membaca file bible.json
with open(r"C:\Users\Totz Tech\Documents\Code\bible.json", 'r') as file:
    bible_data = json.load(file)

# Membaca file teks_per_kitab.json
with open(r"C:\Users\Totz Tech\Documents\Code\teks_per_kitab_filtered2", 'r') as file:
    teks_per_kitab_data = json.load(file)

# Menyalin nilai jumlah_pasal dan jumlah_ayat_per_pasal dari bible.json ke teks_per_kitab.json
for kitab in bible_data:
    teks_per_kitab_data[kitab]["jumlah_pasal"] = bible_data[kitab]['jumlah_pasal']
    teks_per_kitab_data[kitab]["jumlah_ayat_per_pasal"] = bible_data[kitab]['jumlah_ayat_per_pasal']

# Menyimpan hasil perubahan ke file teks_per_kitab.json
with open(r"C:\Users\Totz Tech\Documents\Code\teks_per_kitab_filtered2", 'w') as file:
    json.dump(teks_per_kitab_data, file, indent=4)
