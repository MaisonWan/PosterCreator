# -*- coding: utf-8 -*-
from config import Config
from poster_creator import PosterCreator


def show_template_menu(name_list):
    count = len(name_list)
    print("共有%d个模板，请选择使用模板序号：" % count)
    for t in range(count):
        print("[%d].%s" % (t + 1, name_list[t]))
    index = input()
    try:
        n = int(index)
        if 1 <= n <= count + 1:
            return n - 1
        int('s')
    except ValueError:
        print("序号输入不正确！")
        exit(0)


def show_person_info_menu():
    print("请批量输入海报信息，空行回车视为结束。格式如：天坛，张三，100万")
    info = list()
    line = input()
    while line != "":
        info.append(line[1:] if line.startswith("🔥") else line)
        line = input()
    return info


if __name__ == '__main__':
    config = Config()
    template_index = show_template_menu(config.get_template_name_list())
    info_list = show_person_info_menu()

    for person in info_list:
        creator = PosterCreator(config.get_template(template_index), person)
        creator.build()
