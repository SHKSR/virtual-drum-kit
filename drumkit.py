def run_drumkit():
    import pygame
    pygame.init()
    pygame.mixer.set_num_channels(10)

    # Set up window
    WIDTH, HEIGHT = 1400, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Virtual Drum Kit")

    # Colors and font
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    FONT = pygame.font.SysFont("timesnewroman", 48, italic=True)
    FONT.set_underline(True)

    # Load background image
    background = pygame.transform.scale(
        pygame.image.load("C:/Users/ict20/OneDrive/Desktop/Drum/assets/Drumset.png"),
        (WIDTH, HEIGHT)
    )

    # Load sounds
    sounds = {
        'q': pygame.mixer.Sound('assets/notes/A16.wav'),  # Left Cymbal
        'w': pygame.mixer.Sound('assets/notes/A05.wav'),  # Snare
        'e': pygame.mixer.Sound('assets/notes/A08.wav'),  # Left Tom
        'r': pygame.mixer.Sound('assets/notes/A17.mp3'),  # Right Tom
        's': pygame.mixer.Sound('assets/notes/A18.wav'),  # Bass
        't': pygame.mixer.Sound('assets/notes/A06.wav'),  # Right Hi-Hat
        'n': pygame.mixer.Sound('assets/notes/A01.wav'),  # Right Cymbal
    }

    # Define pad positions (aligned to image)
    pad_positions = {
        'q': (50, 50),     # Left Cymbal
        'w': (200, 250),   # Snare
        'e': (350, 150),   # Left Tom
        'r': (500, 150),   # Right Tom
        's': (350, 320),   # Bass Drum
        't': (600, 280),   # Right Hi-Hat
        'n': (700, 80),    # Right Cymbal
    }

    pad_size = (100, 100)
    active_pads = {key: False for key in pad_positions}
    pad_flash_time = {key: 0 for key in pad_positions}

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.blit(background, (0, 0))

        # Draw quote with outline
        quote_text = "Feel the rhythm. Live the beat."
        quote_surface = FONT.render(quote_text, True, (255, 215, 0))
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            outline = FONT.render(quote_text, True, BLACK)
            screen.blit(outline, (WIDTH // 2 - outline.get_width() // 2 + dx, 30 + dy))
        screen.blit(quote_surface, (WIDTH // 2 - quote_surface.get_width() // 2, 30))

        current_time = pygame.time.get_ticks()

        # Draw active pad rectangles (flash effect)
        for key, (x, y) in pad_positions.items():
            if current_time - pad_flash_time[key] < 200:
                pygame.draw.rect(screen, RED, (x, y, *pad_size), 3)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                if key in sounds:
                    sounds[key].play()
                    active_pads[key] = True
                    pad_flash_time[key] = pygame.time.get_ticks()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                for key, (x, y) in pad_positions.items():
                    rect = pygame.Rect(x, y, *pad_size)
                    if rect.collidepoint(pos):
                        sounds[key].play()
                        active_pads[key] = True
                        pad_flash_time[key] = pygame.time.get_ticks()

            elif event.type == pygame.MOUSEBUTTONUP:
                for key in active_pads:
                    active_pads[key] = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

