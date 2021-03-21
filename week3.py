#Örnek 2:
#Bir dersten geçme notu 50 olarak belirlenmiş olsun. Kullanıcıya notunu
#sorup dersten geçme-kalma durumunu ekrana yazan programı yazınız.
gecme_notu = 50
ogrenci_notu = int(input("Sınav notunuzu yazınız: "))
if ogrenci_notu >= 50:
    print("Dersi geçtiniz.")
else:
    print("Dersi geçemediniz.")

#Örnek 3:
#Bir öğrencinin 2 tane sınav notunu kullanıcıdan alıp ortalamasını
#bulunuz. 100'lük sistemdeki bu notu 5'lik sistemdeki nota dönüştüren
#programı yazınız. (0-24->0; 25-44->1; 45-54->2; 55-69->3; 70-84->4; 85-
#100->5)

sinav1 = int(input("1. sınav notunu giriniz: "))
sinav2 = int(input("2. sınav notunu giriniz: "))
sonuc = (sinav1 + sinav2)/2
print("5'lik sisteme gore notunuz: ")
if sonuc < 0 or sonuc>100:
    print("Geçersiz not girişi")
elif sonuc<=24:
    print("0")
elif sonuc<=44 and sonuc>24:
    print("1")
elif sonuc<=54 and sonuc>44:
    print("2")
elif sonuc<=69 and sonuc>54:
    print("3")
elif sonuc<=84 and sonuc>69:
    print("4")
elif sonuc<=100 and sonuc>84:
    print("5")

#Örnek 4:
#Kullanıcının 1 ile 7 arasında bir sayı girmesini isteyiniz. Girilen sayının
#haftanın hangi günü olduğunu bulan programı yazınız. Hatalı girişlerde
#programın uyarı vermesini sağlayınız.
gun_int= int(input("1-7 arasiında bir sayı giriniz: "))
if gun_int == 1:
    print("Pazartesi")
elif gun_int == 2:
    print("Sali")
elif gun_int == 3:
    print("Çarşamba")
elif gun_int == 4:
    print("Perşembe")
elif gun_int == 5:
    print("Cuma")
elif gun_int == 6:
    print("Cumartesi")
elif gun_int == 7:
    print("Pazar")
else:
    print("Hatalı bir değer girdiniz.")

# Örnek 5:
# Yazılı Ortalaması Girilen Öğrencinin Sınıf Geçme Durumunu (GEÇTİ
# KALDI)Gösteren Python kodu

ortalama = float(input("Yazılı ortalaması giriniz: "))
if ortalama <0 or ortalama >100:
    print("Geçersiz not ortalamasi")
elif ortalama >= 60:
    print("Geçti")
elif ortalama < 60:
    print("Kaldı")

# Örnek 6:
# Girilen SayınınTek mi Çift mi Olduğunu Bulan Python Örneği

sayi = int(input("Sayı giriniz: "))
if sayi % 2 == 0:
    print("Bu sayı çifttir")
else:
    print("Bu sayı tektir.")

# Örnek 7:
# Girilen Sayının Pozitif, Negatif, ya da 0 Olduğunu Bulan Python Örneği

sorgula = int(input("Sorgulanacak sayıyı giriniz: "))
if sorgula < 0:
    print("Negatif")
elif sorgula > 0:
    print("Pozitif")
elif sorgula == 0:
    print("Bu sayi 0")

#Örnek 8:
#YaşıGirilen Kişinin Ehliyet Alıp AlamayacağınıGösteren Python Örneği

yas_sorgu = int(input("Yaşınızı giriniz: "))
if yas_sorgu > 18:
    print("Ehliyet alabilirsiniz.")
elif yas_sorgu < 18 and yas_sorgu > 0:
    print("Ehliyet alamazsınız.")
else:
    print("hatalı değer")
