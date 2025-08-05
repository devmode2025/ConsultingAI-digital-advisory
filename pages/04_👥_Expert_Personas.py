"""Expert Personas Interface - Dynamic persona management and switching"""

import streamlit as st
import sys
from pathlib import Path
from datetime import datetime

st.set_page_config(
    page_title="Expert Personas - ConsultingAI",
    page_icon="👥",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .personas-header {
        background: linear-gradient(90deg, #0891b2 0%, #06b6d4 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 2rem;
    }
    .persona-card {
        background: #f0f9ff;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #bae6fd;
        margin: 1rem 0;
        transition: all 0.3s ease;
    }
    .persona-card:hover {
        border-color: #0891b2;
        box-shadow: 0 4px 12px rgba(8, 145, 178, 0.15);
    }
    .active-persona {
        border: 2px solid #0891b2;
        background: #e0f2fe;
    }
    .expertise-badge {
        background: #0891b2;
        color: white;
        padding: 0.25rem 0.5rem;
        border-radius: 15px;
        font-size: 0.8rem;
        margin: 0.2rem;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown("""
    <div class="personas-header">
        <h1>👥 Expert Personas Dashboard</h1>
        <p>Dynamic persona management and intelligent expertise routing</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation
    if st.button("← Back to Home"):
        st.switch_page("streamlit_app.py")
    
    st.markdown("---")
    
    # Initialize session state
    if 'active_persona' not in st.session_state:
        st.session_state.active_persona = None
    
    # Expert personas
    personas = {
        "Python Guru": {
            "emoji": "🐍",
            "description": "Senior Python developer with 15+ years experience",
            "expertise": ["Python", "Django", "FastAPI", "Microservices", "Performance Optimization"],
            "confidence_areas": ["Code Architecture", "Performance Tuning", "Best Practices"],
            "experience": "15+ years",
            "specialization": "Backend Development & System Architecture"
        },
        "System Architect": {
            "emoji": "🏗️",
            "description": "Enterprise architect specializing in scalable systems",
            "expertise": ["System Design", "Cloud Architecture", "Microservices", "DevOps", "Security"],
            "confidence_areas": ["Scalability", "System Integration", "Technology Strategy"],
            "experience": "12+ years", 
            "specialization": "Enterprise Architecture & Cloud Solutions"
        },
        "Business Analyst": {
            "emoji": "📊",
            "description": "Strategic business analyst with consulting background",
            "expertise": ["Business Strategy", "Process Optimization", "Stakeholder Management", "ROI Analysis"],
            "confidence_areas": ["Business Requirements", "Process Design", "Stakeholder Alignment"],
            "experience": "10+ years",
            "specialization": "Business Strategy & Process Optimization"
        },
        "AI/ML Specialist": {
            "emoji": "🤖",
            "description": "Machine learning engineer and AI researcher",
            "expertise": ["Machine Learning", "Deep Learning", "NLP", "Computer Vision", "MLOps"],
            "confidence_areas": ["Model Development", "AI Strategy", "Data Science"],
            "experience": "8+ years",
            "specialization": "Artificial Intelligence & Machine Learning"
        },
        "DevOps Engineer": {
            "emoji": "⚙️",
            "description": "DevOps specialist focused on automation and reliability",
            "expertise": ["CI/CD", "Kubernetes", "Docker", "Infrastructure as Code", "Monitoring"],
            "confidence_areas": ["Deployment Automation", "System Reliability", "Performance Monitoring"],
            "experience": "9+ years",
            "specialization": "DevOps & Site Reliability Engineering"
        }
    }
    
    # Persona selection
    st.markdown("### 🎯 Available Expert Personas")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        for name, details in personas.items():
            card_class = "persona-card active-persona" if st.session_state.active_persona == name else "persona-card"
            
            st.markdown(f"""
            <div class="{card_class}">
                <h4>{details['emoji']} {name}</h4>
                <p><strong>Specialization:</strong> {details['specialization']}</p>
                <p><strong>Experience:</strong> {details['experience']}</p>
                <p>{details['description']}</p>
                <div>
                    {''.join([f'<span class="expertise-badge">{skill}</span>' for skill in details['expertise'][:3]])}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Activate {name}", key=f"activate_{name}"):
                st.session_state.active_persona = name
                st.rerun()
    
    with col2:
        st.markdown("### 📊 Persona Analytics")
        
        if st.session_state.active_persona:
            active = personas[st.session_state.active_persona]
            st.success(f"**Active:** {st.session_state.active_persona}")
            st.info(f"**Specialization:** {active['specialization']}")
            
            st.markdown("**Expertise Areas:**")
            for skill in active['expertise']:
                st.text(f"• {skill}")
        else:
            st.info("No persona currently active")
        
        st.markdown("---")
        st.metric("Total Personas", "5")
        st.metric("Active Sessions", "1" if st.session_state.active_persona else "0")
        st.metric("Expertise Domains", "20+")
    
    # Dynamic expertise routing simulation
    st.markdown("---")
    st.markdown("### 🎯 Dynamic Expertise Routing")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Scenario Selection:**")
        scenario = st.selectbox("Choose a consulting scenario:", [
            "Python Performance Optimization",
            "Cloud Architecture Design", 
            "Business Process Analysis",
            "AI Strategy Development",
            "DevOps Pipeline Setup"
        ])
        
        if st.button("🚀 Route to Expert", type="primary"):
            # Simulate intelligent routing
            routing_map = {
                "Python Performance Optimization": "Python Guru",
                "Cloud Architecture Design": "System Architect",
                "Business Process Analysis": "Business Analyst", 
                "AI Strategy Development": "AI/ML Specialist",
                "DevOps Pipeline Setup": "DevOps Engineer"
            }
            
            recommended_expert = routing_map.get(scenario, "Python Guru")
            
            with st.spinner("Analyzing scenario and routing to expert..."):
                import time
                time.sleep(1.5)
            
            st.success(f"✅ Routed to: **{recommended_expert}**")
            st.session_state.active_persona = recommended_expert
            
            # Show routing rationale
            expert_details = personas[recommended_expert]
            st.markdown(f"""
            **Routing Rationale:**
            - **Expertise Match:** {expert_details['expertise'][0]}
            - **Experience:** {expert_details['experience']}
            - **Confidence Area:** {expert_details['confidence_areas'][0]}
            """)
    
    with col2:
        st.markdown("**Multi-Expert Consensus:**")
        if st.button("🤝 Initiate Multi-Expert Review"):
            st.markdown("**Consensus Panel Activated:**")
            st.text("🐍 Python Guru: 'Performance optimization approach validated'")
            st.text("🏗️ System Architect: 'Architecture scalability confirmed'") 
            st.text("📊 Business Analyst: 'Business impact assessment complete'")
            
            st.success("✅ Multi-expert consensus achieved (94% agreement)")
    
    # Persona learning and adaptation
    st.markdown("---")
    st.markdown("### 🧠 Persona Learning & Adaptation")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Learning Metrics:**")
        st.metric("Decisions Processed", "156", "↑ 23")
        st.metric("Accuracy Rate", "94%", "↑ 2%")
        st.metric("User Satisfaction", "4.8/5", "↑ 0.1")
    
    with col2:
        st.markdown("**Adaptation Areas:**")
        st.text("• Decision confidence calibration")
        st.text("• Expertise boundary refinement") 
        st.text("• Communication style optimization")
        st.text("• Context understanding improvement")
    
    with col3:
        st.markdown("**Recent Improvements:**")
        st.text("• Enhanced Python performance analysis")
        st.text("• Improved cloud cost optimization")
        st.text("• Better stakeholder communication")
        st.text("• Faster decision routing")
    
    # Action buttons
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🤖 Agent Coordination", use_container_width=True):
            st.switch_page("pages/02_🤖_Agent_Coordination.py")
    
    with col2:
        if st.button("⚡ Escalation System", use_container_width=True):
            st.switch_page("pages/03_⚡_Escalation_System.py")
    
    with col3:
        if st.button("📊 Analytics Dashboard", use_container_width=True):
            st.switch_page("pages/05_📊_Analytics_Dashboard.py")

if __name__ == "__main__":
    main()