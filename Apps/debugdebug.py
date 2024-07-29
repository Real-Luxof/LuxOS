import pygame
import pygame.draw_py

pixels = [
    [
        (255, 255, 255), (255, 255, 255), (255, 255, 255)
    ],
    [
        (255, 255, 255), (255, 255, 255), (0, 0, 0)
    ],
    [
        (255, 255, 255), (255, 255, 255), (255, 255, 255)
    ]
]

pygame.init()
screen = pygame.display.set_mode((600, 600))

pygame.PixelArray

pixels_surface = pygame.Surface((3, 3))
pixels_surface = pygame.pixelcopy.surface_to_array(pixels, pixels_surface)
