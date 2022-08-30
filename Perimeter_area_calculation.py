import time
def dörtgen_kare():
        while True:

            print( ''' 
            
                       a         
                 _____________
                |             |  
              a |             |  a
                |             |      
                |_____________|
                      a
                
                
                
            ''')


            a = int(input("a kenarını giriniz :"))


            if (a <= 0) :
                print("Kenar Ölçüleri 0 ve '-' değer alamaz!")
                time.sleep(1)
                print("Lütfen Kenar Ölçülerini Kare Şartlarına Uygun Giriniz!")
                return

            else:
                 print("Karenin çevresi {}".format(a*4))
                 print("Kare'nin alanı:{}".format(a**2))
                 break





def dörtgen_dikdörtgen():
        while True:

            print('''
             
            
            
                         a
                 _________________
                |                 |  
            b   |                 |  b
                |                 |      
                |_________________|
                         a
            
            ''')




            print("Kenar Ölçülerini Giriniz:")

            a = int(input("a kenarını giriniz :"))
            b = int(input("b kenarını giriniz :"))


            if((a<=0) or (b<=0)):
                print("Kenar Ölçüleri 0 ve '-' değer alamaz!")
                time.sleep(1)
                print("Lütfen Kenar Ölçülerini Dikdörtgen Şartlarına Uygun Giriniz!")
                return



            elif((a==b )):
                print("Dörgenimiz Dikdörtgen değildir.")
                print("Bu dörtgenimiz bir Kare'dir.")
                print("Lütfen Seçim Ekranından Kare'yi seçiniz!")

                return

            else:
                print("Dikdörtgenin çevresi:{}".format((a + b)*2 ))
                print("Dikdörtgenin alanı:{}".format(a *b))
                break


def dörtgen_yamuk():


        while True:

            print("""
            
            
                        a
               ____________________
              /  |                 \ 
           c /   | h                \  b
            /    |                   \ 
           /_____|____________________\ 
                         d   
            
            
            
            
            
            
            
            
            
            """)
            print("Kenar Ölçülerini Giriniz:")

            a = int(input("a kenar uzunluğunu giriniz:"))
            b = int(input("b kenaruzunluğunu giriniz:"))
            c = int(input("c kenar uzunluğunu giriniz :"))
            d = int(input("d kenar uzunluğunu giriniz :"))
            h = int(input("h yüksekliğini  giriniz :"))

            if ((a <= 0) or (b <= 0) or (c <= 0) or (d <= 0) or (h <= 0)):
                print("Kenar Ölçüleri 0 ve '-' değer alamaz!")
                time.sleep(1)
                print("Lütfen Kenar Ölçülerini Yamuk Şartlarına Uygun Giriniz!")
                return

            else:

                print("Yamuğun çevresi:{}".format(a + b + c + d))

                print("Yamuğun alanı:{}".format((a + b)*h/2))
                break



def dörtgen_eşkenar():

        print("""
        
        
                     a
               ___________________
              /  |               / 
          a  /   | h            /  a
            /    |             /      
           /_____|____________/
                     a
        
        
        
        
        """)


        while True:
            print("Kenar Ölçülerini Giriniz:")

            a = int(input("a kenarının uzunluğunu giriniz :"))
            h = int(input("h yüksekliğini giriniz :"))

            if ((a <= 0) or (h <= 0)):
                print("Kenar Ölçüleri 0 ve '-' değer alamaz!")
                time.sleep(1)
                print("Lütfen Kenar Ölçülerini Eşkenar Dörtgen Şartlarına Uygun Giriniz!")
                return

            else:

                print("Eşkenar Dörtgen çevresi:{}".format(a*4))

                print("Eşkenar Dörtgen alanı:{}".format(a * h))
                break
def dörtgen_paralel():

        while True:

            print("""
            
            
                      a
               ___________________
              /  |               / 
           b /   | h            /   b
            /    |             /      
           /_____|____________/
                     a
            
            
            
            
            
            """)

            print("Kenar Ölçülerini Giriniz:")

            a = int(input("a kenarının uzunluğu:"))
            b = int(input("b kenarının uzunluğu:"))
            h = int(input("Yükseklik Giriniz :"))


            if ((a <= 0) or (h <= 0) or (b<=0)):
                print("Kenar Ölçüleri 0 ve '-' değer alamaz!")
                time.sleep(1)
                print("Lütfen Kenar Ölçülerini Paralel Kenar Şartlarına Uygun Giriniz!")
                return

            else:
                print("Paralel Kenar çevresi:{}".format((a+b)*2))

                print("Paralel Kenar alanı:{}".format(a * h))
                break


def üçgen_ikiz():
        while True:

            print("""
    
                        /|\ 
                       / | \        
                    a / h|  \ a
                     /   |   \      
                    /____|____\ 
                         b
    
    
    
    
    
            """)

            print("Kenar Ölçülerini Giriniz:")

            a = int(input("a kenarının uzunluğu:"))
            b = int(input("b kenarının uzunluğu:"))
            h = int(input("Yükseklik Giriniz :"))

            if ((a <= 0) or (h <= 0) or (b <= 0)):
                print("Kenar Ölçüleri 0 ve '-' değer alamaz!")
                time.sleep(1)
                print("Lütfen Kenar Ölçülerini İkiz Kenar Üçgen Şartlarına Uygun Giriniz!")
                return

            elif (a + a > b and a + b > a):
                print("İkiz Kenar Üçgen çevresi:{}".format(a + b + a))

                print("İkiz Kenar Üçgen alanı:{}".format(b * h))
                break
            else:
                print("Üçgen Olma Kurallarına Uygun Değil!")
                time.sleep(1)
                print("İkiz Kenar Üçgen için kenar ölçülerini doğru girdiğinizden emin olun!")
                return


