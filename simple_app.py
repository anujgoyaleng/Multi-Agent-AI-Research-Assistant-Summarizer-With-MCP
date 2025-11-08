import streamlit as st
import asyncio
import datetime
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from get_mcp import get_mcp_use

load_dotenv()

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    api_key=os.getenv("api_key")
)
str_parse = StrOutputParser()

# Streamlit Config
st.set_page_config(
    page_title="Multi-Agent AI Research Assistant",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.title("🤖 AI Research Assistant")
st.sidebar.write("Generate detailed reports, summaries, and latest news.")
st.sidebar.markdown("---")

# Session State
if 'report' not in st.session_state:
    st.session_state['report'] = ""
if 'summary' not in st.session_state:
    st.session_state['summary'] = ""
if 'news' not in st.session_state:
    st.session_state['news'] = ""

# Topic Input
st.title("📝 AI Research Assistant")
topic = st.text_input("Enter a topic to research:")

col1, col2, col3 = st.columns([1,1,1])
with col1:
    generate_report = st.button("📝 Generate Report")
with col2:
    generate_news = st.button("📰 Fetch News")
with col3:
    generate_summary = st.button("📄 Generate Summary")

# Async Operations
async def generate_report_task(topic):
    prompt = f"Research and provide detailed information about: {topic}. Include key findings, important facts, and sources."
    result = await get_mcp_use(prompt)
    return str(result)

async def fetch_news_task(topic):
    prompt = f"Find the latest news and updates about: {topic}. Include headlines, summaries, and sources."
    result = await get_mcp_use(prompt)
    return str(result)

# Run Tasks
if topic:
    if generate_report:
        with st.spinner("🔍 Generating detailed report..."):
            try:
                report_text = asyncio.run(generate_report_task(topic))
                st.session_state['report'] = report_text
                st.success("✅ Report generated!")
                
                # Save report
                os.makedirs("reports", exist_ok=True)
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                with open(f"reports/report_{timestamp}.md", "w", encoding="utf-8") as f:
                    f.write(f"# Report on {topic}\\n\\n{report_text}")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

    if generate_news:
        with st.spinner("📰 Fetching latest news..."):
            try:
                news_text = asyncio.run(fetch_news_task(topic))
                st.session_state['news'] = news_text
                st.success("✅ News fetched!")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

    if generate_summary and st.session_state.get('report'):
        with st.spinner("📄 Generating summary..."):
            try:
                prompt = PromptTemplate(
                    template="Summarize the following content clearly and concisely:\\n\\n{content}",
                    input_variables=['content']
                )
                summary = (prompt | llm | str_parse).invoke({'content': st.session_state['report']})
                st.session_state['summary'] = summary
                st.success("✅ Summary generated!")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# Display Results
tabs = st.tabs(["📄 Report", "📝 Summary", "📰 News"])

with tabs[0]:
    st.subheader("📄 Detailed Report")
    if st.session_state.get('report'):
        st.markdown(st.session_state['report'])
    else:
        st.info("Generate a report to see it here.")

with tabs[1]:
    st.subheader("📝 Summary")
    if st.session_state.get('summary'):
        st.markdown(st.session_state['summary'])
    else:
        st.info("Generate a summary to see it here.")

with tabs[2]:
    st.subheader("📰 Latest News")
    if st.session_state.get('news'):
        st.markdown(st.session_state['news'])
    else:
        st.info("Fetch news to see it here.")

st.markdown("---")
st.caption("Powered by Google Gemini AI & MCP")
