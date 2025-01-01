"""
Fait un Pixel Art.

Arguments : 
    image_path : Chemin de l'image à convertir en Pixel Art.
    output : Répertoire de sortie de l'image avec le nom de l'image.
    save_image : True si tu veux enregistrer l'image, False si tu ne veux pas l'enregistrer. Tu peux te servir de cette fonction avec cet argument sur False si tu veux simplement mettre les pixels avec leur couleur dans une variable.
    colors : Fait le Pixel Art avec les couleurs de votre choix. Tu peux aussi choisir le nombre de couleurs, voici les choix : 1 bit, 4 bits, 8 bits et 16 bits.
    by : Tu décides le Pixel Art est par combien en conservant les proportions.
    
Versions :
    1 : Convertit une image en Pixel Art.
    2 : Amélioration des choix de couleurs de Pixel Art
        Argument n renommé par by
        Argument output_path_and_image_name renommé par output
    3 : Option 16 bits ajoutée à l'argument colors, son utilité : faire un Pixel Art avec les couleurs 16 bits.
        Options renommées dans l'argument colors : 2_COLORS → 1 bit, 16_VGA_COLORS → 4 bits, 256_VGA_COLORS → 8 bits


        
Make a Pixel Art.

Arguments:
    image_path: Path of the image to convert to Pixel Art.
    output: Output directory of the image with the name of the image.
    save_image: True if you want to save the image, False if you don't want to save it. You can use this function with this argument set to False if you just want to put the pixels with their color into a variable.
    colors: Make the Pixel Art with the colors of your choice. You also can choose the number of colors, here is the choices : 1 bit, 4 bits, 8 bits et 16 bits.
    by: You decide the Pixel Art is by how much while keeping the proportions.

Versions:
    1: Convert an image to Pixel Art.
    2: Improved Pixel Art color choices
        Argument n renamed to by
        Argument output_path_and_image_name renamed to output
    3: 16 bits option added to the colors argument, his use: make a Pixel Art with 16-bit colors.
        Renamed options in the colors argument: 2_COLORS → 1 bit, 16_VGA_COLORS → 4 bits, 256_VGA_COLORS → 8 bits
"""

from PIL import Image
from collections import Counter
import math

__version__ = "0.2.0"

