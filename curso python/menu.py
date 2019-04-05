
num1= float(input("Ingrese el numero 1: "))
num2= float(input("Ingrese el numero 2: "))

while True:
    opcion=input("Ingrese la operacion que quiere hacer s=suma, r=resta,m=multiplicar, d=dividir: ")
    if opcion=='s':
        print (num1 +num2)
        break
    elif opcion=='r':
        print(num1 - num2)
        break
    elif opcion =='m':
        print(num1 * num2)
        break
    elif opcion =='d':
        print(num1 / num2)
        break
    else:
        print("no valida")
