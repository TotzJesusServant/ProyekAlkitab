import json
import time



with open("C:\\Users\\Totz Tech\\Documents\\Code\\struktur_alkitab2.json",'r') as file:
    bible_dict = json.load(file)

bible_dict['Psalms']['jumlah_ayat_per_pasal'] = [41, 72, 89, 90, 51, 121, 60, 109, 107, 111, 43, 71, 13, 40, 23, 33, 72, 19, 37, 38, 71, 13, 83, 61, 81, 50, 78, 40, 106, 32, 32, 44, 32, 24, 22, 28, 36, 12, 54, 9, 14, 13, 11, 15, 16, 13, 5, 23, 19, 15, 11, 16, 14, 20, 23, 19, 9, 6, 7, 5, 10, 22, 23, 28, 13, 40, 23, 14, 18, 14, 12, 5, 27, 18, 12, 10, 15, 21, 23, 21, 11, 7, 9, 24, 14, 12, 12, 10, 13, 20, 7, 35, 36, 5, 24, 20, 28, 23, 10, 12, 22, 12, 14, 9, 11, 13, 12, 10, 7, 17, 8, 9, 6, 7, 5, 11, 15, 6, 6, 4, 12, 8, 7, 8, 9, 4, 8, 5, 6, 5, 6, 8, 8, 3, 18, 3, 3, 21, 26, 9, 8, 24, 14, 10, 8, 12, 15, 21, 10, 20, 14, 9, 6]

for kitab in bible_dict:
    
    jumlah_pasal = bible_dict[kitab]['jumlah_pasal']
    data_per_kitab = bible_dict[kitab]["data_per_kitab"]
    
    for i in range(0,jumlah_pasal-1):
        bible_dict[kitab][str(i+1)]={}
        teks_temp = []
        print(i)
        print(kitab)
        print(len(bible_dict[kitab]['jumlah_ayat_per_pasal']))
        jumlah_ayat = bible_dict[kitab]['jumlah_ayat_per_pasal'][i]
        for j in range(0,jumlah_ayat-1):
            #print("j:" + str(j+1))
            string_awal = str(i+1)+":"+str(j+1)
            
            indeks_awal = data_per_kitab.find(string_awal)

            string_akhir = str(i+1)+":"+str(j+2)
            indeks_akhir = data_per_kitab.find(string_akhir)
            
            teks = data_per_kitab[indeks_awal+len(str(i+1)+":"):indeks_akhir]
            bible_dict[kitab][str(i+1)][str(j+1)] = teks
            #print("Ini isi: " )
            #print(bible_dict[kitab][str(i+1)][str(j+1)])

##            with open("C:\\Users\\Totz Tech\\Documents\\Code\\struktur_isi_alkitab4.json",'w') as file:
##                json.dump(bible_dict,file)

##            if input("Lanjut?"):
##                pass
##            
##            ind_dict  =str(i+1)
##            
##        ind = i - 1
##        print(bible_dict[kitab][str(i)])
##        if input("Lanjut?"):
##            pass
        
        
            
        with open("C:\\Users\\Totz Tech\\Documents\\Code\\struktur_isi_alkitab4.json",'w') as file:
            json.dump(bible_dict,file)




        
            

            
