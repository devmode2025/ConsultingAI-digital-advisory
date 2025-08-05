"""Advanced Human Intervention System - Story 2.3 Implementation

This module implements sophisticated human intervention mechanisms that go beyond
basic approve/reject patterns, enabling rich human-AI collaboration.
"""

from typing import Dict, Any, List, Optional, Union, Callable
from enum import Enum
from datetime import datetime
import logging
import json

try:
    from ..interfaces.human_interaction import HumanInteractionInterface
except ImportError:
    # Handle direct execution
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from interfaces.human_interaction import HumanInteractionInterface


class InterventionType(Enum):
    """Types of human intervention available"""
    APPROVAL_REJECTION = "approval_rejection"
    CONTEXTUAL_GUIDANCE = "contextual_guidance"
    DECISION_OVERRIDE = "decision_override"
    PARTIAL_MODIFICATION = "partial_modification"
    EXPERTISE_CONSULTATION = "expertise_consultation"
    STRATEGIC_DIRECTION = "strategic_direction"


class InterventionMode(Enum):
    """Modes of human intervention"""
    INTERACTIVE = "interactive"      # Real-time human input
    SIMULATED = "simulated"         # Automated for demonstration
    GUIDED = "guided"               # Structured decision support


class ExpertiseContext(Enum):
    """Context for expertise-specific interventions"""
    TECHNICAL_REVIEW = "technical_review"
    ARCHITECTURAL_DECISION = "architectural_decision"
    BUSINESS_ANALYSIS = "business_analysis"
    RISK_ASSESSMENT = "risk_assessment"
    STRATEGIC_PLANNING = "strategic_planning"
    COMPLIANCE_REVIEW = "compliance_review"


