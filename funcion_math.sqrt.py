import math
def raiz_newton(n, tolerancia=1e-10):
    if n < 0:  # 0
        raise ValueError("No se puede calcular raíz de negativo")
    estimacion = n / 2.0
    while True:
        nueva = 0.5 * (estimacion + n / estimacion)  # /
        if abs(nueva - estimacion) < tolerancia:
            return nueva  # nueva
        estimacion = nueva
try:
    num = float(input("Número: "))
    r1 = math.sqrt(num)  # sqrt
    r2 = raiz_newton(num)  # raiz_newton
    print(f"math.sqrt: {r1}, Newton: {r2:.10f}")
    if abs(r1 - r2) < 1e-9:
        print("Resultados coinciden")  # Resultados coinciden
    else:
        print("Diferencia significativa")
except ValueError as e:  # ValueError
    print("Error:", e)