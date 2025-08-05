"""Session State Management - Centralized state management for ConsultingAI frontend"""

import streamlit as st
from typing import Any, Dict, List, Optional, Callable
from datetime import datetime
import json
from dataclasses import dataclass, asdict
from enum import Enum

class SessionStateKeys:
    """Centralized session state key definitions"""
    
    # Core application state
    CURRENT_PAGE = "current_page"
    USER_ROLE = "user_role"
    SESSION_ID = "session_id"
    INITIALIZATION_TIME = "initialization_time"
    
    # Client engagement state
    CLIENT_PROFILE = "client_profile"
    ENGAGEMENT_ACTIVE = "engagement_active"
    CURRENT_REQUEST = "current_request"
    REQUEST_HISTORY = "request_history"
    
    # Agent coordination state
    COORDINATION_ACTIVE = "coordination_active"
    ACTIVE_AGENTS = "active_agents"
    AGENT_STATUSES = "agent_statuses"
    COORDINATION_HISTORY = "coordination_history"
    
    # Escalation system state
    ESCALATION_ACTIVE = "escalation_active"
    CURRENT_ESCALATION = "current_escalation"
    ESCALATION_HISTORY = "escalation_history"
    CONFIDENCE_THRESHOLD = "confidence_threshold"
    
    # Expert persona state
    ACTIVE_PERSONA = "active_persona"
    PERSONA_HISTORY = "persona_history"
    EXPERTISE_CONTEXT = "expertise_context"
    
    # Analytics and metrics
    METRICS_DATA = "metrics_data"
    ANALYTICS_FILTERS = "analytics_filters"
    DASHBOARD_CONFIG = "dashboard_config"
    
    # Demo and presentation mode
    DEMO_MODE = "demo_mode"
    PRESENTATION_MODE = "presentation_mode"
    AUTO_ADVANCE = "auto_advance"

@dataclass
class ClientProfile:
    """Client profile data structure"""
    client_name: str = ""
    client_type: str = ""
    industry_sector: str = ""
    company_size: str = ""
    budget_range: str = ""
    project_timeline: str = ""
    primary_objectives: List[str] = None
    technical_requirements: List[str] = None
    stakeholder_context: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.primary_objectives is None:
            self.primary_objectives = []
        if self.technical_requirements is None:
            self.technical_requirements = []
        if self.stakeholder_context is None:
            self.stakeholder_context = {}

@dataclass
class AgentStatus:
    """Agent status data structure"""
    agent_name: str
    status: str  # active, busy, idle, error
    current_task: str = ""
    confidence_level: float = 0.0
    last_update: datetime = None
    performance_metrics: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.last_update is None:
            self.last_update = datetime.now()
        if self.performance_metrics is None:
            self.performance_metrics = {}

@dataclass
class EscalationContext:
    """Escalation context data structure"""
    escalation_id: str
    decision_type: str
    confidence_score: float
    complexity_level: str
    target_tier: str
    escalation_reason: str
    timestamp: datetime = None
    human_input_required: bool = True
    context_data: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()
        if self.context_data is None:
            self.context_data = {}

