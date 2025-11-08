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
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

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

# Generate Functions
def generate_report_content(topic):
    prompt = PromptTemplate(
        template="""You are a research assistant. Create a comprehensive research report about: {topic}
        
        Structure your report with:
        
        ## Introduction
        Provide a brief overview of the topic.
        
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
                    # Add user question to history
                    st.session_state['chat_history'].append({'role': 'user', 'content': user_question})
                    
                    # Generate answer
                    prompt = PromptTemplate(
                        template="""You are a helpful AI assistant. Answer the following question based on the research report provided.
                        
                        Research Report:
                        {report}
                        
                        Question: {question}
                        
                        Provide a clear, concise, and accurate answer. If the information is not in the report, say so and provide general knowledge if helpful.""",
                        input_variables=['report', 'question']
                    )
                    chain = prompt | llm | str_parse
                    answer = chain.invoke({
                        'report': st.session_state['report'],
                        'question': user_question
                    })
                    
                    # Add answer to history
                    st.session_state['chat_history'].append({'role': 'assistant', 'content': answer})
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        
        if clear_button:
            st.session_state['chat_history'] = []
            st.rerun()
        
        # Display chat history
        if st.session_state['chat_history']:
            st.markdown("---")
            for msg in st.session_state['chat_history']:
                if msg['role'] == 'user':
                    st.markdown(f"**🙋 You:** {msg['content']}")
                else:
                    st.markdown(f"<div style='background-color: #E6F3FF; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;'><strong>🤖 AI:</strong> {msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.info("👆 Generate a research report first to start asking questions!")

# Feedback Section
st.markdown("---")
st.subheader("💬 Feedback & Rating")

col_feedback, col_rating = st.columns([3, 1])

with col_feedback:
    feedback_input = st.text_area("Share your feedback:", placeholder="Tell us what you think...")

with col_rating:
    rating = st.slider("⭐ Rate this tool:", 1, 5, 5)

if st.button("📤 Submit Feedback", use_container_width=True):
    if feedback_input:
        sentiment_prompt = PromptTemplate(
            template="""Analyze the sentiment of this feedback and provide a brief, friendly response:
            
            Feedback: {feedback}
            
            Classify as positive or negative, then write a short thank you or acknowledgment message.""",
            input_variables=['feedback']
        )
        try:
            with st.spinner("🔍 Analyzing feedback..."):
                chain = sentiment_prompt | llm | str_parse
                response = chain.invoke({'feedback': feedback_input})
                
                st.success("✅ Thank you for your feedback!")
                st.markdown(f"<div style='background-color: #E6F3FF; padding: 1rem; border-radius: 8px;'><strong>🤖 AI Response:</strong> {response}</div>", unsafe_allow_html=True)
                st.markdown(f"**Your Rating:** {'⭐' * rating}")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("⚠️ Please enter your feedback before submitting!")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #4A90E2; font-weight: 600;'>"
    "🚀 Powered by Google Gemini AI | Built with Streamlit"
    "</div>",
    unsafe_allow_html=True
)
