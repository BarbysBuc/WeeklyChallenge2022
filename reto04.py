# /*
#  * Reto #4
#  * ÁREA DE UN POLÍGONO
#  * Fecha publicación enunciado: 24/01/22
#  * Fecha publicación resolución: 31/01/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
#  * - La función recibirá por parámetro sólo UN polígono a la vez.
#  * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#  * - Imprime el cálculo del área de un polígono de cada tipo.
#  *
#  * Información adicional:
#  * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
#  * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#  * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#  * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#  *
#  */

from turtle import width


def calcularArea(poligono, base, altura):
    if poligono == 'triangulo':
        return (base * altura) / 2
    else:
        return base * altura 

op = True
while op:
    polygon = input('Ingrese el polígono cuya área quiere conocer')
    if polygon.lower() == 'triangulo' or polygon.lower() == 'rectangulo':
        op = False
        width = float(input(f'Ingrese la base del {polygon}'))
        height = float(input(f'Ingrese altura del {polygon}'))
        print(calcularArea(polygon,width, height))
    
    elif polygon.lower() == 'cuadrado':
        op = False
        width = float(input(f'Ingrese el lado del {polygon}'))
        print(calcularArea(polygon, width, width))

#print(calcularArea('triangulo', 4, 3))
#print(calcularArea('rectangulo', 3, 4))
#print(calcularArea('cuadrado', 2, 2))