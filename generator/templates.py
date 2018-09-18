#!/usr/bin/env python
# coding: utf-8

"""
 Created by Hysian on 2018/9/13
"""
__author__ = 'Hysian'
import time
from generator.raws import ENTITY_PARENTS, COLUMN_TYPE, PACKAGE, BASE_ATTR

class BaseAttr:
    def __init__(self, author, business, model_name):
        self.author = author
        self.date = time.strftime('%Y-%m-%d %H:%M')
        self.business = business
        self.model_name = model_name
    
    def set_attr(self, table_name, columns):
        pass


class Entity(BaseAttr):
    template = 'Entity.html'
    filename = '.java'
    filepath = 'entity/'
    
    def __init__(self, author, business, model_name):
        BaseAttr.__init__(self, author, business, model_name)
        self.attrs = []
        self.table_name = ''
        self.entity_parent = ''
        self.entity_imports = []
    
    def format_columns(self, columns):
        for column, type, comment in columns:
            if column in ENTITY_PARENTS:
                self.entity_parent = ENTITY_PARENTS.get(column)
            elif column in BASE_ATTR:
                continue
            else:
                comment = '// ' + comment if comment != '' else ''
                type = COLUMN_TYPE.get(type)
                if type in PACKAGE and type not in self.entity_imports:
                    self.entity_imports.append(PACKAGE.get(type))
                self.attrs.append(dict(column=column, type=type, comment=comment))
        self.entity_imports.insert(0, PACKAGE.get(self.entity_parent))
        self.entity_imports = list(set(self.entity_imports))
    
    def set_attr(self, table_name, columns):
        self.format_columns(columns)
        self.table_name = table_name


class Service(BaseAttr):
    template = 'Service.html'
    filename = 'Service.java'
    filepath = 'service/'


class ApiService(BaseAttr):
    template = 'ApiService.html'
    filename = 'ApiService.java'
    filepath = 'api/'
    
    def __init__(self, author, business, model_name):
        BaseAttr.__init__(self, author, business, model_name)
        self.api = ''
    
    def set_attr(self, table_name, columns):
        self.api = '_'.join(table_name.split('_')[1:])


class ApiController(BaseAttr):
    template = 'ApiController.html'
    filename = 'ApiController.java'
    filepath = 'controller/'
    
    def __init__(self, author, business, model_name):
        BaseAttr.__init__(self, author, business, model_name)
        self.api = ''
    
    def set_attr(self, table_name, columns):
        self.api = '_'.join(table_name.split('_')[1:])


class Mapper(BaseAttr):
    template = 'Mapper.html'
    filename = 'Mapper.java'
    filepath = 'mapper/'


class Impl(BaseAttr):
    template = 'ServiceImpl.html'
    filename = 'ServiceImpl.java'
    filepath = 'service/impl/'
