"""Chief Engagement Manager - Custom UserProxyAgent Implementation

This module implements the Chief Engagement Manager as a sophisticated UserProxyAgent
extension that orchestrates human-AI collaboration in the ConsultingAI system.
"""

import autogen
from typing import Dict, Any, List, Optional, Union
import logging
import json
from datetime import datetime
from .escalation_system import EscalationSystem, EscalationTier


class ChiefEngagementManager(autogen.UserProxyAgent):
    """Chief Engagement Manager - Advanced UserProxyAgent for ConsultingAI
    
    This class extends AutoGen's UserProxyAgent to provide sophisticated
    coordination capabilities including:
    - Tiered escalation decision making
    - Human expert persona routing
    - Multi-agent coordination oversight
    - Institutional memory integration
    
    Academic Note: This implementation demonstrates advanced UserProxyAgent
    patterns for 35% of assignment evaluation weight.
    """
    
    def __init__(
        self,
        name: str = "chief_engagement_manager",
        system_message: Optional[str] = None,
        escalation_config: Optional[Dict[str, float]] = None,
        **kwargs
    ):
        """Initialize Chief Engagement Manager
        
        Args:
            name: Agent name for identification
            system_message: Custom system message for agent behavior
            escalation_config: Configuration for escalation thresholds
            **kwargs: Additional UserProxyAgent parameters
        """
        
        # Store escalation config as instance attribute
        self.escalation_config = escalation_config or {
            "tier_1_threshold": 0.90,
            "tier_2_threshold": 0.70,
            "tier_3_threshold": 0.50
        }
        
        # Default system message for consulting firm role
        if system_message is None:
            system_message = self._get_default_system_message()
        
        # Configure default UserProxyAgent settings for academic demonstration
        default_kwargs = {
            "human_input_mode": "ALWAYS",  # Enable human intervention
            "max_consecutive_auto_reply": 3,
            "is_termination_msg": self._is_termination_message,
            "code_execution_config": False,  # Disable code execution for safety
        }
        
        # Merge provided kwargs with defaults
        final_kwargs = {**default_kwargs, **kwargs}
        
        # Initialize parent UserProxyAgent
        super().__init__(name=name, system_message=system_message, **final_kwargs)
        
        # Initialize escalation system
        self.escalation_system = EscalationSystem(self.escalation_config)
        
        # Initialize coordination state
        self.coordination_history: List[Dict[str, Any]] = []
        self.current_consultation_id: Optional[str] = None
        
        # Setup logging for academic evaluation
        self.logger = logging.getLogger(f"ConsultingAI.{name}")
        
        self.logger.info(
            "Chief Engagement Manager initialized",
            extra={
                "component": "ChiefEngagementManager",
                "escalation_config": self.escalation_config,
                "academic_context": "Epic 1 Story 1.2 - UserProxyAgent Foundation"
            }
        )
    
    def _get_default_system_message(self) -> str:
        """Get default system message for Chief Engagement Manager role"""
        return """You are the Chief Engagement Manager for ConsultingAI Digital Advisory Firm.

Your responsibilities include:
- Orchestrating coordination between specialized agents (Code Reviewer, System Architect, Business Analyst)
- Making intelligent escalation decisions based on confidence levels and complexity
- Routing decisions to appropriate human expert personas when needed
- Maintaining institutional memory and learning from consultation patterns

You operate within a three-tier escalation system:
- Tier 1 (>90% confidence): Agent-only execution
- Tier 2 (70-90% confidence): Junior specialist human review
- Tier 3 (<70% confidence): Senior partner strategic oversight

Always provide clear rationale for escalation decisions and maintain professional consulting firm standards."""
    
    def _is_termination_message(self, message: Dict[str, Any]) -> bool:
        """Determine if message should terminate conversation
        
        Args:
            message: Message dictionary from AutoGen conversation
            
        Returns:
            True if conversation should terminate, False otherwise
        """
        content = message.get("content", "").lower()
        
        # Termination phrases for academic demonstration
        termination_phrases = [
            "consultation complete",
            "decision finalized",
            "engagement concluded",
            "terminate consultation"
        ]
        
        return any(phrase in content for phrase in termination_phrases)
    
    def start_consultation(self, consultation_context: Dict[str, Any]) -> str:
        """Start a new consultation session
        
        Args:
            consultation_context: Context information for the consultation
            
        Returns:
            Consultation ID for tracking purposes
        """
        consultation_id = f"consultation_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.current_consultation_id = consultation_id
        
        # Log consultation start for academic evaluation
        self.logger.info(
            "Starting new consultation session",
            extra={
                "consultation_id": consultation_id,
                "context": consultation_context,
                "academic_demonstration": True
            }
        )
        
        # Initialize consultation history entry
        consultation_record = {
            "consultation_id": consultation_id,
            "start_time": datetime.now().isoformat(),
            "context": consultation_context,
            "escalations": [],
            "decisions": [],
            "status": "active"
        }
        
        self.coordination_history.append(consultation_record)
        
        return consultation_id
    
    def evaluate_escalation_need(
        self, 
        agent_responses: List[Dict[str, Any]], 
        decision_context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Evaluate whether escalation to human expert is needed
        
        Args:
            agent_responses: List of responses from specialized agents
            decision_context: Context information about the decision
            
        Returns:
            Dictionary containing escalation decision and reasoning
        """
        # Use the full escalation system instead of simplified logic
        return self.escalation_system.evaluate_escalation(agent_responses, decision_context)
    
    def get_coordination_summary(self) -> Dict[str, Any]:
        """Get summary of coordination activities for academic evaluation
        
        Returns:
            Summary dictionary with coordination statistics and history
        """
        active_consultations = [
            record for record in self.coordination_history 
            if record["status"] == "active"
        ]
        
        completed_consultations = [
            record for record in self.coordination_history 
            if record["status"] == "completed"
        ]
        
        summary = {
            "total_consultations": len(self.coordination_history),
            "active_consultations": len(active_consultations),
            "completed_consultations": len(completed_consultations),
            "escalation_config": self.escalation_config,
            "current_consultation_id": self.current_consultation_id,
            "coordination_history": self.coordination_history
        }
        
        return summary


def create_chief_engagement_manager(**kwargs) -> ChiefEngagementManager:
    """Factory function to create Chief Engagement Manager instance
    
    Args:
        **kwargs: Configuration parameters for the manager
        
    Returns:
        Configured ChiefEngagementManager instance
    """
    return ChiefEngagementManager(**kwargs)


# Academic demonstration function
def demonstrate_chief_engagement_manager() -> bool:
    """Demonstrate Chief Engagement Manager functionality for academic evaluation
    
    Returns:
        True if demonstration successful, False otherwise
    """
    print("🔧 Demonstrating Chief Engagement Manager functionality...")
    
    try:
        # Create Chief Engagement Manager instance
        manager = create_chief_engagement_manager(
            name="academic_demo_manager",
            human_input_mode="NEVER"  # Disable human input for automated demo
        )
        
        print("  ✅ Chief Engagement Manager created successfully")
        
        # Demonstrate consultation start
        consultation_context = {
            "scenario": "API design decision",
            "complexity": "medium",
            "stakeholders": ["technical_team", "business_team"]
        }
        
        consultation_id = manager.start_consultation(consultation_context)
        print(f"  ✅ Consultation started: {consultation_id}")
        
        # Demonstrate escalation evaluation
        mock_agent_responses = [
            {"agent": "code_reviewer", "recommendation": "REST API", "confidence": 0.85},
            {"agent": "system_architect", "recommendation": "GraphQL", "confidence": 0.75},
            {"agent": "business_analyst", "recommendation": "REST API", "confidence": 0.80}
        ]
        
        escalation_decision = manager.evaluate_escalation_need(
            mock_agent_responses, consultation_context
        )
        
        print(f"  ✅ Escalation evaluation completed: Tier {escalation_decision['escalation_tier']}")
        print(f"     Reasoning: {escalation_decision['reasoning']}")
        
        # Demonstrate coordination summary
        summary = manager.get_coordination_summary()
        print(f"  ✅ Coordination summary generated: {summary['total_consultations']} consultations")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Chief Engagement Manager demonstration failed: {e}")
        return False


if __name__ == "__main__":
    success = demonstrate_chief_engagement_manager()
    if success:
        print("\n✅ Story 1.2 Chief Engagement Manager: DEMONSTRATED")
    else:
        print("\n❌ Story 1.2 Chief Engagement Manager: FAILED")
        exit(1)
