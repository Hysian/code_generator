#!/usr/bin/env python
# coding: utf-8

"""
 Created by Hysian on 2018/9/13
"""

# PO继承对象
ENTITY_PARENTS = {
    'customerId': 'SimpleCustomerEntity',
    'id': 'SimpleEntity',
    'userId': 'SimpleUserEntity',
}

# mysql类型映射Java数据类型
COLUMN_TYPE = {
    'decimal': 'BigDecimal',
    'datetime': 'Date',
    'char': 'String',
    'varchar': 'String',
    'int': 'Integer',
    'double': 'Double'
}

# PO导包
PACKAGE = {
    'Date': 'java.util.Date',
    'BigDecimal': 'java.math.BigDecimal',
    'SimpleEntity': 'com.zhangchu.common.base.entity.SimpleEntity',
    'SimpleUserEntity': 'com.zhangchu.common.base.entity.SimpleUserEntity',
    'SimpleCustomerEntity': 'com.zhangchu.common.base.entity.SimpleCustomerEntity'
}

# 继承属性
BASE_ATTR = ['id', 'lastUpdateTime', 'createTime', 'isDel']
