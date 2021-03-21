def tambahMundur (x,y):
    reverseOutput1 = '' 
    reverseOutput2 = ''  
    penjumlahan = []
    reverseOutput3 = ''
    if type(x) != int or x < 0 or x>359999 or type(y) != int or y<0 or y>35999:
        print('Invalid Input!')
    else:
        # rubah variabel masukan 1 dan 2 menjadi string, kemudian di reverse menggunakan for loop
        # untuk tiap item yang ada pada string atau y akan disimpan pada string kosong reverseOutput1/2
        # dimana item awal akan diletakkan di paling akhir, hingga item terakhir berada di posisi awal
        for i in str(x):
            reverseOutput1 = i + reverseOutput1
        for i in str (y):
            reverseOutput2 = i + reverseOutput2
        # menjumlah nilai masukan 1 dan 2 yang sudah dibalik dengan merubah variabel menjadi int terlebih dahulu
        penjumlahan = int(reverseOutput1) + int(reverseOutput2)
        # membalik kembali variabel hasil penjumlahan
        for i in str (penjumlahan):
            reverseOutput3 = i + reverseOutput3
            # merubah output dari string menjadi int
            hasilAkhir = int (reverseOutput3)
        return hasilAkhir
            
        
# Input #
masukkanAngka1 = 24
masukkanAngka2 = 1
print('Hasil tambah mundurnya: ',tambahMundur(masukkanAngka1,masukkanAngka2))
