import pygame, os

__g = {"labels":[]}

def load_image(path):
    """
    load_image(path) --> None

    Load an image located at the given path argument.
    """
    img = pygame.image.load(path)
    pygame.display.set_mode((1,1), pygame.NOFRAME)
    img = img.convert()
    pygame.display.set_caption(path)
    __g["img"] = img
    __g["width"] = img.get_width()
    __g["height"] = img.get_height()

def new_image(width, height):
    """
    new_image(width, height) --> None

    Creates a new image (all white) with the given width
    and height dimensions (in pixels).
    """
    if width <= 0 or height <= 0 or type(width)!= int or type(height)!= int:
        raise ValueError("Dimensions must be positive integers" % (x,y))
    temp = pygame.surface.Surface((width, height))
    pygame.display.set_mode((1,1), pygame.NOFRAME)
    pygame.display.set_caption("New Image")
    temp = temp.convert()
    temp.fill((255, 255, 255))    
    __g["img"] = temp
    __g["width"] = width
    __g["height"] = height

def save_image(file_name="temp.jpg"):
    """
    save_image(file_name) --> None

    Save the loaded image with the given file_name (optional).
    If the file_name is an absolute path, use it as is.
    If the file_name is not an absolute path, save the
    file in the current working directory.
    If the file_name is not given at all, save the file as temp.jpg
    in the current working directory.
    """
    if not os.path.isabs(file_name):
        file_name = os.path.join(os.getcwd(), file_name)
    for label in __g["labels"]:
        __g["img"].blit(label[0], (label[1], label[2]))
    pygame.image.save(__g["img"], file_name)
    #pygame.display.quit()

def get_red(x, y):
    """
    get_red(x, y) --> int

    Return the red component of the pixel at position (x, y) in the loaded image.
    """
    if x < 0 or x >= __g["width"] or y < 0 or y >= __g["height"]:
        raise ValueError("Coordinate (%i,%i) out of range" % (x,y))
    return __g["img"].get_at((x,y))[0]

def get_green(x, y):
    """
    get_green(x, y) --> int

    Return the green component of the pixel at position (x, y) in the loaded image.
    """
    if x < 0 or x >= __g["width"] or y < 0 or y >= __g["height"]:
        raise ValueError("Coordinate (%i,%i) out of range" % (x,y))
    return __g["img"].get_at((x,y))[1]

def get_blue(x, y):
    """
    get_blue(x, y) --> int

    Return the blue component of the pixel at position (x, y) in the loaded image.
    """
    if x < 0 or x >= __g["width"] or y < 0 or y >= __g["height"]:
        raise ValueError("Coordinate (%i,%i) out of range" % (x,y))
    return __g["img"].get_at((x,y))[2]

def set_red(x, y, value):
    """
    set_red(x, y, value) --> None

    Set the red component of the pixel at position (x, y) in the loaded image
    to the given integer value (between 0 and 255).
    """
    if x < 0 or x >= __g["width"] or y < 0 or y >= __g["height"]:
        raise ValueError("Coordinate (%i,%i) out of range" % (x,y))
    if value < 0 or value > 255:
        raise ValueError("R/G/B value (%i) out of range" % (value))
    __g["img"].set_at((x,y), (value, get_green(x, y), get_blue(x, y)))

def set_green(x, y, value):
    """
    set_green(x, y, value) --> None

    Set the green component of the pixel at position (x, y) in the loaded image
    to the given integer value (between 0 and 255).
    """
    if x < 0 or x >= __g["width"] or y < 0 or y >= __g["height"]:
        raise ValueError("Coordinate (%i,%i) out of range" % (x,y))
    if value < 0 or value > 255:
        raise ValueError("R/G/B value (%i) out of range" % (value))
    __g["img"].set_at((x,y), (get_red(x, y), value, get_blue(x, y)))

def set_blue(x, y, value):
    """
    set_blue(x, y, value) --> None

    Set the blue component of the pixel at position (x, y) in the loaded image
    to the given integer value (between 0 and 255).
    """
    if x < 0 or x >= __g["width"] or y < 0 or y >= __g["height"]:
        raise ValueError("Coordinate (%i,%i) out of range" % (x,y))
    if value < 0 or value > 255:
        raise ValueError("R/G/B value (%i) out of range" % (value))
    __g["img"].set_at((x,y), (get_red(x, y), get_green(x, y), value))

        
