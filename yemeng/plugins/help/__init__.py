from nonebot.rule import to_me
from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11 import Bot, Message, Event, MessageSegment
from pathlib import Path

help = on_command("help", rule=to_me(),aliases={"帮助"},priority=1,block=True)

img1=Path("/root/yemeng/yemeng/plugins/help/data/bf.png")
img2=Path("/root/yemeng/yemeng/plugins/help/data/apex.png")
img3=Path("/root/yemeng/yemeng/plugins/help/data/setu.png")
mes_list=["《战地》系列",MessageSegment.image(img1),"《Apex》系列",MessageSegment.image(img2),"setu",MessageSegment.image(img3),"\n其它文字将被GhatGPT处理。\n后续功能持续开发中..."]

@help.handle()
async def handle_function():
    await help.finish(mes_list)