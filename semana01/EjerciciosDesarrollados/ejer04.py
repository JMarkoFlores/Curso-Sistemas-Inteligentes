'''
4) Una empresa paga a sus vendedores un sueldo básico mensual de S/.300. El sueldo bruto es igual al sueldo básico más una comisión, que es igual al 9% del monto total vendido. Por ley, todo vendedor se somete a un descuento del 11 %. Diseñe un programa que calcule la comisión, el sueldo bruto, el descuento y el sueldo neto de un vendedor de la empresa. Se debe ingresar el monto total vendido. 
'''

try:
        while True:
                mtv = float(input("Ingrese el monto total vendido: "))
                if mtv < 0 :
                        print("No ingrese valores negativos")
                break;
        sbm = 300
        sb = (sbm + 0.9 * mtv) 
except ValueError:
        print("Ingrese valor numérico")
        print(f"Error: {ValueError}")

