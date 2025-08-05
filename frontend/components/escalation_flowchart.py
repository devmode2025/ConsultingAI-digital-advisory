"""Escalation Flowchart Component - Interactive three-tier escalation visualization"""

import streamlit as st
from typing import Dict, Any, Optional
import random

def show_escalation_flowchart(current_confidence: Optional[float] = None):
    """Display interactive escalation flowchart with current decision path
    
    Args:
        current_confidence: Current confidence level to highlight active path
    """
    
    # Generate demo confidence if none provided
    if current_confidence is None:
        current_confidence = random.uniform(60, 95)
    
    # Determine active tier
    if current_confidence >= 90:
        active_tier = "agent"
        tier_color = "#10b981"
    elif current_confidence >= 70:
        active_tier = "junior"
        tier_color = "#f59e0b"
    else:
        active_tier = "senior"
        tier_color = "#ef4444"
    
    # Custom CSS for flowchart
    st.markdown("""
    <style>
    .escalation-flowchart {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: 2rem 0;
        padding: 1rem;
        background: #f8fafc;
        border-radius: 12px;
    }
    .escalation-tier {
        flex: 1;
        text-align: center;
        padding: 1.5rem;
        margin: 0 0.5rem;
        border-radius: 10px;
        border: 2px solid #e5e7eb;
        background: white;
        transition: all 0.3s ease;
    }
    .escalation-tier.active {
        border-color: var(--active-color);
        background: var(--active-bg);
        transform: scale(1.05);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    .tier-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    .tier-title {
        font-weight: 600;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
    }
    .tier-threshold {
        font-size: 0.9rem;
        color: #6b7280;
        margin-bottom: 0.5rem;
    }
    .tier-description {
        font-size: 0.8rem;
        color: #6b7280;
        line-height: 1.4;
    }
    .escalation-arrow {
        font-size: 1.5rem;
        color: #9ca3af;
        margin: 0 0.5rem;
    }
    .confidence-indicator {
        text-align: center;
        margin: 1rem 0;
        padding: 1rem;
        background: white;
        border-radius: 8px;
        border: 2px solid var(--active-color);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Confidence indicator
    st.markdown(f"""
    <div class="confidence-indicator" style="--active-color: {tier_color};">
        <div style="font-size: 1.2rem; font-weight: 600; color: {tier_color};">
            Current Confidence Level: {current_confidence:.1f}%
        </div>
        <div style="font-size: 0.9rem; color: #6b7280; margin-top: 0.5rem;">
            Decision routing to: <strong>{active_tier.title()} Tier</strong>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Escalation flowchart
    st.markdown(f"""
    <div class="escalation-flowchart">
        <div class="escalation-tier {'active' if active_tier == 'agent' else ''}" 
             style="--active-color: #10b981; --active-bg: #f0fdf4;">
            <div class="tier-icon">🤖</div>
            <div class="tier-title">Agent-Only</div>
            <div class="tier-threshold">Confidence ≥ 90%</div>
            <div class="tier-description">
                Automated processing<br>
                No human intervention<br>
                Standard decisions
            </div>
        </div>
        
        <div class="escalation-arrow">→</div>
        
        <div class="escalation-tier {'active' if active_tier == 'junior' else ''}"
             style="--active-color: #f59e0b; --active-bg: #fffbeb;">
            <div class="tier-icon">👨‍💼</div>
            <div class="tier-title">Junior Specialist</div>
            <div class="tier-threshold">Confidence 70-90%</div>
            <div class="tier-description">
                Human review required<br>
                Domain expertise<br>
                Complex decisions
            </div>
        </div>
        
        <div class="escalation-arrow">→</div>
        
        <div class="escalation-tier {'active' if active_tier == 'senior' else ''}"
             style="--active-color: #ef4444; --active-bg: #fef2f2;">
            <div class="tier-icon">👨‍💼</div>
            <div class="tier-title">Senior Partner</div>
            <div class="tier-threshold">Confidence < 70%</div>
            <div class="tier-description">
                Executive oversight<br>
                Strategic decisions<br>
                High-stakes scenarios
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def show_escalation_decision_flow(scenario: Dict[str, Any]):
    """Show step-by-step escalation decision process
    
    Args:
        scenario: Dictionary containing scenario details and decision factors
    """
    
    st.markdown("### 🔄 Escalation Decision Process")
    
    # Decision factors
    factors = scenario.get('factors', {
        'confidence': 75,
        'complexity': 'Medium',
        'risk_level': 'Low',
        'expertise_required': 'Technical',
        'stakeholder_impact': 'Medium'
    })
    
    # Show decision steps
    steps = [
        f"📊 Confidence Analysis: {factors['confidence']}%",
        f"🔍 Complexity Assessment: {factors['complexity']}",
        f"⚠️ Risk Evaluation: {factors['risk_level']}",
        f"🎯 Expertise Required: {factors['expertise_required']}",
        f"👥 Stakeholder Impact: {factors['stakeholder_impact']}"
    ]
    
    for i, step in enumerate(steps):
        st.markdown(f"**Step {i+1}:** {step}")
    
    # Final decision
    confidence = factors['confidence']
    if confidence >= 90:
        decision = "🤖 Route to Agent-Only Processing"
        color = "#10b981"
    elif confidence >= 70:
        decision = "👨‍💼 Escalate to Junior Specialist"
        color = "#f59e0b"
    else:
        decision = "👨‍💼 Escalate to Senior Partner"
        color = "#ef4444"
    
    st.markdown(f"""
    <div style="
        background: {color}15;
        border: 2px solid {color};
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
        text-align: center;
    ">
        <div style="font-size: 1.1rem; font-weight: 600; color: {color};">
            Final Decision: {decision}
        </div>
    </div>
    """, unsafe_allow_html=True)


def show_escalation_metrics():
    """Display escalation system performance metrics"""
    
    st.markdown("### 📈 Escalation System Metrics")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Agent-Only Decisions",
            "156",
            "↑ 12%",
            help="Decisions handled without human intervention"
        )
        
    with col2:
        st.metric(
            "Junior Specialist Reviews",
            "43",
            "↑ 8%",
            help="Decisions requiring specialist review"
        )
        
    with col3:
        st.metric(
            "Senior Partner Escalations",
            "7",
            "↓ 2%",
            help="High-stakes decisions requiring executive oversight"
        )
    
    # Escalation distribution chart
    st.markdown("#### Escalation Distribution")
    escalation_data = {
        "Agent-Only (≥90%)": 76,
        "Junior Specialist (70-90%)": 21,
        "Senior Partner (<70%)": 3
    }
    
    st.bar_chart(escalation_data)


def show_interactive_escalation_simulator():
    """Interactive escalation simulator for testing scenarios"""
    
    st.markdown("### 🎮 Escalation Simulator")
    st.markdown("Adjust parameters to see how decisions are routed:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        confidence = st.slider("Confidence Level", 0, 100, 75, help="Agent confidence in decision")
        complexity = st.selectbox("Complexity", ["Low", "Medium", "High"])
        risk_level = st.selectbox("Risk Level", ["Low", "Medium", "High"])
    
    with col2:
        expertise = st.selectbox("Expertise Required", ["Technical", "Business", "Strategic", "Legal"])
        impact = st.selectbox("Stakeholder Impact", ["Low", "Medium", "High"])
        urgency = st.selectbox("Urgency", ["Low", "Medium", "High"])
    
    # Calculate escalation based on parameters
    scenario = {
        'factors': {
            'confidence': confidence,
            'complexity': complexity,
            'risk_level': risk_level,
            'expertise_required': expertise,
            'stakeholder_impact': impact,
            'urgency': urgency
        }
    }
    
    if st.button("🔄 Run Escalation Analysis"):
        show_escalation_decision_flow(scenario)
        show_escalation_flowchart(confidence)