"""Client Profile Form Component - Professional client intake and profiling"""

import streamlit as st
from typing import Dict, Any, List, Optional
from datetime import datetime
from dataclasses import dataclass
from enum import Enum

class ClientType(Enum):
    ENTERPRISE_CORPORATION = "enterprise_corporation"
    TECHNOLOGY_STARTUP = "technology_startup"
    GOVERNMENT_AGENCY = "government_agency"
    FINANCIAL_SERVICES = "financial_services"
    HEALTHCARE_ORGANIZATION = "healthcare_organization"
    MANUFACTURING = "manufacturing"
    RETAIL_CONSUMER = "retail_consumer"

class EngagementComplexity(Enum):
    STRATEGIC_TRANSFORMATION = "strategic_transformation"
    DIGITAL_TRANSFORMATION = "digital_transformation"
    OPERATIONAL_IMPROVEMENT = "operational_improvement"
    TECHNOLOGY_IMPLEMENTATION = "technology_implementation"
    ORGANIZATIONAL_CHANGE = "organizational_change"
    PROCESS_OPTIMIZATION = "process_optimization"

@dataclass
class ClientProfileData:
    """Client profile data structure"""
    client_name: str
    client_type: ClientType
    industry_sector: str
    organization_size: str
    geographic_presence: List[str]
    business_challenge: str
    engagement_type: EngagementComplexity
    timeline: str
    budget_range: str
    success_criteria: str
    decision_makers: str
    key_influencers: str
    constraints: str = ""
    competitive_context: str = ""

