import math
def mcd(a, b):
    a = abs(a)
    b = abs(b)
    if a == 0 and b == 0:
        return 0
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))
resultado = mcd(num1, num2)
resultado_math = math.gcd(num1, num2)
print(f"MCD calculado: {resultado}")
print(f"MCD con math.gcd: {resultado_math}")
print("Los resultados sí coinciden" if resultado == resultado_math else "No coinciden")
if num1 == 0 and num2 == 0:
    print("Caso especial: ambos números son cero")
else:
    print("Programa terminado")