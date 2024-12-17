# -*- coding: utf-8 -*-
import os.path

from PIL import Image, ImageDraw, ImageFont

import path


def __write_word__(draw, style, text):
    # 获得基本样式
    x = style['position_x']
    y = style['position_y']
    text_font = style['text_font']
    text_size = style['text_size']
    text_color = style['text_color']
    stroke_width = style['stroke_width']
    stroke_color = style['stroke_color']

    font = ImageFont.truetype(font=text_font, size=text_size)  # 创建字体器
    text_length = draw.textlength(text=text, font=font)
    if stroke_width > 0:
        draw.text(xy=(x - text_length / 2, y), text=text, fill=text_color, font=font, stroke_width=stroke_width,
                  stroke_fill=stroke_color)
    else:
        draw.text(xy=(x - text_length / 2, y), text=text, fill=text_color, font=font)


class PosterCreator:
    def __init__(self, config, text_line=''):
        """
        具体绘制的类，初始化文本配置类型，具体打印的文本
        :param config:按照每个文本的类型
        :param text_line:命令行输入的信息，需要拆解
        """
        self.text_style_list = list()
        # 分解文本
        self.text_list = list()
        for t in text_line.split('，'):
            self.text_list.append(t)

        # 模板文件名称
        self.template_file_path = path.get_template_full_path(config['file_name'])

        # 获取文本样式
        for style in config['text_style']:
            self.text_style_list.append(style)

        # 初始化今天日期的文件夹
        self.output_path = path.today_path()
        path.check_dir(self.output_path)

    def build(self):
        """
        开始创建，自动生成到当天日期的文件夹中。以类型数量为基准，文本超限不展示
        """

        image = Image.open(self.template_file_path)  # 打开图片
        draw = ImageDraw.Draw(image)  # 创建写字绘图器

        for index in range(len(self.text_style_list)):
            style = self.text_style_list[index]
            __write_word__(draw, style, self.text_list[index])

        full_path = os.path.join(self.output_path, self.__output_image_file_name_())
        image.save(full_path)
        print("生成海报：%s" % full_path)

    def __output_image_file_name_(self):
        name = ''
        for t in self.text_list:
            name += t + '_'
        return name[:-1] + ".png"

