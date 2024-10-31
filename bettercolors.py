import random

#======================================================#
#        _____  _____  ____  ____  _____  _____        #
#       /  _  \/   __\/    \/    \/   __\/  _  \       #
#      |  _  <|   __|\-  -/\-  -/|   __||  _  <        #
#      \_____/\_____/ |__|  |__| \_____/\__|\_/        #
#       _____  _____  ____   _____  _____  _____       #
#      /     \/  _  \/  _/  /  _  \/  _  \/  ___>      #
#      |  |--||  |  ||  |---|  |  ||  _  <|___  |      #
#      \_____/\_____/\_____/\_____/\__|\_/<_____/      #
#                                                      #
#======================================================#

# BASE COLORS
RED = 196;       DARK_RED = 88;        LIGHT_RED = 197
BLUE = 32;       DARK_BLUE = 24;       LIGHT_BLUE = 39
YELLOW = 226;    DARK_YELLOW = 17;    LIGHT_YELLOW = 226
GREEN = 46;      DARK_GREEN = 22;      LIGHT_GREEN = 83
CYAN = 51;       LIGHT_CYAN = 51;      DARK_CYAN = 37
PINK = 200;      LIGHT_PINK = 213;     DARK_PINK = 125
ORANGE = 208;    DARK_ORANGE = 172;    LIGHT_ORANGE = 214
BROWN = 130;     DARK_BROWN = 88;      LIGHT_BROWN = 94
MAGENTA = 201;   DARK_MAGENTA = 135;   LIGHT_MAGENTA = 207
PURPLE = 129;    DARK_PURPLE = 54;     LIGHT_PURPLE = 55
GREY = 8;        DARK_GREY = 244;      LIGHT_GREY = 250

# OTHER COLORS
GOLD = 220;      SILVER = 7
WHITE = 15;      BLACK = 0
RESET = 39;      RANDOM = random.randint(0,255)
RAINBOW = "rainbow"



esc_char_start = '\033[38;5;'
esc_char_end = '\033[0m'

def code_to_chars(code):
    return esc_char_start + str(code) + 'm'



def Fore(color_code=None, attribute=None, text=None):

    attributes = []
    if attribute == 1:  # BOLD
        attributes.append('1')
    elif attribute == 2:  # STRIKETHROUGH
        attributes.append('9')
    elif attribute == 3:  # UNDERLINE
        attributes.append('4')

    if color_code == RANDOM:
        color_code = random.randint(0,255)

    if color_code is None or color_code == RESET:
        return esc_char_end

    if isinstance(color_code, str):
        color_code = globals().get(color_code.upper(), None)

    if color_code == RAINBOW:
        if text is None:
            return f'[{Fore(RAINBOW, text="BetterColors")}]: incorrect format for: "rainbow". Usage -> ''{Fore(RAINBOW, text="")}\n'
        else:
            return rainbow_text(text, 1)

    attr_str = ';'.join(attributes)
    if attr_str:
        return f"\033[{attr_str};{color_code}m"
    return code_to_chars(color_code)



def Back(color_code=None, text=None):

    if color_code == RANDOM:
        color_code = random.randint(0,255)

    if color_code is None or color_code == RESET:
        return esc_char_end

    if isinstance(color_code, str):
        color_code = globals().get(color_code.upper(), None)

    if color_code == RAINBOW:
        if text is None:
            return f'[{Fore(RAINBOW, text="BetterColors")}]: incorrect format for: "rainbow". Usage -> ''{Fore(RAINBOW, text="")}\n'
        else:
            return rainbow_text(text, 2)

    return f'\033[48;5;{color_code}m'



def rainbow_text(text, attribute):
    colors = [196, 202, 208, 214, 220, 226, 190, 154, 118, 82, 46, 47, 48, 49, 50, 51, 45, 39, 33, 27, 21, 57, 93, 129, 165, 201, 129, 21, 33, 45, 50, 47, 82, 154, 226, 208]
    rainbow_output = ''

    if attribute == 1:  # FORE
        for i, char in enumerate(text):
            color = colors[i % len(colors)]
            rainbow_output += code_to_chars(color) + char
        return rainbow_output + esc_char_end

    elif attribute == 2:  # BACK
        for i, char in enumerate(text):
            color = colors[i % len(colors)]
            rainbow_output += f'\033[48;5;{color}m{char}'
        return rainbow_output + esc_char_end
    return text
