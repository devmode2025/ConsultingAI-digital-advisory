"""ConsultingAI Digital Advisory Firm - Streamlit Frontend

Professional consulting interface demonstrating advanced human-AI collaboration
through Microsoft AutoGen Society of Mind framework.
"""

import streamlit as st
import sys
from pathlib import Path
from datetime import datetime
import json

# Add src to path for backend integration
sys.path.append(str(Path(__file__) / "src"))
sys.path.append(str(Path(__file__) / "frontend"))

# Import spinner component
from frontend.components.consulting_spinner import show_consulting_spinner

# Configure page
st.set_page_config(
    page_title="ConsultingAI Digital Advisory Firm",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for consulting firm theme
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: #f8fafc;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #3b82f6;
        margin: 0.5rem 0;
    }
    .status-active {
        color: #10b981;
        font-weight: bold;
    }
    .status-pending {
        color: #f59e0b;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

def main():
    """Main Streamlit application"""
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🏢 ConsultingAI Digital Advisory Firm</h1>
        <h3>Advanced Human-AI Collaboration Platform</h3>
        <p>Powered by Microsoft AutoGen Society of Mind Framework</p>
        <p style="font-size: 0.9em; opacity: 0.9;">🤖 Enhanced with Ollama Local LLM Integration</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar navigation
    with st.sidebar:
        # Replace the broken placeholder image with a professional text logo
        st.markdown("""
        <div style="
            background: linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%);
            color: white;
            padding: 1.5rem;
            text-align: center;
            border-radius: 10px;
            margin-bottom: 1rem;
        ">
            <h2 style="margin: 0; font-size: 1.5rem;">🏢 ConsultingAI</h2>
            <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; opacity: 0.9;">Digital Advisory Firm</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown("### 🎯 System Status")
        st.markdown('<p class="status-active">● AutoGen Framework: Active</p>', unsafe_allow_html=True)
        st.markdown('<p class="status-active">● Chief Engagement Manager: Ready</p>', unsafe_allow_html=True)
        st.markdown('<p class="status-active">● Multi-Agent Teams: Operational</p>', unsafe_allow_html=True)
        st.markdown('<p class="status-active">● Ollama LLM: Integrated</p>', unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("### 📊 Quick Metrics")
        st.metric("Active Engagements", "3", "↑ 1")
        st.metric("Decisions Processed", "47", "↑ 12")
        st.metric("Human Interventions", "8", "↑ 2")
    
    # Main content area
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("### 🚀 Welcome to ConsultingAI")
        st.markdown("""
        This platform demonstrates sophisticated **Human-AI collaboration** through:
        
        - **🤖 Multi-Agent Coordination** - Specialized AI agents working in teams
        - **⚡ Three-Tier Escalation** - Intelligent decision routing system  
        - **👥 Dynamic Expertise** - Human expert persona switching
        - **🏢 Professional Workflow** - Real consulting firm patterns
        - **🔧 Ollama LLM Integration** - Local AI processing with privacy focus
        """)
        
        st.markdown("---")
        
        # Quick action buttons
        st.markdown("### 🎯 Quick Actions")
        
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("🏢 Start Client Engagement", use_container_width=True):
                show_consulting_spinner(2.0, "🏢 Preparing client engagement interface...")
                st.switch_page("pages/01_🏢_Client_Engagement.py")
                
            if st.button("⚡ View Escalation System", use_container_width=True):
                show_consulting_spinner(1.5, "⚡ Loading escalation system dashboard...")
                st.switch_page("pages/03_⚡_Escalation_System.py")
        
        with col_b:
            if st.button("🤖 Agent Coordination", use_container_width=True):
                show_consulting_spinner(1.8, "🤖 Initializing agent coordination...")
                st.switch_page("pages/02_🤖_Agent_Coordination.py")
                
            if st.button("📊 Analytics Dashboard", use_container_width=True):
                show_consulting_spinner(1.6, "📊 Loading analytics dashboard...")
                st.switch_page("pages/05_📊_Analytics_Dashboard.py")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #6b7280; padding: 1rem;">
        <p>ConsultingAI Digital Advisory Firm | Advanced AI Engineering Assignment</p>
        <p>Demonstrating Microsoft AutoGen Society of Mind Framework</p>
        <p style="font-size: 0.85em; opacity: 0.8;">🤖 Powered by Ollama Local LLM | 🔒 Privacy-First AI Processing</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
