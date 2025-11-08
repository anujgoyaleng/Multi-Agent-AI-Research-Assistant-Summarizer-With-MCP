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
    api_key=os.getenv("api_key"),
    temperature=0.7,
    max_tokens=2048
)
str_parse = StrOutputParser()

# Custom CSS for White and Blue Theme
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .main {
        background-color: white;
        padding: 2rem;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #4A90E2;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 2rem;
        border: none;
        font-weight: 600;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #357ABD;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(74, 144, 226, 0.4);
    }
    .stTextInput>div>div>input {
        border: 2px solid #4A90E2;
        border-radius: 8px;
        padding: 0.75rem;
    }
    .report-box {
        background-color: #F0F8FF;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #4A90E2;
        margin: 1rem 0;
    }
    .summary-box {
        background-color: #E6F3FF;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #2E86DE;
        margin: 1rem 0;
    }
    .news-box {
        background-color: #D6EAF8;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #1A5490;
        margin: 1rem 0;
    }
    h1 {
        color: #2C3E50;
        font-weight: 700;
    }
    h2, h3 {
        color: #4A90E2;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #E8F4F8;
        border-radius: 8px 8px 0 0;
        padding: 10px 20px;
        color: #4A90E2;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background-color: #4A90E2;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Streamlit Config
st.set_page_config(
    page_title="🤖 AI Research Assistant",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
with st.sidebar:
    st.title("🤖 AI Research Assistant")
    st.markdown("---")
    st.markdown("### Features")
    st.markdown("✅ Fast Research Reports")
    st.markdown("✅ Latest News Updates")
    st.markdown("✅ Smart Summaries")
    st.markdown("---")
    st.info("💡 Powered by Google Gemini AI")

# Session State
if 'report' not in st.session_state:
    st.session_state['report'] = ""
if 'summary' not in st.session_state:
    st.session_state['summary'] = ""
if 'news' not in st.session_state:
    st.session_state['news'] = ""

# Main Title
st.title("🔍 AI-Powered Research Assistant")
st.markdown("Get instant research reports, news, and summaries on any topic")

# Topic Input
topic = st.text_input("🎯 Enter your research topic:", placeholder="e.g., Artificial Intelligence, Climate Change, etc.")

# Buttons
col1, col2, col3 = st.columns(3)
with col1:
    generate_report = st.button("📝 Generate Report", use_container_width=True)
with col2:
    generate_news = st.button("📰 Fetch News", use_container_width=True)
with col3:
    generate_summary = st.button("📄 Create Summary", use_container_width=True)

# Async Operations (Optimized)
async def generate_report_task(topic):
    prompt = f"""Research and provide a comprehensive report about: {topic}
    
    Include:
    - Key findings and facts
    - Important statistics
    - Recent developments
    - Reliable sources
    
    Keep it concise but informative."""
    result = await get_mcp_use(prompt)
    return str(result)

async def fetch_news_task(topic):
    prompt = f"""Find the latest news about: {topic}
    
    Include:
    - Recent headlines
    - Brief summaries
    - Key updates
    - News sources
    
    Focus on the most recent and relevant information."""
    result = await get_mcp_use(prompt)
    return str(result)

# Run Tasks
if topic:
    if generate_report:
        with st.spinner("🔍 Researching and generating report..."):
            try:
                report_text = asyncio.run(generate_report_task(topic))
                st.session_state['report'] = report_text
                st.success("✅ Report generated successfully!")
                
                # Save report
                os.makedirs("reports", exist_ok=True)
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                with open(f"reports/report_{timestamp}.md", "w", encoding="utf-8") as f:
                    f.write(f"# Research Report: {topic}\\n\\n{report_text}")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

    if generate_news:
        with st.spinner("📰 Fetching latest news..."):
            try:
                news_text = asyncio.run(fetch_news_task(topic))
                st.session_state['news'] = news_text
                st.success("✅ News fetched successfully!")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

    if generate_summary and st.session_state.get('report'):
        with st.spinner("📄 Creating summary..."):
            try:
                prompt = PromptTemplate(
                    template="Create a concise summary of the following content. Focus on key points and main ideas:\\n\\n{content}",
                    input_variables=['content']
                )
                summary = (prompt | llm | str_parse).invoke({'content': st.session_state['report']})
                st.session_state['summary'] = summary
                st.success("✅ Summary created successfully!")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# Display Results
st.markdown("---")
tabs = st.tabs(["📄 Research Report", "📝 Summary", "📰 Latest News"])

with tabs[0]:
    if st.session_state.get('report'):
        st.markdown('<div class="report-box">', unsafe_allow_html=True)
        st.markdown(st.session_state['report'])
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("👆 Click 'Generate Report' to see research results here")

with tabs[1]:
    if st.session_state.get('summary'):
        st.markdown('<div class="summary-box">', unsafe_allow_html=True)
        st.markdown(st.session_state['summary'])
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("👆 Generate a report first, then create a summary")

with tabs[2]:
    if st.session_state.get('news'):
        st.markdown('<div class="news-box">', unsafe_allow_html=True)
        st.markdown(st.session_state['news'])
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("👆 Click 'Fetch News' to see latest updates here")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #4A90E2; font-weight: 600;'>"
    "🚀 Powered by Google Gemini AI & MCP | Built with Streamlit"
    "</div>",
    unsafe_allow_html=True
)
