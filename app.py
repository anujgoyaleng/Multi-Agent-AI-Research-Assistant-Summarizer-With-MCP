import streamlit as st
import datetime
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    api_key=os.getenv("api_key"),
    temperature=0.7,
    max_tokens=2048
)
str_parse = StrOutputParser()

# Modern Blue Theme CSS
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #7e8ba3 100%);
    }
    .main {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 2rem;
        border-radius: 15px;
    }
    .stButton>button {
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
        color: white;
        border-radius: 10px;
        padding: 0.6rem 2rem;
        border: none;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(37, 99, 235, 0.3);
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #1d4ed8 0%, #1e40af 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(37, 99, 235, 0.5);
    }
    .stTextInput>div>div>input {
        border: 2px solid #3b82f6;
        border-radius: 10px;
        padding: 0.75rem;
        font-size: 1rem;
    }
    .stTextInput>div>div>input:focus {
        border-color: #2563eb;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
    }
    .report-box {
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 5px solid #3b82f6;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(59, 130, 246, 0.1);
    }
    .summary-box {
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 5px solid #2563eb;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(37, 99, 235, 0.1);
    }
    .news-box {
        background: linear-gradient(135deg, #bfdbfe 0%, #93c5fd 100%);
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 5px solid #1d4ed8;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(29, 78, 216, 0.1);
    }
    .chat-box {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 5px solid #0ea5e9;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(14, 165, 233, 0.1);
    }
    h1 {
        color: #1e40af;
        font-weight: 800;
        text-shadow: 2px 2px 4px rgba(30, 64, 175, 0.1);
    }
    h2, h3 {
        color: #2563eb;
        font-weight: 700;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
        border-radius: 10px 10px 0 0;
        padding: 12px 24px;
        color: #1e40af;
        font-weight: 600;
        border: 2px solid transparent;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        border-color: #1d4ed8;
    }
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #1e3c72 0%, #2a5298 100%);
    }
