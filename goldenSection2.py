import math

# Fonksiyon tanımı: f(x) = (x - 1)^2 * (x - 2) * (x - 3)
def f(x):
    f = (x-1)**2*(x-2)*(x-3)
    return f

# Aralık sınırları
xalt = 0        # Alt sınır
xust = 4        # Üst sınır

# Hedef doğruluk değeri
dx = 0.0001   # hoca kaç sıfır verirse round parametresini o yap

# buraya kadar değisicek

# Altın oran hesaplaması
alpha = (1 + math.sqrt(5)) / 2
tau = 1 - 1 / alpha

# Epsilon değeri (normalize edilmiş hata toleransı)
epsilion = dx / (xust - xalt)

# Gerekli iterasyon sayısı (yaklaşık formülle)
N = round(-2.078 * math.log(epsilion))

# İlk iterasyon için k = 0
k = 0 

# İlk iki test noktası belirleniyor
x1 = xalt + tau * (xust - xalt)
f1 = f(x1)

x2 = xust - tau * (xust - xalt)
f2 = f(x2)

# İlk değerler yazdırılıyor
print(k, x1, x2, f1, f2)

# Altın oran algoritması döngüsü başlatılıyor
for k in range(0, N):
    if f1 > f2:
        # f1 daha büyükse, minimum x2 tarafındadır
        xalt = x1
        x1 = x2
        f1 = f2
        x2 = xust - tau * (xust - xalt)
        f2 = f(x2)
    else:
        # f2 daha büyükse, minimum x1 tarafındadır
        xust = x2
        x2 = x1
        f2 = f1
        x1 = xalt + tau * (xust - xalt)
        f1 = f(x1)

    # Her adımda ara değerler yazdırılıyor
    print(round(k+1, 4), round(x1, 4), round(x2, 4), round(f1, 4), round(f2, 4))

# Yaklaşık minimum nokta (x1 ve x2'nin ortalaması)
x = 0.5 * (x1 + x2)

# Minimum nokta yazdırılıyor
print(x)
