from PIL import Image, ImageOps

def invert_png(input_path: str, output_path: str):
    img = Image.open(input_path).convert('RGB')

    inverted_img = ImageOps.invert(img)

    inverted_img.save(output_path)
