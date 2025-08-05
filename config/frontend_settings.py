"""Frontend Configuration Settings for ConsultingAI"""

from typing import Dict, Any, List
from pathlib import Path

# Application settings
APP_CONFIG = {
    "app_name": "ConsultingAI Digital Advisory Firm",
    "app_version": "1.0.0",
    "app_description": "Advanced Human-AI Collaboration Platform",
    "company_name": "ConsultingAI",
    "tagline": "Powered by Microsoft AutoGen Society of Mind Framework"
}

# Theme configuration
THEME_CONFIG = {
    "primary_color": "#3b82f6",
    "secondary_color": "#10b981", 
    "warning_color": "#f59e0b",
    "danger_color": "#ef4444",
    "success_color": "#10b981",
    "background_color": "#ffffff",
    "sidebar_background": "#f8fafc",
    "text_color": "#1f2937",
    "border_color": "#e5e7eb"
}

# Layout configuration
LAYOUT_CONFIG = {
    "sidebar_width": 300,
    "main_content_padding": "2rem",
    "header_height": "80px",
    "footer_height": "60px",
    "card_border_radius": "8px",
    "button_border_radius": "6px"
}

# Page configuration
PAGE_CONFIG = {
    "home": {
        "title": "ConsultingAI Digital Advisory Firm",
        "icon": "🏢",
        "description": "Advanced Human-AI Collaboration Platform"
    },
    "client_engagement": {
        "title": "Client Engagement",
        "icon": "🏢", 
        "description": "Professional client interaction interface"
    },
    "agent_coordination": {
        "title": "Agent Coordination",
        "icon": "🤖",
        "description": "Real-time multi-agent collaboration"
    },
    "escalation_system": {
        "title": "Escalation System", 
        "icon": "⚡",
        "description": "Three-tier decision routing system"
    },
    "expert_personas": {
        "title": "Expert Personas",
        "icon": "👥",
        "description": "Dynamic expertise management"
    },
    "analytics_dashboard": {
        "title": "Analytics Dashboard",
        "icon": "📊", 
        "description": "Performance metrics and insights"
    }
}

# Component configuration
COMPONENT_CONFIG = {
    "spinner_duration": 2.0,
    "toast_duration": 3000,
    "progress_bar_height": 4,
    "metric_card_height": 120,
    "chart_height": 400,
    "table_page_size": 10
}

# Demo mode configuration
DEMO_CONFIG = {
    "auto_advance_delay": 3.0,
    "sample_client_name": "TechCorp Industries",
    "sample_project_budget": "$500K - $1M",
    "sample_timeline": "6-12 months",
    "demo_agent_count": 3,
    "demo_decision_count": 726,
    "demo_accuracy_rate": 94.5
}

# Asset paths
ASSET_PATHS = {
    "logo": "static/images/logo.png",
    "background": "static/images/consulting_bg.jpg", 
    "flow_diagram": "static/images/flow_diagram.png",
    "icons": {
        "agent": "static/icons/agent.svg",
        "escalation": "static/icons/escalation.svg",
        "client": "static/icons/client.svg"
    }
}

# API endpoints (for future backend integration)
API_CONFIG = {
    "base_url": "http://localhost:8000",
    "endpoints": {
        "agents": "/api/v1/agents",
        "escalations": "/api/v1/escalations", 
        "decisions": "/api/v1/decisions",
        "metrics": "/api/v1/metrics"
    },
    "timeout": 30,
    "retry_attempts": 3
}

# Security settings
SECURITY_CONFIG = {
    "session_timeout": 3600,  # 1 hour
    "max_file_size": 10 * 1024 * 1024,  # 10MB
    "allowed_file_types": [".pdf", ".docx", ".txt", ".csv"],
    "enable_csrf_protection": True
}

# Logging configuration
LOGGING_CONFIG = {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "file_path": "logs/frontend.log",
    "max_file_size": 10 * 1024 * 1024,  # 10MB
    "backup_count": 5
}

def get_config(section: str) -> Dict[str, Any]:
    """Get configuration section
    
    Args:
        section: Configuration section name
        
    Returns:
        Configuration dictionary
    """
    config_map = {
        "app": APP_CONFIG,
        "theme": THEME_CONFIG,
        "layout": LAYOUT_CONFIG,
        "pages": PAGE_CONFIG,
        "components": COMPONENT_CONFIG,
        "demo": DEMO_CONFIG,
        "assets": ASSET_PATHS,
        "api": API_CONFIG,
        "security": SECURITY_CONFIG,
        "logging": LOGGING_CONFIG
    }
    
    return config_map.get(section, {})

def get_page_config(page_name: str) -> Dict[str, Any]:
    """Get specific page configuration
    
    Args:
        page_name: Name of the page
        
    Returns:
        Page configuration dictionary
    """
    return PAGE_CONFIG.get(page_name, {})

def get_asset_path(asset_name: str) -> str:
    """Get asset file path
    
    Args:
        asset_name: Name of the asset
        
    Returns:
        Asset file path
    """
    if asset_name in ASSET_PATHS:
        return ASSET_PATHS[asset_name]
    elif asset_name in ASSET_PATHS.get("icons", {}):
        return ASSET_PATHS["icons"][asset_name]
    else:
        return ""

def is_demo_mode_enabled() -> bool:
    """Check if demo mode is enabled"""
    import streamlit as st
    return st.session_state.get("demo_mode", False)