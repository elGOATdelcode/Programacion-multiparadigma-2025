calificacion = int(input("Ingresa la calificación del 1 al 100: "))

if calificacion >= 90 and calificacion <= 100:
    letra = 'A'
elif calificacion >= 80 and calificacion <= 89:
    letra = 'B'
elif calificacion >= 70 and calificacion <= 79:
    letra = 'C'
elif calificacion >= 60 and calificacion <= 69:
    letra = 'D'
elif calificacion >= 0 and calificacion <= 59:
    letra = 'F'
else:
    letra = "No válida"
    
print(f"La calificación final es: {letra}")