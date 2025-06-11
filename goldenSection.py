import math
import numpy as np
import pandas as pd

def altin_oran_yontemi(f_str, a, b, epsilon, max_iter=100):
    """
    Altın oran arama metodu ile fonksiyonun minimumunu bulur.
    
    Parametreler:
    f_str : string olarak verilen fonksiyon
    a, b : arama aralığı
    epsilon : yakınsama toleransı
    max_iter : maksimum iterasyon sayısı
    
    Dönüş:
    pandas.DataFrame : iterasyonlar ve sonuçları gösteren tablo
    """
    # Altın oran sabiti
    golden_ratio = (math.sqrt(5) - 1) / 2  # yaklaşık 0.618
    
    # Fonksiyonu lambda fonksiyonu olarak tanımlama
    x = lambda x: eval(f_str)
    
    # Sonuçları saklamak için veri yapısı
    results = []
    
    # İlk iterasyon için değerleri hesaplama
    c = b - golden_ratio * (b - a)
    d = a + golden_ratio * (b - a)
    fc = x(c)
    fd = x(d)
    
    # İlk iterasyon değerlerini kaydet
    results.append([0, a, b, fc, fd])
    
    # İterasyon sayısını hesaplama (teorik olarak)
    N_theory = -2.078 * math.log(epsilon / (b - a)) / math.log(golden_ratio)
    N_theory = math.ceil(N_theory)
    print(f"Teorik iterasyon sayısı N = {N_theory}")
    
    # Ana döngü
    for i in range(1, max_iter + 1):
        if fc < fd:  # Minimum c'ye daha yakın
            b = d
            d = c
            c = b - golden_ratio * (b - a)
            fd = fc
            fc = x(c)
        else:  # Minimum d'ye daha yakın
            a = c
            c = d
            d = a + golden_ratio * (b - a)
            fc = fd
            fd = x(d)
        
        # Sonuçları kaydet
        results.append([i, c, d, fc, fd])
        
        # Yakınsama kontrolü
        if abs(b - a) < epsilon:
            print(f"Yakınsama sağlandı, iterasyon: {i}")
            break
    
    if i == max_iter:
        print("Maksimum iterasyon sayısına ulaşıldı, yakınsama sağlanamadı.")
    
    # Sonuçları pandas DataFrame'e dönüştür
    df = pd.DataFrame(results, columns=['k', 'x1', 'x2', 'f(x1)', 'f(x2)'])
    df = df.round(4)  # 4 ondalık basamağa yuvarla
    
    return df

# Örnek problem
f_str = "(x - 1)**2 * (x - 2) * (x - 3)"
a = 0.0  # Başlangıç aralığı
b = 4.0
epsilon = 0.0001  # Tolerans

# Altın oran yöntemi ile çözüm
sonuclar = altin_oran_yontemi(f_str, a, b, epsilon)

# Sonuçları göster
print("\nİterasyon Sonuçları:")
print(sonuclar)

# Son iterasyondaki minimum noktayı göster
son_x = (sonuclar.iloc[-1]['x1'] + sonuclar.iloc[-1]['x2']) / 2
son_f = eval(f_str.replace('x', f'({son_x})'))
print(f"\nBulunan minimum nokta: x = {son_x:.4f}, f(x) = {son_f:.4f}")