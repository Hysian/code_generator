#!/usr/bin/env python
# coding: utf-8

"""
 Created by Hysian on 2018/9/13
"""
from generator.templates import Entity, Mapper, Service, Impl, ApiService, ApiController
from generator.assemble import Generator

def generate(database, tables, business, author):
    for table_name in tables:
        generator = Generator(database, table_name, business, author)
        # 从数据库中获取表结构
        generator.select_columns()
        generator.render_template(Entity)
        generator.render_template(Mapper)
        generator.render_template(Service)
        generator.render_template(Impl)
        generator.render_template(ApiService)
        generator.render_template(ApiController)

# tables = ['activity_activity', 'activity_prize', 'activity_winner_info']
# generate('saas', tables, 'activity', 'hyx')

