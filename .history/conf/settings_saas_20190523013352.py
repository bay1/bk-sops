# -*- coding: utf-8 -*-
"""
SaaS上传部署的全局配置
"""
import os

# ===============================================================================
# 数据库设置, 正式环境数据库设置
# ===============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('BKAPP_DB_NAME'),
        'USER': os.environ.get('BKAPP_DB_USERNAME'),
        'PASSWORD': os.environ.get('BKAPP_DB_PASSWORD'),
        'HOST': os.environ.get('BKAPP_DB_HOST'),
        'PORT': os.environ.get('BKAPP_DB_PORT'),
    },
}
