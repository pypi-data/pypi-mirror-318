#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : ecraft
# @Time         : 2024/10/31 16:30
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  :

from meutils.pipe import *
from meutils.io.files_utils import to_url
from meutils.schemas.image_types import ImageRequest, ImagesResponse, RecraftImageRequest
from meutils.notice.feishu import IMAGES, send_message as _send_message
from meutils.config_utils.lark_utils import get_next_token_for_polling, aget_spreadsheet_values
from meutils.decorators.retry import retrying

BASE_URL = "https://api.recraft.ai"

FEISHU_URL = "https://xchatllm.feishu.cn/sheets/GYCHsvI4qhnDPNtI4VPcdw2knEd?sheet=Lrhtf2"

DEFAULT_MODEL = "recraftv3"
MODELS = {}

send_message = partial(
    _send_message,
    title=__name__,
    url=IMAGES
)


@alru_cache(ttl=10 * 60)
@retrying()
async def get_access_token(token: Optional[str] = None):
    token = token or await get_next_token_for_polling(feishu_url=FEISHU_URL, check_token=check_token)
    headers = {"cookie": token}

    async with httpx.AsyncClient(base_url="https://www.recraft.ai", headers=headers, timeout=60) as client:
        response = await client.get("/api/auth/session")
        response.raise_for_status()
        logger.debug(response.json())
        return response.json()["accessToken"]


# @retrying()
async def generate(request: RecraftImageRequest, token: Optional[str] = None):
    token = await get_access_token(token)
    headers = {"Authorization": f"Bearer {token}"}
    # params = {"project_id": "26016b99-3ad0-413b-821b-5f884bd9454e"}  # project_id 是否是必要的
    params = {}  # project_id 是否是必要的
    # params = {"project_id": "47ba6825-0fde-4cea-a17e-ed7398c0a298"}
    payload = request.model_dump(exclude_none=True)
    logger.debug(payload)

    async with httpx.AsyncClient(base_url=BASE_URL, headers=headers, timeout=60) as client:
        response = await client.post(f"/queue_recraft/prompt_to_image", params=params, json=payload)
        response.raise_for_status()
        params = {
            "operation_id": response.json()["operationId"]
        }
        logger.debug(params)

        response = await client.get("/poll_recraft", params=params)
        response.raise_for_status()
        metadata = response.json()
        logger.debug(metadata)

        # {'credits': 1,
        #  'height': 1024,
        #  'images': [{'image_id': 'f9d8e7dd-c31f-4208-abe4-f44cdff050c2',
        #              'image_invariants': {'preset': 'any'},
        #              'transparent': False,
        #              'vector_image': False}],
        #  'random_seed': 1423697946,
        #  'request_id': '77bd917d-0960-4921-916f-038c773a41fd',
        #  'transform_model': 'recraftv3',
        #  'width': 1024}

        params = {"raster_image_content_type": "image/webp"}  #####
        params = {"raster_image_content_type": "image/png"}

        images = []
        for image in response.json()["images"]:
            response = await client.get(f"""/image/{image["image_id"]}""", params=params)
            url = await to_url(response.content)
            images.append(url)

        return ImagesResponse(image=images, metadata=metadata)


async def check_token(token, threshold: float = 1):
    if not isinstance(token, str):
        tokens = token
        r = []
        for batch in tqdm(tokens | xgroup(32)):
            bools = await asyncio.gather(*map(check_token, batch))
            r += list(itertools.compress(batch, bools))
        return r
    try:
        access_token = await get_access_token(token)
        headers = {"Authorization": f"Bearer {access_token}"}

        async with httpx.AsyncClient(base_url=BASE_URL, headers=headers, timeout=60) as client:
            response = await client.get("/users/me")
            response.raise_for_status()
            data = response.json()
            logger.debug(data["credits"])
            return data["credits"] >= threshold
    except Exception as e:
        logger.error(e)
        logger.debug(token)
        return False


if __name__ == '__main__':
    token = None
    # arun(get_access_token())
    request = RecraftImageRequest(
        prompt='一条猫'
    )
    # arun(generate(request, token=token))

    tokens = list(arun(aget_spreadsheet_values(feishu_url=FEISHU_URL, to_dataframe=True))[0]) | xfilter_


    r = arun(check_token(tokens))
