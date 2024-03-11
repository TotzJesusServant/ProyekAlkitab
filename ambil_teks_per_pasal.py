import json
import time

with open("C:\\Users\\Totz Tech\\Documents\\Code\\struktur_alkitab1.json",'r') as file:
    bible_structure2 = json.load(file)

#[nama_perjanjian[nama_kitab#[pasal#[ayat_per_pasal_#1]...]...]...]


# Looping melalui setiap kitab di teks_filtered2
for nama_kitab in bible_structure2:
    #ambil data-data
    isi_kitab = bible_structure2[nama_kitab]['data_per_kitab']
    jumlah_pasal = bible_structure2[nama_kitab]['jumlah_pasal']
    jumlah_ayat_per_pasal = bible_structure2[nama_kitab]['jumlah_ayat_per_pasal']
    
    
    #sediakan variabel array akan dimasukkan ke bible_structure2[nama_kitab]['isi_per_pasal']
    # Looping dari i=1 hingga jumlah_pasal-1
    for i in range(1, jumlah_pasal):
        print(jumlah_ayat_per_pasal[i-1])

        isi_per_pasal = []
        for j in range(1, jumlah_ayat_per_pasal[i-1]+1):
            print("i : " + str(i))
            print("j: " + str(j))
            if j+1 > len(jumlah_ayat_per_pasal):
                awal_index = str(i)+":"+str(j)
                akhir_index = len(isi_kitab)
                isi_temp = 0
                isi_temp = isi_kitab[isi_kitab.find(awal_index):akhir_index]
                isi_per_pasal.append(isi_temp)
            else:
                awal_index = str(i)+":"+str(j)
                akhir_index = str(i)+":"+str(j+1)
                isi_temp = 0
                isi_temp = isi_kitab[isi_kitab.find(awal_index):isi_kitab.find(akhir_index)]
                isi_per_pasal.append(isi_temp)
                

        bible_structure2[nama_kitab]['Pasal '+ str(i)] = isi_per_pasal

    
        print(bible_structure2[nama_kitab]['Pasal ' + str(i)])
    break
        #time.sleep(60)
            
    

    # Untuk i = jumlah_pasal - 1

    # Menambahkan isi_per_pasal ke dalam dictionary
    

# Terserah Anda bagaimana cara Anda menyimpan kembali dictionary ini ke dalam file JSON jika perlu
with open("C:\\Users\\Totz Tech\\Documents\\Code\\struktur_isi_alkitab3.json", 'w') as file:
    json.dump(bible_structure2, file, indent=4)
