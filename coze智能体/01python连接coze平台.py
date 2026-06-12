# 1. 导包
# COZE_COM_BASE_URL常量：代表Coze平台官方地址（COZE_COM_BASE_URL国际版地址；COZE_CN_BASE_URL国内版地址）
# Coze类：用于创建Coze对象，实现Agent调用与操作
# TokenAuth类：用于实现对API_KEY认证，让Coze平台允许Python调用智能体
import os
from cozepy import COZE_CN_BASE_URL, Coze, TokenAuth,ChatEventType,Message,MessageObjectString

# 2. 准备相关配置信息
# coze_api_token代表访问秘钥信息
coze_api_token = "pat_k52zvVlNuZrsKaUraKe2p7a7FpMlM8BEY80Q1C9e6NYnN3z75tUoxYLO2Z1YZagY"
bot_id="7641038367874121754"
user_id='woshikaijiayongshi'
# 3. 创建Coze类对象
coze = Coze(
    auth=TokenAuth(coze_api_token),
    base_url=COZE_CN_BASE_URL
)

upload_File=coze.files.upload(file="./files/02-简历.docx")
if not upload_File:
    print('sorry,upload file err')
    exit()
else:
    print(f'upload file succ:{upload_File}')

#5.组装消息体并发送请求
messages=[
    Message.build_user_question_objects(
        [
            MessageObjectString.build_file(file_id=upload_File.id),
            MessageObjectString.build_text('请帮我分析一下这份简历')
        ]
    )
]
#发送请求
stream=coze.chat.stream(
    bot_id=bot_id,
    user_id=user_id,
    additional_messages=messages
)

result_text=""
for chunk in stream:
    if chunk.event==ChatEventType.CONVERSATION_MESSAGE_DELTA:
        print(chunk.message.content,end="",flush=True)
        result_text+=chunk.message.content
    elif chunk.event in [ChatEventType.CONVERSATION_CHAT_COMPLETED,ChatEventType.CONVERSATION_CHAT_FAILED]:
        break

with open('./RESULT_PATH/result','w',encoding='utf8')as f:
    f.write(result_text)

print('over')