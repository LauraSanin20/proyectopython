# Condiciones multiples

sensorNivelAgua=int(input("Digite el nivel de agua de la represa: "))

print(f"El nivel de agua es: {sensorNivelAgua}")

if sensorNivelAgua > 0  and sensorNivelAgua <= 150:    
    print("muy poca agua, las puertas estan cerradas")
elif sensorNivelAgua > 150 and sensorNivelAgua <= 400:    
    print("Operando normalmente")
elif sensorNivelAgua > 400 and sensorNivelAgua <= 420:
    print("Precaucion! Revise el nivel del agua")
elif sensorNivelAgua > 420:
    print("Este parche se calento, corre.......")
else:
    print("Revise el sensor, medida no valida")