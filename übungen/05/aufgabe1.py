import sdl2
import sdl2.ext
import time

# Konstanten
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
RECT_WIDTH = 50
RECT_HEIGHT = 30
RECT_SPEED = 5  # Pixel pro Schritt
FRAME_TIME_MS = 10  # 10 ms pro Frame

# Funktion zum Zeichnen eines Rechtecks
def paint_rect(renderer, x, y, color):
    renderer.draw_rect([x, y, RECT_WIDTH, RECT_HEIGHT], color)

def main():
    # Initialisierung von SDL2
    sdl2.ext.init()
    window = sdl2.ext.Window("Spielanwendung", size=(WINDOW_WIDTH, WINDOW_HEIGHT))
    window.show()

    renderer = sdl2.ext.Renderer(window)
    running = True

    rect_x = 0
    rect_y = (WINDOW_HEIGHT - RECT_HEIGHT) // 2  # Zentriert vertikal
    rect_color = sdl2.ext.Color(255, 0, 0)  # Rot

    # Hauptschleife
    while running:
        start_time = time.time()
        
        # Ereignisbehandlung
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False

        # Bildschirm löschen
        renderer.clear(sdl2.ext.Color(0, 0, 0))  # Schwarz

        # Rechteck zeichnen
        paint_rect(renderer, rect_x, rect_y, rect_color)

        # Rechteckbewegung
        rect_x += RECT_SPEED
        if rect_x > WINDOW_WIDTH:  # Zurücksetzen, wenn aus dem Fenster
            rect_x = -RECT_WIDTH

        # Renderer aktualisieren
        renderer.present()

        # Zeitsteuerung
        elapsed_time = time.time() - start_time
        sleep_time = FRAME_TIME_MS / 1000.0 - elapsed_time
        if sleep_time > 0:
            time.sleep(sleep_time)

    # Aufräumen
    sdl2.ext.quit()

if __name__ == "__main__":
    main()
