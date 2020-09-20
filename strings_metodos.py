frase='Seguir sin detenerse, ese es el secreto del éxito'
palabra='secreto'
print(palabra in frase)                #True
print('Secreto' not in frase)          #True
ciudad='londres'
print(palabra.upper(),ciudad.capitalize(),'New York'.lower())
print("los angeles".title())                    #Los Angeles
print(ciudad.islower())                         #True
print(ciudad.isupper())                         #False
print("100".isdigit())                          #True
print("Hola Mundo".istitle())                   #True
print("Hola mundo futuro".split()[0])           #Hola
elementos='3840x2160'                           #pixeles 4k UHD 16:9
print(elementos.split('x'))                     #['3840', '2160'] separando por el caracter x
print("   Buenos días     ".strip())            #Buenos días
print("Hola mundo".replace('o','0'))            #H0la mund0
print("por un beso... yo no sé qué te diera por un beso".count("beso"))  #2
print("de Madrid al cielo".find("Madrid"))      #3

