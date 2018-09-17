
# 代码生成器
[![License](https://img.shields.io/github/license/richardchien/coolq-http-api.svg)](https://raw.githubusercontent.com/richardchien/coolq-http-api/master/LICENSE)
这是用Python写的Java基础代码生成器为了实现拓展性和兼容性，核心类Generator几乎不处理模板字段，自行定义代码模板页面与模板类，模板类当中可以自定义方法处理模板将要渲染的数据。。

## 使用方法
 - 建好数据表
 - 调用main.py中的generate方法，传入database数据库, tables要生成对象的表名, 业务模块包名business, 类注释author字段
 
## 有时间再写剩下的
