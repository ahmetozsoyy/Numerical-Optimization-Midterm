import math
#değerlerin fonksiyonda sonucu bulunur, çarpımları eksi ise orada kök vardır. sonra 2 değerin arası alınır hangi aralıkta
#devam edeceğine karar vermek için yeni kökün fonksiyondaki değeri bulunur eski aralığın değerlerinden hangisi ile
#çarpımı negatifse oradan devam edilir

def F(x):
    return x**3 - x -1

def bisection(a, b, hata=0.000001):
    i = 0
    if F(a) * F(b) > 0:
        print("Başlangıç aralığı geçersiz, çünkü işaretler aynı.")
        return
    
    while (b - a) / 2 > hata:
        c = (a + b) / 2  # Orta nokta
        if F(c) == 0:  # Kök bulundu
            break
        elif F(a) * F(c) < 0:
            b = c  # Kök sol yarıda
        else:
            a = c  # Kök sağ yarıda
        
        i += 1
        print(f"{i}. adımda yaklaşık değer = {c:.6f}")
    
    c = (a + b) / 2
    print(f"Yaklaşık kök = {c:.6f}")
    print(f"f({c:.6f}) = {F(c):.6f}")

if __name__ == "__main__":
    a = 1  # Başlangıç aralığı
    b = 2  # Başlangıç aralığı
    print(f"Yönteme başladığımız aralık: [{a}, {b}]")
    bisection(a, b)
    input("Çıkmak için bir tuşa basın...")  # getch() yerine kullanıldı
