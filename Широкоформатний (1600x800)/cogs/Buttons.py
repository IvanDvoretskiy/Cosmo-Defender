import pygame

# Клас кнопки
class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
    def draw(self, screen):
        pygame.draw.rect(screen, (0, 128, 255), self.rect)
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = self.rect.center
        screen.blit(text_surface, text_rect)

    def is_clicked(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_x, mouse_y):
            return pygame.mouse.get_pressed()[0]
        return False


button1 = Button(1270, 670, 300, 100, "Заспавнити метеорит")