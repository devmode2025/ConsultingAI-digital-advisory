"""Escalation System Visualization - Three-tier decision routing display"""

import streamlit as st
import sys
from pathlib import Path
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="Escalation System - ConsultingAI",
    page_icon="⚡", 
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .escalation-header {
        background: linear-gradient(90deg, #dc2626 0%, #ef4444 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 2rem;
    }
    .tier-card {
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        border: 2px solid;
    }
    .tier-1 {
        background: #f0fdf4;
        border-color: #10b981;
    }
    .tier-2 {
        background: #fffbeb;
        border-color: #f59e0b;
    }
    .tier-3 {
        background: #fef2f2;
        border-color: #ef4444;
    }
</style>
""", unsafe_allow_html=True)

def create_escalation_flow():
    """Create escalation flow diagram"""
    fig = go.Figure()
    
    # Add nodes
    fig.add_trace(go.Scatter(
        x=[1, 2, 3],
        y=[1, 1, 1],
        mode='markers+text',
        marker=dict(size=[80, 100, 120], color=['#10b981', '#f59e0b', '#ef4444']),
        text=['Agent-Only<br>Tier', 'Junior<br>Specialist', 'Senior<br>Partner'],
        textposition="middle center",
        textfont=dict(size=12, color='white'),
        name="Escalation Tiers"
    ))
    
    # Add arrows
    fig.add_annotation(x=1.5, y=1, ax=1.3, ay=1, arrowhead=2, arrowsize=1, arrowwidth=2, arrowcolor='#6b7280')
    fig.add_annotation(x=2.5, y=1, ax=2.3, ay=1, arrowhead=2, arrowsize=1, arrowwidth=2, arrowcolor='#6b7280')
    
    fig.update_layout(
        title="Three-Tier Escalation System",
        showlegend=False,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        height=300,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    
    return fig

def create_confidence_distribution():
    """Create confidence score distribution chart"""
    data = pd.DataFrame({
        'Confidence Range': ['90-100%', '80-90%', '70-80%', '60-70%', '<60%'],
        'Decisions': [45, 28, 15, 8, 4],
        'Tier': ['Agent-Only', 'Agent-Only', 'Junior Specialist', 'Junior Specialist', 'Senior Partner']
    })
    
    fig = px.bar(data, x='Confidence Range', y='Decisions', color='Tier',
                 color_discrete_map={
                     'Agent-Only': '#10b981',
                     'Junior Specialist': '#f59e0b', 
                     'Senior Partner': '#ef4444'
                 })
    
    fig.update_layout(
        title="Decision Distribution by Confidence Level",
        height=400
    )
    
    return fig

def main():
    st.markdown("""
    <div class="escalation-header">
        <h1>⚡ Escalation System Dashboard</h1>
        <p>Interactive visualization of three-tier decision routing and escalation patterns</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation
    if st.button("← Back to Home"):
        st.switch_page("streamlit_app.py")
    
    st.markdown("---")
    
    # Escalation flow visualization
    st.markdown("### 🔄 Escalation Flow")
    st.plotly_chart(create_escalation_flow(), use_container_width=True)
    
    # Tier descriptions
    st.markdown("### 📋 Escalation Tier Details")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="tier-card tier-1">
            <h4>🤖 Tier 1: Agent-Only</h4>
            <p><strong>Confidence:</strong> > 90%</p>
            <p><strong>Decision Type:</strong> Standard operational</p>
            <p><strong>Processing:</strong> Fully automated</p>
            <p><strong>Examples:</strong></p>
            <ul>
                <li>Code quality checks</li>
                <li>Standard recommendations</li>
                <li>Routine analysis</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="tier-card tier-2">
            <h4>👨‍💼 Tier 2: Junior Specialist</h4>
            <p><strong>Confidence:</strong> 70-90%</p>
            <p><strong>Decision Type:</strong> Complex technical</p>
            <p><strong>Processing:</strong> Human review required</p>
            <p><strong>Examples:</strong></p>
            <ul>
                <li>Architecture decisions</li>
                <li>Implementation strategies</li>
                <li>Risk assessments</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="tier-card tier-3">
            <h4>👨‍💼 Tier 3: Senior Partner</h4>
            <p><strong>Confidence:</strong> < 70%</p>
            <p><strong>Decision Type:</strong> Strategic/Critical</p>
            <p><strong>Processing:</strong> Executive oversight</p>
            <p><strong>Examples:</strong></p>
            <ul>
                <li>Strategic direction</li>
                <li>Major investments</li>
                <li>Crisis management</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Confidence distribution
    st.markdown("---")
    st.markdown("### 📊 Decision Confidence Distribution")
    st.plotly_chart(create_confidence_distribution(), use_container_width=True)
    
    # Live escalation simulation
    st.markdown("---")
    st.markdown("### 🎯 Live Escalation Simulation")
    
    if st.button("🚀 Simulate Decision Escalation", type="primary"):
        # Simulate decision process
        with st.spinner("Processing decision..."):
            import time
            time.sleep(1)
        
        # Random confidence score
        import random
        confidence = random.randint(60, 95)
        
        if confidence >= 90:
            tier = "Agent-Only"
            color = "success"
            action = "Automatically processed"
        elif confidence >= 70:
            tier = "Junior Specialist"
            color = "warning" 
            action = "Escalated for human review"
        else:
            tier = "Senior Partner"
            color = "error"
            action = "Escalated to executive level"
        
        st.markdown(f"### Decision Result")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Confidence Score", f"{confidence}%")
        with col2:
            st.metric("Escalation Tier", tier)
        with col3:
            st.metric("Processing Time", "1.2s")
        
        if color == "success":
            st.success(f"✅ {action} - {tier}")
        elif color == "warning":
            st.warning(f"⚠️ {action} - {tier}")
        else:
            st.error(f"🚨 {action} - {tier}")
    
    # Action buttons
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🤖 Agent Coordination", use_container_width=True):
            st.switch_page("pages/02_🤖_Agent_Coordination.py")
    
    with col2:
        if st.button("👥 Expert Personas", use_container_width=True):
            st.switch_page("pages/04_👥_Expert_Personas.py")
    
    with col3:
        if st.button("📊 Analytics Dashboard", use_container_width=True):
            st.switch_page("pages/05_📊_Analytics_Dashboard.py")

if __name__ == "__main__":
    main()