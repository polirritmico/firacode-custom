#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fontforge
import psMat

# Usage: fontforge -script italice_font.py

# NOTE: The italic modificaton works, but the metadata has problems. So I've
# have to check them manually with fontforge and try different names in TTF and
# OS/2 until got it working with the Regular.
# Since is working now I'll leave it as it until I have more time to improve
# this script.

INPUT_FONT = "FiraCodeNerdFont-Regular.ttf"
OUTPUT_FONT = "FiraCodeNerdFont-Italic.ttf"
ANGLE = 10 * 3.14159 / 180

# Values from https://learn.microsoft.com/en-us/typography/opentype/spec/os2#fsselection
ITALIC_FLAG = 0b0001

font = fontforge.open(INPUT_FONT)

# TODO: Improve this to copy all the metadata from the source
original_font_values = {
    "family": font.familyname,
    "name": font.fontname,
    "fullname": font.fullname,
    "weight": font.weight,
    "os2stylemap": font.os2_stylemap,
    "mac_style": font.macstyle,
}

basename = font.fontname.rsplit("-", 1)[0]
font.fontname = f"{basename}-Italic"
font.fullname = font.fullname.replace("Regular", "Italic")
font.os2_stylemap = ITALIC_FLAG

font.selection.all()
font.transform(psMat.skew(ANGLE))  # 10° slant (radians)

font.generate(OUTPUT_FONT)
font.close()

print("====================================")
print("Original font metadata:")
print(f"Family Name: {original_font_values["familyname"]}")
print(f"Font Name: {original_font_values["fontname"]}")
print(f"Full Name: {original_font_values["fullname"]}")
print(f"Weight: {original_font_values["weight"]}")
print("OS/2 Style Map:", hex(original_font_values["os2_stylemap"]))
print("Mac Style:", hex(original_font_values["macstyle"]))

output_font = fontforge.open(OUTPUT_FONT)

print("------------------------------------")
print("Generated font metadata:")
print(f"Family Name: {output_font.familyname}")
print(f"Font Name: {output_font.fontname}")
print(f"Full Name: {output_font.fullname}")
print(f"Weight: {output_font.weight}")
print("OS/2 Style Map:", hex(output_font.os2_stylemap))
print("Mac Style:", hex(output_font.macstyle))

output_font.close()
