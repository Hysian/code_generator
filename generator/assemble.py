#!/usr/bin/env python
# coding: utf-8

"""
 Created by Hysian on 2018/9/13
"""
import os
from jinja2 import Environment, PackageLoader
from dbsession_server import session
from generator.utils import meta_sql
from generator.filters import uppercase, lowercase


class Generator:
    
    def __init__(self, data_base, table_name, business, author, templates='template'):
        self.author = author
        self.data_base = data_base
        self.table_name = table_name
        self.business = business
        self.model_name = ''.join(map(lambda x: uppercase(x), table_name.split('_')[1:]))
        self.env = Environment(loader=PackageLoader('generator', templates))
        self.env.filters['uppercase'] = uppercase
        self.env.filters['lowercase'] = lowercase
        self.columns = []
    
    def select_columns(self):
        try:
            self.columns = session.execute(meta_sql(self.data_base, self.table_name)).fetchall()
        except Exception as e:
            raise ValueError('请确认数据库或表是否存在')
        return self.columns
    
    def __get_data(self, Template):
        """
        生成渲染数据
        :param Entity:
        :return:
        """
        entity = Template(self.author, self.business, self.model_name)
        entity.set_attr(self.table_name, self.columns)
        return entity.__dict__
    
    def __get_file(self, Template):
        """
        文件生成路径
        :param Entity:
        :return:
        """
        # 文件路径
        business_path = self.business + '/'
        if not os.path.isdir(business_path):
            os.mkdir(business_path)
        
        if not os.path.isdir(business_path + Template.filepath):
            os.mkdir(business_path + Template.filepath)
        # 文件名
        file_name = self.model_name + Template.filename
        return business_path + Template.filepath + file_name
        
    def render_template(self, Template):
        """
        渲染模板生成文件
        :param Entity:
        :return:
        """
        args = self.__get_data(Template)
        template = self.env.get_template(Template.template)
        content = template.render(args)
     
        with open(self.__get_file(Template), 'w') as f:
            f.write(content)



