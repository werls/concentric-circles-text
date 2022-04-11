# Concentric Circles Text
# Werllen Castro, 2022
# github.com/werls/concentric-circles-text
# 
# Originally made for Grão — Território Percussivo
# 
# Full design process on Behance:
# https://www.behance.net/gallery/130839663/Grao-Territorio-Percussivo

# For the measures, i'm considering the milimeters

from drawBot import *

SCALE_MM_TO_PX = 3.7795275591

def draw_cd():
    cd_diameter = 329 * SCALE_MM_TO_PX
    cd_center_diameter = 103 * SCALE_MM_TO_PX
    cd_hole_diameter = 75 * SCALE_MM_TO_PX

    with savedState():
        strokeWidth(.5)
        stroke(1, 0, 0)
        oval(0, 0, cd_diameter,cd_diameter)
        oval(width / 2 - cd_center_diameter / 2, height / 2 - cd_center_diameter / 2, cd_center_diameter, cd_center_diameter)
        oval(width / 2 - cd_hole_diameter / 2, height / 2 - cd_hole_diameter / 2, cd_hole_diameter, cd_hole_diameter)

def setup():
    size(width, height)
    fill()
    if show_cd:
        draw_cd()
    translate(width / 2, height / 2)
    
    # A font with the same width glyphs
    # produces a better result. For the original
    # project, the font was Botanika Mono
    # (Tomáš Brousil / Suitcase Type Foundry)
    font('Courier', int(FONT_SIZE))
    rotate(pi / 2)

def draw(_text_list):
    _steps = int(STEPS)
    
    def debug_circles(RADIUS_START):
        strokeWidth(.5)
        stroke(0)
        oval(- RADIUS_START, - RADIUS_START, RADIUS_START * 2, RADIUS_START * 2)
        stroke()

    def debug_dots(x, y):
        with savedState():
            # fill()
            stroke()
            fill(0)
            oval(x - FONT_SIZE / 2, y - FONT_SIZE / 2, FONT_SIZE, FONT_SIZE)
            
    def debug_lines(x, y):
        with savedState():
            fill()
            stroke(255, 0, 0)
            line((0, 0), (x, y))
            
    def write_musics():
        with savedState():
            translate(x,y)
            rotate(degrees(a) - 90)
            fill(0)
            text(_text_list[m][i],(-2, -3))
    
    a = 0
    inc = 0
    sobra_steps = _steps
    angle_inc = (pi * 2) / _steps
    _r = RADIUS_START
    lineHeight = int(FONT_SIZE) * 1.5

    for m in range(len(_text_list)):
        sobra_steps -= len(_text_list[m])

        for i in range(_steps):
            x = cos(a) * _r
            y = sin(a) * _r
            
            if debug:
                debug_circles(_r)

            if i < len(_text_list[m]):
                if debug:
                    if _text_list[m][i] != ' ':
                        debug_dots(x, y)
                        # debug_lines(x,y)
                else:
                    write_musics()
                
            a -= angle_inc
        
        if is_sequential:        
            if m < len(_text_list) - 1:
                if sobra_steps <= len(_text_list[m + 1]):
                    sobra_steps = _steps
                    _r += lineHeight
                else:
                    sobra_steps -= len(_text_list[m + 1])
        else:
            _r += lineHeight
    
        a -= angle_inc * (len(_text_list[m]) + 1)    
        inc += .1
        # _r += lineHeight
        # _steps *= 2

ALBUM_SONGS = [
           'GRÃO∙LÉO DE PAULA',
           '01∙SERPENTE',
           '02∙VENTANIA SOLO',
           '03∙À BEIRA',
           '04∙AGÔ',
           '05∙GRÃO',
           '06∙CORTEJO',
           '07∙IPUAN',
           '08∙XIRÊ',
           # 'LÉO DE PAULA',
           '09∙JDU TIBIÁ',
           '10∙DE LÁ E DE CÁ',
           '11∙ABRANDAMENTO',
           '12∙DAS ÁGUAS'
           ]
           
ALBUM_TITLE = [
    'GRÃO',
    'TERRITÓRIO',
    'PERCUSSIVO',
    'LÉO',
    'DE PAULA'
    ]


# Standard values
FONT_SIZE = 8 * SCALE_MM_TO_PX
RADIUS_START = 64 * SCALE_MM_TO_PX
STEPS = 30
is_sequential = True
debug = False
show_cd = True
           
# If you're using DrawBot's IDE,
# here is some UI controls

# Variable([
#     dict(name="FONT_SIZE", ui="Slider",
#     args = dict(
#         value = 8,
#         minValue=5,
#         maxValue=72
#         )),
#     dict(name="RADIUS_START", ui="Slider",
#     args = dict(
#         value = 64,
#         minValue = 0,
#         maxValue = 200
#         )),
#     dict(name="STEPS", ui="Slider",
#         args = dict(
#             value = 30,
#             minValue = 4,
#             maxValue = 100
#             )),
#     dict(name="is_sequential", ui="CheckBox",
#     args = dict(
#         value=True
#         )),
#     dict(name="debug", ui="CheckBox",
#     args = dict(
#         value=False
#         )),
#     dict(name="show_cd", ui="CheckBox",
#         args = dict(
#         value=True
#         )),
#     ], globals())

width, height = 329 * SCALE_MM_TO_PX, 329 * SCALE_MM_TO_PX
setup()
# Rotate to a position specific position
rotate(117)
draw(ALBUM_SONGS)

print('font size:', int(FONT_SIZE))
print('min radius:', int(RADIUS_START))
print('steps:', int(STEPS))

# saveImage('./examples/grao-territorio-percussivo.png')
# saveImage('./examples/grao-territorio-percussivo.svg')
# saveImage('./examples/grao-territorio-percussivo.pdf')