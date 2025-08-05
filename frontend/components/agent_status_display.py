"""Agent Status Display Component - Real-time agent coordination visualization"""

import streamlit as st
from typing import Dict, List, Any, Optional
from datetime import datetime
import random

def show_agent_status_grid(agents: Optional[List[Dict[str, Any]]] = None):
    """Display grid of agent statuses with real-time updates
    
    Args:
        agents: List of agent dictionaries with status information
    """
    
    # Default demo agents if none provided
    if agents is None:
        agents = [
            {
                "name": "Chief Engagement Manager",
                "type": "UserProxyAgent",
                "status": "coordinating",
                "confidence": 95,
                "current_task": "Orchestrating team collaboration",
                "last_update": datetime.now()
            },
            {
                "name": "Code Reviewer",
                "type": "AssistantAgent", 
                "status": "analyzing",
                "confidence": 87,
                "current_task": "Reviewing Python optimization",
                "last_update": datetime.now()
            },
            {
                "name": "System Architect",
                "type": "AssistantAgent",
                "status": "designing", 
                "confidence": 92,
                "current_task": "Cloud architecture planning",
                "last_update": datetime.now()
            },
            {
                "name": "Business Analyst",
                "type": "AssistantAgent",
                "status": "researching",
                "confidence": 78,
                "current_task": "Process analysis",
                "last_update": datetime.now()
            }
        ]
    
    # Custom CSS for agent status cards
    st.markdown("""
    <style>
    .agent-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #3b82f6;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .agent-card.coordinating { border-left-color: #10b981; }
    .agent-card.analyzing { border-left-color: #f59e0b; }
    .agent-card.designing { border-left-color: #8b5cf6; }
    .agent-card.researching { border-left-color: #ef4444; }
    .agent-card.idle { border-left-color: #6b7280; }
    
    .agent-name { font-weight: 600; color: #1f2937; margin-bottom: 0.5rem; }
    .agent-type { font-size: 0.8rem; color: #6b7280; }
    .agent-status { 
        display: inline-block;
        padding: 0.2rem 0.5rem;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: 500;
        margin: 0.5rem 0;
    }
    .status-coordinating { background: #d1fae5; color: #065f46; }
    .status-analyzing { background: #fef3c7; color: #92400e; }
    .status-designing { background: #ede9fe; color: #5b21b6; }
    .status-researching { background: #fee2e2; color: #991b1b; }
    .status-idle { background: #f3f4f6; color: #374151; }
    
    .confidence-bar {
        width: 100%;
        height: 8px;
        background: #e5e7eb;
        border-radius: 4px;
        overflow: hidden;
        margin: 0.5rem 0;
    }
    .confidence-fill {
        height: 100%;
        background: linear-gradient(90deg, #ef4444, #f59e0b, #10b981);
        transition: width 0.3s ease;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Display agents in columns
    cols = st.columns(2)
    
    for i, agent in enumerate(agents):
        with cols[i % 2]:
            status_class = f"agent-card {agent['status']}"
            confidence_width = agent['confidence']
            
            st.markdown(f"""
            <div class="{status_class}">
                <div class="agent-name">{agent['name']}</div>
                <div class="agent-type">{agent['type']}</div>
                <span class="agent-status status-{agent['status']}">
                    {agent['status'].title()}
                </span>
                <div class="confidence-bar">
                    <div class="confidence-fill" style="width: {confidence_width}%"></div>
                </div>
                <div style="font-size: 0.8rem; color: #6b7280;">
                    {agent['current_task']}
                </div>
            </div>
            """, unsafe_allow_html=True)


def show_coordination_flow():
    """Display real-time coordination flow visualization"""
    
    st.markdown("### 🔄 Coordination Flow")
    
    # Simulate coordination steps
    coordination_steps = [
        "📥 Request received by Chief Engagement Manager",
        "🤖 Routing to specialized agent team",
        "⚡ Confidence analysis and escalation check", 
        "👥 Multi-agent collaboration initiated",
        "📊 Results synthesis and quality review",
        "✅ Final recommendation prepared"
    ]
    
    # Show animated progress
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i, step in enumerate(coordination_steps):
        progress = (i + 1) / len(coordination_steps)
        progress_bar.progress(progress)
        status_text.text(step)
        
        if st.session_state.get('demo_mode', False):
            import time
            time.sleep(0.5)
    
    st.success("🎯 Coordination completed successfully!")


def show_escalation_indicator(confidence_level: float):
    """Show escalation tier indicator based on confidence level
    
    Args:
        confidence_level: Confidence percentage (0-100)
    """
    
    if confidence_level >= 90:
        tier = "🤖 Agent-Only"
        color = "#10b981"
        description = "High confidence - automated processing"
    elif confidence_level >= 70:
        tier = "👨‍💼 Junior Specialist"
        color = "#f59e0b" 
        description = "Medium confidence - human review required"
    else:
        tier = "👨‍💼 Senior Partner"
        color = "#ef4444"
        description = "Low confidence - executive oversight needed"
    
    st.markdown(f"""
    <div style="
        background: {color}15;
        border: 2px solid {color};
        border-radius: 8px;
        padding: 1rem;
        text-align: center;
        margin: 1rem 0;
    ">
        <div style="font-size: 1.2rem; font-weight: 600; color: {color};">
            {tier}
        </div>
        <div style="font-size: 0.9rem; color: #6b7280; margin-top: 0.5rem;">
            {description}
        </div>
        <div style="font-size: 0.8rem; color: #6b7280;">
            Confidence: {confidence_level}%
        </div>
    </div>
    """, unsafe_allow_html=True)