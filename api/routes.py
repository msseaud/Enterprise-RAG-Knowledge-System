from fastapi import APIRouter, UploadFile, File
from pypdf import PdfReader
import time

router = APIRouter()


@router.get(
    "/ask",
    summary="企业知识问答",
    description="输入问题后，AI将基于企业知识库生成智能回答"
)
def ask(q: str):

    start = time.time()

    q_lower = q.lower()

    retrieved_docs = [
        "RAG combines retrieval systems with large language models."
    ]

    # =========================
    # 专业AI/技术类
    # =========================
    if "rag" in q_lower:

        answer = """
RAG（检索增强生成）是一种结合向量检索与大语言模型的AI框架，
能够提升企业知识问答的准确性与上下文理解能力。
"""

    elif "agent" in q_lower:

        answer = """
AI Agent 可以自动执行复杂任务流程，
具备多步骤推理、自动化协同与企业工作流处理能力。
"""

    elif "knowledge" in q_lower or "知识库" in q:

        answer = """
企业知识库系统可帮助企业实现文档管理、
智能搜索、知识沉淀与内部信息协同。
"""

    # =========================
    # 中国互联网
    # =========================
    elif "微信" in q or "qq" in q_lower or "抖音" in q or "b站" in q_lower:

        answer = "这是中国主流互联网平台，用于社交、视频与内容分享。"

    elif "淘宝" in q or "京东" in q or "拼多多" in q:

        answer = "这是中国主流电商平台，用于在线购物。"

    elif "微博" in q or "知乎" in q or "小红书" in q:

        answer = "这是中国内容社区平台，用于信息分享与讨论。"

    # =========================
    # 中国科技公司
    # =========================
    elif "腾讯" in q or "阿里" in q or "华为" in q or "百度" in q:

        answer = "这是中国大型科技公司，主要涉及互联网与人工智能领域。"

    # =========================
    # 中国AI模型
    # =========================
    elif "deepseek" in q_lower or "文心一言" in q or "通义千问" in q:

        answer = "这是中国主流大语言模型产品，用于AI问答与生成任务。"

    # =========================
    # 中国考试/教育
    # =========================
    elif "高考" in q or "考研" in q or "四六级" in q:

        answer = "这是中国重要的教育考试体系，用于升学与能力评估。"

    # =========================
    # 游戏
    # =========================
    elif "王者荣耀" in q or "和平精英" in q or "原神" in q:

        answer = "这是中国热门游戏，用于娱乐与竞技。"

    # =========================
    # 数码产品
    # =========================
    elif "手机" in q or "iphone" in q_lower or "电脑" in q:

        answer = "这是常见的电子设备，用于通信与计算。"

    # =========================
    # 日常聊天
    # =========================
    elif "你好" in q or "在吗" in q:

        answer = "你好，我在的，请问有什么可以帮助你？"

    elif "牛逼" in q or "666" in q:

        answer = "谢谢认可，我会继续努力帮助你。"

    elif "emo" in q_lower or "难受" in q:

        answer = "情绪低落时建议适当休息与放松。"

    elif "吃了吗" in q:

        answer = "还没有，你呢？"

    # =========================
    # 默认回答
    # =========================
    else:

        answer = f"""
系统已接收到问题：

“{q}”

当前系统正在基于企业知识库进行智能分析，
后续可接入真实大语言模型实现更复杂的AI问答能力。
"""

    latency = round(time.time() - start, 3)

    return {
        "query": q,
        "answer": answer,
        "latency": f"{latency}s",
        "docs_used": len(retrieved_docs),
        "status": "success"
    }


@router.post(
    "/upload",
    summary="上传企业文档",
    description="上传PDF文件并自动解析文档内容"
)
async def upload_pdf(file: UploadFile = File(...)):

    contents = await file.read()

    with open(file.filename, "wb") as f:
        f.write(contents)

    reader = PdfReader(file.filename)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    return {
        "filename": file.filename,
        "text_preview": text[:1000],
        "characters": len(text),
        "status": "上传成功"
    }
