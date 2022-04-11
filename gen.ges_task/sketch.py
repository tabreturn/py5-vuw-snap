# This sketch is an adaption of:
# P_3_1_3_01 from Generative Gestaltung
# http://www.generative-gestaltung.de/2/sketches/?01_P/P_3_1_3_01

import string

with open('text.txt', 'r') as f:
    joined_txt = f.readlines()

joined_txt = ' '.join(joined_txt).replace('\n', '')
alphabet = string.ascii_uppercase + string.digits + ' .+,'
font_size, leading, tracking = 18, 30, 20
char_counts = [0] * len(alphabet)

for char in joined_txt:
    index = alphabet.index(char.upper())
    if index > -1: char_counts[index] += 1


def setup():
    size(900, 620)
    mono = create_font('Consolas.ttf', font_size)
    text_font(mono)


def draw():
    background('#518')
    pos_x, pos_y = 20, 40

    for c in joined_txt:
        index = alphabet.index(c.upper())
        if index < 0: continue

        fill(255, char_counts[index]*3)
        sort_y = index * 20 + 40
        m = remap(mouse_x, 50, width-50, 0, 1)
        m = constrain(m, 0, 1)
        inter_y = lerp(pos_y, sort_y, m)
        text(c, pos_x, inter_y)
        pos_x += text_width(c)

        if pos_x > width/1.2 and c.upper() == ' ':
            pos_y += leading
            pos_x = tracking
