"""
API Key Manager Module
Handles secure storage and retrieval of user's Google Gemini API key
"""
import streamlit as st
import streamlit.components.v1 as components
import os
from dotenv import load_dotenv

load_dotenv()

def inject_local_storage_script():
    """Inject JavaScript to handle localStorage operations"""
    components.html(
        """
        <script>
        // Function to save API key to localStorage
        function saveApiKey(key) {
            try {
                localStorage.setItem('gemini_api_key', key);
                return true;
            } catch (e) {
                console.error('Error saving to localStorage:', e);
                return false;
            }
        }
        
        // Function to get API key from localStorage
        function getApiKey() {
            try {
                return localStorage.getItem('gemini_api_key') || '';
            } catch (e) {
                console.error('Error reading from localStorage:', e);
                return '';
            }
        }
        
        // Function to remove API key from localStorage
        function removeApiKey() {
            try {
                localStorage.removeItem('gemini_api_key');
                return true;
            } catch (e) {
                console.error('Error removing from localStorage:', e);
                return false;
            }
        }
        
        // Send current key to Streamlit on load
        window.addEventListener('load', function() {
            const key = getApiKey();
            window.parent.postMessage({
                type: 'streamlit:setComponentValue',
                key: 'api_key_from_storage',
                value: key
            }, '*');
        });
        
        // Listen for messages from Streamlit
        window.addEventListener('message', function(event) {
            if (event.data.type === 'save_key') {
                const success = saveApiKey(event.data.key);
                window.parent.postMessage({
                    type: 'streamlit:setComponentValue',
                    key: 'save_result',
                    value: success
                }, '*');
            } else if (event.data.type === 'remove_key') {
                const success = removeApiKey();
                window.parent.postMessage({
                    type: 'streamlit:setComponentValue',
                    key: 'remove_result',
                    value: success
                }, '*');
            } else if (event.data.type === 'get_key') {
                const key = getApiKey();
                window.parent.postMessage({
                    type: 'streamlit:setComponentValue',
                    key: 'api_key_from_storage',
                    value: key
                }, '*');
            }
        });
        </script>
        """,
        height=0,
    )

