import math
#ilk adımda fonksiyonun türevi alınır, aldıktan sonra x1 = x0 - f(x0)/f'(x0)

def F(x):
    return (x-1)**2*(x-2)*(x-3) 

def numerical_derivative(f, x, h=0.0001):
    return (f(x + h) - f(x)) / h

def newton_raphson():
    hata = 0.0000001
    x0 = 0
    x = 0
    i = 0
    
    print(f"Yönteme başladığımız nokta = {x0:.6f}")
    
    while True:
        x = x0
        f_prime_x = numerical_derivative(F, x0)  # Sayısal türev
        x0 = x - F(x) / f_prime_x
        i += 1
        print(f"{i}. adımda yaklaşık değer = {x0:.6f}")
        
        if abs(x0 - x) <= hata:
            break
    
    print(f"Yaklaşık kök = {x0:.6f}")
    print(f"f({x0:.6f}) = {F(x0):.6f}")

if __name__ == "__main__":
    newton_raphson()
    input("Çıkmak için bir tuşa basın...")  # getch() yerine kullanıldı
