# -*- coding: utf-8 -*-
import os
from PIL import Image, ImageDraw, ImageFont

from path import check_dir, base_data


# 获取 macOS 系统中所有可用字体路径
def list_available_fonts():
    font_dirs = [
        "/System/Library/Fonts/",
        "/Library/Fonts/",
        "~/Library/Fonts/"
    ]
    fonts = []
    for font_dir in font_dirs:
        full_path = os.path.expanduser(font_dir)
        if os.path.exists(full_path):
            fonts += [os.path.join(full_path, f) for f in os.listdir(full_path) if f.endswith(".ttf") or f.endswith(".ttc")]
    return fonts

def print_font(text, fonts, font_size, output_path):
    # 设置每行字体的高度
    text_height = 250

    image = Image.new('RGB', (2400, text_height * (len(fonts) + 1)), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    for index in range(len(fonts)):
        try:
            print(index, fonts[index])
            font = ImageFont.truetype(fonts[index], font_size)
            font_color = (0, 0, 0)
            draw.text((100, 50 + text_height * index), str(index) + ": " + fonts[index], font=font, fill=font_color)
            draw.text((100, 50 + text_height / 2 + text_height * index), text, font=font, fill=font_color)
        except OSError as e:
            print(f"Error loading font: {e}")
    image.save(output_path)
    
if __name__ == '__main__':
    fonts = list_available_fonts()
    check_dir(base_data)
    output_path = os.path.join(base_data, "字体范例.png")
    print_font("王逸伟", fonts, 70, output_path)
