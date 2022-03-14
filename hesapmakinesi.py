sayi1=int(input("1. Sayıyı Girin: "))
islem=str(input("İşlemi Girin: "))
sayi2=int(input("2. Sayıyı Girin: "))
if islem=="+" :
    print("SONUÇ: ",sayi1+sayi2)
elif islem=="-" :
    print("SONUÇ: ",sayi1-sayi2)
elif islem=="*" :
    print("SONUÇ: ",sayi1*sayi2)
elif islem=="/" :
    print("SONUÇ: ",sayi1/sayi2)
else :
    print("Hata")