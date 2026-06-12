import os
import time
import streamlit as st
from cozepy import COZE_CN_BASE_URL, Coze, TokenAuth, ChatEventType, Message, MessageObjectString

st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed",
)

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@300;400;600&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.stApp {
    background: linear-gradient(135deg, #f5f0ff 0%, #e8f4ff 30%, #ffffff 100%);
}

h1, h2, h3 {
    font-family: 'Orbitron', sans-serif !important;
    background: linear-gradient(135deg, #6366f1 0%, #06b6d4 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: 2px;
}

h1 { font-size: 2.4rem !important; margin-bottom: 0 !important; }
h2 { font-size: 1.3rem !important; }

.stButton > button {
    font-family: 'Orbitron', sans-serif !important;
    background: linear-gradient(135deg, #6366f1 0%, #06b6d4 100%) !important;
    color: #fff !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.7rem 2.5rem !important;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    box-shadow: 0 4px 20px #6366f144;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    box-shadow: 0 6px 30px #6366f166 !important;
    transform: translateY(-2px);
}

.stButton > button:disabled {
    opacity: 0.4;
    box-shadow: none !important;
}

.result-box {
    background: #ffffff !important;
    border: 1px solid #e0e7ff !important;
    border-radius: 12px !important;
    padding: 2rem !important;
    margin-top: 1.5rem !important;
    box-shadow: 0 4px 24px #6366f10d;
}

.result-box p, .result-box li, .result-box span {
    color: #334155 !important;
    line-height: 1.8 !important;
}

.result-box strong {
    color: #6366f1 !important;
}

.result-box h4, .result-box h5, .result-box h6 {
    font-family: 'Orbitron', sans-serif !important;
    background: linear-gradient(135deg, #6366f1 0%, #06b6d4 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.status-indicator {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    color: #6366f1;
    font-family: 'Orbitron', sans-serif;
    font-size: 0.75rem;
    letter-spacing: 1px;
}

.status-dot {
    width: 8px;
    height: 8px;
    background: #6366f1;
    border-radius: 50%;
    animation: pulse 1.5s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.3; }
}

.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #6366f144, #06b6d444, transparent);
    margin: 1.5rem 0;
}

.block-container { padding-top: 2rem !important; }
footer { display: none !important; }
#MainMenu { visibility: hidden; }
header { visibility: hidden; }

/* Feature cards */
.feature-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    margin: 1.5rem 0;
}
.feature-card {
    background: #ffffff;
    border: 1px solid #e0e7ff;
    border-radius: 12px;
    padding: 1.5rem 1rem;
    text-align: center;
    box-shadow: 0 2px 12px #6366f108;
    transition: all 0.3s ease;
}
.feature-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 30px #6366f118;
}
.feature-icon {
    font-size: 2rem;
    margin-bottom: 0.5rem;
}
.feature-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 0.75rem;
    background: linear-gradient(135deg, #6366f1 0%, #06b6d4 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: 1px;
    margin-bottom: 0.3rem;
}
.feature-desc {
    color: #64748b;
    font-size: 0.8rem;
    line-height: 1.5;
}

