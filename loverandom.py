import random

name_pareja = "name"

#aqui estaras poniendo los mensajes que quieres que aparezcan 
para_ti_random = [
    "mensaje bonito ",
    "mensaje bonito",
    "mensaje bonito",
    
]
random_mensaje = random.choice(para_ti_random)
#puedes personalizar 
print(".⋆♱⫘⫘⫘⛧°.⋆༺♱༻⋆.°⛧⫘⫘⫘♱⋆.") #aqui los marcos 
print("٠࣪⭑   ٠࣪⭑")
print(f"𓆩♡𓆪 ¡Para {name_pareja.upper()}!                           *")
print("٠࣪⭑    ٠࣪⭑")
print(f"𓆩♡𓆪 {random_mensaje.ljust(34)}   *") #en el ljust depende de las letras que escribas puedes poner un numero ajustandolo 
print("٠࣪⭑   ٠࣪⭑")
print(".⋆♱⫘⫘⫘⛧°.⋆༺♱༻⋆.°⛧⫘⫘⫘♱⋆.")