def get_width():
    """
    get_width() --> int

    Return the width of the loaded image (as number of pixels).
    """
    return __g["width"]

def get_height():
    """
    get_height() --> int

    Return the height of the loaded image (as number of pixels).
    """
    return __g["height"]

def get_pixel(x, y):
    """
    get_pixel(x, y) --> list

    Return a 3-part list of ints containing the [red, green, blue] values of
    the pixel at the given (x, y) coordinates in the loaded image.
    """
    if x < 0 or x >= __g["width"] or y < 0 or y >= __g["height"]:
        raise ValueError("Coordinate (%i,%i) out of range" % (x,y))
    return list(__g["img"].get_at((x,y)))[:3]

def set_pixel(x, y, colour):
    """
    set_pixel(x, y, colour) --> None
    
    Set the red, green, and blue values of the pixel at the given (x, y)
    coordinates to the corresponding values contained in the colour argument, 
    which is a 3-part list of ints: [red, green, blue]
    """
    if min(colour) < 0:
        raise ValueError("R/G/B value (%i) out of range" % (min(colour)))
    if max(colour) > 255:
        raise ValueError("R/G/B value (%i) out of range" % (max(colour)))
    if x < 0 or x >= __g["width"] or y < 0 or y >= __g["height"]:
        raise ValueError("Coordinate (%i,%i) out of range" % (x,y))
    
    __g["img"].set_at((x,y), colour)



def get_all_pixels():
    """
    get_all_pixels() --> list of lists of 3-element lists

    Return a list representing rows of pixels, where each row is itself
    a list of individual pixels, and each pixel is a 3-part list of ints
    containing the [red, green, blue] values.
    """
    p = []
    for row in range(int(__g["height"])):
        r = []
        for col in range(int(__g["width"])):
            r.append(get_pixel(col, row))
        p.append(r)
    return p

    
def add_text(text, x, y, colour, font_name, size, bold, italics, merged):
    """
    add_text(text, x, y, colour, font_name, size, bold, italics, merged) --> None

    Add a label with the specified text (a str).
    The top-left corner of the text will be at coordinates (x, y), and will
    be in the specified colour (a 3-part list of ints containing
    the [red, green, blue] values).
    The font_name should be one in the list returned from get_fonts(), but there
    is a built-in default font if font_name is not valid.
    The font size (an int), and bold/italics (both boolean arguments) can also
    be specified.
    If the text should be merged with the image, the boolean merged value
    should be True.  If False, the text will not be modified by any other
    pixel manipulation, and will be applied once the image is saved.
    """
    if min(colour) < 0:
        raise ValueError("R/G/B value (%i) out of range" % (min(colour)))
    if max(colour) > 255:
        raise ValueError("R/G/B value (%i) out of range" % (max(colour)))
    myFont = pygame.font.SysFont(font_name, size, bold, italics)
    label = myFont.render(text, True, colour)
    if merged:
        __g["labels"].append([label,x,y])
    else:
        __g["img"].blit(label, (x, y))
    
def get_fonts():
    """
    get_fonts() --> list

    Return a list of the names of the fonts (as strings) available
    on this system.  These font names may be used with add_text().
    """
    return pygame.font.get_fonts()

def show_image(audio_file=None):
    """
    show_image() --> None

    Display the loaded image in a window.  The calling code will pause until
    the image window is closed.  If an audio file argument (a str) is passed,
    that audio file will be played while the image is showing.
    """
    if audio_file != None:
        if type(audio_file) != str:
            raise ValueError("Argument must be a str")
        pygame.mixer.init()
        sample = pygame.mixer.Sound(audio_file)
        sample.play(-1)

    screen = pygame.display.set_mode((__g["width"], __g["height"]))
    keep_going = True
    while keep_going:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                keep_going = False
                if audio_file != None:
                    sample.stop()
        screen.blit(__g["img"], (0,0))
        pygame.display.flip()
    pygame.display.set_mode((1,1), pygame.NOFRAME)
pygame.init()
