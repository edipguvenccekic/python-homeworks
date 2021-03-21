#1-kullanıcının girdiği 2 sayı arasındaki sayıların toplamını bulan Sorgu
#For ile
print("4. Hafta Ödevi: 1\n2 sayı arasındaki sayıların toplamını bulan program")
say1 = int(input("Birinci sayıyı giriniz: "))
say2 = int(input("İkinci sayıyı giriniz: "))
toplam = 0
if say1 < say2:
    for i in range((say1+1),say2,1):
        toplam+=i
elif say2 < say1:
    for i in range((say2+1),say1,1):
        toplam+=i
print("Girdiğiniz iki sayı arasındaki tamsayıların toplamı: {}".format(toplam))

#2-Klavyeden ardı ardına sayı girişi isteyen ve bu sayı 10 ile 15 arasında
#olmadığı sürece bu işleme devam eden programı yazınız.
print("4. Hafta Ödevi: 2: \n 10-15 arasi sayi girildiğinde programdan çıkılacaktır.")
while True:
    try:
        sayi = int(input("Tamsayı giriniz: "))
    except:
        print("Tamsayı giriniz.")
        sayi = 0
    if sayi >= 10 and sayi <= 15:
         print("Programdan çıkılıyor.")
         break
#3-Kullanıcının istediği kadar girdiği sayıların aritmetik ortalamasını,
#geometrik ortalamasını, en büyüğünü, en küçüğünü bulan programı
#yazınız.
print("Kullanıcı tarafından girilen değerlerin \nen büyüğünü, en küçüğünü, aritmetik ve \ngeometrik ortalamasını hesaplayan program.")
min_bul = 0
max_bul = 0
toplam = 0
carpim = 1
sayi = 0
geometrik = 0
aritmetik = 0
while True:
    try:
        sayi_gir = int(input("Sayı giriniz: "))
    except:
        print("Lutfen tamsayı giriniz: ")
        sayi_gir = 0
        continue
    if sayi_gir < min_bul or min_bul == 0:
        min_bul = sayi_gir
    if sayi_gir > max_bul or max_bul == 0:
        max_bul = sayi_gir
    toplam = toplam + sayi_gir
    carpim = carpim * sayi_gir
    sayi = sayi + 1
    aritmetik = toplam / sayi
    geometrik = carpim**(1/sayi)
    devam = input("\t\tDikkat: Sayi girişini durdurmak için q'ya basınız.")
    if devam == "q":
        break
print("Girilen değerlerin\nEn küçüğü\t\t: {}\nEn büyüğü\t\t: {}\nAritmetik ortalaması\t: {}\nGeometrik ortalaması\t: {}".format(min_bul, max_bul, aritmetik, geometrik))
