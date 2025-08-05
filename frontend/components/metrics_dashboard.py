"""Metrics Dashboard Component - Real-time performance metrics and analytics"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
import numpy as np

def show_kpi_metrics(metrics: Optional[Dict[str, Any]] = None):
    """Display key performance indicator metrics in cards
    
    Args:
        metrics: Dictionary containing KPI values and trends
    """
    
    # Default demo metrics if none provided
    if metrics is None:
        metrics = {
            "total_decisions": {"value": 726, "change": 15, "trend": "up"},
            "decision_accuracy": {"value": 94, "change": 2, "trend": "up"},
            "avg_response_time": {"value": 1.2, "change": -0.3, "trend": "down"},
            "user_satisfaction": {"value": 4.8, "change": 0.2, "trend": "up"},
            "system_uptime": {"value": 99.9, "change": 0.2, "trend": "up"},
            "escalation_rate": {"value": 36, "change": -3, "trend": "down"}
        }
    
    # Custom CSS for KPI cards
    st.markdown("""
    <style>
    .kpi-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        text-align: center;
        height: 140px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .kpi-value {
        font-size: 2rem;
        font-weight: 700;
        color: #1f2937;
        margin: 0.5rem 0;
    }
    .kpi-label {
        font-size: 0.9rem;
        color: #6b7280;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    .kpi-change {
        font-size: 0.8rem;
        font-weight: 600;
        padding: 0.2rem 0.5rem;
        border-radius: 12px;
    }
    .kpi-change.up {
        color: #065f46;
        background: #d1fae5;
    }
    .kpi-change.down {
        color: #991b1b;
        background: #fee2e2;
    }
    .kpi-change.neutral {
        color: #374151;
        background: #f3f4f6;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Display KPI cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        _render_kpi_card("Total Decisions", metrics["total_decisions"]["value"], 
                        metrics["total_decisions"]["change"], metrics["total_decisions"]["trend"])
        
        _render_kpi_card("Avg Response Time", f"{metrics['avg_response_time']['value']}s", 
                        metrics["avg_response_time"]["change"], metrics["avg_response_time"]["trend"], "s")
    
    with col2:
        _render_kpi_card("Decision Accuracy", f"{metrics['decision_accuracy']['value']}%", 
                        metrics["decision_accuracy"]["change"], metrics["decision_accuracy"]["trend"], "%")
        
        _render_kpi_card("System Uptime", f"{metrics['system_uptime']['value']}%", 
                        metrics["system_uptime"]["change"], metrics["system_uptime"]["trend"], "%")
    
    with col3:
        _render_kpi_card("User Satisfaction", f"{metrics['user_satisfaction']['value']}/5", 
                        metrics["user_satisfaction"]["change"], metrics["user_satisfaction"]["trend"])
        
        _render_kpi_card("Escalation Rate", f"{metrics['escalation_rate']['value']}%", 
                        metrics["escalation_rate"]["change"], metrics["escalation_rate"]["trend"], "%")


