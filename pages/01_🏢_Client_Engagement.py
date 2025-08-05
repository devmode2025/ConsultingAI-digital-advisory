"""Client Engagement Interface - Professional consulting client interaction"""

import streamlit as st
import sys
from pathlib import Path
from datetime import datetime
import json

# Add src to path
sys.path.append(str(Path(__file__).parent.parent / "src"))
sys.path.append(str(Path(__file__).parent.parent / "frontend"))

from frontend.components.consulting_spinner import show_client_engagement_spinner, show_consulting_spinner

st.set_page_config(
    page_title="Client Engagement - ConsultingAI",
    page_icon="🏢",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .engagement-header {
        background: linear-gradient(90deg, #059669 0%, #10b981 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 2rem;
    }
    .client-card {
        background: #f0fdf4;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #bbf7d0;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown("""
    <div class="engagement-header">
        <h1>🏢 Client Engagement Interface</h1>
        <p>Professional consulting client interaction and engagement management</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation
    if st.button("← Back to Home"):
        show_consulting_spinner(1.2, "🏠 Returning to main dashboard...")
        st.switch_page("streamlit_app.py")
    
    st.markdown("---")
    
    # Client engagement form
    with st.container():
        st.markdown("### 📋 New Client Engagement")
        
        col1, col2 = st.columns(2)
        
        with col1:
            client_name = st.text_input("Client Organization", placeholder="Acme Corporation")
            client_type = st.selectbox("Client Type", [
                "Enterprise Corporation",
                "Technology Startup", 
                "Government Agency",
                "Financial Services",
                "Healthcare Organization"
            ])
            industry = st.text_input("Industry Sector", placeholder="Technology")
            
        with col2:
            engagement_type = st.selectbox("Engagement Type", [
                "Strategic Transformation",
                "Digital Transformation",
                "Operational Improvement",
                "Technology Implementation",
                "Organizational Change"
            ])
            timeline = st.selectbox("Timeline", [
                "3-6 months",
                "6-12 months", 
                "12-18 months",
                "18+ months"
            ])
            budget_range = st.selectbox("Budget Range", [
                "$100K - $500K",
                "$500K - $1M",
                "$1M - $5M",
                "$5M+"
            ])
    
    # Business challenge
    st.markdown("### 🎯 Business Challenge")
    business_challenge = st.text_area(
        "Describe the primary business challenge",
        placeholder="Our organization is struggling with digital transformation initiatives...",
        height=100
    )
    
    # Success criteria
    st.markdown("### ✅ Success Criteria")
    success_criteria = st.text_area(
        "Define success criteria and expected outcomes",
        placeholder="Increase operational efficiency by 25%, reduce costs by $2M annually...",
        height=80
    )
    
    # Stakeholders
    st.markdown("### 👥 Key Stakeholders")
    col1, col2 = st.columns(2)
    with col1:
        decision_makers = st.text_input("Decision Makers", placeholder="CEO, CTO, CFO")
    with col2:
        influencers = st.text_input("Key Influencers", placeholder="Department heads, team leads")
    
    # Action buttons
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        if st.button("🚀 Initiate Engagement", use_container_width=True, type="primary"):
            if client_name and business_challenge:
                # Show engaging spinner
                show_client_engagement_spinner()
                
                st.success("✅ Client engagement initiated successfully!")
                
                # Display engagement summary
                st.markdown("### 📊 Engagement Summary")
                st.markdown(f"""
                <div class="client-card">
                    <h4>🏢 {client_name}</h4>
                    <p><strong>Type:</strong> {client_type}</p>
                    <p><strong>Engagement:</strong> {engagement_type}</p>
                    <p><strong>Timeline:</strong> {timeline}</p>
                    <p><strong>Challenge:</strong> {business_challenge[:100]}...</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Next steps
                st.markdown("### 🎯 Next Steps")
                st.markdown("""
                1. **Agent Team Assembly** - Specialized agents assigned
                2. **Discovery Phase** - Comprehensive analysis initiated  
                3. **Stakeholder Alignment** - Key stakeholder interviews scheduled
                4. **Proposal Development** - Solution framework creation
                """)
                
                if st.button("🤖 View Agent Coordination"):
                    st.switch_page("pages/02_🤖_Agent_Coordination.py")
            else:
                st.error("Please provide client name and business challenge")

if __name__ == "__main__":
    main()