/* Steps */
.steps-container {
    display: flex;
    justify-content: space-between;
    margin: 1.5rem 0;
    position: relative;
}
.steps-container::before {
    content: '';
    position: absolute;
    top: 20px; left: 10%; right: 10%;
    height: 2px;
    background: linear-gradient(90deg, #6366f1, #06b6d4);
    z-index: 0;
}
.step-item {
    text-align: center;
    z-index: 1;
    flex: 1;
}
.step-circle {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: linear-gradient(135deg, #6366f1, #06b6d4);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #fff;
    font-family: 'Orbitron', sans-serif;
    font-size: 0.85rem;
    font-weight: 700;
    margin: 0 auto 0.5rem;
    box-shadow: 0 4px 16px #6366f133;
}
.step-label {
    color: #475569;
    font-size: 0.8rem;
}

/* Loading animation */
.loading-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 3rem 0;
    gap: 1.5rem;
}
.loading-ring {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    border: 3px solid #e0e7ff;
    border-top-color: #6366f1;
    animation: spin 1s linear infinite;
}
@keyframes spin {
    to { transform: rotate(360deg); }
}
.loading-ring-2 {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    border: 2px solid transparent;
    border-top-color: #06b6d4;
    border-bottom-color: #6366f1;
    animation: spin 1.5s linear infinite;
    position: absolute;
}
.loading-text {
    font-family: 'Orbitron', sans-serif;
    font-size: 0.8rem;
    color: #6366f1;
    letter-spacing: 3px;
    animation: blink 1.2s step-end infinite;
}
@keyframes blink {
    50% { opacity: 0.3; }
}
.loading-dots::after {
    content: '';
    animation: dots 2s steps(4) infinite;
}
@keyframes dots {
    0% { content: ''; }
    25% { content: '.'; }
    50% { content: '..'; }
    75% { content: '...'; }
}

/* Shimmer skeleton */
.skeleton {
    background: linear-gradient(90deg, #f1f5f9 25%, #e2e8f0 50%, #f1f5f9 75%);
    background-size: 200% 100%;
    animation: shimmer 1.5s ease-in-out infinite;
    border-radius: 8px;
}
@keyframes shimmer {
    0% { background-position: 200% 0; }
    100% { background-position: -200% 0; }
}
.skeleton-line {
    height: 14px;
    margin-bottom: 10px;
    width: 100%;
}
.skeleton-line:nth-child(2) { width: 85%; }
.skeleton-line:nth-child(3) { width: 70%; }
.skeleton-line:nth-child(4) { width: 92%; }
.skeleton-line:nth-child(5) { width: 60%; }

/* Bouncing dots */
.bounce-dots {
    display: flex;
    gap: 6px;
    align-items: center;
    justify-content: center;
    padding: 2rem 0;
}
.bounce-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: #6366f1;
    animation: bounce 1.4s ease-in-out infinite both;
}
.bounce-dot:nth-child(1) { animation-delay: -0.32s; }
.bounce-dot:nth-child(2) { animation-delay: -0.16s; }
.bounce-dot:nth-child(3) { animation-delay: 0s; }
@keyframes bounce {
    0%, 80%, 100% { transform: scale(0); opacity: 0.5; }
    40% { transform: scale(1); opacity: 1; }
}

/* Stats bar */
.stats-bar {
    display: flex;
    justify-content: space-around;
    background: #ffffff;
    border: 1px solid #e0e7ff;
    border-radius: 12px;
    padding: 1.2rem;
    margin: 1.5rem 0;
    box-shadow: 0 2px 12px #6366f108;
}
.stat-item {
    text-align: center;
}
.stat-value {
    font-family: 'Orbitron', sans-serif;
    font-size: 1.4rem;
    font-weight: 700;
    background: linear-gradient(135deg, #6366f1 0%, #06b6d4 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.stat-label {
    color: #94a3b8;
    font-size: 0.7rem;
    font-family: 'Orbitron', sans-serif;
    letter-spacing: 1px;
    margin-top: 2px;
}
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

st.markdown(
    "<div style='display:flex;align-items:center;gap:12px;margin-bottom:0'>"
    "<span style='font-size:2rem'>⚡</span>"
    "<h1 style='margin:0'>简历智能分析</h1>"
    "</div>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='color:#64748b;font-size:0.9rem;margin-top:0'>"
    "基于 Coze AI 的智能简历评估系统"
    "</p>",
    unsafe_allow_html=True,
)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

# Stats bar
st.markdown(
    "<div class='stats-bar'>"
    "<div class='stat-item'><div class='stat-value'>AI</div><div class='stat-label'>驱动引擎</div></div>"
    "<div class='stat-item'><div class='stat-value'>10s</div><div class='stat-label'>极速分析</div></div>"
    "<div class='stat-item'><div class='stat-value'>5维</div><div class='stat-label'>全面评估</div></div>"
    "<div class='stat-item'><div class='stat-value'>∞</div><div class='stat-label'>持续优化</div></div>"
    "</div>",
    unsafe_allow_html=True,
)

# Feature cards
st.markdown(
    "<div class='feature-grid'>"
    "<div class='feature-card'>"
    "<div class='feature-icon'>🎯</div>"
    "<div class='feature-title'>岗位匹配</div>"
    "<div class='feature-desc'>AI 智能分析简历与目标岗位的匹配程度</div>"
    "</div>"
    "<div class='feature-card'>"
    "<div class='feature-icon'>📊</div>"
    "<div class='feature-title'>技能评估</div>"
    "<div class='feature-desc'>全面评估技术栈深度与项目经验含金量</div>"
    "</div>"
    "<div class='feature-card'>"
    "<div class='feature-icon'>💡</div>"
    "<div class='feature-title'>优化建议</div>"
    "<div class='feature-desc'>提供针对性修改建议，提升简历竞争力</div>"
    "</div>"
    "</div>",
    unsafe_allow_html=True,
)

# Steps
st.markdown(
    "<div class='steps-container'>"
    "<div class='step-item'><div class='step-circle'>1</div><div class='step-label'>上传简历</div></div>"
    "<div class='step-item'><div class='step-circle'>2</div><div class='step-label'>AI 解析</div></div>"
    "<div class='step-item'><div class='step-circle'>3</div><div class='step-label'>深度评估</div></div>"
    "<div class='step-item'><div class='step-circle'>4</div><div class='step-label'>获取报告</div></div>"
    "</div>",
    unsafe_allow_html=True,
)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "上传简历文件",
    type=["docx", "pdf", "doc"],
    label_visibility="collapsed",
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    analyze_btn = st.button(
        "▶ 开始分析", use_container_width=True, disabled=uploaded_file is None
    )

placeholder_result = st.empty()

if analyze_btn:
    coze_api_token = "pat_k52zvVlNuZrsKaUraKe2p7a7FpMlM8BEY80Q1C9e6NYnN3z75tUoxYLO2Z1YZagY"
    bot_id = "7641038367874121754"
    user_id = "woshikaijiayongshi"

    temp_dir = "temp_uploads"
    os.makedirs(temp_dir, exist_ok=True)
    file_ext = os.path.splitext(uploaded_file.name)[1] or ".docx"
    temp_path = os.path.join(temp_dir, f"resume{file_ext}")
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    try:
        with placeholder_result.container():
            st.markdown(
                "<div class='loading-container'>"
                "<div style='position:relative;display:flex;align-items:center;justify-content:center'>"
                "<div class='loading-ring-2'></div>"
                "<div class='loading-ring'></div>"
                "</div>"
                "<div class='bounce-dots'>"
                "<div class='bounce-dot'></div>"
                "<div class='bounce-dot'></div>"
                "<div class='bounce-dot'></div>"
                "</div>"
                "<div style='text-align:center'>"
                "<div class='status-indicator' style='justify-content:center'>"
                "<span class='status-dot'></span> 正在连接 Coze 分析引擎 ..."
                "</div>"
                "</div>"
                "</div>",
                unsafe_allow_html=True,
            )
            time.sleep(0.5)

        coze = Coze(auth=TokenAuth(coze_api_token), base_url=COZE_CN_BASE_URL)

        upload_result = coze.files.upload(file=temp_path)
        if not upload_result:
            st.error("文件上传失败，请重试")
            st.stop()

        messages = [
            Message.build_user_question_objects(
                [
                    MessageObjectString.build_file(file_id=upload_result.id),
                    MessageObjectString.build_text("请帮我分析一下这份简历"),
                ]
            )
        ]

        stream = coze.chat.stream(
            bot_id=bot_id,
            user_id=user_id,
            additional_messages=messages,
        )

        result_text = ""
        result_placeholder = placeholder_result.empty()

        with result_placeholder.container():
            st.markdown(
                "<div class='loading-container'>"
                "<div style='position:relative;display:flex;align-items:center;justify-content:center'>"
                "<div class='loading-ring-2'></div>"
                "<div class='loading-ring'></div>"
                "</div>"
                "<div class='bounce-dots'>"
                "<div class='bounce-dot'></div>"
                "<div class='bounce-dot'></div>"
                "<div class='bounce-dot'></div>"
                "</div>"
                "<div style='text-align:center'>"
                "<div class='status-indicator' style='justify-content:center'>"
                "<span class='status-dot'></span> 接收分析结果 ..."
                "</div>"
                "<div style='margin-top:1rem'>"
                "<div class='skeleton skeleton-line'></div>"
                "<div class='skeleton skeleton-line'></div>"
                "<div class='skeleton skeleton-line'></div>"
                "<div class='skeleton skeleton-line'></div>"
                "<div class='skeleton skeleton-line'></div>"
                "</div>"
                "</div>"
                "</div>",
                unsafe_allow_html=True,
            )

        for chunk in stream:
            if chunk.event == ChatEventType.CONVERSATION_MESSAGE_DELTA:
                result_text += chunk.message.content
                with result_placeholder.container():
                    st.markdown(
                        f"<div class='result-box'>{result_text}</div>",
                        unsafe_allow_html=True,
                    )
            elif chunk.event in [
                ChatEventType.CONVERSATION_CHAT_COMPLETED,
                ChatEventType.CONVERSATION_CHAT_FAILED,
            ]:
                break

        result_dir = "RESULT_PATH"
        os.makedirs(result_dir, exist_ok=True)
        with open(os.path.join(result_dir, "result"), "w", encoding="utf-8") as f:
            f.write(result_text)

        with result_placeholder.container():
            st.markdown(
                f"<div class='result-box'>{result_text}</div>"
                "<div style='text-align:right;margin-top:0.8rem;color:#22c55e;font-size:0.85rem'>✅ 分析完成</div>",
                unsafe_allow_html=True,
            )

    except Exception as e:
        st.error(f"系统错误: {e}")
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center;color:#94a3b8;font-size:0.75rem;font-family:Orbitron,sans-serif;letter-spacing:2px'>"
    "POWERED BY COZE AI</p>",
    unsafe_allow_html=True,
)
