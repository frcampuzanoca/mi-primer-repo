valor1= int(input("Ingrese el primer numero: "))
valor2= int(input("Ingrese el segundo valor: "))
valor3= int(input("ingrese el tercer valor: "))

if valor1>valor2 and valor1>valor3:
    mayor= valor1
elif valor2>valor1 and valor2>valor3:
    mayor= valor2
elif valor3>valor1 and valor3>valor2:
    mayor= valor3

print(f"El numero mayor es:{mayor}")
