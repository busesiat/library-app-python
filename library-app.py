class Library:
    
    def __init__(self):
        self.kitaplar = {}
        with open('books.txt', 'r') as dosya:
            for satir in dosya:
                 satir = satir.strip()
                 if not satir:
                     continue
                 kitap_bilgileri = satir.split(',')
                 ad = kitap_bilgileri[0].strip()
                 yazar = kitap_bilgileri[1].strip()
                 yil = kitap_bilgileri[2].strip()
                 sayfa_sayisi = kitap_bilgileri[3].strip()
                 self.kitaplar[ad] = Kitap(ad, yazar, yil, sayfa_sayisi)      

                                  
    def addBook(inputAd, inputYazar, inputYil, inputSayfaSayisi):
        with open('books.txt', 'a') as dosya:
            dosya.write(f"{inputAd},{inputYazar},{inputYil},{inputSayfaSayisi}\n")
        print('Kitap basariyla eklendi!')

        
    def removeBook(inputAd):
        with open('books.txt', 'r') as dosya:
            satirlar = dosya.readlines()
    
        with open('books.txt', 'w') as dosya:
            for satir in satirlar:
                if inputAd not in satir:
                    dosya.write(satir)
    
    def listBook():
         for ad, kitap in kutuphane.kitaplar.items():
                print(kitap)
            
    
class Kitap:
    def __init__(self, ad, yazar, yil, sayfa_sayisi):
        self.ad = ad
        self.yazar = yazar
        self.yil = yil
        self.sayfa_sayisi = sayfa_sayisi

    def __str__(self):
        return f"{self.ad},{self.yazar},{self.yil},{self.sayfa_sayisi}"

# Library objesi oluşturma
kutuphane = Library()

while True: 
    print('MENU')
    print('----------')
    print('1) List Books')
    print('2) Add Book')
    print('3) Remove Book')
    print('0) Exit')

    
    userInput = int(input('Option: '))
    
    if userInput == 1:
        # list books
        Library.listBook()
    elif userInput == 2:
            # add book
            inputKitapAdi = input("Kitap Adi: ")
            inputYazar = input("Yazar Adi: ")
            inputYil = int(input("Yil: "))
            inputSayfaSayisi = int(input("Sayfa Sayisi: "))

            Library.addBook(inputKitapAdi, inputYazar, inputYil, inputSayfaSayisi)
    elif userInput == 3:
            # remove book
            inputSilinecekKitap = input('Silinecek Kitap Adi: ')
            Library.removeBook(inputSilinecekKitap)
    elif userInput == 0:
        break;
    else:
            print('Geçersiz seçenek!')






