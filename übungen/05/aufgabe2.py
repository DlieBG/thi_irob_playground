import sdl2
import sdl2.ext
import time

# Konstanten
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
MOON_WIDTH = 800
MOON_HEIGHT = 200
EARTH_WIDTH = 800
EARTH_HEIGHT = 200
FRAME_TIME_MS = 10  # 10 ms pro Frame

# Funktion zum Zeichnen eines Rechtecks
def paint_rect(renderer, x, y, width, height, color):
    renderer.fill([x, y, width, height], color)

def main():
    # Initialisierung von SDL2
    sdl2.ext.init()
    window = sdl2.ext.Window("Rakte zum Mond", size=(WINDOW_WIDTH, WINDOW_HEIGHT))
    window.show()

    renderer = sdl2.ext.Renderer(window)
    running = True

    moon_x = 0
    moon_y = 0
    moon_color = sdl2.ext.Color(192, 192, 192)
    
    earth_x = 0
    earth_y = (WINDOW_HEIGHT - EARTH_HEIGHT)
    earth_color = sdl2.ext.Color(165, 42, 42)

    x: float = 0 # Position der Rakete über Erde
    v: float = 0 # Geschwindigkeit der Rakete
    a: float = 5 # Beschleunigung der Rakete (fest)
    end_speed_time: float = 2  # Zeitpunkt, ab dem die Rakete die Endgeschwindigkeit erreicht
    brake_point: float = 20  # Zeitpunkt, ab dem die Rakete bremst
    stop_time: float = 22  # Zeitpunkt, ab dem die Rakete stoppt
    t_total: float = 0  # Gesamtzeit

    rocket_x = 400
    rocket_color = sdl2.ext.Color(0, 0, 255)  # Blau

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

        # Mond zeichnen
        paint_rect(renderer, moon_x, moon_y, MOON_WIDTH, MOON_HEIGHT, moon_color)
        
        # Erde zeichnen
        paint_rect(renderer, earth_x, earth_y, EARTH_WIDTH, EARTH_HEIGHT, earth_color)

        # Rakete zeichnen
        paint_rect(renderer, rocket_x, earth_y - x, 10, 20, rocket_color)

        # Renderer aktualisieren
        renderer.present()

        # Höhe und Geschwindigkeit aktualisieren
        if t_total >= end_speed_time and t_total < brake_point:
            a = 0
        elif t_total >= brake_point and t_total < stop_time:
            a = -5
        elif t_total >= stop_time:
            a = 0

        v += a * (FRAME_TIME_MS / 1000.0)
        x += v * (FRAME_TIME_MS / 1000.0)

        print("t: {:.2f}, x: {:.2f}, v: {:.2f}, a: {:.2f}".format(t_total, x, v, a))

        # Zeitsteuerung
        elapsed_time = time.time() - start_time
        sleep_time = FRAME_TIME_MS / 1000.0 - elapsed_time
        if sleep_time > 0:
            time.sleep(sleep_time)

        t_total += FRAME_TIME_MS / 1000.0

    # Aufräumen
    sdl2.ext.quit()

if __name__ == "__main__":
    main()
