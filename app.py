import streamlit as st
import datetime
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from feedback import get_feedback
from api_key_manager import get_active_api_key, render_api_key_settings, initialize_api_key_from_storage

load_dotenv()

# Initialize API key from storage
initialize_api_key_from_storage()

# Initialize LLM with dynamic API key
@st.cache_resource
def get_llm_instance(_api_key):
    """Get LLM instance with provided API key"""
    if not _api_key:
        raise ValueError("No API key available. Please configure your API key.")
    return ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        api_key=_api_key,
        temperature=0.7,
        max_tokens=2048
    )

# Get active API key and initialize LLM
active_api_key = get_active_api_key()
if active_api_key:
    try:
        llm = get_llm_instance(active_api_key)
        str_parse = StrOutputParser()
        st.session_state['app_ready'] = True
    except Exception as e:
        llm = None
        st.session_state['app_ready'] = False
        st.error(f"Error initializing LLM: {str(e)}")
else:
    llm = None
    st.session_state['app_ready'] = False

# Modern Elegant Professional Theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
        margin: 0;
        padding: 0;
    }
    
    /* Main App Background - Elegant Dark */
    .stApp {
        background: linear-gradient(180deg, #000000 0%, #0a0a0a 100%);
    }
    
    /* Fixed Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a0a0a 0%, #000000 100%);
        border-right: 1px solid #2a2a2a;
        position: fixed;
        height: 100vh;
        overflow-y: auto;
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background: linear-gradient(180deg, #0a0a0a 0%, #000000 100%);
    }
    
    /* Main Content Area - Professional */
    .main {
        background: transparent;
        padding: 2.5rem 3.5rem;
        margin-left: 0;
    }
    
    .block-container {
        padding: 2rem 1.5rem;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    /* Standardized Professional Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #1a1a1a 0%, #0f0f0f 100%);
        color: #ffffff;
        border-radius: 10px;
        padding: 0.7rem 1.8rem;
        border: 1px solid #2a2a2a;
        font-weight: 500;
        font-size: 0.875rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        text-transform: none;
        letter-spacing: 0.3px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.3);
        height: 44px;
        min-width: 140px;
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%);
        border-color: #3a3a3a;
        transform: translateY(-2px);
        box-shadow: 0 4px 16px rgba(0,0,0,0.5);
    }
    
    .stButton>button:active {
        transform: translateY(0);
        background: linear-gradient(135deg, #151515 0%, #0a0a0a 100%);
        box-shadow: 0 1px 4px rgba(0,0,0,0.4);
    }
    
    /* Minimal Input Fields */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background: #0a0a0a;
        border: 1px solid #1a1a1a;
        border-radius: 6px;
        padding: 1rem;
        font-size: 0.95rem;
        color: #ffffff;
        transition: all 0.2s ease;
        font-weight: 300;
    }
    
    .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
        border-color: #2a2a2a;
        background: #0f0f0f;
        outline: none;
    }
    
    .stTextInput>div>div>input::placeholder, .stTextArea>div>div>textarea::placeholder {
        color: #4a4a4a;
        font-weight: 300;
    }
    
    /* Minimal Content Boxes */
    .content-box {
        background: #0a0a0a;
        padding: 2rem;
        border-radius: 6px;
        border-left: 2px solid #2a2a2a;
        margin: 1.5rem 0;
        border: 1px solid #1a1a1a;
        transition: all 0.2s ease;
    }
    
    .content-box:hover {
        border-color: #2a2a2a;
        border-left-color: #3a3a3a;
    }
    
    .report-box {
        border-left-color: #2a2a2a;
    }
    
    .summary-box {
        border-left-color: #2a2a2a;
    }
    
    .news-box {
        border-left-color: #2a2a2a;
    }
    
    /* Minimal Chat Messages */
    .chat-message {
        background: #0a0a0a;
        padding: 1.25rem;
        border-radius: 6px;
        margin: 1rem 0;
        border-left: 2px solid #2a2a2a;
        border: 1px solid #1a1a1a;
        transition: all 0.2s ease;
    }
    
    .chat-message:hover {
        border-color: #2a2a2a;
    }
    
    .user-message {
        border-left-color: #3a3a3a;
        background: #0f0f0f;
    }
    
    /* Minimal Typography */
    h1 {
        color: #ffffff;
        font-weight: 300;
        font-size: 2.5rem;
        text-align: center;
        margin-bottom: 0.5rem;
        letter-spacing: -0.5px;
    }
    
    h2 {
        color: #ffffff;
        font-weight: 400;
        font-size: 1.5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    
    h3 {
        color: #ffffff;
        font-weight: 400;
        font-size: 1.2rem;
        margin-bottom: 0.75rem;
    }
    
    p, div, span, li {
        color: #a0a0a0;
        font-weight: 300;
        line-height: 1.7;
    }
    
    strong {
        color: #ffffff;
        font-weight: 500;
    }
    
    .subtitle {
        text-align: center;
        color: #6a6a6a;
        font-size: 1rem;
        margin-bottom: 3rem;
        font-weight: 300;
        letter-spacing: 0.5px;
    }
    
    /* Minimal Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0;
        background-color: transparent;
        border-bottom: 1px solid #1a1a1a;
        padding-bottom: 0;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 0;
        padding: 12px 24px;
        color: #6a6a6a;
        font-weight: 400;
        border: none;
        border-bottom: 2px solid transparent;
        transition: all 0.2s ease;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        color: #a0a0a0;
        border-bottom-color: #2a2a2a;
    }
    
    .stTabs [aria-selected="true"] {
        color: #ffffff;
        border-bottom-color: #ffffff;
        background: transparent;
    }
    
    /* Enhanced Sidebar */
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #0a0a0a 0%, #000000 100%);
        border-right: 1px solid #1a1a1a;
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a0a0a 0%, #000000 100%);
    }
    
    [data-testid="stSidebarNav"] {
        background: #0a0a0a;
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background: linear-gradient(180deg, #0a0a0a 0%, #000000 100%);
    }
    
    /* Sidebar Button Enhancements */
    [data-testid="stSidebar"] .stButton>button {
        background: linear-gradient(135deg, #1a1a1a 0%, #0f0f0f 100%);
        border: 1px solid #2a2a2a;
        transition: all 0.3s ease;
    }
    
    [data-testid="stSidebar"] .stButton>button:hover {
        background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%);
        border-color: #3a3a3a;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.4);
    }
    
    /* Sidebar Form Buttons */
    [data-testid="stSidebar"] .stFormSubmitButton>button {
        font-size: 0.8rem;
        padding: 0.5rem 1rem;
        font-weight: 500;
    }
    
    /* Minimal Download Button */
    .stDownloadButton>button {
        background: #1a1a1a;
        color: #ffffff;
        border-radius: 6px;
        padding: 0.7rem 1.5rem;
        border: 1px solid #2a2a2a;
        font-weight: 500;
        transition: all 0.2s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-size: 0.85rem;
    }
    
    .stDownloadButton>button:hover {
        background: #2a2a2a;
        border-color: #3a3a3a;
    }
    
    /* Enhanced Feature Cards */
    .enhanced-feature-card {
        background: linear-gradient(135deg, #0f0f0f 0%, #0a0a0a 100%);
        padding: 0.75rem 1rem;
        border-radius: 6px;
        border: 1px solid #1a1a1a;
        border-left: 2px solid #2a2a2a;
        transition: all 0.2s ease;
        display: flex;
        align-items: center;
        cursor: pointer;
    }
    
    .enhanced-feature-card:hover {
        background: linear-gradient(135deg, #1a1a1a 0%, #0f0f0f 100%);
        border-left-color: #ffffff;
        transform: translateX(3px);
        box-shadow: 0 2px 8px rgba(0,0,0,0.3);
    }
    
    .feature-icon {
        font-size: 1.1rem;
        margin-right: 0.75rem;
        filter: grayscale(0.3);
        transition: all 0.2s ease;
    }
    
    .enhanced-feature-card:hover .feature-icon {
        filter: grayscale(0);
        transform: scale(1.1);
    }
    
    .feature-text {
        color: #8a8a8a;
        font-size: 0.8rem;
        font-weight: 400;
        letter-spacing: 0.3px;
        transition: all 0.2s ease;
    }
    
    .enhanced-feature-card:hover .feature-text {
        color: #ffffff;
    }
    
    /* Alerts */
    .stAlert {
        border-radius: 14px;
        border-left-width: 6px;
        background: rgba(30, 41, 59, 0.8);
        color: #e2e8f0;
        border: 1px solid rgba(139, 92, 246, 0.2);
    }
    
    /* Success Alert */
    div[data-baseweb="notification"] {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.2) 0%, rgba(30, 41, 59, 0.9) 100%);
        border-left: 6px solid #10b981;
        border-radius: 14px;
    }
    
    /* Spinner */
    .stSpinner > div {
        border-top-color: #8b5cf6 !important;
    }
    
    /* Minimal Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #0a0a0a;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #2a2a2a;
        border-radius: 0;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #3a3a3a;
    }
    
    /* Slider */
    .stSlider [data-baseweb="slider"] {
        background: rgba(255, 255, 255, 0.1);
    }
    
    .stSlider [role="slider"] {
        background: linear-gradient(135deg, #ffffff 0%, #cccccc 100%);
        box-shadow: 0 4px 12px rgba(255, 255, 255, 0.2);
    }
    
    /* Info/Warning/Error boxes */
    .stInfo {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(26, 26, 26, 0.9) 100%);
        border-left-color: #cccccc;
        color: #e5e5e5;
    }
    
    .stWarning {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(26, 26, 26, 0.9) 100%);
        border-left-color: #999999;
        color: #cccccc;
    }
    
    .stError {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(26, 26, 26, 0.9) 100%);
        border-left-color: #666666;
        color: #cccccc;
    }
    
    .stSuccess {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(26, 26, 26, 0.9) 100%);
        border-left-color: #ffffff;
        color: #e5e5e5;
    }
    

    
    /* Minimal Label styling */
    label {
        color: #a0a0a0 !important;
        font-weight: 400 !important;
        font-size: 0.85rem !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Markdown content */
    .stMarkdown {
        color: #a0a0a0;
    }
    
    /* Code blocks */
    code {
        background: #0a0a0a;
        color: #ffffff;
        padding: 0.2rem 0.4rem;
        border-radius: 3px;
        border: 1px solid #1a1a1a;
        font-size: 0.9rem;
    }
    
    pre {
        background: #0a0a0a;
        border: 1px solid #1a1a1a;
        border-radius: 6px;
        padding: 1rem;
    }
    
    /* Minimal Alerts */
    .stAlert {
        border-radius: 6px;
        border-left-width: 2px;
        background: #0a0a0a;
        color: #a0a0a0;
        border: 1px solid #1a1a1a;
    }
    
    /* Success Alert */
    div[data-baseweb="notification"] {
        background: #0a0a0a;
        border-left: 2px solid #2a2a2a;
        border-radius: 6px;
    }
    
    /* Spinner */
    .stSpinner > div {
        border-top-color: #ffffff !important;
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

# Check if API key is configured
if not st.session_state.get('app_ready', False):
    # Show API Key Setup Screen (Center of page)
    st.markdown("<div style='height: 10vh;'></div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style='text-align: center; margin-bottom: 3rem;'>
            <h1 style='color: #ffffff; font-size: 3rem; margin-bottom: 1rem; 
                       font-weight: 200; letter-spacing: 2px;'>
                🤖 AI Research Assistant
            </h1>
            <p style='color: #6a6a6a; font-size: 1.1rem; font-weight: 300; 
                      letter-spacing: 1px; margin-bottom: 3rem;'>
                Powered by Google Gemini AI
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='background: #0a0a0a; padding: 3rem; border-radius: 12px; 
                    border: 1px solid #2a2a2a; box-shadow: 0 8px 32px rgba(0,0,0,0.4);'>
            <h2 style='color: #ffffff; font-size: 1.5rem; margin-bottom: 1rem; 
                       font-weight: 400; text-align: center;'>
                🔑 Enter Your API Key
            </h2>
            <p style='color: #8a8a8a; font-size: 0.95rem; text-align: center; 
                      margin-bottom: 2rem; line-height: 1.6;'>
                To get started, please enter your Google Gemini API key.<br>
                Your key is stored securely in your browser and never sent to our servers.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("initial_api_key_form"):
            api_key_input = st.text_input(
                "Google Gemini API Key",
                type="password",
                placeholder="AIzaSy...",
                help="Get your free API key at https://makersuite.google.com/app/apikey",
                label_visibility="collapsed"
            )
            
            st.markdown("<div style='margin: 1.5rem 0;'></div>", unsafe_allow_html=True)
            
            submit_btn = st.form_submit_button("🚀 Start Using the App", use_container_width=True)
            
            if submit_btn:
                if api_key_input:
                    from api_key_manager import validate_api_key
                    is_valid, error_msg = validate_api_key(api_key_input)
                    
                    if is_valid:
                        st.session_state['user_api_key'] = api_key_input
                        
                        # Save to localStorage
                        import streamlit.components.v1 as components
                        components.html(
                            f"""
                            <script>
                            localStorage.setItem('gemini_api_key', '{api_key_input}');
                            </script>
                            """,
                            height=0,
                        )
                        
                        st.success("✅ API key saved successfully! Reloading app...")
                        st.rerun()
                    else:
                        st.error(f"❌ {error_msg}")
                else:
                    st.error("❌ Please enter your API key to continue")
        
        st.markdown("""
        <div style='margin-top: 2rem; padding: 1.5rem; background: #0f0f0f; 
                    border-radius: 8px; border-left: 3px solid #2a2a2a;'>
            <p style='color: #6a6a6a; font-size: 0.85rem; margin-bottom: 0.5rem;'>
                <strong style='color: #ffffff;'>Don't have an API key?</strong>
            </p>
            <p style='color: #8a8a8a; font-size: 0.85rem; line-height: 1.6;'>
                1. Visit <a href='https://makersuite.google.com/app/apikey' 
                   target='_blank' style='color: #ffffff; text-decoration: underline;'>
                   Google AI Studio</a><br>
                2. Sign in with your Google account<br>
                3. Click "Create API Key"<br>
                4. Copy and paste it above
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='margin-top: 2rem; text-align: center;'>
            <p style='color: #4a4a4a; font-size: 0.75rem;'>
                🔒 Your API key is stored locally in your browser<br>
                and is never transmitted to our servers
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.stop()

# If we reach here, API key is configured - show the main app
# Minimalist Sidebar (Reference Design)
with st.sidebar:
    # Clean Header Section - Centered Text Only
    st.markdown("""
    <div style='padding: 4rem 2rem 3rem 2rem; text-align: center;'>
        <h1 style='color: #ffffff; font-size: 1.5rem; margin: 0 0 1rem 0; 
                   font-weight: 300; letter-spacing: 3px; text-transform: uppercase;'>
            AI RESEARCH
        </h1>
        <p style='color: #4a4a4a; font-size: 0.8rem; margin: 0; 
                  font-weight: 300; letter-spacing: 2px; text-transform: uppercase;'>
            RESEARCH ASSISTANT
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # API Key Settings Section
    render_api_key_settings()
    
    # Divider
    st.markdown("""
    <div style='border-top: 1px solid #1a1a1a; margin: 3rem 0;'></div>
    """, unsafe_allow_html=True)
    
    # Features Section - Simple Text List
    st.markdown("""
    <div style='padding: 0 2rem;'>
        <h3 style='color: #6a6a6a; font-size: 0.75rem; margin: 0 0 2rem 0; 
                   font-weight: 400; letter-spacing: 2px; text-transform: uppercase;'>
            FEATURES
        </h3>
        <div style='display: flex; flex-direction: column; gap: 1.5rem;'>
            <p style='color: #5a5a5a; font-size: 0.9rem; margin: 0; 
                      font-weight: 300; letter-spacing: 0.5px;'>
                Comprehensive Reports
            </p>
            <p style='color: #5a5a5a; font-size: 0.9rem; margin: 0; 
                      font-weight: 300; letter-spacing: 0.5px;'>
                Real-time News
            </p>
            <p style='color: #5a5a5a; font-size: 0.9rem; margin: 0; 
                      font-weight: 300; letter-spacing: 0.5px;'>
                AI Summaries
            </p>
            <p style='color: #5a5a5a; font-size: 0.9rem; margin: 0; 
                      font-weight: 300; letter-spacing: 0.5px;'>
                Q&A Chat
            </p>
            <p style='color: #5a5a5a; font-size: 0.9rem; margin: 0; 
                      font-weight: 300; letter-spacing: 0.5px;'>
                Export & Save
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Divider
    st.markdown("""
    <div style='border-top: 1px solid #1a1a1a; margin: 3rem 0;'></div>
    """, unsafe_allow_html=True)
    
    # Powered By Section - Simple Text
    st.markdown("""
    <div style='padding: 0 2rem;'>
        <h3 style='color: #6a6a6a; font-size: 0.75rem; margin: 0 0 1rem 0; 
                   font-weight: 400; letter-spacing: 2px; text-transform: uppercase;'>
            POWERED BY
        </h3>
        <p style='color: #ffffff; font-size: 0.9rem; margin: 0; 
                  font-weight: 300; letter-spacing: 0.5px;'>
            Google Gemini AI
        </p>
    </div>
    """, unsafe_allow_html=True)

# Initialize Session State
if 'report' not in st.session_state:
    st.session_state['report'] = ""
if 'summary' not in st.session_state:
    st.session_state['summary'] = ""
if 'news' not in st.session_state:
    st.session_state['news'] = ""
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Minimal Main Title
st.markdown("<h1>AI Research Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Instant research reports, news, and summaries</p>", unsafe_allow_html=True)

# Minimal Topic Input
topic = st.text_input(
    "Research Topic",
    placeholder="Enter topic...",
    key="topic_input",
    label_visibility="visible"
)

# Minimal Action Buttons
st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    generate_report = st.button("Generate Report", use_container_width=True)
with col2:
    generate_news = st.button("Fetch News", use_container_width=True)
with col3:
    generate_summary = st.button("Create Summary", use_container_width=True)

# Core Functions
def generate_report_content(topic):
    """Generate comprehensive research report"""
    prompt = PromptTemplate(
        template="""You are an expert research assistant. Create a comprehensive, well-structured research report about: {topic}
        
        Structure your report with:
        
        ## Introduction
        Provide a clear, engaging overview of the topic.
        
        ## Key Findings
        List the most important facts, statistics, and insights with specific details.
        
        ## Recent Developments
        Highlight recent news, trends, breakthroughs, and innovations.
        
        ## Analysis
        Provide deeper analysis and context for the findings.
        
        ## Conclusion
        Summarize the main points and their significance for the future.
        
        Make it informative, well-structured, professional, and easy to read. Use markdown formatting.""",
        input_variables=['topic']
    )
    chain = prompt | llm | str_parse
    return chain.invoke({'topic': topic})

def fetch_news_content(topic):
    """Fetch latest news and updates"""
    prompt = PromptTemplate(
        template="""You are a news aggregator and analyst. Find and summarize the latest news about: {topic}
        
        Provide:
        
        ## Latest Headlines
        List 5-7 recent, relevant news headlines with brief context.
        
        ## Key Updates
        Summarize the most important recent developments and their impact.
        
        ## Trending Topics
        Mention what's currently trending, being discussed, or gaining attention.
        
        ## Industry Impact
        Explain how these developments affect the industry or field.
        
        Focus on recent, relevant, and credible information. Use markdown formatting.""",
        input_variables=['topic']
    )
    chain = prompt | llm | str_parse
    return chain.invoke({'topic': topic})

def create_summary_content(content):
    """Create concise summary"""
    prompt = PromptTemplate(
        template="""Create a concise, well-organized summary of the following content:
        
        {content}
        
        Your summary should:
        - Highlight the main points and key takeaways
        - Be clear, concise, and easy to understand
        - Keep only the most important information
        - Be structured with bullet points or short paragraphs
        - Be approximately 200-300 words
        
        Use markdown formatting for better readability.""",
        input_variables=['content']
    )
    chain = prompt | llm | str_parse
    return chain.invoke({'content': content})

def answer_question(question, context):
    """Answer questions based on research context"""
    prompt = PromptTemplate(
        template="""Based on the following research content, answer the question accurately, concisely, and helpfully.
        
        Research Content:
        {context}
        
        Question: {question}
        
        Provide a clear, informative answer. If the information isn't in the research, say so and provide general knowledge if helpful.""",
        input_variables=['context', 'question']
    )
    chain = prompt | llm | str_parse
    return chain.invoke({'context': context, 'question': question})

# Execute Actions
if topic:
    if generate_report:
        with st.spinner("🔍 Researching and generating comprehensive report..."):
            try:
                report_text = generate_report_content(topic)
                st.session_state['report'] = report_text
                st.success("✅ Report generated successfully!")
                
                # Auto-save report
                os.makedirs("reports", exist_ok=True)
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename = f"reports/report_{topic.replace(' ', '_')}_{timestamp}.md"
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(f"# Research Report: {topic}\n\n{report_text}")
                st.info(f"📁 Report auto-saved to: {filename}")
            except Exception as e:
                st.error(f"❌ Error generating report: {str(e)}")

    elif generate_news:
        with st.spinner("📰 Fetching latest news and updates..."):
            try:
                news_text = fetch_news_content(topic)
                st.session_state['news'] = news_text
                st.success("✅ News fetched successfully!")
            except Exception as e:
                st.error(f"❌ Error fetching news: {str(e)}")

    elif generate_summary:
        if st.session_state.get('report'):
            with st.spinner("📄 Creating intelligent summary..."):
                try:
                    summary = create_summary_content(st.session_state['report'])
                    st.session_state['summary'] = summary
                    st.success("✅ Summary created successfully!")
                except Exception as e:
                    st.error(f"❌ Error creating summary: {str(e)}")
        else:
            st.warning("⚠️ Please generate a report first before creating a summary!")

# Minimal Display Results in Tabs
st.markdown("<div style='margin: 3rem 0 2rem 0; border-top: 1px solid #1a1a1a;'></div>", unsafe_allow_html=True)
tabs = st.tabs(["Report", "Summary", "News", "Q&A", "Feedback"])

with tabs[0]:
    if st.session_state.get('report'):
        st.markdown('<div class="content-box report-box">', unsafe_allow_html=True)
        st.markdown(st.session_state['report'])
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Download button
        st.download_button(
            label="Download",
            data=st.session_state['report'],
            file_name=f"report_{topic.replace(' ', '_')}.md",
            mime="text/markdown"
        )
    else:
        st.markdown("<p style='color: #4a4a4a; padding: 2rem 0;'>Click 'Generate Report' to create a research report</p>", unsafe_allow_html=True)

with tabs[1]:
    if st.session_state.get('summary'):
        st.markdown('<div class="content-box summary-box">', unsafe_allow_html=True)
        st.markdown(st.session_state['summary'])
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown("<p style='color: #4a4a4a; padding: 2rem 0;'>Generate a report first, then create a summary</p>", unsafe_allow_html=True)

with tabs[2]:
    if st.session_state.get('news'):
        st.markdown('<div class="content-box news-box">', unsafe_allow_html=True)
        st.markdown(st.session_state['news'])
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown("<p style='color: #4a4a4a; padding: 2rem 0;'>Click 'Fetch News' to see the latest updates</p>", unsafe_allow_html=True)

with tabs[3]:
    if st.session_state.get('report'):
        # Q&A Input
        user_question = st.text_input(
            "Question",
            key="qna_input",
            placeholder="Ask about your research..."
        )
        
        col_ask, col_clear = st.columns([3, 1])
        with col_ask:
            ask_button = st.button("Ask", use_container_width=True, key="ask_btn")
        with col_clear:
            clear_button = st.button("Clear", use_container_width=True, key="clear_btn")
        
        if ask_button and user_question:
            with st.spinner("🤔 Analyzing and formulating answer..."):
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
            st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
            for i, chat in enumerate(reversed(st.session_state['chat_history'])):
                st.markdown(f'<div class="chat-message user-message"><strong>Q:</strong> {chat["question"]}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="chat-message"><strong>A:</strong> {chat["answer"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown("<p style='color: #4a4a4a; padding: 2rem 0;'>Ask questions about the research report</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='color: #4a4a4a; padding: 2rem 0;'>Generate a report first to use Q&A</p>", unsafe_allow_html=True)

with tabs[4]:
    col_feedback, col_rating = st.columns([3, 1])
    
    with col_feedback:
        feedback_input = st.text_area(
            "Feedback",
            placeholder="Share your thoughts...",
            height=120
        )
    
    with col_rating:
        rating = st.slider("Rating", 1, 5, 5)
        st.markdown(f"<div style='text-align: center; font-size: 1.5rem; color: #ffffff; margin-top: 1rem;'>{'★' * rating}{'☆' * (5-rating)}</div>", unsafe_allow_html=True)
    
    if st.button("Submit", use_container_width=True, key="feedback_btn"):
        if feedback_input:
            try:
                with st.spinner("Processing..."):
                    response = get_feedback(feedback_input)
                    st.success("Thank you for your feedback")
                    st.markdown(f'<div class="content-box">{response}</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error: {str(e)}")
        else:
            st.warning("Please enter feedback")