class SessionStateManager:
    """Centralized session state management"""
    
    @staticmethod
    def initialize_session():
        """Initialize session state with default values"""
        
        # Core application state
        if SessionStateKeys.SESSION_ID not in st.session_state:
            st.session_state[SessionStateKeys.SESSION_ID] = f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        if SessionStateKeys.INITIALIZATION_TIME not in st.session_state:
            st.session_state[SessionStateKeys.INITIALIZATION_TIME] = datetime.now()
        
        if SessionStateKeys.CURRENT_PAGE not in st.session_state:
            st.session_state[SessionStateKeys.CURRENT_PAGE] = "home"
        
        if SessionStateKeys.USER_ROLE not in st.session_state:
            st.session_state[SessionStateKeys.USER_ROLE] = "client"
        
        # Client engagement defaults
        if SessionStateKeys.CLIENT_PROFILE not in st.session_state:
            st.session_state[SessionStateKeys.CLIENT_PROFILE] = ClientProfile()
        
        if SessionStateKeys.ENGAGEMENT_ACTIVE not in st.session_state:
            st.session_state[SessionStateKeys.ENGAGEMENT_ACTIVE] = False
        
        if SessionStateKeys.REQUEST_HISTORY not in st.session_state:
            st.session_state[SessionStateKeys.REQUEST_HISTORY] = []
        
        # Agent coordination defaults
        if SessionStateKeys.COORDINATION_ACTIVE not in st.session_state:
            st.session_state[SessionStateKeys.COORDINATION_ACTIVE] = False
        
        if SessionStateKeys.ACTIVE_AGENTS not in st.session_state:
            st.session_state[SessionStateKeys.ACTIVE_AGENTS] = []
        
        if SessionStateKeys.AGENT_STATUSES not in st.session_state:
            st.session_state[SessionStateKeys.AGENT_STATUSES] = {}
        
        if SessionStateKeys.COORDINATION_HISTORY not in st.session_state:
            st.session_state[SessionStateKeys.COORDINATION_HISTORY] = []
        
        # Escalation system defaults
        if SessionStateKeys.ESCALATION_ACTIVE not in st.session_state:
            st.session_state[SessionStateKeys.ESCALATION_ACTIVE] = False
        
        if SessionStateKeys.ESCALATION_HISTORY not in st.session_state:
            st.session_state[SessionStateKeys.ESCALATION_HISTORY] = []
        
        if SessionStateKeys.CONFIDENCE_THRESHOLD not in st.session_state:
            st.session_state[SessionStateKeys.CONFIDENCE_THRESHOLD] = 70.0
        
        # Expert persona defaults
        if SessionStateKeys.ACTIVE_PERSONA not in st.session_state:
            st.session_state[SessionStateKeys.ACTIVE_PERSONA] = None
        
        if SessionStateKeys.PERSONA_HISTORY not in st.session_state:
            st.session_state[SessionStateKeys.PERSONA_HISTORY] = []
        
        # Analytics defaults
        if SessionStateKeys.METRICS_DATA not in st.session_state:
            st.session_state[SessionStateKeys.METRICS_DATA] = {}
        
        if SessionStateKeys.ANALYTICS_FILTERS not in st.session_state:
            st.session_state[SessionStateKeys.ANALYTICS_FILTERS] = {}
        
        # Demo mode defaults
        if SessionStateKeys.DEMO_MODE not in st.session_state:
            st.session_state[SessionStateKeys.DEMO_MODE] = False
        
        if SessionStateKeys.PRESENTATION_MODE not in st.session_state:
            st.session_state[SessionStateKeys.PRESENTATION_MODE] = False
    
    @staticmethod
    def get_client_profile() -> ClientProfile:
        """Get current client profile"""
        return st.session_state.get(SessionStateKeys.CLIENT_PROFILE, ClientProfile())
    
    @staticmethod
    def update_client_profile(profile_data: Dict[str, Any]):
        """Update client profile with new data"""
        current_profile = SessionStateManager.get_client_profile()
        
        for key, value in profile_data.items():
            if hasattr(current_profile, key):
                setattr(current_profile, key, value)
        
        st.session_state[SessionStateKeys.CLIENT_PROFILE] = current_profile
    
    @staticmethod
    def add_request_to_history(request_data: Dict[str, Any]):
        """Add request to history"""
        history = st.session_state.get(SessionStateKeys.REQUEST_HISTORY, [])
        
        request_entry = {
            "timestamp": datetime.now().isoformat(),
            "request_id": f"req_{len(history) + 1:04d}",
            **request_data
        }
        
        history.append(request_entry)
        st.session_state[SessionStateKeys.REQUEST_HISTORY] = history
    
    @staticmethod
    def update_agent_status(agent_name: str, status_data: Dict[str, Any]):
        """Update agent status"""
        agent_statuses = st.session_state.get(SessionStateKeys.AGENT_STATUSES, {})
        
        if agent_name not in agent_statuses:
            agent_statuses[agent_name] = AgentStatus(agent_name=agent_name, status="idle")
        
        current_status = agent_statuses[agent_name]
        for key, value in status_data.items():
            if hasattr(current_status, key):
                setattr(current_status, key, value)
        
        current_status.last_update = datetime.now()
        agent_statuses[agent_name] = current_status
        st.session_state[SessionStateKeys.AGENT_STATUSES] = agent_statuses
    
    @staticmethod
    def get_agent_statuses() -> Dict[str, AgentStatus]:
        """Get all agent statuses"""
        return st.session_state.get(SessionStateKeys.AGENT_STATUSES, {})
    
    @staticmethod
    def add_coordination_event(event_data: Dict[str, Any]):
        """Add coordination event to history"""
        history = st.session_state.get(SessionStateKeys.COORDINATION_HISTORY, [])
        
        event_entry = {
            "timestamp": datetime.now().isoformat(),
            "event_id": f"coord_{len(history) + 1:04d}",
            **event_data
        }
        
        history.append(event_entry)
        st.session_state[SessionStateKeys.COORDINATION_HISTORY] = history
    
    @staticmethod
    def create_escalation_context(escalation_data: Dict[str, Any]) -> EscalationContext:
        """Create new escalation context"""
        escalation_id = f"esc_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        escalation_context = EscalationContext(
            escalation_id=escalation_id,
            **escalation_data
        )
        
        st.session_state[SessionStateKeys.CURRENT_ESCALATION] = escalation_context
        
        # Add to history
        history = st.session_state.get(SessionStateKeys.ESCALATION_HISTORY, [])
        history.append(asdict(escalation_context))
        st.session_state[SessionStateKeys.ESCALATION_HISTORY] = history
        
        return escalation_context
    
    @staticmethod
    def get_current_escalation() -> Optional[EscalationContext]:
        """Get current escalation context"""
        return st.session_state.get(SessionStateKeys.CURRENT_ESCALATION)
    
    @staticmethod
    def clear_current_escalation():
        """Clear current escalation context"""
        if SessionStateKeys.CURRENT_ESCALATION in st.session_state:
            del st.session_state[SessionStateKeys.CURRENT_ESCALATION]
    
    @staticmethod
    def set_active_persona(persona_type: str, context: Dict[str, Any] = None):
        """Set active expert persona"""
        st.session_state[SessionStateKeys.ACTIVE_PERSONA] = persona_type
        
        if context:
            st.session_state[SessionStateKeys.EXPERTISE_CONTEXT] = context
        
        # Add to persona history
        history = st.session_state.get(SessionStateKeys.PERSONA_HISTORY, [])
        history.append({
            "timestamp": datetime.now().isoformat(),
            "persona_type": persona_type,
            "context": context or {}
        })
        st.session_state[SessionStateKeys.PERSONA_HISTORY] = history
    
    @staticmethod
    def get_active_persona() -> Optional[str]:
        """Get active expert persona"""
        return st.session_state.get(SessionStateKeys.ACTIVE_PERSONA)
    
    @staticmethod
    def update_metrics_data(metrics: Dict[str, Any]):
        """Update metrics data"""
        current_metrics = st.session_state.get(SessionStateKeys.METRICS_DATA, {})
        current_metrics.update(metrics)
        st.session_state[SessionStateKeys.METRICS_DATA] = current_metrics
    
    @staticmethod
    def get_metrics_data() -> Dict[str, Any]:
        """Get current metrics data"""
        return st.session_state.get(SessionStateKeys.METRICS_DATA, {})
    
    @staticmethod
    def enable_demo_mode(auto_advance: bool = False):
        """Enable demo mode for presentations"""
        st.session_state[SessionStateKeys.DEMO_MODE] = True
        st.session_state[SessionStateKeys.AUTO_ADVANCE] = auto_advance
        
        # Initialize demo data
        SessionStateManager._initialize_demo_data()
    
    @staticmethod
    def disable_demo_mode():
        """Disable demo mode"""
        st.session_state[SessionStateKeys.DEMO_MODE] = False
        st.session_state[SessionStateKeys.AUTO_ADVANCE] = False
    
    @staticmethod
    def is_demo_mode() -> bool:
        """Check if demo mode is active"""
        return st.session_state.get(SessionStateKeys.DEMO_MODE, False)
    
    @staticmethod
    def _initialize_demo_data():
        """Initialize demo data for presentations"""
        
        # Demo client profile
        demo_profile = ClientProfile(
            client_name="TechCorp Industries",
            client_type="Enterprise",
            industry_sector="Technology",
            company_size="1000-5000 employees",
            budget_range="$500K - $1M",
            project_timeline="6-12 months",
            primary_objectives=["Digital Transformation", "Process Automation", "Cost Optimization"],
            technical_requirements=["Cloud Migration", "API Integration", "Security Enhancement"]
        )
        st.session_state[SessionStateKeys.CLIENT_PROFILE] = demo_profile
        
        # Demo agent statuses
        demo_agents = {
            "Code Reviewer Agent": AgentStatus(
                agent_name="Code Reviewer Agent",
                status="active",
                current_task="Analyzing system architecture",
                confidence_level=94.5
            ),
            "System Architect Agent": AgentStatus(
                agent_name="System Architect Agent", 
                status="busy",
                current_task="Designing solution framework",
                confidence_level=87.2
            ),
            "Business Analyst Agent": AgentStatus(
                agent_name="Business Analyst Agent",
                status="active", 
                current_task="Stakeholder requirement analysis",
                confidence_level=91.8
            )
        }
        st.session_state[SessionStateKeys.AGENT_STATUSES] = demo_agents
        
        # Demo metrics
        demo_metrics = {
            "total_decisions": {"value": 726, "change": 15, "trend": "up"},
            "decision_accuracy": {"value": 94, "change": 2, "trend": "up"},
            "avg_response_time": {"value": 1.2, "change": -0.3, "trend": "down"},
            "user_satisfaction": {"value": 4.8, "change": 0.2, "trend": "up"}
        }
        st.session_state[SessionStateKeys.METRICS_DATA] = demo_metrics
    
    @staticmethod
    def export_session_state() -> str:
        """Export session state as JSON"""
        exportable_state = {}
        
        for key, value in st.session_state.items():
            try:
                # Convert dataclasses to dictionaries
                if hasattr(value, '__dataclass_fields__'):
                    exportable_state[key] = asdict(value)
                else:
                    json.dumps(value)  # Test if serializable
                    exportable_state[key] = value
            except (TypeError, ValueError):
                # Skip non-serializable values
                exportable_state[key] = str(value)
        
        return json.dumps(exportable_state, indent=2, default=str)
    
    @staticmethod
    def clear_session_state(preserve_core: bool = True):
        """Clear session state with option to preserve core settings"""
        
        if preserve_core:
            # Preserve core application state
            core_keys = [
                SessionStateKeys.SESSION_ID,
                SessionStateKeys.INITIALIZATION_TIME,
                SessionStateKeys.USER_ROLE,
                SessionStateKeys.DEMO_MODE
            ]
            
            preserved_values = {key: st.session_state.get(key) for key in core_keys if key in st.session_state}
            st.session_state.clear()
            st.session_state.update(preserved_values)
        else:
            st.session_state.clear()
        
        # Reinitialize with defaults
        SessionStateManager.initialize_session()

# Convenience functions for common operations
def get_session_id() -> str:
    """Get current session ID"""
    return st.session_state.get(SessionStateKeys.SESSION_ID, "unknown")

def is_engagement_active() -> bool:
    """Check if client engagement is active"""
    return st.session_state.get(SessionStateKeys.ENGAGEMENT_ACTIVE, False)

def is_coordination_active() -> bool:
    """Check if agent coordination is active"""
    return st.session_state.get(SessionStateKeys.COORDINATION_ACTIVE, False)

def get_confidence_threshold() -> float:
    """Get current confidence threshold for escalation"""
    return st.session_state.get(SessionStateKeys.CONFIDENCE_THRESHOLD, 70.0)