def extra(fonk):
    def wrapper(*args):
        ciftler_toplami=0
        cift_sayilar=0
        tekler_toplami=0
        tek_sayilar=0

        for i in args:
            if i % 2 == 0:
                ciftler_toplami += i
                cift_sayilar += 1
            else:
                tekler_toplami += i
                tek_sayilar += 1
        print("Teklerin Ortalamasi:",tekler_toplami/tek_sayilar)
        print("Ciftlerin Ortalamasi:",ciftler_toplami/cift_sayilar)

        fonk(*args)
    return wrapper

@extra
def ortalama_bul(*args):
    toplam=0
    for i in args:
        toplam += i
    print("Ortalama:",toplam/len(args))

ortalama_bul(1,2,3,4,5,6,32,100,42,105)

# ---------------------------------------------
# Tekrar Deneyelim..
# 2. adimda extra fonksiyon ekliyorum ve assadaki fonksiyon oncelikle ekstra ozelliklerimde donuyor

def ekstra(fonk):
    def wrapper(sayilar): # assadaki sayilar listemi gonderdik.
        ciftler_top=0
        cif_sayilar=0
        tekler_top=0
        tek_saylar=0

        for i in sayilar:
            if (i % 2 == 0):
                ciftler_top+=i
                cif_sayilar+=1
            else:
                tekler_top+=i
                tek_saylar+=1
        print("tekler ortlamasi:",tekler_top/tek_saylar)
        print("ciftler ortalamasi:",ciftler_top/cif_sayilar)

        fonk(sayilar) # sayilari fonksiyona gondermis olduk.
    return wrapper #Sonra bunu decerator fonksiyonu icinden donebiliriz.


@ekstra
# 1. adimda bunu yazdim
def ort_bul(sayilar):
    toplam=0
    for i in sayilar:
        toplam+=i
    print("Ort:",toplam/len(sayilar))

ort_bul([1,2,3,4,12,232,12,4,6,7,2,3])
