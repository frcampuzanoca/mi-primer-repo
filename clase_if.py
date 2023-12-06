print("""
              BIENVENIDO A MI PROGRAMA
         HOY VAMOS A TRABAJAR CON UNA FUNCIONALIDAD DE UN MENU
               INGRESE 1 : PARA SUMAR DOS NUMEROS..................
               INGRESE 2 : PARA RESTAR DOS NUMEROS.................
               INGRESE 3 : PARA MULTIPLICAR DOS NUMEROS............
               INGRESE 4 : PARA DIVIDIR DOS NUMEROS................""")

opt= input("Ingrese su selección: ")

if opt=="1":
    a= int(input("ingresa el primer valor: "))
    b= int(input("Ingrese el segundo valor: "))
    print(f"{a}+{b}={a+b}")
elif opt=="2":
    a= int(input("ingresa el primer valor: "))
    b= int(input("Ingrese el segundo valor: "))
    print(f"{a}-{b}={a-b}")
elif opt=="3":
    a= int(input("ingresa el primer valor: "))
    b= int(input("Ingrese el segundo valor: "))
    print(f"{a}*{b}={a*b}")
elif opt=="4":
    a= int(input("ingresa el primer valor: "))
    b= int(input("Ingrese el segundo valor: "))
    print(f"{a}/{b}={a/b}")
else:
    print("la selecion ingresada no es valida")
    

    