import sympy as sp

def newton_raphson_minimize_auto(f_str, x0, interval, tol=1e-6, max_iter=100):
    """
    Kullanıcının verdiği fonksiyonu otomatik türevleyerek Newton-Raphson ile minimizasyon yapar.

    f_str    : string olarak verilen fonksiyon (örnek: "(x - 1)**2 * (x - 2) * (x - 3)")
    x0       : başlangıç tahmini
    interval : (a, b) şeklinde minimum aranacak aralık
    """
    x = sp.Symbol('x')
    f = sp.sympify(f_str)
    f_prime = sp.diff(f, x)
    f_double_prime = sp.diff(f_prime, x)

    f_lambd = sp.lambdify(x, f, "numpy")
    f1_lambd = sp.lambdify(x, f_prime, "numpy")
    f2_lambd = sp.lambdify(x, f_double_prime, "numpy")

    x_val = x0
    for i in range(max_iter):
        f1 = f1_lambd(x_val)
        f2 = f2_lambd(x_val)

        if f2 == 0:
            print("2. türev sıfır, yöntem durdu.")
            return None
        
        x_new = x_val - f1 / f2
        
        # Aralık dışına çıktıysa sınırlıyoruz
        x_new = max(min(x_new, interval[1]), interval[0])

        print(f"İterasyon {i+1}: x = {x_new}, f(x) = {f_lambd(x_new)}")

        if abs(x_new - x_val) < tol:
            print("Yaklaşım tamamlandı.")
            return x_new

        x_val = x_new

    print("Maksimum iterasyon tamamlandı.")
    return x_val


# --- Kullanıcıdan fonksiyon alma ve çözüm ---

# Örnek: f(x) = (x - 1)^2(x - 2)(x - 3)
f_str = "(x - 1)**2 * (x - 2) * (x - 3)"                                 #!!!!!!!!Fonksiyon string olarak gir!!!!!!
x0 = 3  # x0 başlangıç değeri
interval = (0, 4)  # x'in aralığı

sonuc = newton_raphson_minimize_auto(f_str, x0, interval)
print(f"\nMinimum yaklaşık olarak x = {sonuc: .4f}")