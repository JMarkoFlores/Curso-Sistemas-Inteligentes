'''
10) Calcular el interés generado por un capital depositado durante cierta cantidad de períodos a una tasa de interés determinada y expresada en porcentaje. Aplicar las siguientes fórmulas: 
i. Monto = Capital*(1 + tasa/100) Número Períodos 
ii. Interés = Monto – Capital
'''
try:
        while True:
                capital = float(input("Ingrese el capital depositado: "))
                tiempo = int(input("Ingrese el numero de periodo: "))
                tasa = float(input("Ingrese la tasa de interes: "))
                if capital > 0 and tiempo > 0 and tasa > 0:
                        print("Valores válido") 
                        break;
                else:
                        print("Ingrese valores mayor que 0")
        monto = capital * (1 + tasa/100) ** tiempo
        interes = monto - capital
        print(f"Interes generado: {interes}")
except ValueError:
        print("Ingrese valor numérico enteros positivos")
        print(f"Error: {ValueError}")
        