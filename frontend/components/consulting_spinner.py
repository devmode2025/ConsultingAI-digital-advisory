"""Consulting-themed spinner component for page transitions"""

import streamlit as st
import time
import random

def show_consulting_spinner(duration: float = 2.0, message: str = None):
    """Show consulting-themed spinner with professional animations
    
    Args:
        duration: How long to show spinner (seconds)
        message: Custom message to display
    """
    
    # Random consulting messages
    consulting_messages = [
        "🏢 Assembling expert team...",
        "🤖 Coordinating AI agents...",
        "⚡ Processing escalation logic...",
        "📊 Analyzing business requirements...",
        "🎯 Optimizing solution framework...",
        "👥 Consulting expert personas...",
        "🔄 Synchronizing multi-agent coordination...",
        "💼 Preparing strategic recommendations...",
        "🧠 Applying Society of Mind framework...",
        "⭐ Delivering consulting excellence..."
    ]
    
    display_message = message or random.choice(consulting_messages)
    
    # Custom CSS for consulting spinner
    st.markdown("""
    <style>
    .consulting-spinner-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 3rem;
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        border-radius: 15px;
        margin: 2rem 0;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }
    
    .consulting-spinner {
        width: 60px;
        height: 60px;
        border: 4px solid #e2e8f0;
        border-top: 4px solid #1e3a8a;
        border-radius: 50%;
        animation: consulting-spin 1s linear infinite;
        margin-bottom: 1rem;
    }
    
    .consulting-dots {
        display: flex;
        gap: 8px;
        margin-bottom: 1rem;
    }
    
    .consulting-dot {
        width: 12px;
        height: 12px;
        background: #3b82f6;
        border-radius: 50%;
        animation: consulting-pulse 1.5s ease-in-out infinite;
    }
    
    .consulting-dot:nth-child(2) { animation-delay: 0.3s; }
    .consulting-dot:nth-child(3) { animation-delay: 0.6s; }
    .consulting-dot:nth-child(4) { animation-delay: 0.9s; }
    
    .consulting-message {
        color: #1e3a8a;
        font-size: 1.1rem;
        font-weight: 600;
        text-align: center;
        animation: consulting-fade 2s ease-in-out infinite;
    }
    
    @keyframes consulting-spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    @keyframes consulting-pulse {
        0%, 100% { transform: scale(1); opacity: 0.7; }
        50% { transform: scale(1.3); opacity: 1; }
    }
    
    @keyframes consulting-fade {
        0%, 100% { opacity: 0.7; }
        50% { opacity: 1; }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Show spinner
    spinner_placeholder = st.empty()
    
    with spinner_placeholder.container():
        st.markdown(f"""
        <div class="consulting-spinner-container">
            <div class="consulting-spinner"></div>
            <div class="consulting-dots">
                <div class="consulting-dot"></div>
                <div class="consulting-dot"></div>
                <div class="consulting-dot"></div>
                <div class="consulting-dot"></div>
            </div>
            <div class="consulting-message">{display_message}</div>
        </div>
        """, unsafe_allow_html=True)
        
        time.sleep(duration)
    
    # Clear spinner
    spinner_placeholder.empty()


def show_agent_coordination_spinner():
    """Specialized spinner for agent coordination"""
    show_consulting_spinner(
        duration=1.8,
        message="🤖 Coordinating multi-agent collaboration..."
    )


def show_escalation_spinner():
    """Specialized spinner for escalation system"""
    show_consulting_spinner(
        duration=1.5,
        message="⚡ Analyzing escalation requirements..."
    )


def show_client_engagement_spinner():
    """Specialized spinner for client engagement"""
    show_consulting_spinner(
        duration=2.2,
        message="🏢 Preparing client engagement interface..."
    )