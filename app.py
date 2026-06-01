import streamlit as st
from monitor import check_url_content
import time
import pandas as pd

st.set_page_config(page_title="Monitor App", page_icon="🟢", layout="centered")

# Custom CSS for modern look
st.markdown("""
<style>
    div[data-testid="stSidebar"] {
        padding-top: 2rem;
    }
    .main .block-container {
        padding-top: 2rem;
        max-width: 800px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 50px;
        font-weight: bold;
        font-size: 16px;
    }
    .metric-card {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #333;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #00E676;
    }
</style>
""", unsafe_allow_html=True)

st.title("🟢 Content Monitor")
st.markdown("Ensure your critical website content is online and correctly rendered.", unsafe_allow_html=True)

st.divider()

# Input Section (Mobile Friendly Layout)
st.subheader("Configuration")
url = st.text_input("Article URL", placeholder="https://yourwebsite.com/article-1", help="The full web address of the page you want to check.")
target_text = st.text_input("Target Text to Verify", placeholder="e.g., 'Welcome to my blog'", help="Specific text that MUST exist on the page to verify it's not a 404 or empty template.")

col1, col2 = st.columns(2)
with col1:
    visits = st.number_input("Number of Visits", min_value=1, max_value=100, value=3)
with col2:
    gap_seconds = st.number_input("Gap (seconds)", min_value=1, max_value=3600, value=5)

st.write("")
start_button = st.button("🚀 Start Monitoring", type="primary")

if start_button:
    if not url or not target_text:
        st.warning("⚠️ Please provide both a URL and the Target Text to verify.")
    else:
        st.divider()
        st.subheader("Live Status")
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Placeholder for logs
        log_container = st.container()
        
        results = []
        success_count = 0
        
        with log_container:
            for i in range(visits):
                status_text.markdown(f"**Visit {i+1} of {visits}** in progress...")
                
                success, message = check_url_content(url, target_text)
                results.append({"Visit": i+1, "Status": "✅ Online" if success else "❌ Missing", "Details": message})
                
                if success:
                    success_count += 1
                    st.success(f"Visit {i+1}: Verified successfully.")
                else:
                    st.error(f"Visit {i+1}: Failed. {message}")
                
                progress_bar.progress((i + 1) / visits)
                
                if i < visits - 1:
                    time.sleep(gap_seconds)
                    
        status_text.markdown("**Monitoring Complete!**")
        st.divider()
        
        st.subheader("Summary")
        sc1, sc2, sc3 = st.columns(3)
        sc1.markdown(f'<div class="metric-card">Total Visits<br><span class="metric-value">{visits}</span></div>', unsafe_allow_html=True)
        sc2.markdown(f'<div class="metric-card">Success<br><span class="metric-value">{success_count}</span></div>', unsafe_allow_html=True)
        sc3.markdown(f'<div class="metric-card">Failed<br><span class="metric-value" style="color: #FF5252;">{visits - success_count}</span></div>', unsafe_allow_html=True)
        
        st.write("")
        st.dataframe(pd.DataFrame(results), use_container_width=True)
