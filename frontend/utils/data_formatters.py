"""Data Formatting Utilities - Format data for Streamlit display"""

import pandas as pd
from typing import Dict, Any, List, Optional, Union
from datetime import datetime, timedelta
import json

def format_currency(amount: float, currency: str = "USD") -> str:
    """Format currency values for display
    
    Args:
        amount: Currency amount
        currency: Currency code
        
    Returns:
        Formatted currency string
    """
    currency_symbols = {
        "USD": "$",
        "EUR": "€",
        "GBP": "£",
        "JPY": "¥"
    }
    
    symbol = currency_symbols.get(currency, currency)
    
    if amount >= 1_000_000:
        return f"{symbol}{amount/1_000_000:.1f}M"
    elif amount >= 1_000:
        return f"{symbol}{amount/1_000:.1f}K"
    else:
        return f"{symbol}{amount:,.2f}"

def format_percentage(value: float, decimal_places: int = 1) -> str:
    """Format percentage values
    
    Args:
        value: Percentage value (0-100)
        decimal_places: Number of decimal places
        
    Returns:
        Formatted percentage string
    """
    return f"{value:.{decimal_places}f}%"

def format_duration(seconds: float) -> str:
    """Format duration in human-readable format
    
    Args:
        seconds: Duration in seconds
        
    Returns:
        Formatted duration string
    """
    if seconds < 60:
        return f"{seconds:.1f}s"
    elif seconds < 3600:
        minutes = seconds / 60
        return f"{minutes:.1f}m"
    else:
        hours = seconds / 3600
        return f"{hours:.1f}h"

def format_large_number(number: int) -> str:
    """Format large numbers with appropriate suffixes
    
    Args:
        number: Number to format
        
    Returns:
        Formatted number string
    """
    if number >= 1_000_000_000:
        return f"{number/1_000_000_000:.1f}B"
    elif number >= 1_000_000:
        return f"{number/1_000_000:.1f}M"
    elif number >= 1_000:
        return f"{number/1_000:.1f}K"
    else:
        return str(number)

def format_confidence_level(confidence: float) -> Dict[str, str]:
    """Format confidence level with color coding
    
    Args:
        confidence: Confidence value (0-100)
        
    Returns:
        Dictionary with formatted value and color
    """
    if confidence >= 90:
        return {"value": f"{confidence:.1f}%", "color": "#10b981", "level": "High"}
    elif confidence >= 70:
        return {"value": f"{confidence:.1f}%", "color": "#f59e0b", "level": "Medium"}
    else:
        return {"value": f"{confidence:.1f}%", "color": "#ef4444", "level": "Low"}

def format_agent_status(status: str) -> Dict[str, str]:
    """Format agent status with appropriate styling
    
    Args:
        status: Agent status string
        
    Returns:
        Dictionary with formatted status and styling
    """
    status_map = {
        "active": {"display": "🟢 Active", "color": "#10b981"},
        "busy": {"display": "🟡 Busy", "color": "#f59e0b"},
        "idle": {"display": "⚪ Idle", "color": "#6b7280"},
        "error": {"display": "🔴 Error", "color": "#ef4444"},
        "offline": {"display": "⚫ Offline", "color": "#374151"}
    }
    
    return status_map.get(status.lower(), {"display": status, "color": "#6b7280"})

def format_escalation_tier(tier: str) -> Dict[str, str]:
    """Format escalation tier with styling
    
    Args:
        tier: Escalation tier name
        
    Returns:
        Dictionary with formatted tier and styling
    """
    tier_map = {
        "agent": {"display": "🤖 Agent-Only", "color": "#10b981", "icon": "🤖"},
        "junior": {"display": "👨‍💼 Junior Specialist", "color": "#f59e0b", "icon": "👨‍💼"},
        "senior": {"display": "👔 Senior Partner", "color": "#ef4444", "icon": "👔"}
    }
    
    return tier_map.get(tier.lower(), {"display": tier, "color": "#6b7280", "icon": "❓"})

def format_client_profile_summary(profile_data: Dict[str, Any]) -> str:
    """Format client profile data for summary display
    
    Args:
        profile_data: Client profile dictionary
        
    Returns:
        Formatted summary string
    """
    summary_parts = []
    
    if profile_data.get("client_name"):
        summary_parts.append(f"**Client:** {profile_data['client_name']}")
    
    if profile_data.get("client_type"):
        summary_parts.append(f"**Type:** {profile_data['client_type']}")
    
    if profile_data.get("industry_sector"):
        summary_parts.append(f"**Industry:** {profile_data['industry_sector']}")
    
    if profile_data.get("budget_range"):
        summary_parts.append(f"**Budget:** {profile_data['budget_range']}")
    
    return " | ".join(summary_parts)

