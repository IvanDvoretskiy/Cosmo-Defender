import pygame as pg

pg.init()

COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 30)

speed, size, coordinates, speed_b = "","","", ""

translator = {
    "Координати появи": coordinates, 
    "Швидкість метеориту": speed, 
    "Розмір метеориту": size,
    "Швидкість кулі": speed_b
}

class InputBox:
    def __init__(self, x, y, w, h, text='', max_length=None, placeholder=''):
        self.initial_window_width = pg.display.get_surface().get_width()
        self.initial_window_height = pg.display.get_surface().get_height()
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.max_length = max_length
        self.placeholder = placeholder

    def handle_event(self, event):
        global speed, size, coordinates, translator

        #Перевіряємо чи користувач нажав на поле
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE

        #Записуємо введені данні користувача
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_BACKSPACE:
                    if translator[self.placeholder] != "":
                        translator[self.placeholder] = translator[self.placeholder][:-1]
                    else:
                        translator[self.placeholder] = ""
                    self.text = translator[self.placeholder]
                else:
                    self.text += event.unicode 
                    translator[self.placeholder] += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)
        return translator[self.placeholder], self.placeholder

    def draw(self, screen):
        if not self.text:
            placeholder_surface = FONT.render(self.placeholder, True, self.color)
            screen.blit(placeholder_surface, (self.rect.x + 5, self.rect.y + 5))
        else:
            screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pg.draw.rect(screen, self.color, self.rect, 2)

