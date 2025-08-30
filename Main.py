import pygame

pygame.init()
pygame.mixer.set_num_channels(10)

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Digital Drum Kit")

GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)

background = pygame.transform.scale(
    pygame.image.load("C:/Users/user/Desktop/Drum/Drum/assets/Drumset.png"),
    (WIDTH, HEIGHT)
)


sounds = {
    'q': pygame.mixer.Sound('assets/notes/A16.wav'),  # Hi-hat
    'w': pygame.mixer.Sound('assets/notes/A05.wav'),  # Snare
    'e': pygame.mixer.Sound('assets/notes/A08.wav'),  # Tom
    'r': pygame.mixer.Sound('assets/notes/A17.wav'),  # Crash
    's': pygame.mixer.Sound('assets/notes/A18.wav'),  # Kick
    't': pygame.mixer.Sound('assets/notes/A06.wav'),  # Floor tom
    'n': pygame.mixer.Sound('assets/notes/A01.wav'),  # Ride
}

pad_positions = {
    'q': (50, 50),   # Hi-hat
    'w': (200, 250),   # Snare
    'e': (350, 150),   # Tom
    'r': (500, 150),   # Crash
    's': (350, 350),   # Kick
    't': (600, 280),   # Floor tom
    'n': (700, 80),  # Ride
}


active_pads = {key: False for key in pad_positions.keys()}

clock = pygame.time.Clock()
running = True

while running:
    screen.blit(background, (0, 0))  

   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            key = event.unicode.lower()
            if key in sounds:
                sounds[key].play()
                active_pads[key] = True

        if event.type == pygame.KEYUP:
            key = event.unicode.lower()
            if key in active_pads:
                active_pads[key] = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            for key, (x, y) in pad_positions.items():
                rect = pygame.Rect(x, y, 100, 100)
                if rect.collidepoint(pos):
                    sounds[key].play()
                    active_pads[key] = True

        if event.type == pygame.MOUSEBUTTONUP:
            for key in active_pads.keys():
                active_pads[key] = False

    
            for key, (x, y) in pad_positions.items():
             if active_pads[key]:
                 pygame.draw.rect(screen, GRAY, (x, y, 100, 100), 3)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


