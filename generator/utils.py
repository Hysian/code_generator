#!/usr/bin/env python
# coding: utf-8

"""
 Created by Hysian on 2018/9/13
"""


def meta_sql(database, tablename):
    """
    构造数据表结构查询语句
    :param database:
    :param tablename:
    :return:
    """
    sql = 'select COLUMN_NAME, DATA_TYPE, COLUMN_COMMENT from information_schema.columns' \
          ' where table_schema = \'{}\'' \
          ' and table_name = \'{}\';'
    return sql.format(database, tablename)

