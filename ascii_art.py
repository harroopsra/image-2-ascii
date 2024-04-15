import argparse
import os

def ascii_art(image_path, output_file=None):
    characters = [' ', '.', '*', ':', 'o', '&', '8', '#', '@']
    try:
        from PIL import Image
    except ImportError:
        raise Exception("The Python Imaging Library is required to run this code.")
        
    try:
        image = Image.open(image_path)
    except:
        raise Exception("Unable to open the specified image file.")
        
    image = image.resize((80, 80), Image.LANCZOS)
    gray_image = image.convert("L")
    pixels = gray_image.load()

    output = ''
    for i in range(80):
        for j in range(80):
            intensity = pixels[j, i]
            index = intensity // 32
            output += characters[index] + ' '
        output += '\n'
    
    if output_file:
        with open(output_file, 'w') as f:
            f.write(output)
        print(f"ASCII art written to {output_file}")
    else:
        print(output)
        with open("ascii_image_draw.txt", "w") as f:
            f.write(output)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate ASCII art from an image.')
    parser.add_argument('image_path', help='Path to the input image file.')
    parser.add_argument('-o', '--output', help='Path to the output ASCII art file.')
    args = parser.parse_args()
    
    ascii_art(args.image_path, args.output)