def format_decision_metrics(metrics: Dict[str, Any]) -> pd.DataFrame:
    """Format decision metrics for table display
    
    Args:
        metrics: Decision metrics dictionary
        
    Returns:
        Formatted DataFrame
    """
    formatted_data = []
    
    for metric_name, metric_data in metrics.items():
        formatted_data.append({
            "Metric": metric_name.replace("_", " ").title(),
            "Current Value": metric_data.get("current", "N/A"),
            "Previous Value": metric_data.get("previous", "N/A"),
            "Change": f"{metric_data.get('change', 0):+.1f}%",
            "Trend": "↑" if metric_data.get("change", 0) > 0 else "↓" if metric_data.get("change", 0) < 0 else "→"
        })
    
    return pd.DataFrame(formatted_data)

def format_agent_coordination_data(coordination_data: List[Dict[str, Any]]) -> pd.DataFrame:
    """Format agent coordination data for display
    
    Args:
        coordination_data: List of coordination event dictionaries
        
    Returns:
        Formatted DataFrame
    """
    formatted_data = []
    
    for event in coordination_data:
        formatted_data.append({
            "Timestamp": event.get("timestamp", datetime.now()).strftime("%H:%M:%S"),
            "Agent": event.get("agent_name", "Unknown"),
            "Action": event.get("action", "N/A"),
            "Status": format_agent_status(event.get("status", "unknown"))["display"],
            "Confidence": format_confidence_level(event.get("confidence", 0))["value"],
            "Details": event.get("details", "")[:50] + "..." if len(event.get("details", "")) > 50 else event.get("details", "")
        })
    
    return pd.DataFrame(formatted_data)

def format_json_for_display(data: Dict[str, Any], max_depth: int = 3) -> str:
    """Format JSON data for readable display
    
    Args:
        data: Dictionary to format
        max_depth: Maximum nesting depth to display
        
    Returns:
        Formatted JSON string
    """
    def truncate_deep_objects(obj, current_depth=0):
        if current_depth >= max_depth:
            return "..."
        
        if isinstance(obj, dict):
            return {k: truncate_deep_objects(v, current_depth + 1) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [truncate_deep_objects(item, current_depth + 1) for item in obj[:5]]  # Limit list items
        else:
            return obj
    
    truncated_data = truncate_deep_objects(data)
    return json.dumps(truncated_data, indent=2, default=str)

def format_time_series_data(data: List[Dict[str, Any]], time_field: str = "timestamp") -> pd.DataFrame:
    """Format time series data for chart display
    
    Args:
        data: List of time series data points
        time_field: Name of the timestamp field
        
    Returns:
        Formatted DataFrame with datetime index
    """
    df = pd.DataFrame(data)
    
    if time_field in df.columns:
        df[time_field] = pd.to_datetime(df[time_field])
        df = df.set_index(time_field)
    
    return df

def create_summary_statistics(data: pd.DataFrame, numeric_columns: List[str] = None) -> Dict[str, Any]:
    """Create summary statistics for numeric data
    
    Args:
        data: DataFrame to analyze
        numeric_columns: List of numeric columns to analyze
        
    Returns:
        Dictionary of summary statistics
    """
    if numeric_columns is None:
        numeric_columns = data.select_dtypes(include=['number']).columns.tolist()
    
    summary = {}
    
    for col in numeric_columns:
        if col in data.columns:
            summary[col] = {
                "mean": data[col].mean(),
                "median": data[col].median(),
                "std": data[col].std(),
                "min": data[col].min(),
                "max": data[col].max(),
                "count": data[col].count()
            }
    
    return summary

def format_escalation_flow_data(flow_data: Dict[str, Any]) -> List[Dict[str, str]]:
    """Format escalation flow data for step-by-step display
    
    Args:
        flow_data: Escalation flow dictionary
        
    Returns:
        List of formatted flow steps
    """
    steps = []
    
    # Initial assessment
    steps.append({
        "step": "1",
        "title": "Initial Assessment",
        "description": f"Confidence: {flow_data.get('confidence', 0):.1f}%",
        "status": "completed"
    })
    
    # Complexity analysis
    steps.append({
        "step": "2", 
        "title": "Complexity Analysis",
        "description": f"Level: {flow_data.get('complexity', 'Unknown')}",
        "status": "completed"
    })
    
    # Risk evaluation
    steps.append({
        "step": "3",
        "title": "Risk Evaluation", 
        "description": f"Risk: {flow_data.get('risk_level', 'Unknown')}",
        "status": "completed"
    })
    
    # Final routing decision
    tier = flow_data.get('final_tier', 'unknown')
    tier_info = format_escalation_tier(tier)
    
    steps.append({
        "step": "4",
        "title": "Routing Decision",
        "description": f"Route to: {tier_info['display']}",
        "status": "active"
    })
    
    return steps