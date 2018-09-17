#!/usr/bin/env python
# coding: utf-8

"""
 Created by Hysian on 2018/9/13
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

config = {
    'username': 'root',
    'password': '123456',
    'ip': '127.0.0.1',
    'database': 'saas'
}


def format_uri(config):
    uri = 'mysql+pymysql://{username}:{password}@{ip}:33063/{database}?charset=utf8'
    return uri.format(**config)

# 初始化数据库连接:
uri = format_uri(config)
engine = create_engine(uri)
Session = sessionmaker(bind=engine, expire_on_commit=False)
session = Session()