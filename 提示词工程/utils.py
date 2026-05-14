
from openai import OpenAI
import os
from dotenv import load_dotenv


def get_llm_client():
    # 第三步: 加载.env文件中的环境变量
    load_dotenv()

    # 第四步:创建openai客户端对象
    client = OpenAI(
        api_key=os.getenv("api_key"),
        base_url=os.getenv("base_url")
    )
    return client
