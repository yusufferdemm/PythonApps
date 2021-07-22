
# ! Her Next Yaptigimda 3`un Bir Buvvetini Alan Bir Sinif Yazmak Istiyorum.

class Kuvvet3():
	def __init__(self,max=0): #~ max 3 un kacinci kuvvetini alabilecegimiz bir ozellik ekliyoruz
		self.max=max
		self.kuvvet=0 #~ ucun 0. kuvvetini ilk olarak alamk istedigimizi soyluyoruz
	def __iter__(self): # ~ Bunu yazarak sinifimiza iterable bir obje seklinde olusturabilecegiz.
		return self # ~ Objemizi direkt donuyoruz burada yapilacak tek islem..
	def next(self):
		if self.kuvvet<=self.max: #~ Max a ulasmamissam kuvvet almaya devam edicegim diyoruz
			sonuc = (3**self.kuvvet) #~ self.kuvvet 0 oldugundan 3^0 dan 1 degerini sonuca atamis olduk
			self.kuvvet+=1 #` Her next yaptigimda kuvveti bir arttirmasi icin next metodunun icinde aktariyoruz.

			return sonuc #~ Sonucu bastirabilmekcicin icin bu sekilde sonucu donduruyoruz
		else:
			raise StopIteration #~ Max i gecerse bunu firlatiyoruz(Python 3^6 ya kadar gosterebildigi icin sonrasinda bu hatayi firlaticak)

kuvvet=Kuvvet3(6) # ~ Oblemizi olusturuyoruz (max 6 olacak sekilde)
iterator=iter(kuvvet) # ` kuvvet objemzi iterable olarak olsuturduk  bu itareble bir obje oldugu icin iteartor olusturuyoruz.

#` print(next(iterator)) # 1 
#` print(next(iterator)) # 3
#` print(next(iterator)) # 9
#` print(next(iterator)) # 27
#` print(next(iterator)) # 81 
#` print(next(iterator)) # 243

# ` Yukaridaki olayi for dongusu ile gormeye caliscalim.

for i in kuvvet:
	print(i) # 1 ,3 ,9 ,27, 81,243

# Tekrar bu donguyu bastimaya calisalim

for j in kuvvet:
	print(j) # Bastirmadi!!