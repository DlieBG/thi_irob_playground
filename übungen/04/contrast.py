from PIL import Image

def create_contrast_curve(factor):
    """
    Erstellt eine Lookup-Tabelle, um den Kontrast zu erhöhen.
    
    :param factor: Kontrastfaktor (> 1 erhöht den Kontrast, < 1 verringert ihn).
    :return: Eine Liste mit 256 Werten für die Lookup-Tabelle.
    """
    midpoint = 128  # Der mittlere Grauwert
    lut = [
        max(0, min(255, int(midpoint + (i - midpoint) * factor))) for i in range(256)
    ]
    return lut

def contrast(image_path, output_path, factor=1.5):
    """
    Erhöht den Kontrast eines Bildes mit einer Lookup-Tabelle.
    
    :param image_path: Pfad zum Eingabebild.
    :param output_path: Pfad zum Ausgabebild.
    :param factor: Kontrastfaktor (Standard: 1.5).
    """
    # Bild laden
    image = Image.open(image_path)
    
    # Sicherstellen, dass das Bild im "L" (Graustufen) oder "RGB"-Modus ist
    if image.mode not in ["L", "RGB"]:
        image = image.convert("RGB")
    
    # Lookup-Tabelle für Kontrast erstellen
    lut = create_contrast_curve(factor)
    
    # Kontrast über die Lookup-Tabelle anwenden
    if image.mode == "RGB":
        # LUT für RGB-Modus erweitern
        lut = lut * 3
    
    enhanced_image = image.point(lut)
    
    # Bild speichern
    enhanced_image.save(output_path)
    print(f"Kontrastiertes Bild wurde gespeichert: {output_path}")

contrast("images/background.jpg", "images/background_contrast.jpg")
