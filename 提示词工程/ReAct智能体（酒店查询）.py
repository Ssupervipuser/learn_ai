import os
import random
from datetime import datetime

from utils import get_llm_client
from openai import OpenAI

client = get_llm_client()

# 1. 定义工具获取当前日期（如用户未指定日期，则通过这个函数获取当天日期，用于支撑用户提到的明天、后天等信息）
def get_current_date():
    # return f"{datetime.now()}"
    return datetime.now().strftime("%Y-%m-%d")

# 2. 定义工具获取用户所在地（如用户未提供目的地，则用这个函数获取城市作为目的地）
def get_user_location():
    return random.choice(['郑州', '南京', '北京', '上海'])

# 3. 定义工具查询酒店客房（传入目的地、日期）返回客房信息（内容随意编造即可）

def query_hotel_room(target,date):
