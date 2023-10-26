print('''
Sillahkan Pilih tools dibawah ini dengan mengirimkan nomornya
==========================
Tools yang tersedia
==========================
1. Luas Persegi
2. Luas Lingkaran
3. Luas Lingkaran
==========================
''')
a = int(input("Masukkan Pilihan kamu : "))

match a:
    case 1:
        luasPersegi = int(input("masukkan nilai sisi : ")) 
        hasilLuas = luasPersegi * luasPersegi
        print ("luas persegi adalah ",hasilLuas)
    case 2:
        nilaiPhi = float(input("Masukkan Nilai Phi : "))
        nilaiJari = int(input("Masukkan Nilai Jari jari : "))
        jarijari = nilaiJari * nilaiJari
        luasLingkaran = nilaiPhi * jarijari
        print("Luas Lingkaran Adalah : ",luasLingkaran) 
    case 3:
        rumus = float(0.5)
        alas = int(input("Masukkan Nilai Alas : "))
        tinggi = int(input("Masukkan Nilai Tinggi : "))
        hasilLuas = rumus * alas * tinggi
        print("Luas Segitiga adalah : ",hasilLuas)
    case _:
        print("Pilihan Kamu tidak ada di pilihan")