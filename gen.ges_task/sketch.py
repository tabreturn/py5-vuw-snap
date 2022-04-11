# This sketch is an adaption of:
# P_3_1_3_01 from Generative Gestaltung
# http://www.generative-gestaltung.de/2/sketches/?01_P/P_3_1_3_01

import string


def setup():
    # processing setup code
    size(1000//2, 600//2)
    color_mode(HSB, 360, 100, 100, 100)
    mono = create_font('data/Consolas.ttf', 18)
    text_font(mono)
    
    # text and alphabet lists
    global joined_txt, alphabet, counters
    
    with open('data/text.txt', 'r') as f:
        joined_txt = f.readlines()

    alphabet = string.ascii_uppercase + string.digits + ' .+,';
    joined_txt = ' '.join(joined_txt).replace('\n','')
    counters = [0] * len(alphabet)
    count_characters()


def draw():
    background('#FFF')
    pos_x, pos_y = 20, 40
    
    for c in joined_txt:
        index = alphabet.index(c.upper())
        if index < 0: continue
        
        fill(0, 100, 255, counters[index]*3)
        sort_y = index * 20 + 40
        m = remap(mouse_x, 50, width-50, 0, 1)
        m = constrain(m, 0, 1)
        inter_y = lerp(pos_y, sort_y, m)

        text(c, pos_x, inter_y)
        
        if pos_x > width-200 and c.upper() == ' ':
            pos_y += 30
            pos_x += 20


def count_characters():
    global counters
    
    for c in joined_txt:
        index = alphabet.index(c.upper())
        if index > -1: counters[index] += 1

   

