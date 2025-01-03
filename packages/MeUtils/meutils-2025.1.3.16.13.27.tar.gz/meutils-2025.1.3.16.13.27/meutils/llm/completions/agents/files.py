#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : files
# @Time         : 2025/1/3 15:38
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  : 支持文档、图片、音频、视频问答
"""单一智能体
任意模型支持文档、图片、音频、视频问答
api形式
- /agents/v1
- /v1 前缀区分 agents-{model}【底层调用 /agents/v1】

"""

from meutils.pipe import *
