# /*
#  * Reto #9
#  * CÓDIGO MORSE
#  * Fecha publicación enunciado: 02/03/22
#  * Fecha publicación resolución: 07/03/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
#  * - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
#  * - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
#  * - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
#  *
#  * Información adicional:
#  * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
#  * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
#  * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
#  * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#  *
#  */

from typing import TextIO


equivalencias = {
    'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....', 'I':'..',
    'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'.--',
    'N':'-.', 'Ñ':'--.--', 'O':'---', 'P':'.--.',
    'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-',
    'Y':'-.--', 'Z':'--..', '0':'-----', '1':'.----',
    '2':'..---', '3':'...--', '4':'....-', '5':'.....',
    '6':'-....', '7':'--...', '8':'---..', '9':'----.',
    '.':'.-.-.-', ',':'--..--', '?':'..--..', '"':'.-..-.',
    '/':'-..-.'
}

def textoAMorse(textoInicial):
    textoFinal = ""
    textoInicial = textoInicial.upper()
    for caracter in textoInicial:
        if caracter == ' ':
            textoFinal += ' '
        else:
            textoFinal += equivalencias[caracter] + ' '
    return textoFinal


def morseATexto(textoInicial):
    textoFinal = ''
    lista = textoInicial.split('  ')
    for palabra in lista:
        texto = ''
        subpalabra = palabra.split()
        for letra in subpalabra:
            for caracter in equivalencias:
                if equivalencias[caracter] == letra:
                    texto += caracter
        textoFinal += texto + ' '
        
    return textoFinal


#textoInicial = input('Ingrese el texto a decodificar\n')
#print(textoAMorse('hola bebe'))
#print(morseATexto('.... --- .-.. .-  -... . -... .'))