def show_client_profile_form() -> Optional[ClientProfileData]:
    """Display comprehensive client profile form
    
    Returns:
        ClientProfileData if form is completed, None otherwise
    """
    
    # Custom CSS for form styling
    st.markdown("""
    <style>
    .form-section {
        background: #f8fafc;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #3b82f6;
    }
    .form-section h4 {
        color: #1f2937;
        margin-bottom: 1rem;
    }
    .required-field {
        color: #ef4444;
        font-weight: 600;
    }
    .help-text {
        font-size: 0.8rem;
        color: #6b7280;
        font-style: italic;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📋 Client Profile & Engagement Details")
    
    # Basic Client Information
    st.markdown('<div class="form-section">', unsafe_allow_html=True)
    st.markdown("#### 🏢 Basic Client Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        client_name = st.text_input(
            "Client Organization *",
            placeholder="Acme Corporation",
            help="Full legal name of the client organization"
        )
        
        client_type = st.selectbox(
            "Client Type *",
            options=[ct.value.replace('_', ' ').title() for ct in ClientType],
            help="Primary classification of the client organization"
        )
        
        industry_sector = st.text_input(
            "Industry Sector *",
            placeholder="Financial Services, Technology, Healthcare...",
            help="Primary industry or sector"
        )
    
    with col2:
        organization_size = st.selectbox(
            "Organization Size *",
            ["Startup (1-50)", "Small (51-200)", "Medium (201-1000)", 
             "Large (1001-5000)", "Enterprise (5000+)"],
            help="Number of employees"
        )
        
        geographic_presence = st.multiselect(
            "Geographic Presence",
            ["North America", "Europe", "Asia Pacific", "Latin America", 
             "Middle East", "Africa", "Global"],
            help="Regions where the organization operates"
        )
        
        timeline = st.selectbox(
            "Engagement Timeline *",
            ["3-6 months", "6-12 months", "12-18 months", "18+ months"],
            help="Expected duration of the engagement"
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Engagement Details
    st.markdown('<div class="form-section">', unsafe_allow_html=True)
    st.markdown("#### 🎯 Engagement Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        engagement_type = st.selectbox(
            "Engagement Type *",
            options=[et.value.replace('_', ' ').title() for et in EngagementComplexity],
            help="Primary type of consulting engagement"
        )
        
        budget_range = st.selectbox(
            "Budget Range *",
            ["$50K - $100K", "$100K - $500K", "$500K - $1M", 
             "$1M - $5M", "$5M - $10M", "$10M+"],
            help="Estimated budget for the engagement"
        )
    
    with col2:
        business_challenge = st.text_area(
            "Primary Business Challenge *",
            placeholder="Describe the main challenge or opportunity...",
            height=100,
            help="Detailed description of the business challenge to be addressed"
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Success Criteria & Stakeholders
    st.markdown('<div class="form-section">', unsafe_allow_html=True)
    st.markdown("#### ✅ Success Criteria & Stakeholders")
    
    success_criteria = st.text_area(
        "Success Criteria *",
        placeholder="Increase efficiency by 25%, reduce costs by $2M annually...",
        height=80,
        help="Specific, measurable outcomes that define success"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        decision_makers = st.text_input(
            "Key Decision Makers *",
            placeholder="CEO, CTO, CFO, Board Members...",
            help="Individuals with final decision authority"
        )
    
    with col2:
        key_influencers = st.text_input(
            "Key Influencers",
            placeholder="Department heads, team leads, subject matter experts...",
            help="Individuals who influence decisions but may not have final authority"
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Additional Context (Optional)
    with st.expander("📝 Additional Context (Optional)"):
        constraints = st.text_area(
            "Constraints & Considerations",
            placeholder="Regulatory requirements, technology limitations, cultural factors...",
            help="Any constraints or special considerations for the engagement"
        )
        
        competitive_context = st.text_area(
            "Competitive Context",
            placeholder="Market pressures, competitive threats, industry trends...",
            help="Relevant competitive or market context"
        )
    
    # Form validation and submission
    st.markdown("---")
    
    # Required field validation
    required_fields = {
        "Client Name": client_name,
        "Client Type": client_type,
        "Industry Sector": industry_sector,
        "Organization Size": organization_size,
        "Engagement Type": engagement_type,
        "Timeline": timeline,
        "Budget Range": budget_range,
        "Business Challenge": business_challenge,
        "Success Criteria": success_criteria,
        "Decision Makers": decision_makers
    }
    
    missing_fields = [field for field, value in required_fields.items() if not value]
    
    if missing_fields:
        st.warning(f"Please complete the following required fields: {', '.join(missing_fields)}")
        return None
    
    # Create client profile data
    try:
        # Convert string selections back to enums
        client_type_enum = ClientType([ct for ct in ClientType if ct.value.replace('_', ' ').title() == client_type][0])
        engagement_type_enum = EngagementComplexity([et for et in EngagementComplexity if et.value.replace('_', ' ').title() == engagement_type][0])
        
        profile_data = ClientProfileData(
            client_name=client_name,
            client_type=client_type_enum,
            industry_sector=industry_sector,
            organization_size=organization_size,
            geographic_presence=geographic_presence or [],
            business_challenge=business_challenge,
            engagement_type=engagement_type_enum,
            timeline=timeline,
            budget_range=budget_range,
            success_criteria=success_criteria,
            decision_makers=decision_makers,
            key_influencers=key_influencers,
            constraints=constraints,
            competitive_context=competitive_context
        )
        
        return profile_data
        
    except Exception as e:
        st.error(f"Error processing form data: {str(e)}")
        return None


def show_client_profile_summary(profile_data: ClientProfileData):
    """Display formatted client profile summary
    
    Args:
        profile_data: Client profile data to display
    """
    
    st.markdown("### 📊 Client Profile Summary")
    
    # Client overview card
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    ">
        <h3 style="margin: 0; color: white;">🏢 {profile_data.client_name}</h3>
        <p style="margin: 0.5rem 0; opacity: 0.9;">
            {profile_data.client_type.value.replace('_', ' ').title()} • {profile_data.industry_sector}
        </p>
        <p style="margin: 0; opacity: 0.8; font-size: 0.9rem;">
            {profile_data.organization_size} • {profile_data.timeline}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Engagement details
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🎯 Engagement Overview")
        st.markdown(f"**Type:** {profile_data.engagement_type.value.replace('_', ' ').title()}")
        st.markdown(f"**Budget:** {profile_data.budget_range}")
        st.markdown(f"**Timeline:** {profile_data.timeline}")
        
        if profile_data.geographic_presence:
            st.markdown(f"**Geographic Presence:** {', '.join(profile_data.geographic_presence)}")
    
    with col2:
        st.markdown("#### 👥 Key Stakeholders")
        st.markdown(f"**Decision Makers:** {profile_data.decision_makers}")
        if profile_data.key_influencers:
            st.markdown(f"**Key Influencers:** {profile_data.key_influencers}")
    
    # Business challenge and success criteria
    st.markdown("#### 🎯 Business Challenge")
    st.markdown(f"> {profile_data.business_challenge}")
    
    st.markdown("#### ✅ Success Criteria")
    st.markdown(f"> {profile_data.success_criteria}")
    
    # Additional context if provided
    if profile_data.constraints:
        st.markdown("#### ⚠️ Constraints & Considerations")
        st.markdown(f"> {profile_data.constraints}")
    
    if profile_data.competitive_context:
        st.markdown("#### 🏆 Competitive Context")
        st.markdown(f"> {profile_data.competitive_context}")


def show_engagement_recommendations(profile_data: ClientProfileData):
    """Show AI-generated engagement recommendations based on client profile
    
    Args:
        profile_data: Client profile data for generating recommendations
    """
    
    st.markdown("### 🤖 AI-Generated Engagement Recommendations")
    
    # Generate recommendations based on client type and engagement type
    recommendations = _generate_engagement_recommendations(profile_data)
    
    for i, rec in enumerate(recommendations, 1):
        st.markdown(f"""
        <div style="
            background: #f0fdf4;
            border: 1px solid #bbf7d0;
            border-radius: 8px;
            padding: 1rem;
            margin: 0.5rem 0;
        ">
            <h5 style="color: #065f46; margin: 0 0 0.5rem 0;">
                💡 Recommendation {i}: {rec['title']}
            </h5>
            <p style="margin: 0; color: #374151;">
                {rec['description']}
            </p>
        </div>
        """, unsafe_allow_html=True)


def _generate_engagement_recommendations(profile_data: ClientProfileData) -> List[Dict[str, str]]:
    """Generate engagement recommendations based on client profile"""
    
    recommendations = []
    
    # Base recommendations on client type
    if profile_data.client_type == ClientType.TECHNOLOGY_STARTUP:
        recommendations.extend([
            {
                "title": "Agile Engagement Approach",
                "description": "Recommend rapid iteration cycles with weekly check-ins and flexible scope adjustments to match startup pace."
            },
            {
                "title": "Scalability Focus",
                "description": "Prioritize solutions that can scale with rapid growth and changing requirements."
            }
        ])
    elif profile_data.client_type == ClientType.ENTERPRISE_CORPORATION:
        recommendations.extend([
            {
                "title": "Structured Governance Framework",
                "description": "Implement formal governance with steering committees and executive briefings for enterprise alignment."
            },
            {
                "title": "Change Management Program",
                "description": "Develop comprehensive change management strategy for large-scale organizational impact."
            }
        ])
    
    # Add engagement type specific recommendations
    if profile_data.engagement_type == EngagementComplexity.DIGITAL_TRANSFORMATION:
        recommendations.append({
            "title": "Phased Digital Roadmap",
            "description": "Create multi-phase digital transformation roadmap with quick wins and long-term strategic initiatives."
        })
    
    return recommendations[:3]  # Return top 3 recommendations