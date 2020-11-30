#poner los exclude en un diccionario

with open('exclude.txt', 'r') as exclude:
    ex_words = exclude.read()
    #dividr los string por cada salto de linea para generar una lista
    ex_words = ex_words.strip()
    ex_words = ex_words.split('\n')

    print(ex_words)



# contar las palabras del archivo de los tweets, por defecto la funcion open tiene el 'r' de read

counter = open('tweet.txt', encoding='utf-8')
#crear el diccionario, haciendo un break del loop previamente vemos que nos devuelve un objeto string
palabras = {}
for linea in counter:
    linea = linea.strip()
    linea = linea.lower()
    linea = linea.split()
    for palabra in linea:
        palabras[palabra] = palabras.get(palabra, 0) + 1 #esto cada vez que encuentra una palabra nueva le pone un 0, pero si la encuentra denuevo le suma 1 , para controlar el uso
        #print(palabras)


# ordernar palabras desde las mas usadas hasta las menos usadas 

mas_usadas = sorted(palabras, key=palabras.get, reverse=True)
count = 1
for palabra in mas_usadas:
    #top de palabras
    if count < 31 and palabra not in ex_words:
        print('Top ', count, ': ', 'Utilizada: ', palabras[palabra], 'veces ', '---> ', palabra)
        count += 1
   
