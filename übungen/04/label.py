from PIL import Image, ImageDraw
import numpy as np
import random

# Funktion zur Generierung zufälliger Farben
def random_color():
    return tuple(random.randint(0, 255) for _ in range(3))

# Hauptfunktion: Labeling
def label_objects_pillow(image_path, output_path):
    # Lade das Bild
    image = Image.open(image_path).convert("L")  # In Graustufen konvertieren
    binary = image.point(lambda p: p > 128 and 255)  # Binarisierung (Schwellenwert = 128)
    
    # Konvertiere das Bild zu einem NumPy-Array
    binary_array = np.array(binary)
    labels = np.zeros_like(binary_array, dtype=int)  # Label-Array
    height, width = binary_array.shape
    current_label = 1
    label_colors = {}

    # Flood-Fill-ähnlicher Ansatz zur Labelvergabe
    def flood_fill(x, y, label):
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            if 0 <= cx < width and 0 <= cy < height and binary_array[cy, cx] == 255 and labels[cy, cx] == 0:
                labels[cy, cx] = label
                stack.extend([(cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1)])

    # Objekte finden und labeln
    for y in range(height):
        for x in range(width):
            if binary_array[y, x] == 255 and labels[y, x] == 0:
                flood_fill(x, y, current_label)
                label_colors[current_label] = random_color()
                current_label += 1

    # Generiere ein Ausgabebild mit Farben für jedes Label
    output_image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(output_image)

    for y in range(height):
        for x in range(width):
            if labels[y, x] > 0:
                draw.point((x, y), label_colors[labels[y, x]])

    # Speichere das Ergebnis
    output_image.save(output_path)
    output_image.show()

# Teste das Skript
image_path = "images/mono.png"  # Eingabebild
output_path = "images/mono_labeled.png"  # Ausgabebild
label_objects_pillow(image_path, output_path)


