#Gerekli kütüphaneleri ekliyoruz.
import random
import os
#Harfleri ekliyoruz.
kelist=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
#Şekil şükül olsun :D
print("*||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||*");
print("||                                                                    ||")
print("||  ||   || |||||| ||  || |||||||     ||       ||         ||          ||");
print("||  ||   || ||     || ||  ||   ||    || ||     ||        || ||        ||");
print("||  ||||||| ||     ||||   ||   ||   ||   ||    ||       ||   ||       ||");
print("||  ||   || ||     || ||  ||   ||  |||||||||   ||      |||||||||      ||");
print("||  ||   || |||||| ||  || ||||||| ||       ||  |||||| ||       ||     ||");
print("||                                                                    ||")
print("*||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||*");
print("\nHCKoala Şifre Üreticiye Hoşgeldiniz.");
#Bazı web siteleri Türkçe karakter kabul etmediği için bir ayrım yapıyoruz.
tkk=input("\nŞifrede Türkçe karakter kullanılsın mı ? [E/H]\n");
if tkk=="e" or tkk=="E":
    #Türkçe'ye uygun olan karakter listesi ile şifre üretiyoruz.
    klist=["!","+","#","?","&","%","*","é","'","/","-",".","ş","ğ","ı","ç","ö"];
    #Random olarak belirtilen alanlardan verileri alıyor.
    pinlist=[random.randint(0,100),random.randint(0,100),random.choice(kelist),random.choice(klist),random.randint(0,100),
         random.choice(kelist),random.choice(klist),random.randint(0,100),random.choice(klist),random.randint(0,100),
         random.choice(klist),random.randint(0,100),random.choice(kelist)];
    #Rastgele gelen verileri tekrar karıştırıyoruz.
    random.shuffle(pinlist);
    #Şifrenin adını alıyoruz.
    a=input("Şifre İsmi Nedir?\n");
    #Ana klasörün içinde bulunan sifreler.txt dosyasının içine şifre ve adını yazdırıyoruz.
    sifre=open("sifreler.txt","w");
    sifre.write(a+" Şifresi = "+str(pinlist));
    sifre.close();
    print(a+" Şifreniz= "+str(pinlist));
    #Kullanıcıya seçenekler sunarak gerekli bilgileri almasını sağlıyoruz.
    b=input("Kullanılabilir seçenekler;\nProgramı kapatmak için: E\nKapatmamak için: H\nProgram hakkında bilgi almak için: Hakkında \nİletişim için: iletisim\nWeb sitesini ziyaret etmek için: website\nKomutları kullanılabilir.\n");
    if b=="h" or b=="H":
        print("Program kapatılmayacak.");
        input();
    elif b=="e" or b=="E":
        os.system("taskkill /im pin.py");
    elif b=="Hakkında" or b=="hakkında" or b=="Hakkinda" or b=="hakkinda":
        print("Bu amatör program daha kuvvetli şifreler üretmek için HCKoala tarafından yazılmıştır.");
        input();
    elif b=="iletisim":
        print("admin@halaycekenkoala.com");
        input();
    elif b=="website":
        os.system("start chrome.exe halaycekenkoala.com");
    else:
        print("HATALI GİRİŞ");
        input();
elif tkk=="h" or tkk=="H":
    klist=["!","+","#","?","&","%","*","é","'","/","-","."];
    pinlist=[random.randint(0,100),random.randint(0,100),random.choice(kelist),random.choice(klist),random.randint(0,100),
         random.choice(kelist),random.choice(klist),random.randint(0,100),random.choice(klist),random.randint(0,100),
         random.choice(klist),random.randint(0,100),random.choice(kelist)];
    random.shuffle(pinlist);
    a=input("Şifre İsmi Nedir?\n");
    sifre=open("sifreler.txt","w");
    sifre.write(a+" Şifresi = "+str(pinlist));
    sifre.close();
    print(a+" Şifreniz= "+str(pinlist));
    b=input("Kullanılabilir seçenekler;\nProgramı kapatmak için: E\nKapatmamak için: H\nProgram hakkında bilgi almak için: Hakkında \nİletişim için: iletisim\nWeb sitesini ziyaret etmek için: website\nKomutları kullanılabilir.\n");
    if b=="h" or b=="H":
        print("Program kapatılmayacak.");
        input();
    elif b=="e" or b=="E":
        os.system("taskkill /im pin.exe");
    elif b=="Hakkında" or b=="hakkında" or b=="Hakkinda" or b=="hakkinda":
        print("Bu amatör program daha kuvvetli şifreler üretmek için HCKoala tarafından yazılmıştır.");
        input();
    elif b=="iletisim":
        print("admin@halaycekenkoala.com");
        input();
    elif b=="Website":
        os.system("start chrome.exe halaycekenkoala.com");
    else:
        print("HATALI GİRİŞ");
        input();

