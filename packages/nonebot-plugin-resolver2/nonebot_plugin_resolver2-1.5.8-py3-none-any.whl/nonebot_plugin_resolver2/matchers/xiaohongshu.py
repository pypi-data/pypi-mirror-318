import re
import httpx
import json
import asyncio

from nonebot.rule import Rule
from nonebot.log import logger
from nonebot.plugin.on import on_keyword, on_message
from nonebot.adapters.onebot.v11 import (
    Bot,
    Message,
    MessageEvent,
    MessageSegment
)
from urllib.parse import parse_qs, urlparse

from .filter import is_not_in_disable_group
from .utils import get_video_seg, construct_nodes

from ..constant import COMMON_HEADER
from ..data_source.common import download_video, download_img
from ..config import *

# 小红书下载链接
XHS_REQ_LINK = "https://www.xiaohongshu.com/explore/"

def is_xhs(event: MessageEvent) -> bool:
    message = str(event.message).strip()
    return any(key in message for key in {"xiaohongshu.com", "xhslink.com"})

# xiaohongshu = on_keyword(
#     keywords={"xiaohongshu.com", "xhslink.com"},
#     rule = Rule(is_not_in_disable_group),
#     block = True
# )

xiaohongshu = on_message(
    rule = Rule(is_not_in_disable_group, is_xhs)
)

@xiaohongshu.handle()
async def _(bot: Bot, event: MessageEvent):
    # message: str = event.message.extract_plain_text().replace("&amp;", "&").strip()
    message: str = str(event.message).replace("&amp;", "&").strip()
    if match := re.search(r"(http:|https:)\/\/(xhslink|(www\.)xiaohongshu).com\/[A-Za-z\d._?%&+\-=\/#@]*",message):
        msg_url = match.group(0)
    # 请求头
    headers = {
                  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                            'application/signed-exchange;v=b3;q=0.9',
                  'cookie': rconfig.r_xhs_ck,
              } | COMMON_HEADER
    if "xhslink" in msg_url:
        async with httpx.AsyncClient() as client:
            resp = await client.get(msg_url, headers=headers, follow_redirects=True)
            msg_url = str(resp.url)
    # ?: 非捕获组
    pattern = r'(?:/explore/|/discovery/item/|source=note&noteId=)(\w+)'
    if match := re.search(pattern, msg_url):
        xhs_id = match.group(1)
    else:
        return
    # 解析 URL 参数
    parsed_url = urlparse(msg_url)
    params = parse_qs(parsed_url.query)
    # 提取 xsec_source 和 xsec_token
    xsec_source = params.get('xsec_source', [None])[0] or "pc_feed"
    xsec_token = params.get('xsec_token', [None])[0]
    async with httpx.AsyncClient() as client:
        resp = await client.get(f'{XHS_REQ_LINK}{xhs_id}?xsec_source={xsec_source}&xsec_token={xsec_token}', headers=headers)
        html = resp.text
    pattern = r'window.__INITIAL_STATE__=(.*?)</script>'
    if match := re.search(pattern, html):
        json_str = match.group(1)
    else:
        await xiaohongshu.finish("小红书 cookie 可能已失效")
    json_str = json_str.replace("undefined", "null")
    json_obj = json.loads(json_str)
    note_data = json_obj['note']['noteDetailMap'][xhs_id]['note']
    type = note_data['type']
    note_title = note_data['title']
    note_desc = note_data['desc']
    title_msg = f"{NICKNAME}解析 | 小红书 - {note_title}\n{note_desc}"

    if type == 'normal':
        aio_task = []
        image_list = note_data['imageList']
        # 批量
        for index, item in enumerate(image_list):
            aio_task.append(asyncio.create_task(
                download_img(item['urlDefault'], img_name=f'{index}.jpg')))
        img_path_list = await asyncio.gather(*aio_task)
        # 发送图片
        segs = [title_msg] + [MessageSegment.image(img_path) for img_path in img_path_list]
        nodes = construct_nodes(bot.self_id, segs)
        await xiaohongshu.finish(nodes)
    elif type == 'video':
        await xiaohongshu.send(title_msg)
        # 这是一条解析有水印的视频
        # logger.info(note_data['video'])
        video_url = note_data['video']['media']['stream']['h264'][0]['masterUrl']
        # video_url = f"http://sns-video-bd.xhscdn.com/{note_data['video']['consumer']['originVideoKey']}"
        await xiaohongshu.finish(await get_video_seg(url = video_url))
    


