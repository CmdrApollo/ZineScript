import pygame
import random
import math
import sys

def distance(x1, y1, x2, y2):
    return math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

RDPI = 295
DPI = 300
PAPER_WIDTH = 11.0 * RDPI
PAPER_HEIGHT = 8.5 * RDPI

pygame.display.set_mode((1, 1))
pygame.init()

from typing import Any
from lupa import LuaRuntime
from PIL import Image, ImageFilter, ImageOps

def pil_to_pygame(image: Image.Image):
    mode = image.mode
    size = image.size
    data = image.tobytes()
    return pygame.image.frombytes(data, size, mode)

class Surface:
    def __init__(self, x, y, w=None, h=None):
        self.x = x
        self.y = y
        self.w = w if w is not None else 1
        self.h = h if h is not None else 1

        self.surface = pygame.Surface((self.w, self.h), pygame.SRCALPHA)

class ColoredSurface(Surface):
    def __init__(self, x, y, w=None, h=None, color=None, centered=None):
        self.x = x
        self.y = y
        self.w = w if w is not None else 1
        self.h = h if h is not None else 1
        self.color = color if color is not None else 'white'
        self.centered = centered if centered is not None else False

        self.surface = pygame.Surface((self.w, self.h))
        self.surface.fill(self.color)

        if self.centered:
            self.x -= self.surface.get_width() // 2
            self.y -= self.surface.get_height() // 2

class TextSurface(Surface):
    def __init__(self, text, x, y, font, size, color, background_color, antialias, centered, wrap_width, bold, italic):
        self.x = x
        self.y = y

        self.text = text
        self.font = font
        self.size = size
        self.color = color
        self.background_color = background_color
        self.antialias = antialias
        self.centered = centered
        self.wrap_width = wrap_width * RDPI
        self.bold = bold
        self.italic = italic

        self.font_obj = pygame.font.SysFont(font, size, bold=bold, italic=italic)

        self.surface = self.font_obj.render(self.text, self.antialias, self.color, self.background_color, self.wrap_width)

        if self.centered:
            self.x -= self.surface.get_width() // 2
            self.y -= self.surface.get_height() // 2

class ImageSurface(Surface):
    def __init__(self, path, x, y, centered):
        self.x = x
        self.y = y
        self.centered = centered
        
        self.surface = pygame.image.load(path).convert_alpha()

        if self.centered:
            self.x -= self.surface.get_width() // 2
            self.y -= self.surface.get_height() // 2