class AdvancedHumanInteractionManager:
    """Advanced Human Interaction Manager for sophisticated intervention patterns
    
    This class provides comprehensive human intervention capabilities including:
    - Multiple intervention types beyond approve/reject
    - Context-aware expertise routing
    - Decision modification and override mechanisms
    - Rich feedback collection and learning
    - Simulation modes for academic demonstration
    
    Academic Note: Demonstrates sophisticated human-AI collaboration patterns
    for Epic 2 Story 2.3 - comprehensive human intervention mechanisms.
    """
    
    def __init__(self, intervention_mode: InterventionMode = InterventionMode.SIMULATED):
        """Initialize Advanced Human Interaction Manager
        
        Args:
            intervention_mode: Mode for human interaction (interactive/simulated/guided)
        """
        self.intervention_mode = intervention_mode
        self.intervention_history: List[Dict[str, Any]] = []
        self.expertise_patterns: Dict[str, Any] = {}
        
        # Initialize base interaction interface
        self.base_interface = HumanInteractionInterface("advanced_manager")
        
        # Configure intervention capabilities
        self.available_interventions = {
            InterventionType.APPROVAL_REJECTION: self._handle_approval_rejection,
            InterventionType.CONTEXTUAL_GUIDANCE: self._handle_contextual_guidance,
            InterventionType.DECISION_OVERRIDE: self._handle_decision_override,
            InterventionType.PARTIAL_MODIFICATION: self._handle_partial_modification,
            InterventionType.EXPERTISE_CONSULTATION: self._handle_expertise_consultation,
            InterventionType.STRATEGIC_DIRECTION: self._handle_strategic_direction
        }
        
        # Simulated expert personas for demonstration
        self.simulated_experts = {
            ExpertiseContext.TECHNICAL_REVIEW: "Senior Technical Expert",
            ExpertiseContext.ARCHITECTURAL_DECISION: "Principal System Architect",
            ExpertiseContext.BUSINESS_ANALYSIS: "Strategic Business Analyst",
            ExpertiseContext.RISK_ASSESSMENT: "Risk Management Specialist", 
            ExpertiseContext.STRATEGIC_PLANNING: "Senior Partner",
            ExpertiseContext.COMPLIANCE_REVIEW: "Compliance Officer"
        }
        
        self.logger = logging.getLogger("ConsultingAI.AdvancedHumanInteraction")
        
        self.logger.info(
            "Advanced Human Interaction Manager initialized",
            extra={
                "intervention_mode": intervention_mode.value,
                "available_interventions": len(self.available_interventions),
                "academic_context": "Epic 2 Story 2.3 - Human Intervention Mechanisms"
            }
        )
    
    def request_human_intervention(
        self,
        intervention_request: Dict[str, Any],
        suggested_intervention_type: Optional[InterventionType] = None
    ) -> Dict[str, Any]:
        """Request sophisticated human intervention based on context
        
        Args:
            intervention_request: Detailed request for human intervention
            suggested_intervention_type: Suggested type of intervention needed
            
        Returns:
            Complete intervention result with human input and decision modifications
        """
        intervention_id = self._generate_intervention_id()
        
        self.logger.info(
            "Human intervention requested",
            extra={
                "intervention_id": intervention_id,
                "request_context": intervention_request,
                "suggested_type": suggested_intervention_type.value if suggested_intervention_type else None,
                "academic_demonstration": "human_intervention_capabilities"
            }
        )
        
        # Analyze intervention context and determine best approach
        intervention_analysis = self._analyze_intervention_context(
            intervention_request, suggested_intervention_type
        )
        
        # Select appropriate intervention type
        selected_intervention = intervention_analysis["recommended_intervention"]
        expertise_context = intervention_analysis["expertise_context"]
        
        # Execute the intervention
        intervention_handler = self.available_interventions[selected_intervention]
        intervention_result = intervention_handler(
            intervention_request, expertise_context, intervention_id
        )
        
        # Enhance result with metadata
        complete_result = {
            "intervention_id": intervention_id,
            "timestamp": datetime.now().isoformat(),
            "intervention_type": selected_intervention,
            "expertise_context": expertise_context,
            "intervention_analysis": intervention_analysis,
            "human_input": intervention_result,
            "intervention_mode": self.intervention_mode,
            "request_context": intervention_request
        }
        
        # Store for learning and analytics
        self.intervention_history.append(complete_result)
        self._update_expertise_patterns(complete_result)
        
        self.logger.info(
            "Human intervention completed",
            extra={
                "intervention_result": complete_result,
                "academic_evaluation": "human_ai_collaboration"
            }
        )
        
        return complete_result
    
    def _analyze_intervention_context(
        self,
        request: Dict[str, Any],
        suggested_type: Optional[InterventionType]
    ) -> Dict[str, Any]:
        """Analyze intervention context to determine best approach
        
        Args:
            request: Intervention request details
            suggested_type: Suggested intervention type
            
        Returns:
            Analysis of intervention context with recommendations
        """
        decision_context = request.get("decision_context", {})
        escalation_info = request.get("escalation_info", {})
        agent_recommendations = request.get("agent_recommendations", [])
        
        # Determine expertise context
        decision_type = decision_context.get("type", "general")
        if "technical" in decision_type.lower():
            expertise_context = ExpertiseContext.TECHNICAL_REVIEW
        elif "architecture" in decision_type.lower():
            expertise_context = ExpertiseContext.ARCHITECTURAL_DECISION
        elif "business" in decision_type.lower():
            expertise_context = ExpertiseContext.BUSINESS_ANALYSIS
        elif "strategic" in decision_type.lower():
            expertise_context = ExpertiseContext.STRATEGIC_PLANNING
        else:
            expertise_context = ExpertiseContext.TECHNICAL_REVIEW
        
        # Determine intervention complexity
        escalation_tier = escalation_info.get("escalation_tier", "JUNIOR_SPECIALIST")
        consensus_quality = request.get("consensus_analysis", {}).get("quality_score", 0.5)
        
        # Recommend intervention type
        if suggested_type:
            recommended_intervention = suggested_type
        elif escalation_tier == "SENIOR_PARTNER":
            recommended_intervention = InterventionType.STRATEGIC_DIRECTION
        elif consensus_quality < 0.3:
            recommended_intervention = InterventionType.DECISION_OVERRIDE
        elif len(agent_recommendations) > 1:
            recommended_intervention = InterventionType.PARTIAL_MODIFICATION
        else:
            recommended_intervention = InterventionType.APPROVAL_REJECTION
        
        return {
            "expertise_context": expertise_context,
            "recommended_intervention": recommended_intervention,
            "intervention_complexity": self._assess_intervention_complexity(request),
            "context_factors": {
                "decision_type": decision_type,
                "escalation_tier": escalation_tier,
                "consensus_quality": consensus_quality,
                "agent_count": len(agent_recommendations)
            }
        }
    
    def _assess_intervention_complexity(self, request: Dict[str, Any]) -> str:
        """Assess complexity of intervention required"""
        escalation_info = request.get("escalation_info", {})
        decision_context = request.get("decision_context", {})
        
        risk_level = escalation_info.get("risk_analysis", {}).get("overall_risk_level", "medium")
        business_impact = decision_context.get("business_impact", "medium")
        stakeholder_count = len(decision_context.get("stakeholders", []))
        
        complexity_score = 0
        if risk_level in ["high", "critical"]:
            complexity_score += 2
        if business_impact == "high":
            complexity_score += 2
        if stakeholder_count > 3:
            complexity_score += 1
        
        if complexity_score >= 4:
            return "high"
        elif complexity_score >= 2:
            return "medium"
        else:
            return "low"
    
    def _handle_approval_rejection(
        self,
        request: Dict[str, Any],
        expertise_context: ExpertiseContext,
        intervention_id: str
    ) -> Dict[str, Any]:
        """Handle approval/rejection intervention"""
        
        if self.intervention_mode == InterventionMode.SIMULATED:
            return self._simulate_approval_rejection(request, expertise_context)
        else:
            return self._interactive_approval_rejection(request, expertise_context)
    
    def _simulate_approval_rejection(
        self,
        request: Dict[str, Any],
        expertise_context: ExpertiseContext
    ) -> Dict[str, Any]:
        """Simulate approval/rejection decision for demonstration"""
        
        escalation_info = request.get("escalation_info", {})
        consensus_quality = request.get("consensus_analysis", {}).get("quality_score", 0.5)
        overall_confidence = escalation_info.get("confidence_analysis", {}).get("overall_confidence", 0.5)
        
        # Simulate decision based on confidence and consensus
        if overall_confidence > 0.8 and consensus_quality > 0.7:
            decision = "approved"
            confidence = 0.9
            rationale = "High agent confidence and strong consensus support approval"
        elif overall_confidence < 0.6 or consensus_quality < 0.4:
            decision = "rejected"
            confidence = 0.8
            rationale = "Low confidence or poor consensus requires alternative approach"
        else:
            decision = "approved_with_conditions"
            confidence = 0.7
            rationale = "Moderate confidence allows approval with additional monitoring"
        
        return {
            "intervention_type": "approval_rejection",
            "decision": decision,
            "confidence": confidence,
            "rationale": rationale,
            "expert_persona": self.simulated_experts[expertise_context],
            "additional_conditions": self._generate_approval_conditions(decision, request)
        }
    
    def _interactive_approval_rejection(
        self,
        request: Dict[str, Any],
        expertise_context: ExpertiseContext
    ) -> Dict[str, Any]:
        """Handle interactive approval/rejection"""
        
        agent_recommendations = request.get("agent_recommendations", [])
        escalation_info = request.get("escalation_info", {})
        
        prompt = f"Review the following recommendation for {expertise_context.value}:\n\n"
        
        for i, rec in enumerate(agent_recommendations, 1):
            prompt += f"{i}. {rec.get('agent', 'Agent')}: {rec.get('recommendation', 'No recommendation')}\n"
            prompt += f"   Confidence: {rec.get('confidence', 0):.1%}\n"
            prompt += f"   Rationale: {rec.get('rationale', 'No rationale provided')}\n\n"
        
        prompt += f"Escalation Reasoning: {escalation_info.get('escalation_reasoning', 'No reasoning provided')}\n\n"
        prompt += "Please provide your decision (approve/reject/approve_with_conditions) and rationale:"
        
        response = self.base_interface.request_human_input(
            prompt, 
            request.get("decision_context", {}),
            "approval_rejection"
        )
        
        return {
            "intervention_type": "approval_rejection",
            "raw_response": response,
            "expert_persona": self.simulated_experts[expertise_context],
            "parsed_decision": self._parse_approval_response(response)
        }
    
    def _handle_contextual_guidance(
        self,
        request: Dict[str, Any],
        expertise_context: ExpertiseContext,
        intervention_id: str
    ) -> Dict[str, Any]:
        """Handle contextual guidance provision"""
        
        if self.intervention_mode == InterventionMode.SIMULATED:
            return self._simulate_contextual_guidance(request, expertise_context)
        else:
            return self._interactive_contextual_guidance(request, expertise_context)
    
    def _simulate_contextual_guidance(
        self,
        request: Dict[str, Any],
        expertise_context: ExpertiseContext
    ) -> Dict[str, Any]:
        """Simulate contextual guidance for demonstration"""
        
        decision_context = request.get("decision_context", {})
        decision_type = decision_context.get("type", "general")
        
        # Generate context-specific guidance
        guidance_templates = {
            ExpertiseContext.TECHNICAL_REVIEW: {
                "key_considerations": ["Performance implications", "Security requirements", "Maintainability"],
                "recommended_approach": "Focus on technical feasibility and long-term maintenance",
                "risk_factors": ["Implementation complexity", "Technology maturity"],
                "success_criteria": ["Code quality metrics", "Performance benchmarks"]
            },
            ExpertiseContext.ARCHITECTURAL_DECISION: {
                "key_considerations": ["Scalability requirements", "Integration complexity", "Future extensibility"],
                "recommended_approach": "Balance current needs with future architectural vision",
                "risk_factors": ["Vendor lock-in", "Migration complexity"],
                "success_criteria": ["System performance", "Development velocity"]
            },
            ExpertiseContext.BUSINESS_ANALYSIS: {
                "key_considerations": ["Stakeholder impact", "ROI implications", "Timeline constraints"],
                "recommended_approach": "Align technical solution with business objectives",
                "risk_factors": ["Market timing", "Resource availability"],
                "success_criteria": ["User satisfaction", "Business metrics"]
            }
        }
        
        template = guidance_templates.get(expertise_context, guidance_templates[ExpertiseContext.TECHNICAL_REVIEW])
        
        return {
            "intervention_type": "contextual_guidance",
            "guidance": template,
            "expert_persona": self.simulated_experts[expertise_context],
            "context_specific_advice": self._generate_specific_advice(decision_context, expertise_context),
            "recommended_next_steps": self._recommend_next_steps(request, template)
        }
    
    def _handle_decision_override(
        self,
        request: Dict[str, Any],
        expertise_context: ExpertiseContext,
        intervention_id: str
    ) -> Dict[str, Any]:
        """Handle decision override intervention"""
        
        if self.intervention_mode == InterventionMode.SIMULATED:
            return self._simulate_decision_override(request, expertise_context)
        else:
            return self._interactive_decision_override(request, expertise_context)
    
    def _simulate_decision_override(
        self,
        request: Dict[str, Any],
        expertise_context: ExpertiseContext
    ) -> Dict[str, Any]:
        """Simulate decision override for demonstration"""
        
        agent_recommendations = request.get("agent_recommendations", [])
        decision_context = request.get("decision_context", {})
        
        # Generate alternative recommendation based on expertise context
        override_recommendations = {
            ExpertiseContext.TECHNICAL_REVIEW: "Implement proof-of-concept before full deployment",
            ExpertiseContext.ARCHITECTURAL_DECISION: "Adopt hybrid approach combining best elements from options",
            ExpertiseContext.BUSINESS_ANALYSIS: "Prioritize MVP with phased feature rollout",
            ExpertiseContext.STRATEGIC_PLANNING: "Establish strategic working group for comprehensive analysis",
            ExpertiseContext.RISK_ASSESSMENT: "Implement enhanced risk mitigation before proceeding"
        }
        
        override_recommendation = override_recommendations.get(
            expertise_context, 
            "Re-evaluate approach with additional stakeholder input"
        )
        
        return {
            "intervention_type": "decision_override",
            "original_recommendations": [rec.get("recommendation") for rec in agent_recommendations],
            "override_recommendation": override_recommendation,
            "override_rationale": self._generate_override_rationale(request, expertise_context),
            "confidence": 0.85,
            "expert_persona": self.simulated_experts[expertise_context],
            "implementation_guidance": self._provide_implementation_guidance(override_recommendation)
        }
    
    def _handle_partial_modification(
        self,
        request: Dict[str, Any],
        expertise_context: ExpertiseContext,
        intervention_id: str
    ) -> Dict[str, Any]:
        """Handle partial modification of recommendations"""
        
        if self.intervention_mode == InterventionMode.SIMULATED:
            return self._simulate_partial_modification(request, expertise_context)
        else:
            return self._interactive_partial_modification(request, expertise_context)
    
    def _simulate_partial_modification(
        self,
        request: Dict[str, Any],
        expertise_context: ExpertiseContext
    ) -> Dict[str, Any]:
        """Simulate partial modification for demonstration"""
        
        agent_recommendations = request.get("agent_recommendations", [])
        
        if not agent_recommendations:
            return {
                "intervention_type": "partial_modification",
                "error": "No recommendations to modify"
            }
        
        # Select primary recommendation to modify
        primary_rec = agent_recommendations[0]
        
        # Generate modifications based on expertise context
        modifications = {
            "original_recommendation": primary_rec.get("recommendation"),
            "modifications": [],
            "rationale": "",
            "confidence_adjustment": 0.0
        }
        
        if expertise_context == ExpertiseContext.TECHNICAL_REVIEW:
            modifications["modifications"] = [
                "Add comprehensive security review",
                "Include performance benchmarking",
                "Enhance error handling and monitoring"
            ]
            modifications["rationale"] = "Technical enhancements needed for production readiness"
            modifications["confidence_adjustment"] = 0.1
        
        elif expertise_context == ExpertiseContext.BUSINESS_ANALYSIS:
            modifications["modifications"] = [
                "Include stakeholder impact assessment",
                "Add ROI analysis and success metrics",
                "Consider phased implementation approach"
            ]
            modifications["rationale"] = "Business considerations require additional analysis"
            modifications["confidence_adjustment"] = 0.05
        
        else:
            modifications["modifications"] = [
                "Add risk assessment and mitigation plan",
                "Include stakeholder review process",
                "Enhance documentation requirements"
            ]
            modifications["rationale"] = "Additional oversight needed for complex decision"
            modifications["confidence_adjustment"] = 0.08
        
        return {
            "intervention_type": "partial_modification",
            "original_recommendation": primary_rec,
            "modifications": modifications,
            "expert_persona": self.simulated_experts[expertise_context],
            "modified_confidence": min(1.0, primary_rec.get("confidence", 0.5) + modifications["confidence_adjustment"])
        }
    
    def _handle_expertise_consultation(
        self,
        request: Dict[str, Any],
        expertise_context: ExpertiseContext,
        intervention_id: str
    ) -> Dict[str, Any]:
        """Handle expertise consultation intervention"""
        
        return {
            "intervention_type": "expertise_consultation",
            "expert_persona": self.simulated_experts[expertise_context],
            "consultation_areas": self._identify_consultation_areas(request, expertise_context),
            "expert_recommendations": self._generate_expert_recommendations(request, expertise_context),
            "follow_up_actions": self._suggest_follow_up_actions(request, expertise_context)
        }
    
    def _handle_strategic_direction(
        self,
        request: Dict[str, Any],
        expertise_context: ExpertiseContext,
        intervention_id: str
    ) -> Dict[str, Any]:
        """Handle strategic direction intervention"""
        
        return {
            "intervention_type": "strategic_direction",
            "expert_persona": self.simulated_experts[ExpertiseContext.STRATEGIC_PLANNING],
            "strategic_context": self._analyze_strategic_context(request),
            "strategic_recommendations": self._provide_strategic_recommendations(request),
            "resource_allocation": self._recommend_resource_allocation(request),
            "timeline_guidance": self._provide_timeline_guidance(request)
        }
    
    # Helper methods for generating simulated responses
    
    def _generate_approval_conditions(self, decision: str, request: Dict[str, Any]) -> List[str]:
        """Generate conditions for approval decisions"""
        if decision == "approved_with_conditions":
            return [
                "Regular progress monitoring required",
                "Stakeholder review at key milestones",
                "Performance metrics tracking"
            ]
        elif decision == "approved":
            return ["Standard monitoring and reporting"]
        else:
            return ["Alternative approach required"]
    
    def _generate_specific_advice(
        self, 
        decision_context: Dict[str, Any], 
        expertise_context: ExpertiseContext
    ) -> str:
        """Generate context-specific advice"""
        decision_type = decision_context.get("type", "general")
        
        advice_templates = {
            ExpertiseContext.TECHNICAL_REVIEW: f"For {decision_type}, prioritize code quality and security",
            ExpertiseContext.ARCHITECTURAL_DECISION: f"Consider long-term scalability implications for {decision_type}",
            ExpertiseContext.BUSINESS_ANALYSIS: f"Ensure {decision_type} aligns with business objectives"
        }
        
        return advice_templates.get(
            expertise_context,
            f"Apply best practices for {decision_type} implementation"
        )
    
    def _recommend_next_steps(self, request: Dict[str, Any], guidance: Dict[str, Any]) -> List[str]:
        """Recommend next steps based on guidance"""
        return [
            "Review guidance with project team",
            "Update implementation plan based on recommendations",
            "Schedule follow-up review session"
        ]
    
    def _generate_override_rationale(
        self, 
        request: Dict[str, Any], 
        expertise_context: ExpertiseContext
    ) -> str:
        """Generate rationale for decision override"""
        escalation_info = request.get("escalation_info", {})
        risk_level = escalation_info.get("risk_analysis", {}).get("overall_risk_level", "medium")
        
        if risk_level in ["high", "critical"]:
            return f"High risk level requires {expertise_context.value} oversight and modified approach"
        else:
            return f"Expert {expertise_context.value} indicates alternative approach would be more effective"
    
    def _provide_implementation_guidance(self, recommendation: str) -> List[str]:
        """Provide implementation guidance for override recommendation"""
        return [
            "Begin with stakeholder alignment session",
            "Develop detailed implementation plan",
            "Establish success criteria and monitoring"
        ]
    
    def _identify_consultation_areas(
        self, 
        request: Dict[str, Any], 
        expertise_context: ExpertiseContext
    ) -> List[str]:
        """Identify areas for expert consultation"""
        base_areas = ["Technical feasibility", "Implementation approach", "Risk assessment"]
        
        context_areas = {
            ExpertiseContext.TECHNICAL_REVIEW: ["Code quality", "Performance optimization"],
            ExpertiseContext.ARCHITECTURAL_DECISION: ["Scalability planning", "Integration strategy"],
            ExpertiseContext.BUSINESS_ANALYSIS: ["Stakeholder impact", "ROI analysis"]
        }
        
        return base_areas + context_areas.get(expertise_context, [])
    
    def _generate_expert_recommendations(
        self, 
        request: Dict[str, Any], 
        expertise_context: ExpertiseContext
    ) -> List[str]:
        """Generate expert recommendations for consultation"""
        return [
            "Conduct thorough analysis of proposed approach",
            "Consider alternative solutions and trade-offs",
            "Engage relevant stakeholders for input"
        ]
    
    def _suggest_follow_up_actions(
        self, 
        request: Dict[str, Any], 
        expertise_context: ExpertiseContext
    ) -> List[str]:
        """Suggest follow-up actions after consultation"""
        return [
            "Schedule expert review session",
            "Prepare detailed technical documentation", 
            "Plan stakeholder communication strategy"
        ]
    
    def _analyze_strategic_context(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze strategic context for senior partner intervention"""
        decision_context = request.get("decision_context", {})
        
        return {
            "business_alignment": "Strategic decision requires senior oversight",
            "organizational_impact": decision_context.get("business_impact", "medium"),
            "resource_implications": "Significant resource allocation decision",
            "timeline_criticality": decision_context.get("timeline", "normal")
        }
    
    def _provide_strategic_recommendations(self, request: Dict[str, Any]) -> List[str]:
        """Provide strategic recommendations"""
        return [
            "Establish cross-functional working group",
            "Conduct comprehensive stakeholder analysis",
            "Develop strategic implementation roadmap",
            "Create success metrics and governance framework"
        ]
    
    def _recommend_resource_allocation(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Recommend resource allocation for strategic decisions"""
        return {
            "human_resources": "Senior technical and business experts",
            "timeline": "Extended timeline for strategic analysis",
            "budget_considerations": "Additional budget for external consultation if needed",
            "governance": "Senior partner oversight throughout implementation"
        }
    
    def _provide_timeline_guidance(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Provide timeline guidance for strategic decisions"""
        return {
            "analysis_phase": "2-3 weeks for comprehensive analysis",
            "decision_phase": "1 week for stakeholder alignment and decision",
            "implementation_phase": "Phased approach over 3-6 months",
            "review_milestones": "Monthly senior partner reviews"
        }
    
    def _parse_approval_response(self, response: str) -> Dict[str, Any]:
        """Parse human approval response"""
        response_lower = response.lower().strip()
        
        if any(word in response_lower for word in ["approve", "accept", "yes"]):
            if "condition" in response_lower:
                decision = "approved_with_conditions"
            else:
                decision = "approved"
        elif any(word in response_lower for word in ["reject", "deny", "no"]):
            decision = "rejected"
        else:
            decision = "unclear"
        
        return {
            "decision": decision,
            "raw_response": response,
            "confidence": 0.8 if decision != "unclear" else 0.3
        }
    
    def _update_expertise_patterns(self, intervention_result: Dict[str, Any]) -> None:
        """Update learned expertise patterns based on intervention results"""
        expertise_context = intervention_result.get("expertise_context")
        intervention_type = intervention_result.get("intervention_type")
        
        if expertise_context not in self.expertise_patterns:
            self.expertise_patterns[expertise_context] = {
                "total_interventions": 0,
                "intervention_types": {},
                "average_confidence": 0.0,
                "common_recommendations": []
            }
        
        pattern = self.expertise_patterns[expertise_context]
        pattern["total_interventions"] += 1
        
        # Update intervention type distribution
        type_name = intervention_type.value if hasattr(intervention_type, 'value') else str(intervention_type)
        pattern["intervention_types"][type_name] = pattern["intervention_types"].get(type_name, 0) + 1
        
        # Track confidence levels
        human_input = intervention_result.get("human_input", {})
        confidence = human_input.get("confidence", 0.5)
        pattern["average_confidence"] = (
            (pattern["average_confidence"] * (pattern["total_interventions"] - 1) + confidence) /
            pattern["total_interventions"]
        )
    
    def _generate_intervention_id(self) -> str:
        """Generate unique intervention ID"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        return f"intervention_{timestamp}"
    
    def get_intervention_analytics(self) -> Dict[str, Any]:
        """Get comprehensive intervention analytics"""
        return {
            "total_interventions": len(self.intervention_history),
            "intervention_mode": self.intervention_mode.value,
            "expertise_patterns": self.expertise_patterns,
            "intervention_type_distribution": self._calculate_intervention_distribution(),
            "average_intervention_quality": self._calculate_average_quality(),
            "recent_interventions": self.intervention_history[-3:]  # Last 3 for brevity
        }
    
    def _calculate_intervention_distribution(self) -> Dict[str, int]:
        """Calculate distribution of intervention types"""
        distribution = {}
        for intervention in self.intervention_history:
            int_type = intervention.get("intervention_type")
            type_name = int_type.value if hasattr(int_type, 'value') else str(int_type)
            distribution[type_name] = distribution.get(type_name, 0) + 1
        return distribution
    
    def _calculate_average_quality(self) -> float:
        """Calculate average quality of interventions"""
        if not self.intervention_history:
            return 0.0
        
        # Simplified quality calculation based on confidence
        total_quality = 0.0
        for intervention in self.intervention_history:
            human_input = intervention.get("human_input", {})
            quality = human_input.get("confidence", 0.5)
            total_quality += quality
        
        return total_quality / len(self.intervention_history)


def create_advanced_human_interaction_manager(**kwargs) -> AdvancedHumanInteractionManager:
   """Factory function to create Advanced Human Interaction Manager
   
   Args:
       **kwargs: Configuration parameters for the manager
       
   Returns:
       Configured AdvancedHumanInteractionManager instance
   """
   return AdvancedHumanInteractionManager(**kwargs)


def demonstrate_advanced_human_intervention() -> bool:
   """Demonstrate advanced human intervention capabilities for Story 2.3
   
   Returns:
       True if demonstration successful, False otherwise
   """
   print("🔧 Demonstrating Advanced Human Intervention Mechanisms...")
   
   try:
       # Create advanced human interaction manager
       manager = create_advanced_human_interaction_manager(
           intervention_mode=InterventionMode.SIMULATED
       )
       
       print("  ✅ Advanced Human Interaction Manager created")
       
       # Test different intervention types
       intervention_scenarios = [
           {
               "name": "Approval/Rejection Scenario",
               "type": InterventionType.APPROVAL_REJECTION,
               "request": {
                   "decision_context": {
                       "type": "technical_implementation",
                       "description": "API authentication implementation",
                       "business_impact": "medium",
                       "stakeholders": ["engineering", "security"]
                   },
                   "agent_recommendations": [
                       {
                           "agent": "security_expert",
                           "recommendation": "OAuth2 with JWT tokens",
                           "confidence": 0.85,
                           "rationale": "Industry standard with good security"
                       }
                   ],
                   "escalation_info": {
                       "escalation_tier": "JUNIOR_SPECIALIST",
                       "confidence_analysis": {"overall_confidence": 0.85}
                   },
                   "consensus_analysis": {"quality_score": 0.8}
               }
           },
           {
               "name": "Decision Override Scenario", 
               "type": InterventionType.DECISION_OVERRIDE,
               "request": {
                   "decision_context": {
                       "type": "architecture_decision",
                       "description": "Database architecture for high-scale application",
                       "business_impact": "high",
                       "stakeholders": ["engineering", "product", "operations"]
                   },
                   "agent_recommendations": [
                       {
                           "agent": "architect_1",
                           "recommendation": "NoSQL document database",
                           "confidence": 0.60,
                           "rationale": "Flexible schema for rapid development"
                       },
                       {
                           "agent": "architect_2", 
                           "recommendation": "Relational database with caching",
                           "confidence": 0.55,
                           "rationale": "Data consistency and mature tooling"
                       }
                   ],
                   "escalation_info": {
                       "escalation_tier": "SENIOR_PARTNER",
                       "risk_analysis": {"overall_risk_level": "high"}
                   },
                   "consensus_analysis": {"quality_score": 0.3}
               }
           },
           {
               "name": "Partial Modification Scenario",
               "type": InterventionType.PARTIAL_MODIFICATION, 
               "request": {
                   "decision_context": {
                       "type": "deployment_strategy",
                       "description": "Production deployment approach",
                       "business_impact": "medium",
                       "stakeholders": ["engineering", "operations"]
                   },
                   "agent_recommendations": [
                       {
                           "agent": "devops_expert",
                           "recommendation": "Blue-green deployment with automated rollback",
                           "confidence": 0.75,
                           "rationale": "Minimizes downtime and provides safety"
                       }
                   ],
                   "escalation_info": {
                       "escalation_tier": "JUNIOR_SPECIALIST"
                   },
                   "consensus_analysis": {"quality_score": 0.6}
               }
           },
           {
               "name": "Strategic Direction Scenario",
               "type": InterventionType.STRATEGIC_DIRECTION,
               "request": {
                   "decision_context": {
                       "type": "strategic_technology_decision",
                       "description": "Enterprise architecture modernization strategy",
                       "business_impact": "high", 
                       "stakeholders": ["engineering", "product", "executives", "customers"],
                       "timeline": "urgent"
                   },
                   "agent_recommendations": [
                       {
                           "agent": "enterprise_architect",
                           "recommendation": "Gradual microservices migration",
                           "confidence": 0.70,
                           "rationale": "Balanced approach managing risk and innovation"
                       }
                   ],
                   "escalation_info": {
                       "escalation_tier": "SENIOR_PARTNER",
                       "risk_analysis": {"overall_risk_level": "critical"}
                   },
                   "consensus_analysis": {"quality_score": 0.4}
               }
           }
       ]
       
       # Execute intervention scenarios
       intervention_results = []
       
       for i, scenario in enumerate(intervention_scenarios, 1):
           print(f"\n  🧪 Scenario {i}: {scenario['name']}")
           
           result = manager.request_human_intervention(
               scenario["request"],
               scenario["type"]
           )
           
           intervention_results.append(result)
           
           # Display results
           intervention_type = result["intervention_type"]
           expertise_context = result["expertise_context"]
           human_input = result["human_input"]
           
           print(f"     Intervention type: {intervention_type.value}")
           print(f"     Expertise context: {expertise_context.value}")
           print(f"     Expert persona: {human_input.get('expert_persona', 'Unknown')}")
           
           # Show type-specific results
           if intervention_type == InterventionType.APPROVAL_REJECTION:
               decision = human_input.get("decision", "unknown")
               confidence = human_input.get("confidence", 0.0)
               print(f"     Decision: {decision} (confidence: {confidence:.1%})")
               
           elif intervention_type == InterventionType.DECISION_OVERRIDE:
               override_rec = human_input.get("override_recommendation", "No override")
               print(f"     Override recommendation: {override_rec}")
               
           elif intervention_type == InterventionType.PARTIAL_MODIFICATION:
               modifications = human_input.get("modifications", {}).get("modifications", [])
               print(f"     Modifications: {len(modifications)} suggested changes")
               
           elif intervention_type == InterventionType.STRATEGIC_DIRECTION:
               strategic_recs = human_input.get("strategic_recommendations", [])
               print(f"     Strategic recommendations: {len(strategic_recs)} strategic actions")
       
       # Test analytics
       analytics = manager.get_intervention_analytics()
       print(f"\n  ✅ Intervention analytics: {analytics['total_interventions']} interventions processed")
       print(f"     Intervention types: {list(analytics['intervention_type_distribution'].keys())}")
       print(f"     Average quality: {analytics['average_intervention_quality']:.2f}")
       
       # Validate results
       expected_types = [
           InterventionType.APPROVAL_REJECTION,
           InterventionType.DECISION_OVERRIDE,
           InterventionType.PARTIAL_MODIFICATION,
           InterventionType.STRATEGIC_DIRECTION
       ]
       
       actual_types = [result["intervention_type"] for result in intervention_results]
       
       success = len(set(actual_types)) == len(expected_types)
       
       if success:
           print("\n  🎯 All intervention types demonstrated successfully!")
           print("     ✅ Approval/Rejection - Basic decision validation")
           print("     ✅ Decision Override - Alternative recommendation provided")
           print("     ✅ Partial Modification - Enhancement suggestions added")
           print("     ✅ Strategic Direction - Senior partner strategic guidance")
       else:
           print(f"\n  ❌ Some intervention types missing or incorrect")
       
       return success
       
   except Exception as e:
       print(f"  ❌ Advanced human intervention demonstration failed: {e}")
       import traceback
       traceback.print_exc()
       return False


if __name__ == "__main__":
   print("🚀 Starting Advanced Human Intervention Demonstration - Story 2.3")
   
   success = demonstrate_advanced_human_intervention()
   if success:
       print("\n✅ Story 2.3: Human Intervention Mechanisms - DEMONSTRATED")
   else:
       print("\n❌ Story 2.3: Human Intervention Mechanisms - FAILED")
       exit(1)
