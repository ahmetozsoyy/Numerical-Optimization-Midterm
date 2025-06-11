import sympy as sp

def bisection_minimize_auto(f_str, a, b, tol=1e-6, max_iter=100):
    """
    Verilen fonksiyonun türevini kullanarak Bisection yöntemiyle minimum noktayı bulur.
    f_str: fonksiyonun string hali (örnek: "(x - 1)**2 * (x - 2) * (x - 3)")
    a, b: arama aralığı (örnek: 0, 4)
    """
    x = sp.Symbol('x')
    f = sp.sympify(f_str)
    f_prime = sp.diff(f, x)

    f1_lambd = sp.lambdify(x, f_prime, "numpy")
    f_lambd = sp.lambdify(x, f, "numpy")

    fa = f1_lambd(a)
    fb = f1_lambd(b)

    if fa * fb > 0:
        print("Bu aralıkta türev işaret değiştirmiyor, yani minimum garanti değil!")
        return None

    for i in range(max_iter):
        c = (a + b) / 2
        fc = f1_lambd(c)

        print(f"İterasyon {i+1}: x = {c:.6f}, f'(x) = {fc:.6f}")

        if abs(fc) < tol or (b - a)/2 < tol:
            print("Yaklaşım tamamlandı.")
            return c

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    print("Maksimum iterasyon tamamlandı.")
    return (a + b) / 2


# --- Örnek kullanım (senin sorunun aynısı) ---

f_str = "(x - 1)**2 * (x - 2) * (x - 3)"
interval = (0,4) # aralık burada belirlenir a ve b değerleri 

minimum_x = bisection_minimize_auto(f_str, *interval)
print(f"\nMinimum yaklaşık olarak x = {minimum_x}")
