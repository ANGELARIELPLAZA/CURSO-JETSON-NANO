Variable=5
variable=3
VaRiAbLe=8
#Son todas variables distintas porque Python (como muchos otros lenguajes) distingue mayúsculas y minúsculas

a=5
a=18
#a tomará el último valor asignado (lo que tuviera guardado anteriormente la variable, se pierde).

#1variable=23.95
#Arroja error porque los nombres de variables sólo pueden comenzar con letras o guiones bajos (_).


n1=int(input())
n2=float(input())
#Sabemos que input() lee lo que el usuario escribe en el programa, pero el tipo de eso que lee será siempre 
# string. Si necesitamos que sea un número debemos convertir lo que input() devuelve. Para convertir a número 
# entero usamos int(input()) y para convertir a número con decimales usamos float(input()).