class Zine:
    def __init__(self):
        self.title_text = None
        self.author_name = None
        self.final_surface = None

        self.pages = {}
        self.active_page = -1

    def pageWidth(self):
        return (PAPER_WIDTH // 4) / RDPI
    
    def pageHeight(self):
        return (PAPER_HEIGHT // 2) / RDPI

    def newSurface(self, options: dict[str, Any]):
        x = options['x'] * RDPI if 'x' in options else 0
        y = options['y'] * RDPI if 'y' in options else 0
        w = options['width'] * RDPI if 'width' in options else 0
        h = options['height'] * RDPI if 'height' in options else 0

        return Surface(x, y, w, h)
    
    def random(self):
        return random.random()

    def randomColor(self):
        r = hex(random.randint(0, 255)).removeprefix('0x').rjust(2, '0')
        g = hex(random.randint(0, 255)).removeprefix('0x').rjust(2, '0')
        b = hex(random.randint(0, 255)).removeprefix('0x').rjust(2, '0')

        return f"#{r}{g}{b}"

    def tableToColor(self, table):
        r, g, b = table.values()
        
        r = hex(int(r)).removeprefix('0x').rjust(2, '0')
        g = hex(int(g)).removeprefix('0x').rjust(2, '0')
        b = hex(int(b)).removeprefix('0x').rjust(2, '0')

        return f"#{r}{g}{b}"

    def title(self, t):
        self.title_text = t

    def author(self, a):
        self.author_name = a

    def startpage(self, pagenum):
        self.pages[pagenum] = []
        self.active_page = pagenum

    def background(self, color=None):
        self.pages[self.active_page].append(ColoredSurface(0, 0, PAPER_WIDTH // 4, PAPER_HEIGHT // 2, color))

    def fill(self, options: dict[str, Any]):
        surface = options['surface'] if 'surface' in options else None
        color = options['color'] if 'color' in options else 'black'
        
        surface.surface.fill(color)
        
        return surface

    def noise(self, options: dict[str, Any]):
        surface = options['surface'] if 'surface' in options else None
        color = options['color'] if 'color' in options else 'black'
        region = list(options['region'].values()) if 'region' in options else [0, 0, 1, 1]
        coverage = options['coverage'] if 'coverage' in options else 0.5

        x, y, w, h = region

        for i in range(int(x * RDPI), int((x + w) * RDPI), 5):
            for j in range(int(y * RDPI), int((y + h) * RDPI), 5):
                if random.random() < coverage:
                    pygame.draw.rect(surface.surface, color, (i, j, 5, 5))
        
        return surface

    def spraypaint(self, options: dict[str, Any]):
        surface = options['surface'] if 'surface' in options else None
        color = options['color'] if 'color' in options else 'black'
        region = list(options['region'].values()) if 'region' in options else [0, 0, 1, 1]
        coverage = options['coverage'] if 'coverage' in options else 1.0
        inverted = options['inverted'] if 'inverted' in options else False
        pixelSize = options['pixelSize'] if 'pixelSize' in options else 5

        x, y, w, h = region

        for i in range(int(x * RDPI), int((x + w) * RDPI), pixelSize):
            for j in range(int(y * RDPI), int((y + h) * RDPI), pixelSize):
                dist = distance(i / RDPI, j / RDPI, x + w / 2, y + h / 2) / (min(w, h) / 2)
                if dist > 1 or dist < 0:
                    continue
                if not inverted:
                    dist = 1 - dist
                if random.random() < dist * coverage:
                    pygame.draw.rect(surface.surface, color, (i, j, pixelSize, pixelSize))
        
        return surface

    def text(self, options: dict[str, Any]):
        text = options['text'] if 'text' in options else ''
        x = options['x'] * RDPI if 'x' in options else 0
        y = options['y'] * RDPI if 'y' in options else 0

        text_options = options['textOptions'] if 'textOptions' in options else {}

        font = text_options['font'] if 'font' in text_options else 'arial'
        size = text_options['size'] if 'size' in text_options else 12
        color = text_options['color'] if 'color' in text_options else 'black'
        background_color = text_options['backgroundColor'] if 'backgroundColor' in text_options else None
        antialias = text_options['antialias'] if 'antialias' in text_options else True
        centered = text_options['centered'] if 'centered' in text_options else False
        wrap_width = text_options['wrapWidth'] if 'wrapWidth' in text_options else 0
        bold = text_options['bold'] if 'bold' in text_options else False
        italic = text_options['italic'] if 'italic' in text_options else False

        return TextSurface(text, x, y, font, size, color, background_color, antialias, centered, wrap_width, bold, italic)

    def image(self, options: dict[str, Any]):
        path = options['path'] if 'path' in options else ''
        x = options['x'] * RDPI if 'x' in options else 0
        y = options['y'] * RDPI if 'y' in options else 0
        centered = options['centered'] if 'centered' in options else False

        # You'd append this to current page in real use
        return ImageSurface(path, x, y, centered)

    def rotate(self, options: dict[str, Any]):
        surface = options['surface'] if 'surface' in options else None
        angle = options['angle'] if 'angle' in options else 0
        w, h = surface.surface.get_size()
        surface.surface = pygame.transform.rotate(surface.surface, angle)
        nw, nh = surface.surface.get_size()
        if surface.centered:
            surface.x += w // 2
            surface.x -= nw // 2
            surface.y += h // 2
            surface.y -= nh // 2
        return surface

    def scale(self, options: dict[str, Any]):
        surface = options['surface'] if 'surface' in options else None
        scale = options['scale'] if 'scale' in options else 0
        w, h = surface.surface.get_size()
        nw = w * scale
        nh = h * scale
        surface.surface = pygame.transform.scale(surface.surface, (nw, nh))
        if surface.centered:
            surface.x += w // 2
            surface.x -= nw // 2
            surface.y += h // 2
            surface.y -= nh // 2
        return surface

    def invert(self, surface: Surface):
        mode = "RGB"
        data = pygame.image.tobytes(surface.surface, mode)
        img = Image.frombytes(mode, surface.surface.get_size(), data)
        img = ImageOps.invert(img)

        surface.surface = pil_to_pygame(img)
        
        return surface

    def blur(self, surface: Surface):
        mode = "RGBA" if surface.surface.get_bitsize() == 32 else "RGB"
        data = pygame.image.tobytes(surface.surface, mode)
        img = Image.frombytes(mode, surface.surface.get_size(), data)
        img = img.filter(ImageFilter.GaussianBlur)

        surface.surface = pil_to_pygame(img)
        
        return surface

    def wavy(self, options: dict[str, Any]):
        surface = options['surface'] if 'surface' in options else None
        frequency = options['frequency'] if 'frequency' in options else 10
        amplitude = options['amplitude'] if 'amplitude' in options else 0.1
        w, h = surface.surface.get_size()

        surf = surface.surface.copy()

        surface.surface = pygame.Surface((int(surf.get_width() + amplitude * 2 * RDPI), surf.get_height()), pygame.SRCALPHA)

        for y in range(surface.surface.get_height()):
            surface.surface.blit(surf.subsurface((0, y, w, 1)), (amplitude * RDPI + math.sin((y / RDPI) * frequency) * amplitude * RDPI, y))
        
        nw, nh = surface.surface.get_size()
        if surface.centered:
            surface.x += w // 2
            surface.x -= nw // 2
            surface.y += h // 2
            surface.y -= nh // 2
        return surface

    def add(self, surface: Surface):
        self.pages[self.active_page].append(surface)

    def endpage(self):
        self.active_page = -1
    
    def render(self):
        paper_surface = pygame.Surface(((PAPER_WIDTH / RDPI) * DPI, (PAPER_HEIGHT / RDPI) * DPI), pygame.SRCALPHA)
        paper_surface.fill('white')

        gap_width = paper_surface.get_width() - PAPER_WIDTH
        gap_height = paper_surface.get_height() - PAPER_HEIGHT

        for page in self.pages:
            page_surf = pygame.Surface((PAPER_WIDTH // 4, PAPER_HEIGHT // 2))
            page_surf.fill('white')

            for surface in self.pages[page]:
                page_surf.blit(surface.surface, (surface.x, surface.y))
        
            x, y = {
                1: (0, 0),
                2: (0, 1),
                3: (1, 1),
                4: (2, 1),
                5: (3, 1),
                6: (3, 0),
                7: (2, 0),
                8: (1, 0),
            }[page]

            if y == 0:
                page_surf = pygame.transform.rotate(page_surf, 180)
            
            pygame.draw.rect(page_surf, 'black', (0, 0, *page_surf.get_size()), 1)
            paper_surface.blit(page_surf, (x * (PAPER_WIDTH // 4 + gap_width // 5) + gap_width // 5, y * (PAPER_HEIGHT // 2 + gap_height // 3) + gap_height // 3))

        self.final_surface = paper_surface

    def save(self, filename: str):
        pygame.image.save(self.final_surface, filename)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: ZineScript <filename>")
        sys.exit()

    filename = sys.argv[1]

    zine = Zine()

    lua = LuaRuntime(unpack_returned_tuples=True)
    lua.globals().zine = zine

    lua_code = open(filename, 'r').read()

    lua.execute(lua_code)