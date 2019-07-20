import nonebot
import config
from nonebot import on_notice, NoticeSession, on_request, RequestSession
from nonebot.message import MessageSegment, Message,Context_T,message_preprocessor,NoneBot
import random
import time

"""
# 将函数注册为群成员增加通知处理器
@on_notice('group_increase')
async def _(session: NoticeSession):
        # 发送欢迎消息
    bot = session.bot
    user_id = session.ctx['user_id']   #获取新入群的成员的QQ号
    seg = MessageSegment.at(user_id)
    await bot.send_group_msg(group_id=517632499, message= seg+' '+'欢迎,进群请改名片\n未录取新生群备注：年份-省份/文理-昵称\n录取新生群备注：年份-专业-昵称\n在校生群备注：年份-专业-昵称\n'+'!!!!注意!!!!\n如果不改名可能会被暴躁管理踢出群哦')

@on_request('group')
    #同意加群请求
async def _(session: RequestSession):
    await session.approve()
"""
nonebot.init()
bot = nonebot.get_bot()
"""
a={}
b=time.strftime("%H",time.localtime())
if b == 0:
    a.clear()

@bot.on_message('group')
async def handle(context):
    if str(context['message']) == '肉':
        b=random.randint(1,100)
        if context['user_id'] in a:
            await bot.send(context, MessageSegment.at(context['user_id'])+Message('\n您今天已经roll过了，点数为%d' %a[context['user_id']]))
        if context['user_id'] not in a:
            a[context['user_id']]=b
            await bot.send(context, MessageSegment.at(context['user_id'])+Message('\nroll到了%d点' %b))
"""


@bot.on_message('group')
async def handle(context):
    #if str(context['message']) == '赞':
       # await bot.send_like(user_id=context['user_id'],times=10)
       # await bot.send(context,Message('已赞'))
    x=await bot.get_group_member_info(group_id=context['group_id'],user_id=context['user_id'],no_cache=True)
    n = x['card']
    if n == '':
        await bot.send(context,MessageSegment.at(context['user_id'])+Message('\n请修改群名片哦，群名片格式：\n年级-专业-名称,不知道专业可填预录取'))

if __name__ == '__main__':
    nonebot.load_builtin_plugins()
    nonebot.run(host='172.17.0.1', port=8080)

