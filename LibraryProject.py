import sqlite3 # Modulumuzu Dagil Ediyoruz
import time # Programa gercekcilik katmak icin sleep fonksiyonu dahil edecegiz

class Kitap():
    def __init__(self,isim,yazar,yayinevi,tur,baski):
        self.isim=isim
        self.yazar=yazar
        self.yayinevi=yayinevi
        self.tur=tur
        self.baski=baski
    def __str__(self): # Printle bastirmak icin str fonksiyonu tanimliyoruz.
        return "Kitap Ismi:{}\nYazar:{}\nYayinevi:{}\nTur:{}\nBaski:{}".format(self.isim,self.yazar,self.yayinevi,self.tur,self.baski)

class Kutuphane(): # asil islemleri burda yapicaz.sqlite veritabanina baglanicaz ve kitaplarla ilgili islemler gerceklestirecegiz
    def __init__(self):
        self.baglanti_olustur() # sqlite veritabanina baglanmak icin ilk fonksiyonum bu olucak

    def baglanti_olustur(self):
        self.con= sqlite3.connect("Kutuphane.Db") # Sqlite veritabanina baglaniyoruz.
        self.cursor=self.con.cursor() # Imlecimizi baglanti uzerinden olusturmamiz gerekir
        # Cursor olusturdugumuza gore tablo olusturalim
        sorgu="Create TABLE if not exist kitaplar (isim TEXT,yazar TEXT,yayinevi TEXT,tur TEXT,baski INT)" # Kitalar ismindeki tabloyu olusturduk ve iceriklerin turlerini belirttik
        self.cursor.execute(sorgu) # Sorguyu gonderiyoruz, bu sekilde sorgu caliscak ve tablo oluscak
        self.con.commit() # Veritabaninda islemin etkili olabilmesi icin commit fonk.
    def baglanti_kes(self):
        self.con.close() # Baglantiyi kesmek icin bu fonkiyonu tanimladim.
    def kitaplari_goster(self): # Simdi tablo uzerinde islemlere basliyoruz.Kitaplari Gorster ile
        sorgu="Select * from kitaplar" # Select * ile : kitaplar tablosundan tum kitaplari cekmek istiyoruz
        self.cursor.execute(sorgu) # Bu sorgu calisinca veritabanindaki bilgiler donuyor.
        kitaplar=self.cursor.fetchall() # Bilgiler kitaplar degiskenine liste icinde demet halinde buluncak
        if len(kitaplar) == 0: # Listede eleman yoksa uzunluk 0 dir
            print("Kutuphanede kitap Bulunmuyor") # Yani Boyle demek uygun olur
        else:
            for i in kitaplar:
                kitap=Kitap(i[0],i[1],i[2],i[3],i[4]) # Kitaplik Class i olusturmusutuk , simdi bir kitap objesi olusturmus olduk.
                print(kitap) #her i bir kitap olucak veritabani genisledikce.Bizde kitabin Ozelliklerini kitap objesinden tek tek cekiyoruz
                            # Kitabin Icinde Str fonksiyonu tanimlamistik  print kitap demek yeterli olucak
    def kitap_sorgula(self,isim): # isme gore kitablar tablosundaki kitabi sorgulamis olacagim
        sorgu="Select * from kitaplar where isim=?"
        self.cursor.execute(sorgu,(isim,)) # 2. parametre olarak Isim'i(isim,) seklinde tek elemanli demet halinde gonderiyoruz
        kitaplar=self.cursor.fetchall() # Kitap Bulunuyorsa bu kitaplar tek elemanli liste icinde demet olucak.
        if len(kitaplar) == 0: # Kitap yoksa Bu listede hicbirsey olmuycak
            print("Boyle Bir Kitap Bulunmuyor.")
        else: # Kitap Bulunuyorsa;
            kitap=Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4]) # Yine bir tane daha kitap objesi olusturuyoruz eleman tek elemanli liste oldugu icin
                                                                                                    # For Dongusune gerek yok kitaplar listesinden kitabin ismini yayinevini baskisini vs cekicez.
            print(kitap) # Boyle de bastiricaz ktiabi.
    def kitap_ekle(self,kitap): # Kitap da tanidigimiz obje oldugu icin diger degiskenler gibi gonderilebiliyor.
        sorgu="Insert into kitaplar VALUES(?,?,?,?,?)"
        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayinevi,kitap.tur,kitap.baski)) # sorguyu gonderiyoruz ve 5 elemanli demet gondermemiz gerek.
        self.con.commit() # Bu sekidel tabloya bilgi gondermis olduk , bilginin guncellenmesi icin commit.
    def kitap_sil(self,isim):
        sorgu="Delete from kitaplar where isim=?"
        self.cursor.execute(sorgu,(isim,))
        self.con.commit()
    def baski_yukselt(self,isim):
        sorgu="Select * from kitaplar where isim=?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar=self.cursor.fetchall()
        if len(kitaplar) == 0:
            print("Boyle Bir Kitap Bulunmuyor")
        else:
            baski=kitaplar[0][4]
            baski +=1
            sorgu2="Update kitaplar set baski=? where isim=?"
            self.cursor.execute(sorgu2,(baski,isim))
