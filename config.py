# -*- coding: utf-8 -*-
import json


class Config:

    def __init__(self):
        self.template_list = list()
        with open('config/config.json', 'r') as f:
            json_file = json.load(f)
            for t in json_file['templates']:
                self.template_list.append(t)

    def get_template(self, index):
        return self.template_list[index]

    def get_template_name_list(self):
        name_list = list()
        for t in self.template_list:
            name_list.append(t['name'])
        return name_list
    
    def count(self):
        return len(self.template_list)
