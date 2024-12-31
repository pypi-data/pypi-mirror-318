"""
Fait un Pixel Art.

Arguments : 
    image_path : Chemin de l'image à convertir en Pixel Art.
    output_path_and_image_name : Répertoire de sortie de l'image avec le nom de l'image.
    save_image : True si tu veux enregistrer l'image, False si tu ne veux pas l'enregistrer. Tu peux te servir de cette fonction avec cet argument sur False si tu veux simplement mettre les pixels avec leur couleur dans une variable.
    colors : Fait le Pixel Art avec les couleurs de votre choix. Tu peux aussi choisir le nombre de couleurs, voici les choix : 2_COLORS, 16_VGA_COLORS et 256_VGA_COLORS.
    n : Uniquement dans la fonction ByNumberKeepProportions(*args) car dans cette fonction, du décides le Pixel Art est par combien en conservant les proportions.
    
Versions :
    1 : Convertit une image en Pixel Art.
     

        
Make a Pixel Art.

Arguments:
    image_path: Path of the image to convert to Pixel Art.
    output_path_and_image_name: Output directory of the image with the name of the image.
    save_image: True if you want to save the image, False if you don't want to save it. You can use this function with this argument set to False if you just want to put the pixels with their color into a variable.
    colors: Make the Pixel Art with the colors of your choice. You also can choose the number of colors, here is the choices : 2_COLORS, 16_VGA_COLORS and 256.
    n: Only in the ByNumberKeepProportions(*args) function because in this function, you decide the Pixel Art is by how much .

Versions:
    1: Convert an image to Pixel Art.
"""

from . import PixelArt
from PIL import Image
from collections import Counter
import math

__version__ = "0.1.0"

def PixelArt(image_path: str, n: int, output_path_and_image_name: str = "./PixelArt.png", save_image: bool = True, colors = None):
    if save_image != True or False:
        save_image = True

    if colors == "2_COLORS":
        colors = [(255, 255, 255, 255), (0, 0, 0, 255)]
    elif colors == "16_VGA_COLORS":
        colors = [(0, 0, 0, 255), (0, 0, 170, 255), (0, 170, 0, 255), (0, 170, 170, 255), (170, 0, 0, 255), (170, 0, 170, 255), (170, 85, 0, 255), (170, 170, 170, 255), (85, 85, 85, 255), (85, 85, 255, 255), (85, 255, 85, 255), (85, 255, 255, 255), (255, 85, 85, 255), (255, 85, 255, 255), (255, 255, 85, 255), (255, 255, 255, 255)]
    elif colors == "256_VGA_COLORS":
        colors = []
        base_colors = [(0, 0, 0, 255), (0, 0, 170, 255), (0, 170, 0, 255), (0, 170, 170, 255), (170, 0, 0, 255), (170, 0, 170, 255), (170, 85, 0, 255), (170, 170, 170, 255), (85, 85, 85, 255), (85, 85, 255, 255), (85, 255, 85, 255), (85, 255, 255, 255), (255, 85, 85, 255), (255, 85, 255, 255), (255, 255, 85, 255), (255, 255, 255, 255)]
        for color in base_colors:
            r, g, b, a = color
            for i in range(16):
                colors.append((
                    min(255, int(r * i / 15)),
                    min(255, int(g * i / 15)),
                    min(255, int(b * i / 15)),
                    255
                ))

    image = Image.open(image_path)
    image = image.convert("RGBA")
    x, y = image.size

    too_small_image_error_message = f"Image trop petite pour y en faire un Pixel Art {str(n)}×{str(n)} ou > {str(n)}×{str(n)}.\n\nToo small image to make a Pixel Art = {str(n)}×{str(n)} or > {str(n)}×{str(n)}."

    if x <= n+1 or y <= n+1:
        raise ValueError(too_small_image_error_message)

    if x == y:
        new_x = n
        new_y = n
    elif x >= y:
        new_x = int(n * x / y)
        new_y = n
    else:
        new_x = n
        new_y = int(n * y / x)

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
                pixel_art[(X, Y)] = min(colors, key=lambda color: math.sqrt(sum((Counter(pixels[(X, Y)]).most_common(1)[0][0][i] - color[i]) ** 2 for i in range(4)))) if colors != None else Counter(pixels[(X, Y)]).most_common(1)[0][0]

    if save_image == True:
        pixel_art_image = Image.new("RGBA", (new_x, new_y), (0, 0, 0, 0))

        pixels_in_pixel_art = pixel_art_image.load()

        for X in range(0, new_x):
            for Y in range(0, new_y):
                try:
                    pixels_in_pixel_art[X, Y] = pixel_art[X+1, Y+1]
                except KeyError:
                    pass

        pixel_art_image.save(output_path_and_image_name)

    return pixel_art