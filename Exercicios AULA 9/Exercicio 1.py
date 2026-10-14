intervalos = [0, 0, 0, 0]

numero = int(input("Digite um número: "))

while numero >= 0:
    if numero >= 0 and numero <= 25:
        intervalos[0] += 1
    elif numero <= 50:
        intervalos[1] += 1
    elif numero <= 75:
        intervalos[2] += 1
    elif numero <= 100:
        intervalos[3] += 1
        
    numero = int(input("Digite um número: "))
    
    print("Intervalo [0, 25):", intervalos[0])
    print("Intervalo [25, 50):", intervalos[1])
    print("Intervalo [50, 75):", intervalos[2])
    print("Intervalo [75, 100]:", intervalos[3])
    
    