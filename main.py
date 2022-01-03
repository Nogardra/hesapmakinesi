import time

#print ("Hello world")
#name = "Beyza"
#surname = "Güneren"
#fullname = name + surname
#print (fullname)
#age = 12
#age += 2
#print (age)
#print("your age is:"+str(age))
#height = ( 158.8)
#print(type(height))
#print("your height is:" +str( height)+"cm")
#human = True
#print(type(human))
#print("Are you really a human:"+str(human))


#name , age , doğruluk = "beyza" , 14 , True
#print(name)
#print(age)
#print(doğruluk)

#cat = dog = parrot = "Zeytin"
#print(cat)
#print(dog)
#print(parrot)


#name = "Beyza"
#print(len(name))
#print(name.find("e"))
#print(name.upper())
#print(name.capitalize())
#print(name.lower())
#print(name.isdigit())
#print(name.isalpha())
#print(name.count("b"))
#print(name.replace("b","F"))
#print(name*5)


#isim = (input("what is your name"))
#print ("Hello"+isim)

#soru = (input("Yaşadığın ülke nedir:?"))
#if soru == "Türkiye":
    #print ("Geçmiş olsun")
#elif soru == "Norveç":
     #print("Hayalim:(")
#elif soru == "Almanya":
    #print("O da efsane")
#else:
    #print("yaşamıyon mu lan")

#name = ""
#while len(name) == 0:
    #name = input("please enter your name: ")
#print ("Welcome " + name)



#for saniye in range(10,0,-1):
    #print(saniye)
    #time.sleep(0.5)

#print("happy new year")


hesap_makinesi = ""
while len(hesap_makinesi)==0:
    print("toplama yapmak için 1 e")
    print("çıkartma yapmak için 2 ye")
    print("çarpma yapmak için 3 e")
    print("bölme yapmak için 4 e ")
    print("çıkmak için 0 a basın")
    hesap_makinesi = input("yapmak istediğiniz işlemin numarsını yazın")

    while hesap_makinesi == str(0):
        print("görüşmek üzere:)")
        hesap_makinesi= "görüşürüz"


while hesap_makinesi == str(1):
    a = int(input("birinci sayının değerini girin"))
    b = int(input("ikinci sayının değerini girin"))
    print(int(a + b))
    hesap_makinesi = "bitti"
    
while hesap_makinesi == str(2):
        c = int(input("birinci sayının değerini girin"))
        d = int(input("ikinci sayının değerini girin"))
        print(int(c-d))
        hesap_makinesi = "bitti"

while hesap_makinesi == str(3):
    e = int(input("birinci sayının değerini girin"))
    f = int(input("ikinci sayının değerini girin"))
    print(int(e*f))
    hesap_makinesi = "bitti"

while hesap_makinesi == str(4):
    g = int(input("birinci sayının değerini girin"))
    h = int(input("ikinci sayının değerini girin"))
    print (int(g/h))
    hesap_makinesi = "bitti"
    



