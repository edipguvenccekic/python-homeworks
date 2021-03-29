#Kullanıcıdan alınan bir string dizisinin girilen bir cümle içinde olup olmadığını kontrol eden
#ve eğer bulursa o bölümü büyük harflerle yazan program.
bul = input("Bulunmasını istediğiniz karakter dizisini büyük harfle gösteren program\n Bulunmasını istediğiniz diziyi giriniz: ")
cumle = input("Aranacağı yer:\n")
buyuk = bul.upper()
print("\n" + str(cumle.replace(bul,buyuk)))


#Kullanıcıdan alınan bir cümle içindeki tüm sesli harfleri
#bulup sayan program. 
print("\nKullanıcıdan alınan bir cümle içindeki tüm sesli harfleri bulup sayan program\n\n")
ara = "aeıioöuü"
sira = 0
cumle = str(input("Herhangi bir cümle girip enter tuşuna basınız: "))
print("Cümle içinde yer alan sesli harfler:\n")
for i in ara:
    bul = 0
    for j in cumle.lower():
        if (i == j):
            bul = bul + 1
    print(i+": "+str(bul))

#Kullanıcıdan aldığı cümledeki her kelimeyi bir alt satırda gösteren program
cumle = input("Girilen cümle içindeki her kelimeyi ayrı bir alt satırda boşluk bırakarak gösteren program\n Cümleyi giriniz: ")
cumle = cumle.split()
liste = [0]
x = 0
for i in range(len(cumle)):
    x = x + len(cumle[i])
    liste.append(x)
for i in range(len(cumle)):
    print(" "*liste[i]+ cumle[i])
