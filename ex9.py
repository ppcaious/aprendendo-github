frase = input("Digite uma frase:")
frase_corrigida = ""
c = 0
e = 0

while c < len(frase):
    if frase[c] == " ":
        e = e + 1
        if e == 2:
            frase_corrigida = frase_corrigida + " "
            e = 0
    else:
        frase_corrigida = frase_corrigida + frase[c]

    
    c = c + 1
    
print(frase_corrigida)
            
