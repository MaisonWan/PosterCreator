# -*- coding: utf-8 -*-
import os
import time

# 工作区目录
base_workspace = os.getcwd()

# 数据文件夹根目录
base_data = os.path.join(base_workspace, 'poster')

# 模板文件夹
base_template = os.path.join(base_workspace, "template")

# 导入数据文件的文件夹
poster_today_path = ''

# 系统字体的目录
font_dirs = [
    "/System/Library/Fonts/",
    "/Library/Fonts/",
    "~/Library/Fonts/",
    os.path.join(os.getcwd(), "font")
]

# 检查，不存在则创建文件目录
def check_dir(file_dir):
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)


def today_path():
    date_name = time.strftime("%Y%m%d", time.localtime(time.time()))
    global poster_today_path
    poster_today_path = os.path.join(base_data, date_name)
    return poster_today_path


def get_template_full_path(file_name):
    return os.path.join(base_template, file_name)


# 遍历目录下文件
def file_list(file_dir):
    file_paths = list()
    for root, dirs, files in os.walk(file_dir, topdown=False):
        for name in files:
            file_paths.append(os.path.join(root, name))
    return file_paths

# 获取字体路径
def get_font_path(font_name):
    for font_dir in font_dirs:
        full_path = os.path.join(font_dir, font_name)
        if os.path.exists(full_path):
            return full_path
    raise FileNotFoundError(f"Font '{font_name}' not found in system font directories.")
