# Vector del correo electrónico
correo = ["oferta", "gratis", "dinero", "ganar", "clic"]

#Vector de palabras comunes en correo spam
spam_words = ["oferta", "gratis", "dinero", "ganar", "clic"]

# Calcular la cantidad de palabras spam en el correo
cantidad_de_spam = sum([1 for word in correo if word in spam_words])

if cantidad_de_spam > 2:
    print("¡Alerta! Este correo electrónico podría ser spam.")
else:
    print("Este correo electrónico parece ser legitimo")