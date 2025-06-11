import sympy as sp

# Değişkeni tanımla
x = sp.Symbol('x')

# Fonksiyonu string olarak al
f_str = "(x - 1)**2 * (x - 2) * (x - 3)"  # Örneğin bu fonksiyon log(x) = ln(x) log(x,10) 10 tabanında log e^x e üzeri x

# String ifadeyi matematiksel ifadeye çevir
f = sp.sympify(f_str)

# Türevini al
f_prime = sp.diff(f, x)

# Sonuçları yazdır
print("Fonksiyon:", f)
print("Türevi:", f_prime)
