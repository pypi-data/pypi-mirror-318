#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : zhipu_智能体
# @Time         : 2024/12/30 17:34
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  : 

from meutils.pipe import *

from zhipuai import ZhipuAI
api_key = "YOUR API KEY"
url = "https://open.bigmodel.cn/api/paas/v4"
client = ZhipuAI(
    api_key="e21bd630f681c4d90b390cd609720483.WSFVgA3KkwNCX0mN",
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)

print(bjson(client.assistant.query_support()))
generate = client.assistant.conversation(
    # assistant_id="65a265419d72d299a9230616",
    assistant_id="65940acff94777010aa6b796",
    conversation_id=None,
    model="glm-4-assistant",
    messages=[
        {
            "role": "user",
            "content": [{
                "type": "text",
                # "text": "北京未来七天气温，做个折线图",

                "text": "画条狗"

            }]
        }
    ],
    stream=True,
    attachments=None,
    metadata=None
)

for resp in generate:
    print(resp)