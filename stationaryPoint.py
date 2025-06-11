import sympy as sp

# Değişkenleri tanımla
x1, x2 = sp.symbols('x1 x2')

# Fonksiyonu tanımla
f = x1**2 - 2*x1 - 3*x2*x1 +12*x2 

# Gradyan
grad_f = [sp.diff(f, var) for var in (x1, x2)]

# Durağan noktalar (gradyanı sıfıra eşitle)
stationary = sp.solve(grad_f, (x1, x2))
print("Durağan Nokta:", stationary)

# Hessian matrisi
H = sp.hessian(f, (x1, x2))
print("Hessian Matrisi:")
sp.pprint(H)

# Hessian'ı durağan noktada değerlendir
H_at_stationary = H.subs(stationary)
det_H = H_at_stationary.det()
print("Hessian determinantı:", det_H)

# Tip belirleme
if det_H > 0:
    if H_at_stationary[0, 0] > 0:
        print("Yerel minimum")
    else:
        print("Yerel maksimum")
elif det_H < 0:
    print("Saddle point")
else:
    print("Kararsız")

