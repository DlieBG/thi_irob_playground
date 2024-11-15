from PIL import Image, ImageFilter

def smooth(image_path, output_path, radius=7):
    """
    Weichzeichnet ein Bild mit einem Boxfilter mit dem angegebenen Radius.
    
    :param image_path: Pfad zum Eingabebild.
    :param output_path: Pfad zum Ausgabebild.
    :param radius: Radius des Boxfilters (Standard ist 7).
    """
    # Bild laden
    image = Image.open(image_path)
    
    # Boxfilter mit Radius anwenden
    smoothed_image = image.filter(ImageFilter.BoxBlur(radius))
    
    # Weichgezeichnetes Bild speichern
    smoothed_image.save(output_path)
    print(f"Weichgezeichnetes Bild wurde gespeichert: {output_path}")

smooth("images/background.jpg", "images/background_smooth.jpg")
