"""Agent Coordination Dashboard - Real-time multi-agent collaboration visualization"""

import streamlit as st
import sys
from pathlib import Path
from datetime import datetime
import time
import random

st.set_page_config(
    page_title="Agent Coordination - ConsultingAI", 
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .coordination-header {
        background: linear-gradient(90deg, #7c3aed 0%, #a855f7 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 2rem;
    }
    .agent-card {
        background: #faf5ff;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #d8b4fe;
        margin: 0.5rem 0;
    }
    .active-agent {
        border-left: 4px solid #10b981;
        background: #f0fdf4;
    }
    .thinking-agent {
        border-left: 4px solid #f59e0b;
        background: #fffbeb;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown("""
    <div class="coordination-header">
        <h1>🤖 Agent Coordination Dashboard</h1>
        <p>Real-time visualization of multi-agent collaboration and decision-making</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation
    if st.button("← Back to Home"):
        st.switch_page("streamlit_app.py")
    
    st.markdown("---")
    
    # Real-time coordination display
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🔄 Active Agent Coordination")
        
        # Simulate real-time agent activity
        if 'coordination_active' not in st.session_state:
            st.session_state.coordination_active = False
        
        if st.button("▶️ Start Agent Coordination", type="primary"):
            st.session_state.coordination_active = True
        
        if st.session_state.coordination_active:
            # Agent status display
            agents = [
                {"name": "Code Reviewer Agent", "status": "active", "task": "Analyzing system architecture"},
                {"name": "System Architect Agent", "status": "thinking", "task": "Designing solution framework"},
                {"name": "Business Analyst Agent", "status": "active", "task": "Stakeholder requirement analysis"},
                {"name": "Chief Engagement Manager", "status": "coordinating", "task": "Orchestrating team collaboration"}
            ]
            
            for agent in agents:
                status_class = "active-agent" if agent["status"] == "active" else "thinking-agent"
                status_emoji = "🟢" if agent["status"] == "active" else "🟡" if agent["status"] == "thinking" else "🔵"
                
                st.markdown(f"""
                <div class="agent-card {status_class}">
                    <h4>{status_emoji} {agent["name"]}</h4>
                    <p><strong>Status:</strong> {agent["status"].title()}</p>
                    <p><strong>Current Task:</strong> {agent["task"]}</p>
                </div>
                """, unsafe_allow_html=True)
            
            # Coordination messages
            st.markdown("### 💬 Agent Communication")
            messages = [
                "Code Reviewer: 'System architecture analysis complete. Confidence: 85%'",
                "Chief Manager: 'Escalating to human expert for final validation'",
                "System Architect: 'Proposing microservices architecture approach'",
                "Business Analyst: 'Stakeholder requirements aligned with technical solution'"
            ]
            
            for msg in messages:
                st.text(f"🔸 {msg}")
    
    with col2:
        st.markdown("### 📊 Coordination Metrics")
        
        # Live metrics
        st.metric("Active Agents", "4", "↑ 1")
        st.metric("Decisions Made", "12", "↑ 3")
        st.metric("Escalations", "2", "↑ 1")
        st.metric("Confidence Score", "87%", "↑ 5%")
        
        st.markdown("---")
        
        st.markdown("### 🎯 Current Focus")
        st.info("**Digital Transformation Strategy**\n\nTeam is analyzing client requirements and developing comprehensive solution framework.")
        
        # Team performance
        st.markdown("### 📈 Team Performance")
        st.progress(0.87, "Overall Progress")
        st.progress(0.92, "Code Quality")
        st.progress(0.78, "Stakeholder Alignment")
    
    # Escalation system preview
    st.markdown("---")
    st.markdown("### ⚡ Escalation System Status")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        **🤖 Agent-Only Tier**
        - Confidence > 90%
        - Standard decisions
        - Automated processing
        """)
    
    with col2:
        st.markdown("""
        **👨‍💼 Junior Specialist**
        - Confidence 70-90%
        - Complex decisions
        - Human review required
        """)
    
    with col3:
        st.markdown("""
        **👨‍💼 Senior Partner**
        - Confidence < 70%
        - Strategic decisions
        - Executive oversight
        """)
    
    # Action buttons
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("⚡ View Escalation System", use_container_width=True):
            st.switch_page("pages/03_⚡_Escalation_System.py")
    
    with col2:
        if st.button("👥 Expert Personas", use_container_width=True):
            st.switch_page("pages/04_👥_Expert_Personas.py")
    
    with col3:
        if st.button("📊 Analytics Dashboard", use_container_width=True):
            st.switch_page("pages/05_📊_Analytics_Dashboard.py")

if __name__ == "__main__":
    main()