def validate_api_key(key):
    """
    Validate Google Gemini API key format
    
    Args:
        key (str): API key to validate
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not key:
        return False, "API key cannot be empty"
    
    if not key.startswith("AIza"):
        return False, "Invalid API key format. Google API keys should start with 'AIza'"
    
    if len(key) < 30:
        return False, "API key seems too short. Please check your key"
    
    return True, ""

def get_active_api_key():
    """
    Get the active API key from session state (user's own key only)
    
    Returns:
        str: Active API key or None
    """
    # Check session state (set from localStorage)
    if 'user_api_key' in st.session_state and st.session_state['user_api_key']:
        return st.session_state['user_api_key']
    
    return None

def render_api_key_settings():
    """
    Render the API Key Settings UI component - Compact Minimal Design
    Returns the active API key if available
    """
    # Compact Header Card
    st.markdown("""
    <div style='background: #0f0f0f; 
                padding: 1.2rem 1.3rem; border-radius: 14px; 
                border: 1px solid #1a1a1a; margin-bottom: 1.2rem;'>
        <div style='display: flex; align-items: center; margin-bottom: 0.6rem;'>
            <div style='background: #1a1a1a;
                        padding: 0.55rem; border-radius: 10px; margin-right: 0.85rem;'>
                <span style='font-size: 1.3rem;'>🔑</span>
            </div>
            <h3 style='color: #ffffff; font-size: 1rem; margin: 0; 
                       font-weight: 400; letter-spacing: 0.2px;'>
                API Key Settings
            </h3>
        </div>
        <p style='color: #5a5a5a; font-size: 0.8rem; margin: 0; 
                  display: flex; align-items: center; gap: 0.4rem; padding-left: 0.2rem;'>
            <span style='font-size: 0.9rem;'>🔒</span> Stored locally in your browser
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize session state
    if 'user_api_key' not in st.session_state:
        st.session_state['user_api_key'] = None
    if 'show_key_input' not in st.session_state:
        st.session_state['show_key_input'] = False
    
    # Get current active key
    active_key = get_active_api_key()
    
    # Display current status - Compact Green Card
    if active_key:
        masked_key = f"{active_key[:8]}...{active_key[-4:]}"
        
        st.markdown(f"""
        <div style='background: #0a1a0a; 
                    padding: 1rem 1.1rem; border-radius: 14px; 
                    border-left: 3px solid #2ecc71; 
                    border: 1px solid #1a2a1a;
                    margin-bottom: 0.9rem;'>
            <div style='display: flex; align-items: center; margin-bottom: 0.7rem;'>
                <span style='color: #2ecc71; font-size: 1.1rem; margin-right: 0.5rem;'>✓</span>
                <span style='color: #ffffff; font-size: 0.9rem; font-weight: 400;'>Active</span>
            </div>
            <div style='color: #6a6a6a; font-size: 0.8rem; font-family: "Courier New", monospace;
                        background: #000000; padding: 0.65rem 0.85rem; border-radius: 8px;
                        border: 1px solid #1a1a1a;'>
                {masked_key}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Compact Change Key Button
        st.markdown("""
        <div style='margin-bottom: 0.8rem;'></div>
        """, unsafe_allow_html=True)
        
        if st.button("🔄 Change Key", use_container_width=True, key="change_key_btn"):
            st.session_state['show_key_input'] = True
            st.rerun()
    else:
        st.markdown("""
        <div style='background: #1a0f0a; 
                    padding: 0.9rem 1.1rem; border-radius: 14px; 
                    border-left: 3px solid #e67e22;
                    border: 1px solid #2a1a1a;
                    margin-bottom: 0.9rem;'>
            <div style='display: flex; align-items: center;'>
                <span style='color: #e67e22; font-size: 1.1rem; margin-right: 0.5rem;'>⚠</span>
                <span style='color: #ffffff; font-size: 0.9rem; font-weight: 400;'>No API key configured</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.session_state['show_key_input'] = True
    
    # Show input form if needed - Compact Design
    if st.session_state.get('show_key_input') or not active_key:
        with st.form("api_key_form"):
            st.markdown("""
            <p style='color: #6a6a6a; font-size: 0.8rem; margin-bottom: 0.7rem; font-weight: 300;'>
                Enter your API key below:
            </p>
            """, unsafe_allow_html=True)
            
            new_key = st.text_input(
                "Google Gemini API Key",
                type="password",
                placeholder="AIza...",
                help="Get your key at https://makersuite.google.com/app/apikey",
                label_visibility="collapsed"
            )
            
            st.markdown("<div style='margin: 0.8rem 0;'></div>", unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                save_btn = st.form_submit_button("💾 Save", use_container_width=True)
            with col2:
                remove_btn = st.form_submit_button("🗑️ Remove", use_container_width=True)
            
            cancel_btn = st.form_submit_button("❌ Cancel", use_container_width=True)
            
            if save_btn:
                is_valid, error_msg = validate_api_key(new_key)
                if is_valid:
                    st.session_state['user_api_key'] = new_key
                    st.session_state['show_key_input'] = False
                    
                    # Save to localStorage via JavaScript
                    components.html(
                        f"""
                        <script>
                        localStorage.setItem('gemini_api_key', '{new_key}');
                        window.parent.postMessage({{
                            type: 'streamlit:setComponentValue',
                            key: 'key_saved',
                            value: true
                        }}, '*');
                        </script>
                        """,
                        height=0,
                    )
                    
                    st.success("✅ API key saved successfully!")
                    st.rerun()
                else:
                    st.error(f"❌ {error_msg}")
            
            if remove_btn:
                st.session_state['user_api_key'] = None
                st.session_state['show_key_input'] = False
                
                # Remove from localStorage via JavaScript
                components.html(
                    """
                    <script>
                    localStorage.removeItem('gemini_api_key');
                    window.parent.postMessage({
                        type: 'streamlit:setComponentValue',
                        key: 'key_removed',
                        value: true
                    }, '*');
                    </script>
                    """,
                    height=0,
                )
                
                st.success("✅ API key removed successfully!")
                st.rerun()
            
            if cancel_btn:
                st.session_state['show_key_input'] = False
                st.rerun()
    
    # Load key from localStorage on page load
    if 'key_loaded_from_storage' not in st.session_state:
        components.html(
            """
            <script>
            const storedKey = localStorage.getItem('gemini_api_key');
            if (storedKey) {
                window.parent.postMessage({
                    type: 'streamlit:setComponentValue',
                    key: 'stored_api_key',
                    value: storedKey
                }, '*');
            }
            </script>
            """,
            height=0,
        )
        st.session_state['key_loaded_from_storage'] = True
    
    return active_key

def initialize_api_key_from_storage():
    """
    Initialize API key from localStorage on app startup
    This should be called early in the app
    """
    if 'api_key_initialized' not in st.session_state:
        # Try to get key from query params (set by JavaScript)
        query_params = st.query_params
        if 'stored_key' in query_params:
            stored_key = query_params['stored_key']
            if stored_key:
                st.session_state['user_api_key'] = stored_key
        
        st.session_state['api_key_initialized'] = True
