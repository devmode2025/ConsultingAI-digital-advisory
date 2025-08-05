"""Streamlit Helper Functions - Utility functions for Streamlit components"""

import streamlit as st
from typing import Dict, Any, Optional, List
import plotly.graph_objects as go
import plotly.express as px

def create_metric_card(
    title: str, 
    value: str, 
    delta: Optional[str] = None,
    delta_color: str = "normal"
) -> None:
    """Create a styled metric card
    
    Args:
        title: Metric title
        value: Metric value
        delta: Change indicator
        delta_color: Color for delta (normal, inverse, off)
    """
    st.metric(
        label=title,
        value=value,
        delta=delta,
        delta_color=delta_color
    )

def create_status_badge(status: str, text: str = None) -> str:
    """Create a colored status badge
    
    Args:
        status: Status type (active, busy, idle, error)
        text: Optional custom text
        
    Returns:
        HTML string for status badge
    """
    status_colors = {
        "active": "#10b981",
        "busy": "#f59e0b", 
        "idle": "#6b7280",
        "error": "#ef4444",
        "offline": "#374151"
    }
    
    color = status_colors.get(status.lower(), "#6b7280")
    display_text = text or status.title()
    
    return f"""
    <span style="
        background-color: {color};
        color: white;
        padding: 0.25rem 0.5rem;
        border-radius: 0.375rem;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
    ">
        {display_text}
    </span>
    """

def create_progress_ring(percentage: float, size: int = 100) -> str:
    """Create a circular progress ring
    
    Args:
        percentage: Progress percentage (0-100)
        size: Ring size in pixels
        
    Returns:
        HTML/CSS for progress ring
    """
    circumference = 2 * 3.14159 * 45  # radius = 45
    stroke_dasharray = circumference
    stroke_dashoffset = circumference - (percentage / 100) * circumference
    
    return f"""
    <div style="display: flex; justify-content: center; align-items: center;">
        <svg width="{size}" height="{size}" style="transform: rotate(-90deg);">
            <circle
                cx="50" cy="50" r="45"
                fill="none"
                stroke="#e5e7eb"
                stroke-width="8"
            />
            <circle
                cx="50" cy="50" r="45"
                fill="none"
                stroke="#3b82f6"
                stroke-width="8"
                stroke-dasharray="{stroke_dasharray}"
                stroke-dashoffset="{stroke_dashoffset}"
                stroke-linecap="round"
            />
        </svg>
        <div style="position: absolute; font-weight: bold; font-size: 1.2rem;">
            {percentage:.1f}%
        </div>
    </div>
    """

def create_info_card(title: str, content: str, icon: str = "ℹ️") -> None:
    """Create an information card
    
    Args:
        title: Card title
        content: Card content
        icon: Icon for the card
    """
    st.markdown(f"""
    <div style="
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    ">
        <h4 style="margin: 0 0 0.5rem 0; color: #1f2937;">
            {icon} {title}
        </h4>
        <p style="margin: 0; color: #6b7280;">
            {content}
        </p>
    </div>
    """, unsafe_allow_html=True)

def create_alert(message: str, alert_type: str = "info") -> None:
    """Create a styled alert
    
    Args:
        message: Alert message
        alert_type: Type of alert (info, success, warning, error)
    """
    alert_styles = {
        "info": {"bg": "#dbeafe", "border": "#3b82f6", "text": "#1e40af"},
        "success": {"bg": "#d1fae5", "border": "#10b981", "text": "#065f46"},
        "warning": {"bg": "#fef3c7", "border": "#f59e0b", "text": "#92400e"},
        "error": {"bg": "#fee2e2", "border": "#ef4444", "text": "#dc2626"}
    }
    
    style = alert_styles.get(alert_type, alert_styles["info"])
    
    st.markdown(f"""
    <div style="
        background: {style['bg']};
        border-left: 4px solid {style['border']};
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0 8px 8px 0;
    ">
        <p style="margin: 0; color: {style['text']}; font-weight: 500;">
            {message}
        </p>
    </div>
    """, unsafe_allow_html=True)

def create_collapsible_section(title: str, content: str, expanded: bool = False) -> None:
    """Create a collapsible section
    
    Args:
        title: Section title
        content: Section content
        expanded: Whether section starts expanded
    """
    with st.expander(title, expanded=expanded):
        st.markdown(content)

def apply_custom_css() -> None:
    """Apply custom CSS styling to the Streamlit app"""
    st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        border: 1px solid #e5e7eb;
    }
    
    .status-active {
        color: #10b981;
        font-weight: 600;
    }
    
    .status-busy {
        color: #f59e0b;
        font-weight: 600;
    }
    
    .status-idle {
        color: #6b7280;
        font-weight: 600;
    }
    
    .consulting-button {
        background: linear-gradient(90deg, #3b82f6 0%, #1e40af 100%);
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 6px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s;
    }
    
    .consulting-button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)