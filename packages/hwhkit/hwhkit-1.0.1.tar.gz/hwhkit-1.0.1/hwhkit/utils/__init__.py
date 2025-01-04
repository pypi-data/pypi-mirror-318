# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# Time       ：2024/4/22 18:36
# Author     ：Maxwell
# Description：
"""

from loguru import logger


# 定义日志格式
logger.add("./logs/info.log", level='INFO', rotation="200 MB")
logger.add("./logs/warning.log", level='WARNING', rotation="200 MB")
logger.add("./logs/debug.log", level='DEBUG', rotation="200 MB")
logger.add("./logs/error.log", level='ERROR', rotation="200 MB")