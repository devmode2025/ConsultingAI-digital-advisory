"""Analytics Dashboard - Performance metrics and system insights"""

import streamlit as st
import sys
from pathlib import Path
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

st.set_page_config(
    page_title="Analytics Dashboard - ConsultingAI",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .analytics-header {
        background: linear-gradient(90deg, #7c2d12 0%, #ea580c 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 2rem;
    }
    .metric-container {
        background: #fff7ed;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #fed7aa;
        text-align: center;
    }
    .insight-card {
        background: #f0f9ff;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #0891b2;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

def generate_sample_data():
    """Generate sample analytics data"""
    dates = pd.date_range(start='2024-01-01', end='2024-01-31', freq='D')
    
    # Decision volume data
    decisions_data = pd.DataFrame({
        'Date': dates,
        'Agent_Only': np.random.poisson(15, len(dates)),
        'Junior_Specialist': np.random.poisson(8, len(dates)),
        'Senior_Partner': np.random.poisson(3, len(dates))
    })
    
    # Performance metrics
    performance_data = pd.DataFrame({
        'Metric': ['Decision Accuracy', 'Response Time', 'User Satisfaction', 'System Uptime'],
        'Current': [94, 1.2, 4.8, 99.9],
        'Target': [95, 1.0, 4.5, 99.5],
        'Previous': [92, 1.5, 4.6, 99.7]
    })
    
    return decisions_data, performance_data

def create_decision_volume_chart(data):
    """Create decision volume over time chart"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data['Date'], y=data['Agent_Only'],
        mode='lines+markers', name='Agent-Only',
        line=dict(color='#10b981', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=data['Date'], y=data['Junior_Specialist'],
        mode='lines+markers', name='Junior Specialist',
        line=dict(color='#f59e0b', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=data['Date'], y=data['Senior_Partner'],
        mode='lines+markers', name='Senior Partner',
        line=dict(color='#ef4444', width=3)
    ))
    
    fig.update_layout(
        title='Decision Volume by Escalation Tier',
        xaxis_title='Date',
        yaxis_title='Number of Decisions',
        height=400,
        hovermode='x unified'
    )
    
    return fig

def create_performance_radar(data):
    """Create performance radar chart"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=data['Current'],
        theta=data['Metric'],
        fill='toself',
        name='Current Performance',
        line_color='#0891b2'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=data['Target'],
        theta=data['Metric'],
        fill='toself',
        name='Target Performance',
        line_color='#10b981'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=True,
        title="Performance Metrics Radar",
        height=400
    )
    
    return fig

def main():
    st.markdown("""
    <div class="analytics-header">
        <h1>📊 Analytics Dashboard</h1>
        <p>Comprehensive performance metrics and system insights</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation
    if st.button("← Back to Home"):
        st.switch_page("streamlit_app.py")
    
    st.markdown("---")
    
    # Generate sample data
    decisions_data, performance_data = generate_sample_data()
    
    # Key metrics overview
    st.markdown("### 🎯 Key Performance Indicators")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-container">
            <h3>726</h3>
            <p>Total Decisions</p>
            <small>↑ 15% vs last month</small>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-container">
            <h3>94%</h3>
            <p>Decision Accuracy</p>
            <small>↑ 2% vs last month</small>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-container">
            <h3>1.2s</h3>
            <p>Avg Response Time</p>
            <small>↓ 0.3s vs last month</small>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-container">
            <h3>4.8/5</h3>
            <p>User Satisfaction</p>
            <small>↑ 0.2 vs last month</small>
        </div>
        """, unsafe_allow_html=True)
    
    # Charts section
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(create_decision_volume_chart(decisions_data), use_container_width=True)
    
    with col2:
        st.plotly_chart(create_performance_radar(performance_data), use_container_width=True)
    
    # Escalation analysis
    st.markdown("---")
    st.markdown("### ⚡ Escalation Analysis")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Escalation distribution pie chart
        escalation_data = pd.DataFrame({
            'Tier': ['Agent-Only', 'Junior Specialist', 'Senior Partner'],
            'Count': [465, 186, 75],
            'Percentage': [64, 26, 10]
        })
        
        fig = px.pie(escalation_data, values='Count', names='Tier',
                     color_discrete_map={
                         'Agent-Only': '#10b981',
                         'Junior Specialist': '#f59e0b',
                         'Senior Partner': '#ef4444'
                     })
        fig.update_layout(title="Decision Distribution by Escalation Tier")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("**Escalation Insights:**")
        st.markdown("""
        <div class="insight-card">
            <h4>🎯 Optimization Opportunity</h4>
            <p>64% of decisions handled automatically, indicating efficient agent performance</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="insight-card">
            <h4>⚠️ Review Required</h4>
            <p>26% escalated to specialists - within expected range for complex decisions</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="insight-card">
            <h4>🚨 Executive Attention</h4>
            <p>10% require senior oversight - strategic decisions handled appropriately</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Agent performance
    st.markdown("---")
    st.markdown("### 🤖 Agent Performance Analysis")
    
    agent_performance = pd.DataFrame({
        'Agent': ['Code Reviewer', 'System Architect', 'Business Analyst', 'Chief Manager'],
        'Decisions': [245, 198, 167, 116],
        'Accuracy': [96, 93, 91, 98],
        'Avg_Confidence': [87, 84, 82, 92]
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.bar(agent_performance, x='Agent', y='Decisions',
                     title='Decisions Processed by Agent')
        fig.update_traces(marker_color='#0891b2')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.scatter(agent_performance, x='Accuracy', y='Avg_Confidence',
                        size='Decisions', hover_name='Agent',
                        title='Agent Accuracy vs Confidence')
        fig.update_traces(marker_color='#ea580c')
        st.plotly_chart(fig, use_container_width=True)
    
    # System health
    st.markdown("---")
    st.markdown("### 🔧 System Health & Reliability")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Uptime Metrics:**")
        st.metric("System Uptime", "99.9%", "↑ 0.2%")
        st.metric("API Response Rate", "99.8%", "→ 0%")
        st.metric("Error Rate", "0.1%", "↓ 0.05%")
    
    with col2:
        st.markdown("**Performance Trends:**")
        st.metric("Avg Processing Time", "1.2s", "↓ 0.3s")
        st.metric("Memory Usage", "78%", "↓ 5%")
        st.metric("CPU Utilization", "45%", "↓ 8%")
    
    with col3:
        st.markdown("**Quality Metrics:**")
        st.metric("Decision Quality Score", "4.8/5", "↑ 0.2")
        st.metric("User Feedback Score", "4.7/5", "↑ 0.1")
        st.metric("System Reliability", "99.5%", "↑ 0.3%")
    
    # Recommendations
    st.markdown("---")
    st.markdown("### 💡 AI-Powered Recommendations")
    
    recommendations = [
        {
            "priority": "High",
            "title": "Optimize Agent-Only Threshold",
            "description": "Consider raising confidence threshold from 90% to 92% to reduce false positives",
            "impact": "Potential 5% improvement in decision accuracy"
        },
        {
            "priority": "Medium", 
            "title": "Enhance Business Analyst Training",
            "description": "Business Analyst shows lower confidence scores - additional training recommended",
            "impact": "Expected 3% improvement in stakeholder alignment"
        },
        {
            "priority": "Low",
            "title": "Expand Expert Persona Library",
            "description": "Add specialized personas for emerging technology domains",
            "impact": "Broader expertise coverage for complex decisions"
        }
    ]
    
    for rec in recommendations:
        priority_color = {"High": "#ef4444", "Medium": "#f59e0b", "Low": "#10b981"}[rec["priority"]]
        
        st.markdown(f"""
        <div class="insight-card" style="border-left-color: {priority_color}">
            <h4>{rec["title"]} <span style="color: {priority_color}">({rec["priority"]} Priority)</span></h4>
            <p>{rec["description"]}</p>
            <small><strong>Expected Impact:</strong> {rec["impact"]}</small>
        </div>
        """, unsafe_allow_html=True)
    
    # Action buttons
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🏢 Client Engagement", use_container_width=True):
            st.switch_page("pages/01_🏢_Client_Engagement.py")
    
    with col2:
        if st.button("🤖 Agent Coordination", use_container_width=True):
            st.switch_page("pages/02_🤖_Agent_Coordination.py")
    
    with col3:
        if st.button("⚡ Escalation System", use_container_width=True):
            st.switch_page("pages/03_⚡_Escalation_System.py")

if __name__ == "__main__":
    main()