def _render_kpi_card(label: str, value: str, change: float, trend: str, unit: str = ""):
    """Render individual KPI card"""
    
    trend_class = "up" if trend == "up" else "down" if trend == "down" else "neutral"
    trend_icon = "↑" if trend == "up" else "↓" if trend == "down" else "→"
    change_text = f"{trend_icon} {abs(change)}{unit}" if change != 0 else "→ 0%"
    
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">{label}</div>
        <div class="kpi-value">{value}</div>
        <div class="kpi-change {trend_class}">{change_text} vs last month</div>
    </div>
    """, unsafe_allow_html=True)


def show_decision_volume_chart(data: Optional[pd.DataFrame] = None):
    """Display decision volume over time chart
    
    Args:
        data: DataFrame with Date and decision volume columns
    """
    
    # Generate demo data if none provided
    if data is None:
        dates = pd.date_range(start='2024-01-01', end='2024-01-31', freq='D')
        data = pd.DataFrame({
            'Date': dates,
            'Agent_Only': np.random.poisson(15, len(dates)),
            'Junior_Specialist': np.random.poisson(8, len(dates)),
            'Senior_Partner': np.random.poisson(3, len(dates))
        })
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data['Date'], y=data['Agent_Only'],
        mode='lines+markers', name='Agent-Only',
        line=dict(color='#10b981', width=3),
        fill='tonexty'
    ))
    
    fig.add_trace(go.Scatter(
        x=data['Date'], y=data['Junior_Specialist'],
        mode='lines+markers', name='Junior Specialist',
        line=dict(color='#f59e0b', width=3),
        fill='tonexty'
    ))
    
    fig.add_trace(go.Scatter(
        x=data['Date'], y=data['Senior_Partner'],
        mode='lines+markers', name='Senior Partner',
        line=dict(color='#ef4444', width=3),
        fill='tonexty'
    ))
    
    fig.update_layout(
        title='Decision Volume by Escalation Tier',
        xaxis_title='Date',
        yaxis_title='Number of Decisions',
        height=400,
        hovermode='x unified',
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    st.plotly_chart(fig, use_container_width=True)


def show_performance_radar_chart(data: Optional[pd.DataFrame] = None):
    """Display performance metrics radar chart
    
    Args:
        data: DataFrame with performance metrics
    """
    
    # Generate demo data if none provided
    if data is None:
        data = pd.DataFrame({
            'Metric': ['Decision Accuracy', 'Response Time', 'User Satisfaction', 'System Uptime', 'Quality Score'],
            'Current': [94, 85, 96, 99, 92],
            'Target': [95, 90, 95, 99.5, 95],
            'Previous': [92, 80, 94, 99.2, 89]
        })
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=data['Current'],
        theta=data['Metric'],
        fill='toself',
        name='Current Performance',
        line_color='#3b82f6',
        fillcolor='rgba(59, 130, 246, 0.1)'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=data['Target'],
        theta=data['Metric'],
        fill='toself',
        name='Target Performance',
        line_color='#10b981',
        fillcolor='rgba(16, 185, 129, 0.1)'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=data['Previous'],
        theta=data['Metric'],
        fill='toself',
        name='Previous Period',
        line_color='#6b7280',
        fillcolor='rgba(107, 114, 128, 0.1)'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                ticksuffix='%'
            )),
        showlegend=True,
        title="Performance Metrics Comparison",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)


def show_escalation_distribution_chart():
    """Display escalation distribution pie chart"""
    
    escalation_data = pd.DataFrame({
        'Tier': ['Agent-Only', 'Junior Specialist', 'Senior Partner'],
        'Count': [465, 186, 75],
        'Percentage': [64, 26, 10]
    })
    
    fig = px.pie(
        escalation_data, 
        values='Count', 
        names='Tier',
        title="Decision Distribution by Escalation Tier",
        color_discrete_map={
            'Agent-Only': '#10b981',
            'Junior Specialist': '#f59e0b',
            'Senior Partner': '#ef4444'
        }
    )
    
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(height=400)
    
    st.plotly_chart(fig, use_container_width=True)


def show_agent_performance_metrics():
    """Display individual agent performance metrics"""
    
    agent_data = pd.DataFrame({
        'Agent': ['Code Reviewer', 'System Architect', 'Business Analyst', 'Chief Manager'],
        'Decisions': [245, 198, 167, 116],
        'Accuracy': [96, 93, 91, 98],
        'Avg_Confidence': [87, 84, 82, 92],
        'Response_Time': [1.1, 1.3, 1.5, 0.9]
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Decisions processed bar chart
        fig = px.bar(
            agent_data, 
            x='Agent', 
            y='Decisions',
            title='Decisions Processed by Agent',
            color='Decisions',
            color_continuous_scale='Blues'
        )
        fig.update_layout(height=350)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Accuracy vs Confidence scatter plot
        fig = px.scatter(
            agent_data, 
            x='Accuracy', 
            y='Avg_Confidence',
            size='Decisions', 
            hover_name='Agent',
            title='Agent Accuracy vs Confidence',
            color='Response_Time',
            color_continuous_scale='RdYlGn_r'
        )
        fig.update_layout(height=350)
        st.plotly_chart(fig, use_container_width=True)


def show_system_health_metrics():
    """Display system health and reliability metrics"""
    
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


def show_real_time_activity_feed():
    """Display real-time activity feed"""
    
    st.markdown("### 📡 Real-Time Activity Feed")
    
    # Simulate real-time activities
    activities = [
        {"time": "2 min ago", "event": "🤖 Agent-Only decision completed", "details": "Code review approved with 94% confidence"},
        {"time": "5 min ago", "event": "👨‍💼 Junior Specialist review", "details": "Architecture proposal escalated for expert review"},
        {"time": "8 min ago", "event": "✅ Client engagement initiated", "details": "New digital transformation project started"},
        {"time": "12 min ago", "event": "📊 Performance metrics updated", "details": "Daily analytics refresh completed"},
        {"time": "15 min ago", "event": "🔄 Multi-agent coordination", "details": "Team collaboration for strategic planning"}
    ]
    
    for activity in activities:
        st.markdown(f"""
        <div style="
            background: #f8fafc;
            border-left: 3px solid #3b82f6;
            padding: 0.8rem;
            margin: 0.5rem 0;
            border-radius: 0 8px 8px 0;
        ">
            <div style="font-size: 0.9rem; font-weight: 600; color: #1f2937;">
                {activity['event']}
            </div>
            <div style="font-size: 0.8rem; color: #6b7280; margin: 0.2rem 0;">
                {activity['details']}
            </div>
            <div style="font-size: 0.7rem; color: #9ca3af;">
                {activity['time']}
            </div>
        </div>
        """, unsafe_allow_html=True)


def show_comprehensive_metrics_dashboard():
    """Display complete metrics dashboard with all components"""
    
    st.markdown("## 📊 Comprehensive Analytics Dashboard")
    
    # KPI Overview
    st.markdown("### 🎯 Key Performance Indicators")
    show_kpi_metrics()
    
    st.markdown("---")
    
    # Charts section
    col1, col2 = st.columns(2)
    
    with col1:
        show_decision_volume_chart()
        show_escalation_distribution_chart()
    
    with col2:
        show_performance_radar_chart()
        show_agent_performance_metrics()
    
    st.markdown("---")
    
    # System health and activity
    col1, col2 = st.columns([2, 1])
    
    with col1:
        show_system_health_metrics()
    
    with col2:
        show_real_time_activity_feed()


def show_custom_metrics_builder():
    """Interactive metrics builder for custom dashboards"""
    
    st.markdown("### 🛠️ Custom Metrics Builder")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Select Metrics to Display:**")
        
        metrics_options = st.multiselect(
            "Choose metrics",
            ["Decision Volume", "Accuracy Trends", "Response Times", 
             "Escalation Patterns", "Agent Performance", "System Health"],
            default=["Decision Volume", "Accuracy Trends"]
        )
        
        time_range = st.selectbox(
            "Time Range",
            ["Last 7 days", "Last 30 days", "Last 90 days", "Last year"]
        )
        
        chart_type = st.selectbox(
            "Chart Type",
            ["Line Chart", "Bar Chart", "Area Chart", "Scatter Plot"]
        )
    
    with col2:
        st.markdown("**Dashboard Preview:**")
        
        if "Decision Volume" in metrics_options:
            st.markdown("📈 Decision Volume Chart")
        if "Accuracy Trends" in metrics_options:
            st.markdown("🎯 Accuracy Trends")
        if "Response Times" in metrics_options:
            st.markdown("⏱️ Response Time Analysis")
        
        if st.button("Generate Custom Dashboard"):
            st.success("Custom dashboard generated! Metrics updated based on your selection.")