</style>
""", unsafe_allow_html=True)

# Streamlit Config
st.set_page_config(
    page_title="🤖 AI Research Assistant",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
with st.sidebar:
    st.title("🤖 AI Research Assistant")
    st.markdown("---")
    st.markdown("### ✨ Features")
    st.markdown("📝 Comprehensive Research Reports")
    st.markdown("📰 Real-time News Updates")
    st.markdown("📄 Smart Summaries")
    st.markdown("💬 Interactive Q&A")
    st.markdown("---")
    st.info("💡 Powered by Google Gemini AI")
    st.markdown("---")
    st.caption("Built with ❤️ using Streamlit")

# Session State
if 'report' not in st.session_state:
    st.session_state['report'] = ""
if 'summary' not in st.session_state:
    st.session_state['summary'] = ""
if 'news' not in st.session_state:
    st.session_state['news'] = ""
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Main Title
st.title("🔍 AI-Powered Research Assistant")
st.markdown("### Get instant research reports, news, and summaries on any topic")

# Topic Input
topic = st.text_input("🎯 Enter your research topic:", placeholder="e.g., Artificial Intelligence, Climate Change, Quantum Computing...")

# Buttons
col1, col2, col3 = st.columns(3)
with col1:
    generate_report = st.button("📝 Generate Report", use_container_width=True)
with col2:
    generate_news = st.button("📰 Fetch News", use_container_width=True)
with col3:
    generate_summary = st.button("📄 Create Summary", use_container_width=True)

# Generate Functions
def generate_report_content(topic):
    prompt = PromptTemplate(
        template="""You are an expert research assistant. Create a comprehensive research report about: {topic}
        
        Structure your report with:
        
        ## Introduction
        Provide a clear overview of the topic.
        
        ## Key Findings
        List the most important facts, statistics, and insights.
        
        ## Recent Developments
        Highlight recent news, trends, or breakthroughs.
        
        ## Conclusion
        Summarize the main points and their significance.
        
        Make it informative, well-structured, and easy to read.""",
        input_variables=['topic']
    )
    chain = prompt | llm | str_parse
    return chain.invoke({'topic': topic})

def fetch_news_content(topic):
    prompt = PromptTemplate(
        template="""You are a news aggregator. Find and summarize the latest news about: {topic}
        
        Provide:
        
        ## Latest Headlines
        List 5-7 recent news headlines related to this topic.
        
        ## Key Updates
        Summarize the most important recent developments.
        
        ## Trending Topics
        Mention what's currently trending or being discussed.
        
        Focus on recent, relevant, and credible information.""",
        input_variables=['topic']
    )
    chain = prompt | llm | str_parse
    return chain.invoke({'topic': topic})

def create_summary_content(content):
    prompt = PromptTemplate(
        template="""Create a concise summary of the following content:
        
        {content}
        
        Your summary should:
        - Highlight the main points
        - Be clear and easy to understand
        - Keep only the most important information
        - Be about 200-300 words""",
        input_variables=['content']
    )
    chain = prompt | llm | str_parse
    return chain.invoke({'content': content})

def answer_question(question, context):
    prompt = PromptTemplate(
        template="""Based on the following research content, answer the question accurately and concisely.
        
        Research Content:
        {context}
        
        Question: {question}
        
        Answer:""",
        input_variables=['context', 'question']
    )
    chain = prompt | llm | str_parse
    return chain.invoke({'context': context, 'question': question})

# Run Tasks
if topic:
    if generate_report:
        with st.spinner("🔍 Researching and generating report..."):
            try:
                report_text = generate_report_content(topic)
                st.session_state['report'] = report_text
                st.success("✅ Report generated successfully!")
                
                # Save report
                os.makedirs("reports", exist_ok=True)
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                with open(f"reports/report_{timestamp}.md", "w", encoding="utf-8") as f:
                    f.write(f"# Research Report: {topic}\n\n{report_text}")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

    if generate_news:
        with st.spinner("📰 Fetching latest news..."):
            try:
                news_text = fetch_news_content(topic)
                st.session_state['news'] = news_text
                st.success("✅ News fetched successfully!")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

    if generate_summary and st.session_state.get('report'):
        with st.spinner("📄 Creating summary..."):
            try:
                summary = create_summary_content(st.session_state['report'])
                st.session_state['summary'] = summary
                st.success("✅ Summary created successfully!")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    elif generate_summary and not st.session_state.get('report'):
        st.warning("⚠️ Please generate a report first before creating a summary!")

# Display Results
st.markdown("---")
tabs = st.tabs(["📄 Research Report", "📝 Summary", "📰 Latest News", "💬 Q&A Chat"])

with tabs[0]:
    if st.session_state.get('report'):
        st.markdown('<div class="report-box">', unsafe_allow_html=True)
        st.markdown(st.session_state['report'])
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Download button
        st.download_button(
            label="📥 Download Report",
            data=st.session_state['report'],
            file_name=f"report_{topic.replace(' ', '_')}.md",
            mime="text/markdown"
        )
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

with tabs[3]:
    st.subheader("💬 Ask Questions About Your Research")
    
    if st.session_state.get('report'):
        # Q&A Input
        user_question = st.text_input("Ask a question:", key="qna_input", placeholder="e.g., What are the main findings?")
        
        col_ask, col_clear = st.columns([3, 1])
        with col_ask:
            ask_button = st.button("🔍 Ask Question", use_container_width=True)
        with col_clear:
            clear_button = st.button("🗑️ Clear Chat", use_container_width=True)
        
        if ask_button and user_question:
            with st.spinner("🤔 Thinking..."):
                try:
                    answer = answer_question(user_question, st.session_state['report'])
                    st.session_state['chat_history'].append({
                        'question': user_question,
                        'answer': answer
                    })
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        
        if clear_button:
            st.session_state['chat_history'] = []
            st.rerun()
        
        # Display Chat History
        if st.session_state['chat_history']:
            st.markdown("### Chat History")
            for i, chat in enumerate(reversed(st.session_state['chat_history'])):
                st.markdown('<div class="chat-box">', unsafe_allow_html=True)
                st.markdown(f"**Q:** {chat['question']}")
                st.markdown(f"**A:** {chat['answer']}")
                st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.info("💡 Ask questions about the research report to get started!")
    else:
        st.warning("⚠️ Please generate a report first to use the Q&A feature!")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #2563eb; font-weight: 600; font-size: 1.1rem;'>"
    "🚀 Powered by Google Gemini AI | Built with Streamlit"
    "</div>",
    unsafe_allow_html=True
)