def PixelArt(image_path: str, by: int, output: str = "./PixelArt.png", save_image: bool = True, colors=None):
    if save_image != True or False:
        save_image = True

    if colors == "1 bit":
        colors = [(255, 255, 255, 255), (0, 0, 0, 255)]
    elif colors == "4 bits":
        colors = [(0, 0, 0, 255), (0, 0, 170, 255), (0, 170, 0, 255), (0, 170, 170, 255), (170, 0, 0, 255), (170, 0, 170, 255), (170, 85, 0, 255), (170, 170, 170, 255), (85, 85, 85, 255), (85, 85, 255, 255), (85, 255, 85, 255), (85, 255, 255, 255), (255, 85, 85, 255), (255, 85, 255, 255), (255, 255, 85, 255), (255, 255, 255, 255)]
    elif colors == "8 bits":
        colors = [(0, 0, 0, 255), (0, 0, 85, 255), (0, 0, 170, 255), (0, 0, 255, 255), (0, 36, 0, 255), (0, 36, 85, 255), (0, 36, 170, 255), (0, 36, 255, 255), (0, 72, 0, 255), (0, 72, 85, 255), (0, 72, 170, 255), (0, 72, 255, 255), (0, 109, 0, 255), (0, 109, 85, 255), (0, 109, 170, 255), (0, 109, 255, 255), (0, 145, 0, 255), (0, 145, 85, 255), (0, 145, 170, 255), (0, 145, 255, 255), (0, 182, 0, 255), (0, 182, 85, 255), (0, 182, 170, 255), (0, 182, 255, 255), (0, 218, 0, 255), (0, 218, 85, 255), (0, 218, 170, 255), (0, 218, 255, 255), (0, 255, 0, 255), (0, 255, 85, 255), (0, 255, 170, 255), (0, 255, 255, 255), (36, 0, 0, 255), (36, 0, 85, 255), (36, 0, 170, 255), (36, 0, 255, 255), (36, 36, 0, 255), (36, 36, 85, 255), (36, 36, 170, 255), (36, 36, 255, 255), (36, 72, 0, 255), (36, 72, 85, 255), (36, 72, 170, 255), (36, 72, 255, 255), (36, 109, 0, 255), (36, 109, 85, 255), (36, 109, 170, 255), (36, 109, 255, 255), (36, 145, 0, 255), (36, 145, 85, 255), (36, 145, 170, 255), (36, 145, 255, 255), (36, 182, 0, 255), (36, 182, 85, 255), (36, 182, 170, 255), (36, 182, 255, 255), (36, 218, 0, 255), (36, 218, 85, 255), (36, 218, 170, 255), (36, 218, 255, 255), (36, 255, 0, 255), (36, 255, 85, 255), (36, 255, 170, 255), (36, 255, 255, 255), (72, 0, 0, 255), (72, 0, 85, 255), (72, 0, 170, 255), (72, 0, 255, 255), (72, 36, 0, 255), (72, 36, 85, 255), (72, 36, 170, 255), (72, 36, 255, 255), (72, 72, 0, 255), (72, 72, 85, 255), (72, 72, 170, 255), (72, 72, 255, 255), (72, 109, 0, 255), (72, 109, 85, 255), (72, 109, 170, 255), (72, 109, 255, 255), (72, 145, 0, 255), (72, 145, 85, 255), (72, 145, 170, 255), (72, 145, 255, 255), (72, 182, 0, 255), (72, 182, 85, 255), (72, 182, 170, 255), (72, 182, 255, 255), (72, 218, 0, 255), (72, 218, 85, 255), (72, 218, 170, 255), (72, 218, 255, 255), (72, 255, 0, 255), (72, 255, 85, 255), (72, 255, 170, 255), (72, 255, 255, 255), (109, 0, 0, 255), (109, 0, 85, 255), (109, 0, 170, 255), (109, 0, 255, 255), (109, 36, 0, 255), (109, 36, 85, 255), (109, 36, 170, 255), (109, 36, 255, 255), (109, 72, 0, 255), (109, 72, 85, 255), (109, 72, 170, 255), (109, 72, 255, 255), (109, 109, 0, 255), (109, 109, 85, 255), (109, 109, 170, 255), (109, 109, 255, 255), (109, 145, 0, 255), (109, 145, 85, 255), (109, 145, 170, 255), (109, 145, 255, 255), (109, 182, 0, 255), (109, 182, 85, 255), (109, 182, 170, 255), (109, 182, 255, 255), (109, 218, 0, 255), (109, 218, 85, 255), (109, 218, 170, 255), (109, 218, 255, 255), (109, 255, 0, 255), (109, 255, 85, 255), (109, 255, 170, 255), (109, 255, 255, 255), (145, 0, 0, 255), (145, 0, 85, 255), (145, 0, 170, 255), (145, 0, 255, 255), (145, 36, 0, 255), (145, 36, 85, 255), (145, 36, 170, 255), (145, 36, 255, 255), (145, 72, 0, 255), (145, 72, 85, 255), (145, 72, 170, 255), (145, 72, 255, 255), (145, 109, 0, 255), (145, 109, 85, 255), (145, 109, 170, 255), (145, 109, 255, 255), (145, 145, 0, 255), (145, 145, 85, 255), (145, 145, 170, 255), (145, 145, 255, 255), (145, 182, 0, 255), (145, 182, 85, 255), (145, 182, 170, 255), (145, 182, 255, 255), (145, 218, 0, 255), (145, 218, 85, 255), (145, 218, 170, 255), (145, 218, 255, 255), (145, 255, 0, 255), (145, 255, 85, 255), (145, 255, 170, 255), (145, 255, 255, 255), (182, 0, 0, 255), (182, 0, 85, 255), (182, 0, 170, 255), (182, 0, 255, 255), (182, 36, 0, 255), (182, 36, 85, 255), (182, 36, 170, 255), (182, 36, 255, 255), (182, 72, 0, 255), (182, 72, 85, 255), (182, 72, 170, 255), (182, 72, 255, 255), (182, 109, 0, 255), (182, 109, 85, 255), (182, 109, 170, 255), (182, 109, 255, 255), (182, 145, 0, 255), (182, 145, 85, 255), (182, 145, 170, 255), (182, 145, 255, 255), (182, 182, 0, 255), (182, 182, 85, 255), (182, 182, 170, 255), (182, 182, 255, 255), (182, 218, 0, 255), (182, 218, 85, 255), (182, 218, 170, 255), (182, 218, 255, 255), (182, 255, 0, 255), (182, 255, 85, 255), (182, 255, 170, 255), (182, 255, 255, 255), (218, 0, 0, 255), (218, 0, 85, 255), (218, 0, 170, 255), (218, 0, 255, 255), (218, 36, 0, 255), (218, 36, 85, 255), (218, 36, 170, 255), (218, 36, 255, 255), (218, 72, 0, 255), (218, 72, 85, 255), (218, 72, 170, 255), (218, 72, 255, 255), (218, 109, 0, 255), (218, 109, 85, 255), (218, 109, 170, 255), (218, 109, 255, 255), (218, 145, 0, 255), (218, 145, 85, 255), (218, 145, 170, 255), (218, 145, 255, 255), (218, 182, 0, 255), (218, 182, 85, 255), (218, 182, 170, 255), (218, 182, 255, 255), (218, 218, 0, 255), (218, 218, 85, 255), (218, 218, 170, 255), (218, 218, 255, 255), (218, 255, 0, 255), (218, 255, 85, 255), (218, 255, 170, 255), (218, 255, 255, 255), (255, 0, 0, 255), (255, 0, 85, 255), (255, 0, 170, 255), (255, 0, 255, 255), (255, 36, 0, 255), (255, 36, 85, 255), (255, 36, 170, 255), (255, 36, 255, 255), (255, 72, 0, 255), (255, 72, 85, 255), (255, 72, 170, 255), (255, 72, 255, 255), (255, 109, 0, 255), (255, 109, 85, 255), (255, 109, 170, 255), (255, 109, 255, 255), (255, 145, 0, 255), (255, 145, 85, 255), (255, 145, 170, 255), (255, 145, 255, 255), (255, 182, 0, 255), (255, 182, 85, 255), (255, 182, 170, 255), (255, 182, 255, 255), (255, 218, 0, 255), (255, 218, 85, 255), (255, 218, 170, 255), (255, 218, 255, 255), (255, 255, 0, 255), (255, 255, 85, 255), (255, 255, 170, 255), (255, 255, 255, 255)]
    elif colors == "16 bits":
        colors = []

        for r in range(32):
            for g in range(64):
                for b in range(32):
                    red = (r * 255) // 31
                    green = (g * 255) // 63
                    blue = (b * 255) // 31
                    colors.append((red, green, blue, 255))

    image = Image.open(image_path)
    image = image.convert("RGBA")
    x, y = image.size

    too_small_image_error_message = f"Image trop petite pour y en faire un Pixel Art {str(by)}×{str(by)} ou > {str(by)}×{str(by)}.\n\nToo small image to make a Pixel Art = {str(by)}×{str(by)} or > {str(by)}×{str(by)}."

    if x <= by+1 or y <= by+1:
        raise ValueError(too_small_image_error_message)

    if x == y:
        new_x = by
        new_y = by
    elif x >= y:
        new_x = int(by * x / y)
        new_y = by
    else:
        new_x = by
        new_y = int(by * y / x)

    x_sections = x // new_x
    y_sections = y // new_y

    pixels = {}
    pixel_art = {}

    for X in range(1, new_x + 1):
        for Y in range(1, new_y + 1):
            pixels[(X, Y)] = []

    for X in range(1, new_x + 1):
        for Y in range(1, new_y + 1):
            try:
                pixels[(X, Y)].append(image.getpixel((x_sections * (X - 1), y_sections * (Y - 1))))
            except IndexError:
                pass

    for X in range(1, new_x + 1):
        for Y in range(1, new_y + 1):
            if pixels[(X, Y)]:
                pixel_art[(X, Y)] = min(colors, key=lambda c: math.sqrt(sum((Counter(pixels[(X, Y)]).most_common(1)[0][0][i] - c[i])**2 for i in range(4)))) if colors != None else Counter(pixels[(X, Y)]).most_common(1)[0][0]

    if save_image == True:
        pixel_art_image = Image.new("RGBA", (new_x, new_y), (0, 0, 0, 0))

        pixels_in_pixel_art = pixel_art_image.load()

        for X in range(0, new_x):
            for Y in range(0, new_y):
                try:
                    pixels_in_pixel_art[X, Y] = pixel_art[X+1, Y+1]
                except KeyError:
                    pass

        pixel_art_image.save(output)

    return pixel_art