def üçgen_eşkenar():
        while True:

            print("""
    
                        /\ 
                       /  \        
                    a /    \ a
                     /      \      
                    /________\ 
                         a
    
    
    
    
    
            """)

            print("Kenar Ölçülerini Giriniz:")

            a = int(input("a kenarının uzunluğu:"))


            if ((a <= 0)):
                print("Kenar Ölçüleri 0 ve '-' değer alamaz!")
                time.sleep(1)
                print("Lütfen Kenar Ölçülerini Eşkenar Üçgen Şartlarına Uygun Giriniz!")
                return

            else :
                print("Eşkenar Üçgen çevresi:{}".format(a*3))

                print("Eşkenar Üçgen alanı:{}".format(((a **2)*((3**(1/2))/4))))
                break


def üçgen_normal():
        while True:

            print("""
               
                    /|\ 
                   / | \        
                a / h|  \ c
                 /   |   \      
                /____|____\ 
                     b
    
    
    
    
            """)

            print("Kenar Ölçülerini Giriniz:")

            a = int(input("a kenar uzunluğunu giriniz:"))
            b = int(input("b kenaruzunluğunu giriniz:"))
            c = int(input("c kenar uzunluğunu giriniz :"))
            h = int(input("h yüksekliğini  giriniz :"))

            if ((a <= 0) or (b <= 0) or (c <= 0) or (h <= 0)):
                print("Kenar Ölçüleri 0 ve '-' değer alamaz!")
                time.sleep(1)
                print("Lütfen Kenar Ölçülerini Üçgen Şartlarına Uygun Giriniz!")
                return

            elif (a + b > c and a + c > b and b + c > a):
                print("Üçgenin çevresi:{}".format(a * 3))

                print("Üçgenin alanı:{}".format(b*h/2))
                break
            else:
                print("Üçgen Olma Kurallarına Uygun Değil!")
                time.sleep(1)
                print("Üçgen için kenar ölçülerini doğru girdiğinizden emin olun!")
                return


def üçgen_dik():
        while True:

            print("""
            
            
            
                    |\ 
                    | \        
                   a|  \ c
                    |   \      
                    |____\ 
                      b
    
    
    
    
            """)

            print("Kenar Ölçülerini Giriniz:")

            a = int(input("a kenarının uzunluğu:"))
            b = int(input("b kenarının uzunluğu:"))
            c = int(input("c kenarının uzunluğu :"))

            if ((a <= 0) or (c <= 0) or (b <= 0)):
                print("Kenar Ölçüleri 0 ve '-' değer alamaz!")
                time.sleep(1)
                print("Lütfen Kenar Ölçülerini Dik Üçgen Şartlarına Uygun Giriniz!")
                return

            elif (a + c > b and a + b > c and b+c>a):
                print("Dik Üçgen çevresi:{}".format(a + b + c))

                print("Dik Üçgen alanı:{}".format(b * a))
                break
            else:
                print("Üçgen Olma Kurallarına Uygun Değil!")
                time.sleep(1)
                print("Dik Üçgen için kenar ölçülerini doğru girdiğinizden emin olun!")
                return


def daire():
        while True:
            print("""
    
                                                
                          | |   
                       |        |   
                    |             |
                   |   r           |
                  |_________.       |
                   |               |
                    |             |
                       |        | 
                          | | 
                                   
    
                    
    
    
    
            """)
            print("pi sayısı 3 alınmıştır!")
            r = int(input("Yarıçapı Giriniz:"))

            if(r<=0):
                print("Dairenin yarı çapı 0 ve '-' değer alamaz!")
                time.sleep(1)
                print("Lütfen yarı çap ölçüsünü şartlarına uygun Giriniz!")
                return

            else:
                print ("Dairenin yarı çapı {} ise çevresi {} olur".format(r,(2*r*3)))
                print ("Dairenin yarı çapı {} ise alanı {} olur".format(r,(3*(r**2))))
                break


if __name__ == '__main__':
        print("""
        1  - Kare
        2  - Dikdörtgen
        3  - Yamuk
        4  - Eşkenar Dörtgen 
        5  - Paralelkenar
        6  - İkiz Kenar Üçgen
        7  - Eş Kenar Üçgen
        8  - Çeşit Kenar Üçgen
        9  - Dik Üçgen
        10 - Daire 
        
        """)

        şekil = int(input("İşlem yapmak istediğiniz şekil: "))

        if şekil == 1:
            dörtgen_kare()
        elif şekil == 2:
            dörtgen_dikdörtgen()
        elif şekil == 3:
            dörtgen_yamuk()
        elif şekil == 4:
            dörtgen_eşkenar()
        elif şekil == 5:
            dörtgen_paralel()
        elif şekil == 6:
            üçgen_ikiz()
        elif şekil == 7:
            üçgen_eşkenar()
        elif şekil == 8:
            üçgen_normal()
        elif şekil == 9:
            üçgen_dik()
        elif şekil == 10:
            daire()
        else:
            print("Geçersiz İşlem!!")


