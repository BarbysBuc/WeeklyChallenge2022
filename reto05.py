# /*
#  * Reto #5
#  * ASPECT RATIO DE UNA IMAGEN
#  * Fecha publicación enunciado: 01/02/22
#  * Fecha publicación resolución: 07/02/22
#  * Dificultad: DIFÍCIL
#  *
#  * Enunciado: Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.
#  * - Nota: Esta prueba no se puede resolver con el playground online de Kotlin. Se necesita Android Studio.
#  * - Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
#  * - Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.
#  *
#  * Información adicional:
#  * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
#  * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#  * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#  * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#  *
#  */

import requests
from PIL import ImageFile

def aspectRatio(ancho, alto):
    precision = 0.02
    relacion = round((ancho / alto),2)
    for i in range(2,51):
        x = relacion * i
        y = round(x)
        diferencia = abs(y-x)
        if diferencia <= precision:
            print(f'El Aspect Ratio de la imagen es {int(y)}:{i}')
            return

url = input('Ingrese la url de la imagen')
resume_header = {'Range': 'bytes=0-2000000'}    # el numero de bytes a descargar
data = requests.get(url, stream = True, headers = resume_header).content
p = ImageFile.Parser()
p.feed(data) # obtiene la info de la foto de los headers de la pagina
if p.image:
    width = p.image.size[0]
    height = p.image.size[1]

aspectRatio(width,height)


