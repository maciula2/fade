# Module made by @venaxyt on Github
from random import randint
from os import system

def blackwhite(text, horizontal=False):
    system(""); faded = ""
    lines = text.splitlines()
    if horizontal:
        for i, line in enumerate(lines):
            width = len(line)
            for i, char in enumerate(line):
                if width > 1:
                    t=i/(width-1)
                else:
                    t=0
                red = int(180 *(1-t))
                green = int(180 *(1-t))
                blue = int(180 *(1-t))
                faded += f"\033[38;2;{red};{green};{blue}m{char}\033[0m"
            if line != lines[len(lines)-1]:
                faded += "\n"
        return faded
    red = 0; green = 0; blue = 0
    for i, line in enumerate(lines):
        if line != lines[len(lines)-1]:
            faded += (f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n")
        else:
            faded += (f"\033[38;2;{red};{green};{blue}m{line}\033[0m")
        if not red == 255 and not green == 255 and not blue == 255:
            red += 20; green += 20; blue += 20
            if red > 255 and green > 255 and blue > 255:
                red = 255; green = 255; blue = 255
    return faded

def purplepink(text, horizontal=False):
    system(""); faded = ""
    lines = text.splitlines()
    if horizontal:
        for i, line in enumerate(lines):
            width = len(line)
            for i, char in enumerate(line):
                if width > 1:
                    t=i/(width-1)
                else:
                    t=0
                red = int(195 *(1-t))
                faded += f"\033[38;2;{red};0;220m{char}\033[0m"
            if line != lines[len(lines)-1]:
                faded += "\n"
        return faded
    system(""); faded = ""
    red = 40
    for i, line in enumerate(lines):
        if line != lines[len(lines)-1]:
            faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
        else:
            faded += (f"\033[38;2;{red};0;220m{line}\033[0m")

        if not red == 255:
            red += 15
            if red > 255:
                red = 255
    return faded

def greenblue(text, horizontal=False):
    system(""); faded = ""
    lines = text.splitlines()
    if horizontal:
        for i, line in enumerate(lines):
            width = len(line)
            for i, char in enumerate(line):
                if width > 1:
                    t=i/(width-1)
                else:
                    t=0
                blue = int(235 *(1-t))
                faded += f"\033[38;2;0;255;{blue}m{char}\033[0m"
            if line != lines[len(lines)-1]:
                faded += "\n"
        return faded
    blue = 100
    for i, line in enumerate(lines):
        if line != lines[len(lines)-1]:
            faded += (f"\033[38;2;0;255;{blue}m{line}\033[0m\n")
        else:
            faded += (f"\033[38;2;0;255;{blue}m{line}\033[0m")
        if not blue == 255:
            blue += 15
            if blue > 255:
                blue = 255
    return faded

def pinkred(text, horizontal=False):
    system(""); faded = ""
    lines = text.splitlines()
    if horizontal:
        for i, line in enumerate(lines):
            width = len(line)
            for i, char in enumerate(line):
                if width > 1:
                    t=i/(width-1)
                else:
                    t=0
                blue = int(250 *(1-t))
                faded += f"\033[38;2;255;0;{blue}m{char}\033[0m"
            if line != lines[len(lines)-1]:
                faded += "\n"
        return faded
    blue = 255
    for i, line in enumerate(lines):
        if line != lines[len(lines)-1]:
            faded += (f"\033[38;2;255;0;{blue}m{line}\033[0m\n")
        else:
            faded += (f"\033[38;2;255;0;{blue}m{line}\033[0m")
        if not blue == 0:
            blue -= 20
            if blue < 0:
                blue = 0
    return faded

def purpleblue(text, horizontal=False):
    system(""); faded = ""
    lines = text.splitlines()
    if horizontal:
        for i, line in enumerate(lines):
            width = len(line)
            for i, char in enumerate(line):
                if width > 1:
                    t=i/(width-1)
                else:
                    t=0
                red = int(110 *(1-t))
                faded += f"\033[38;2;{red};0;255m{char}\033[0m"
            if line != lines[len(lines)-1]:
                faded += "\n"
        return faded
    red = 110
    for i, line in enumerate(lines):
        if line != lines[len(lines)-1]:
            faded += (f"\033[38;2;{red};0;255m{line}\033[0m\n")
        else:
            faded += (f"\033[38;2;{red};0;255m{line}\033[0m")
        if not red == 0:
            red -= 15
            if red < 0:
                red = 0
    return faded

def water(text, horizontal=False):
    system(""); faded = ""
    lines = text.splitlines()
    if horizontal:
        for i, line in enumerate(lines):
            width = len(line)
            for i, char in enumerate(line):
                if width > 1:
                    t=i/(width-1)
                else:
                    t=0
                green = int(200 *(1-t))
                faded += f"\033[38;2;0;{green};255m{char}\033[0m"
            if line != lines[len(lines)-1]:
                faded += "\n"
        return faded
    green = 10
    for i, line in enumerate(lines):
        if line != lines[len(lines)-1]:
            faded += (f"\033[38;2;0;{green};255m{line}\033[0m\n")
        else:
            faded += (f"\033[38;2;0;{green};255m{line}\033[0m")
        if not green == 255:
            green += 15
            if green > 255:
                green = 255
    return faded


def fire(text, horizontal=False):
    system(""); faded = ""
    lines = text.splitlines()
    if horizontal:
        for i, line in enumerate(lines):
            width = len(line)
            for i, char in enumerate(line):
                if width > 1:
                    t=i/(width-1)
                else:
                    t=0
                green = int(250 *(1-t))
                faded += f"\033[38;2;255;{green};0m{char}\033[0m"
            if line != lines[len(lines)-1]:
                faded += "\n"
        return faded
    green = 250    
    for i, line in enumerate(lines):
        if line != lines[len(lines)-1]:
            faded += (f"\033[38;2;255;{green};0m{line}\033[0m\n")
        else:
            faded += (f"\033[38;2;255;{green};0m{line}\033[0m")
        if not green == 0:
            green -= 25
            if green < 0:
                green = 0
    return faded

def brazil(text, horizontal=False):
    system(""); faded = ""
    lines = text.splitlines()
    if horizontal:
        for i, line in enumerate(lines):
            width = len(line)
            for i, char in enumerate(line):
                if width > 1:
                    t=i/(width-1)
                else:
                    t=0
                red = int(250 *(1-t))
                faded += f"\033[38;2;{red};255;0m{char}\033[0m"
            if line != lines[len(lines)-1]:
                faded += "\n"
        return faded
    red = 0
    for i, line in enumerate(lines):
        if line != lines[len(lines)-1]:
            faded += (f"\033[38;2;{red};255;0m{line}\033[0m\n")
        else:
            faded += (f"\033[38;2;{red};255;0m{line}\033[0m")
        if not red > 200:
            red += 30
    return faded

def random(text):
    system(""); faded = ""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        for character in line:
            faded += (f"\033[38;2;{randint(0,255)};{randint(0,255)};{randint(0,255)}m{character}\033[0m")
        if line != lines[len(lines)-1]:
                faded += "\n"
    return faded
