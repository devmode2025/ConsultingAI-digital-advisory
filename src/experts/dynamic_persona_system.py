"""Dynamic Expert Persona System - Story 3.1 Implementation

This module implements the core framework for dynamic human expert persona switching,
enabling contextual expertise routing with role-specific guidance and interaction patterns.
"""

from typing import Dict, Any, List, Optional, Callable, Union
from enum import Enum
from datetime import datetime
from dataclasses import dataclass, field
import logging
import json


class ExpertPersonaType(Enum):
    """Types of expert personas available in the consulting firm"""
    PYTHON_GURU = "python_guru"
    SYSTEM_ARCHITECT_EXPERT = "system_architect_expert"
    BUSINESS_ANALYST_EXPERT = "business_analyst_expert"
    SECURITY_SPECIALIST = "security_specialist"
    PERFORMANCE_EXPERT = "performance_expert"
    COMPLIANCE_OFFICER = "compliance_officer"
    SENIOR_PARTNER = "senior_partner"


class PersonaSwitchingTrigger(Enum):
    """Triggers that can cause persona switching"""
    DECISION_TYPE_CHANGE = "decision_type_change"
    EXPERTISE_REQUIREMENT = "expertise_requirement"
    ESCALATION_TIER = "escalation_tier"
    STAKEHOLDER_REQUEST = "stakeholder_request"
    CONTEXT_EVOLUTION = "context_evolution"
    MULTI_DOMAIN_NEED = "multi_domain_need"


@dataclass
class ExpertPersonaProfile:
    """Profile definition for an expert persona"""
    persona_type: ExpertPersonaType
    display_name: str
    expertise_domains: List[str]
    decision_frameworks: List[str]
    interaction_style: Dict[str, Any]
    confidence_thresholds: Dict[str, float]
    preferred_contexts: List[str]
    decision_patterns: Dict[str, Any] = field(default_factory=dict)
    interaction_history: List[Dict[str, Any]] = field(default_factory=list)
    performance_metrics: Dict[str, float] = field(default_factory=dict)


@dataclass
class PersonaSwitchingContext:
    """Context information for persona switching decisions"""
    current_persona: Optional[ExpertPersonaType]
    target_persona: ExpertPersonaType
    switching_trigger: PersonaSwitchingTrigger
    decision_context: Dict[str, Any]
    required_expertise: List[str]
    switching_rationale: str
    confidence_score: float
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


class DynamicPersonaManager:
    """Dynamic Expert Persona Management System
    
    This class provides comprehensive persona switching capabilities including:
    - Dynamic persona selection based on decision context
    - Role-specific interaction patterns and guidance
    - Context preservation across persona transitions
    - Learning from persona performance and preferences
    - Multi-domain expertise coordination
    
    Academic Note: Demonstrates advanced human-AI collaboration patterns
    for Epic 3 Story 3.1 - dynamic expertise sourcing framework.
    """
    
    def __init__(self):
        """Initialize Dynamic Persona Manager"""
        self.expert_personas = self._initialize_expert_personas()
        self.current_persona: Optional[ExpertPersonaType] = None
        self.persona_history: List[PersonaSwitchingContext] = []
        self.context_memory: Dict[str, Any] = {}
        
        # Persona switching rules and patterns
        self.switching_rules = self._initialize_switching_rules()
        self.persona_compatibility = self._initialize_persona_compatibility()
        
        # Performance tracking
        self.persona_performance: Dict[ExpertPersonaType, Dict[str, Any]] = {}
        
        self.logger = logging.getLogger("ConsultingAI.DynamicPersonaManager")
        
        self.logger.info(
            "Dynamic Persona Manager initialized",
            extra={
                "available_personas": len(self.expert_personas),
                "persona_types": [p.value for p in ExpertPersonaType],
                "academic_context": "Epic 3 Story 3.1 - Expert Persona Framework"
            }
        )
    
    def _initialize_expert_personas(self) -> Dict[ExpertPersonaType, ExpertPersonaProfile]:
        """Initialize expert persona profiles with detailed characteristics"""
        
        personas = {}
        
        # Python Guru Persona
        personas[ExpertPersonaType.PYTHON_GURU] = ExpertPersonaProfile(
            persona_type=ExpertPersonaType.PYTHON_GURU,
            display_name="Senior Python Development Expert",
            expertise_domains=[
                "python_best_practices", "performance_optimization", "code_quality",
                "testing_strategies", "framework_selection", "library_evaluation"
            ],
            decision_frameworks=[
                "pythonic_patterns", "performance_analysis", "maintainability_assessment",
                "security_review", "testing_pyramid"
            ],
            interaction_style={
                "communication_tone": "technical_detailed",
                "decision_approach": "evidence_based_analytical",
                "preferred_detail_level": "high_technical_detail",
                "example_preference": "code_examples_required",
                "documentation_style": "comprehensive_technical"
            },
            confidence_thresholds={
                "python_implementation": 0.9,
                "performance_optimization": 0.85,
                "code_review": 0.9,
                "testing_strategy": 0.8,
                "general_technical": 0.7
            },
            preferred_contexts=[
                "code_implementation", "performance_issues", "python_specific",
                "technical_architecture", "development_practices"
            ]
        )
        
        # System Architect Expert Persona
        personas[ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT] = ExpertPersonaProfile(
            persona_type=ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT,
            display_name="Principal System Architecture Specialist",
            expertise_domains=[
                "system_design", "scalability_architecture", "integration_patterns",
                "cloud_architecture", "microservices_design", "data_architecture"
            ],
            decision_frameworks=[
                "architectural_patterns", "scalability_analysis", "integration_strategy",
                "technology_selection", "system_design_principles"
            ],
            interaction_style={
                "communication_tone": "strategic_technical",
                "decision_approach": "holistic_systems_thinking",
                "preferred_detail_level": "architectural_overview_with_details",
                "example_preference": "architecture_diagrams_preferred",
                "documentation_style": "strategic_with_implementation_guidance"
            },
            confidence_thresholds={
                "system_architecture": 0.9,
                "scalability_design": 0.85,
                "integration_planning": 0.8,
                "technology_selection": 0.85,
                "cloud_strategy": 0.8
            },
            preferred_contexts=[
                "system_design", "architecture_decisions", "scalability_planning",
                "integration_challenges", "technology_strategy"
            ]
        )
        
        # Business Analyst Expert Persona
        personas[ExpertPersonaType.BUSINESS_ANALYST_EXPERT] = ExpertPersonaProfile(
            persona_type=ExpertPersonaType.BUSINESS_ANALYST_EXPERT,
            display_name="Strategic Business Analysis Consultant",
            expertise_domains=[
                "requirements_analysis", "stakeholder_management", "business_process_optimization",
                "roi_analysis", "change_management", "compliance_requirements"
            ],
            decision_frameworks=[
                "business_value_analysis", "stakeholder_impact_assessment", "risk_benefit_analysis",
                "process_optimization", "compliance_framework"
            ],
            interaction_style={
                "communication_tone": "business_focused_strategic",
                "decision_approach": "stakeholder_value_optimization",
                "preferred_detail_level": "business_impact_with_technical_context",
                "example_preference": "business_case_examples",
                "documentation_style": "executive_summary_with_details"
            },
            confidence_thresholds={
                "business_analysis": 0.9,
                "stakeholder_management": 0.85,
                "requirements_gathering": 0.85,
                "process_optimization": 0.8,
                "compliance_assessment": 0.75
            },
            preferred_contexts=[
                "business_requirements", "stakeholder_decisions", "process_improvements",
                "compliance_issues", "strategic_planning"
            ]
        )
        
        # Security Specialist Persona
        personas[ExpertPersonaType.SECURITY_SPECIALIST] = ExpertPersonaProfile(
            persona_type=ExpertPersonaType.SECURITY_SPECIALIST,
            display_name="Cybersecurity and Compliance Expert",
            expertise_domains=[
                "security_architecture", "vulnerability_assessment", "compliance_frameworks",
                "incident_response", "risk_assessment", "security_protocols"
            ],
            decision_frameworks=[
                "security_risk_assessment", "compliance_validation", "threat_modeling",
                "security_architecture_review", "incident_response_planning"
            ],
            interaction_style={
                "communication_tone": "security_focused_precise",
                "decision_approach": "risk_mitigation_priority",
                "preferred_detail_level": "security_implementation_specific",
                "example_preference": "security_patterns_and_examples",
                "documentation_style": "security_policy_comprehensive"
            },
            confidence_thresholds={
                "security_architecture": 0.9,
                "vulnerability_assessment": 0.85,
                "compliance_review": 0.8,
                "incident_response": 0.85,
                "risk_assessment": 0.8
            },
            preferred_contexts=[
                "security_decisions", "compliance_requirements", "vulnerability_issues",
                "incident_response", "risk_management"
            ]
        )
        
        # Senior Partner Persona
        personas[ExpertPersonaType.SENIOR_PARTNER] = ExpertPersonaProfile(
            persona_type=ExpertPersonaType.SENIOR_PARTNER,
            display_name="Senior Partner - Strategic Oversight",
            expertise_domains=[
                "strategic_leadership", "executive_decision_making", "organizational_transformation",
                "high_stakes_negotiations", "crisis_management", "strategic_partnerships"
            ],
            decision_frameworks=[
                "strategic_impact_analysis", "executive_decision_framework", "organizational_change_management",
                "stakeholder_alignment", "strategic_risk_management"
            ],
            interaction_style={
                "communication_tone": "executive_strategic",
                "decision_approach": "strategic_value_optimization",
                "preferred_detail_level": "executive_summary_with_strategic_context",
                "example_preference": "strategic_case_studies",
                "documentation_style": "executive_briefing_comprehensive"
            },
            confidence_thresholds={
                "strategic_decisions": 0.9,
                "executive_oversight": 0.85,
                "organizational_change": 0.8,
                "crisis_management": 0.85,
                "strategic_partnerships": 0.8
            },
            preferred_contexts=[
                "strategic_decisions", "executive_oversight", "organizational_transformation",
                "crisis_situations", "high_stakes_decisions"
            ]
        )
        
        return personas
    
    def _initialize_switching_rules(self) -> Dict[str, Any]:
        """Initialize persona switching rules and logic"""
        return {
            "decision_type_mapping": {
                "code_implementation": ExpertPersonaType.PYTHON_GURU,
                "architecture_design": ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT,
                "business_requirements": ExpertPersonaType.BUSINESS_ANALYST_EXPERT,
                "security_review": ExpertPersonaType.SECURITY_SPECIALIST,
                "strategic_planning": ExpertPersonaType.SENIOR_PARTNER
            },
            "escalation_tier_mapping": {
                "JUNIOR_SPECIALIST": [
                    ExpertPersonaType.PYTHON_GURU,
                    ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT,
                    ExpertPersonaType.BUSINESS_ANALYST_EXPERT
                ],
                "SENIOR_PARTNER": [
                    ExpertPersonaType.SENIOR_PARTNER,
                    ExpertPersonaType.SECURITY_SPECIALIST
                ]
            },
            "complexity_thresholds": {
                "simple": 0.3,
                "moderate": 0.6,
                "complex": 0.8
            },
            "multi_domain_triggers": {
                "technical_business": [
                    ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT,
                    ExpertPersonaType.BUSINESS_ANALYST_EXPERT
                ],
                "security_compliance": [
                    ExpertPersonaType.SECURITY_SPECIALIST,
                    ExpertPersonaType.BUSINESS_ANALYST_EXPERT
                ]
            }
        }
    
    def _initialize_persona_compatibility(self) -> Dict[ExpertPersonaType, List[ExpertPersonaType]]:
        """Initialize persona compatibility matrix for multi-expert scenarios"""
        return {
            ExpertPersonaType.PYTHON_GURU: [
                ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT,
                ExpertPersonaType.SECURITY_SPECIALIST
            ],
            ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT: [
                ExpertPersonaType.PYTHON_GURU,
                ExpertPersonaType.BUSINESS_ANALYST_EXPERT,
                ExpertPersonaType.SECURITY_SPECIALIST,
                ExpertPersonaType.SENIOR_PARTNER
            ],
            ExpertPersonaType.BUSINESS_ANALYST_EXPERT: [
                ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT,
                ExpertPersonaType.SENIOR_PARTNER,
                ExpertPersonaType.SECURITY_SPECIALIST
            ],
            ExpertPersonaType.SECURITY_SPECIALIST: [
                ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT,
                ExpertPersonaType.BUSINESS_ANALYST_EXPERT,
                ExpertPersonaType.SENIOR_PARTNER
            ],
            ExpertPersonaType.SENIOR_PARTNER: [
                ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT,
                ExpertPersonaType.BUSINESS_ANALYST_EXPERT,
                ExpertPersonaType.SECURITY_SPECIALIST
            ]
        }
    
    def select_optimal_persona(
        self,
        decision_context: Dict[str, Any],
        current_persona: Optional[ExpertPersonaType] = None,
        required_expertise: Optional[List[str]] = None
    ) -> PersonaSwitchingContext:
        """Select optimal expert persona based on decision context
        
        Args:
            decision_context: Context information about the decision
            current_persona: Currently active persona (if any)
            required_expertise: Specific expertise requirements
            
        Returns:
            PersonaSwitchingContext with selected persona and rationale
        """
        # Analyze decision context for persona requirements
        context_analysis = self._analyze_decision_context(decision_context)
        
        # Determine candidate personas
        candidate_personas = self._identify_candidate_personas(
            context_analysis, required_expertise
        )
        
        # Score candidates based on context fit
        persona_scores = self._score_persona_candidates(
            candidate_personas, context_analysis, decision_context
        )
        
        # Select optimal persona
        optimal_persona = max(persona_scores.items(), key=lambda x: x[1]["total_score"])[0]
        
        # Determine switching trigger and rationale
        switching_context = self._create_switching_context(
            current_persona, optimal_persona, context_analysis, 
            persona_scores[optimal_persona], decision_context
        )
        
        return switching_context
    
    def execute_persona_switch(
        self, 
        switching_context: PersonaSwitchingContext
    ) -> Dict[str, Any]:
        """Execute persona switching with context preservation
        
        Args:
            switching_context: Context for the persona switch
            
        Returns:
            Switch execution result with new persona configuration
        """
        previous_persona = self.current_persona
        target_persona = switching_context.target_persona
        
        # Update current persona
        self.current_persona = target_persona
        
        # Preserve context across switch
        self._preserve_context_across_switch(switching_context)
        
        # Configure new persona environment
        persona_config = self._configure_persona_environment(target_persona, switching_context)
        
        # Log persona switch
        self.persona_history.append(switching_context)
        
        # Update persona performance tracking
        self._update_persona_tracking(target_persona, switching_context)
        
        switch_result = {
            "switch_id": self._generate_switch_id(),
            "timestamp": datetime.now().isoformat(),
            "previous_persona": previous_persona.value if previous_persona else None,
            "new_persona": target_persona.value,
            "switching_trigger": switching_context.switching_trigger.value,
            "switching_rationale": switching_context.switching_rationale,
            "confidence_score": switching_context.confidence_score,
            "persona_configuration": persona_config,
            "context_preserved": True,
            "switch_successful": True
        }
        
        self.logger.info(
            "Persona switch executed",
            extra={
                "switch_result": switch_result,
                "academic_demonstration": "dynamic_persona_switching"
            }
        )
        
        return switch_result
    
    def get_current_persona_interface(self) -> Dict[str, Any]:
        """Get current persona interface configuration and guidance
        
        Returns:
            Current persona interface setup with role-specific guidance
        """
        if not self.current_persona:
            return {"error": "No active persona"}
        
        persona_profile = self.expert_personas[self.current_persona]
        
        interface_config = {
            "persona_type": self.current_persona.value,
            "display_name": persona_profile.display_name,
            "expertise_domains": persona_profile.expertise_domains,
            "decision_frameworks": persona_profile.decision_frameworks,
            "interaction_style": persona_profile.interaction_style,
            "confidence_thresholds": persona_profile.confidence_thresholds,
            "role_specific_guidance": self._generate_role_guidance(persona_profile),
            "decision_support_tools": self._get_decision_support_tools(persona_profile),
            "context_awareness": self._get_context_awareness(persona_profile)
        }
        
        return interface_config
    
    def _analyze_decision_context(self, decision_context: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze decision context for persona selection"""
        decision_type = decision_context.get("type", "general")
        complexity = decision_context.get("complexity", "medium")
        business_impact = decision_context.get("business_impact", "medium")
        stakeholders = decision_context.get("stakeholders", [])
        
        # Analyze required expertise domains
        required_domains = []
        if "technical" in decision_type.lower():
            required_domains.extend(["technical_implementation", "code_quality"])
        if "architecture" in decision_type.lower():
            required_domains.extend(["system_design", "scalability"])
        if "business" in decision_type.lower():
            required_domains.extend(["business_analysis", "stakeholder_management"])
        if "security" in decision_type.lower():
            required_domains.extend(["security_architecture", "compliance"])
        
        # Assess decision complexity
        complexity_score = {
            "low": 0.2, "medium": 0.5, "high": 0.8, "very_high": 0.9
        }.get(complexity, 0.5)
        
        return {
            "decision_type": decision_type,
            "complexity": complexity,
            "complexity_score": complexity_score,
            "business_impact": business_impact,
            "stakeholder_count": len(stakeholders),
            "required_domains": required_domains,
            "multi_domain_requirement": len(required_domains) > 2
        }
    
    def _identify_candidate_personas(
        self, 
        context_analysis: Dict[str, Any], 
        required_expertise: Optional[List[str]]
    ) -> List[ExpertPersonaType]:
        """Identify candidate personas based on context analysis"""
        candidates = []
        
        # Based on decision type
        decision_type = context_analysis["decision_type"]
        if decision_type in self.switching_rules["decision_type_mapping"]:
            candidates.append(self.switching_rules["decision_type_mapping"][decision_type])
        
        # Based on required domains
        required_domains = context_analysis["required_domains"]
        for persona_type, profile in self.expert_personas.items():
            domain_overlap = set(required_domains) & set(profile.expertise_domains)
            if domain_overlap:
                candidates.append(persona_type)
        
        # Based on complexity (senior partner for high complexity)
        if context_analysis["complexity_score"] > 0.8:
            candidates.append(ExpertPersonaType.SENIOR_PARTNER)
        
        # Remove duplicates while preserving order
        seen = set()
        unique_candidates = []
        for candidate in candidates:
            if candidate not in seen:
                seen.add(candidate)
                unique_candidates.append(candidate)
        
        return unique_candidates
    
    def _score_persona_candidates(
        self,
        candidates: List[ExpertPersonaType],
        context_analysis: Dict[str, Any],
        decision_context: Dict[str, Any]
    ) -> Dict[ExpertPersonaType, Dict[str, Any]]:
        """Score persona candidates for context fit"""
        scores = {}
        
        for candidate in candidates:
            profile = self.expert_personas[candidate]
            
            # Domain expertise score
            required_domains = set(context_analysis["required_domains"])
            available_domains = set(profile.expertise_domains)
            domain_overlap = required_domains & available_domains
            domain_score = len(domain_overlap) / max(len(required_domains), 1)
            
            # Context preference score
            decision_type = context_analysis["decision_type"]
            context_score = 1.0 if decision_type in profile.preferred_contexts else 0.5
            
            # Complexity handling score
            complexity_score = context_analysis["complexity_score"]
            if candidate == ExpertPersonaType.SENIOR_PARTNER:
                complexity_handling = min(1.0, complexity_score + 0.2)
            else:
                complexity_handling = max(0.3, 1.0 - complexity_score * 0.5)
            
            # Historical performance score
            performance_score = self._get_persona_performance_score(candidate, decision_context)
            
            # Calculate total score
            total_score = (
                domain_score * 0.4 +
                context_score * 0.25 +
                complexity_handling * 0.2 +
                performance_score * 0.15
            )
            
            scores[candidate] = {
                "domain_score": domain_score,
                "context_score": context_score,
                "complexity_handling": complexity_handling,
                "performance_score": performance_score,
                "total_score": total_score,
                "domain_overlap": list(domain_overlap)
            }
        
        return scores
    
    def _get_persona_performance_score(
        self, 
        persona: ExpertPersonaType, 
        decision_context: Dict[str, Any]
    ) -> float:
        """Get historical performance score for persona"""
        if persona not in self.persona_performance:
            return 0.7  # Default neutral score
        
        performance = self.persona_performance[persona]
        return performance.get("average_confidence", 0.7)
    
    def _create_switching_context(
        self,
        current_persona: Optional[ExpertPersonaType],
        target_persona: ExpertPersonaType,
        context_analysis: Dict[str, Any],
        persona_score: Dict[str, Any],
        decision_context: Dict[str, Any]
    ) -> PersonaSwitchingContext:
        """Create persona switching context"""
        
        # Determine switching trigger
        if current_persona is None:
            trigger = PersonaSwitchingTrigger.EXPERTISE_REQUIREMENT
            rationale = f"Initial persona selection based on {context_analysis['decision_type']} requirements"
        elif current_persona != target_persona:
            trigger = PersonaSwitchingTrigger.DECISION_TYPE_CHANGE
            rationale = f"Switching from {current_persona.value} to {target_persona.value} for optimal expertise match"
        else:
            trigger = PersonaSwitchingTrigger.CONTEXT_EVOLUTION
            rationale = f"Continuing with {target_persona.value} for consistent expertise"
        
        return PersonaSwitchingContext(
            current_persona=current_persona,
            target_persona=target_persona,
            switching_trigger=trigger,
            decision_context=decision_context,
            required_expertise=context_analysis["required_domains"],
            switching_rationale=rationale,
            confidence_score=persona_score["total_score"]
        )
    
    def _preserve_context_across_switch(self, switching_context: PersonaSwitchingContext) -> None:
        """Preserve context information across persona switches"""
        context_key = f"switch_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        self.context_memory[context_key] = {
            "decision_context": switching_context.decision_context,
            "previous_persona": switching_context.current_persona,
            "switching_rationale": switching_context.switching_rationale,
            "preserved_context": True
        }
    
    def _configure_persona_environment(
        self, 
        persona: ExpertPersonaType, 
        switching_context: PersonaSwitchingContext
    ) -> Dict[str, Any]:
        """Configure environment for new persona"""
        profile = self.expert_personas[persona]
        
        return {
            "active_persona": persona.value,
            "display_name": profile.display_name,
            "expertise_focus": profile.expertise_domains,
            "decision_frameworks": profile.decision_frameworks,
            "interaction_preferences": profile.interaction_style,
            "confidence_thresholds": profile.confidence_thresholds,
            "context_awareness": switching_context.decision_context,
            "switching_context": switching_context.switching_rationale
        }
    
    def _update_persona_tracking(
        self, 
        persona: ExpertPersonaType, 
        switching_context: PersonaSwitchingContext
    ) -> None:
        """Update persona performance tracking"""
        if persona not in self.persona_performance:
            self.persona_performance[persona] = {
                "total_activations": 0,
                "average_confidence": 0.7,
                "successful_switches": 0,
                "domain_usage": {}
            }
        
        tracking = self.persona_performance[persona]
        tracking["total_activations"] += 1
        tracking["successful_switches"] += 1
        
        # Update average confidence
        new_confidence = switching_context.confidence_score
        current_avg = tracking["average_confidence"]
        total_activations = tracking["total_activations"]
        
        tracking["average_confidence"] = (
            (current_avg * (total_activations - 1) + new_confidence) / total_activations
        )
    
    def _generate_role_guidance(self, persona_profile: ExpertPersonaProfile) -> Dict[str, Any]:
        """Generate role-specific guidance for current persona"""
        return {
            "decision_approach": persona_profile.interaction_style["decision_approach"],
            "communication_style": persona_profile.interaction_style["communication_tone"],
            "key_considerations": persona_profile.expertise_domains[:3],
            "decision_frameworks": persona_profile.decision_frameworks[:2],
            "confidence_guidelines": self._generate_confidence_guidelines(persona_profile)
        }
    
    def _generate_confidence_guidelines(self, persona_profile: ExpertPersonaProfile) -> List[str]:
        """Generate confidence guidelines for persona"""
        high_confidence_domains = [
            domain for domain, threshold in persona_profile.confidence_thresholds.items()
            if threshold > 0.8
        ]
        
        return [
            f"High confidence in: {', '.join(high_confidence_domains[:2])}",
            f"Approach decisions using {persona_profile.decision_frameworks[0]}",
            f"Communicate with {persona_profile.interaction_style['communication_tone']} style"
        ]
    
    def _get_decision_support_tools(self, persona_profile: ExpertPersonaProfile) -> List[str]:
        """Get decision support tools for persona"""
        tools_mapping = {
            ExpertPersonaType.PYTHON_GURU: ["Code analysis tools", "Performance profiling", "Testing frameworks"],
            ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT: ["Architecture diagrams", "Scalability analysis", "Integration planning"],
            ExpertPersonaType.BUSINESS_ANALYST_EXPERT: ["Stakeholder analysis", "Business case templates", "Process mapping"],
            ExpertPersonaType.SECURITY_SPECIALIST: ["Security frameworks", "Risk assessment tools", "Compliance checklists"],
            ExpertPersonaType.SENIOR_PARTNER: ["Strategic planning tools", "Executive dashboards", "Stakeholder alignment"]
        }
        
        return tools_mapping.get(persona_profile.persona_type, ["General decision support tools"])
    
    def _get_context_awareness(self, persona_profile: ExpertPersonaProfile) -> Dict[str, Any]:
        """Get context awareness information for persona"""
        recent_context = self.context_memory
        
        return {
            "recent_decisions": len(recent_context),
            "expertise_focus": persona_profile.expertise_domains,
            "preferred_contexts": persona_profile.preferred_contexts,
            "interaction_history": len(persona_profile.interaction_history)
        }
    
    def _generate_switch_id(self) -> str:
        """Generate unique switch ID"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        return f"switch_{timestamp}"
    
    def get_persona_analytics(self) -> Dict[str, Any]:
        """Get comprehensive persona analytics"""
        return {
            "available_personas": len(self.expert_personas),
            "current_persona": self.current_persona.value if self.current_persona else None,
            "total_switches": len(self.persona_history),
            "persona_performance": {
                persona.value: metrics for persona, metrics in self.persona_performance.items()
            },
            "switching_patterns": self._analyze_switching_patterns(),
            "context_memory_size": len(self.context_memory)
        }
    
    def _analyze_switching_patterns(self) -> Dict[str, Any]:
        """Analyze persona switching patterns"""
        if not self.persona_history:
            return {"no_data": True}
        
        triggers = {}
        personas_used = {}
        
        for switch in self.persona_history:
            trigger = switch.switching_trigger.value
            triggers[trigger] = triggers.get(trigger, 0) + 1
            
            persona = switch.target_persona.value
            personas_used[persona] = personas_used.get(persona, 0) + 1
        
        return {
            "switching_triggers": triggers,
            "persona_usage": personas_used,
            "average_confidence": sum(s.confidence_score for s in self.persona_history) / len(self.persona_history),
            "most_common_trigger": max(triggers.items(), key=lambda x: x[1])[0] if triggers else None,
            "most_used_persona": max(personas_used.items(), key=lambda x: x[1])[0] if personas_used else None
       }


def create_dynamic_persona_manager() -> DynamicPersonaManager:
   """Factory function to create Dynamic Persona Manager
   
   Returns:
       Configured DynamicPersonaManager instance
   """
   return DynamicPersonaManager()


def demonstrate_dynamic_persona_framework() -> bool:
   """Demonstrate dynamic persona framework for Story 3.1
   
   Returns:
       True if demonstration successful, False otherwise
   """
   print("🔧 Demonstrating Dynamic Expert Persona Framework...")
   
   try:
       # Create dynamic persona manager
       manager = create_dynamic_persona_manager()
       
       print("  ✅ Dynamic Persona Manager created")
       print(f"     Available personas: {len(manager.expert_personas)}")
       
       # Test scenario 1: Python implementation decision
       print("\n  🧪 Scenario 1: Python implementation decision...")
       
       python_context = {
           "type": "code_implementation",
           "description": "Optimize database query performance in Python",
           "complexity": "medium",
           "business_impact": "medium",
           "stakeholders": ["engineering", "product"],
           "technical_requirements": ["performance", "maintainability"]
       }
       
       switching_context_1 = manager.select_optimal_persona(
           python_context,
           required_expertise=["python_optimization", "performance"]
       )
       
       switch_result_1 = manager.execute_persona_switch(switching_context_1)
       
       print(f"     Selected persona: {switching_context_1.target_persona.value}")
       print(f"     Switching rationale: {switching_context_1.switching_rationale}")
       print(f"     Confidence score: {switching_context_1.confidence_score:.2f}")
       
       # Get current persona interface
       interface_1 = manager.get_current_persona_interface()
       print(f"     Interface configured: {interface_1['display_name']}")
       print(f"     Expertise domains: {len(interface_1['expertise_domains'])}")
       
       # Test scenario 2: Architecture decision (should trigger persona switch)
       print("\n  🧪 Scenario 2: System architecture decision...")
       
       architecture_context = {
           "type": "architecture_design",
           "description": "Design microservices architecture for high-scale application",
           "complexity": "high",
           "business_impact": "high",
           "stakeholders": ["engineering", "product", "operations"],
           "technical_requirements": ["scalability", "reliability", "maintainability"]
       }
       
       switching_context_2 = manager.select_optimal_persona(
           architecture_context,
           current_persona=manager.current_persona,
           required_expertise=["system_architecture", "scalability"]
       )
       
       switch_result_2 = manager.execute_persona_switch(switching_context_2)
       
       print(f"     Switched to persona: {switching_context_2.target_persona.value}")
       print(f"     Switching trigger: {switching_context_2.switching_trigger.value}")
       print(f"     Confidence score: {switching_context_2.confidence_score:.2f}")
       
       interface_2 = manager.get_current_persona_interface()
       print(f"     New interface: {interface_2['display_name']}")
       
       # Test scenario 3: Strategic business decision (should trigger senior partner)
       print("\n  🧪 Scenario 3: Strategic business decision...")
       
       strategic_context = {
           "type": "strategic_planning",
           "description": "Enterprise-wide technology transformation strategy",
           "complexity": "very_high",
           "business_impact": "critical",
           "stakeholders": ["executives", "engineering", "product", "operations", "customers"],
           "timeline": "urgent"
       }
       
       switching_context_3 = manager.select_optimal_persona(
           strategic_context,
           current_persona=manager.current_persona,
           required_expertise=["strategic_planning", "organizational_transformation"]
       )
       
       switch_result_3 = manager.execute_persona_switch(switching_context_3)
       
       print(f"     Escalated to persona: {switching_context_3.target_persona.value}")
       print(f"     Switching rationale: {switching_context_3.switching_rationale}")
       print(f"     Confidence score: {switching_context_3.confidence_score:.2f}")
       
       # Test analytics
       analytics = manager.get_persona_analytics()
       print(f"\n  ✅ Persona analytics: {analytics['total_switches']} switches executed")
       print(f"     Current persona: {analytics['current_persona']}")
       print(f"     Most used persona: {analytics['switching_patterns'].get('most_used_persona', 'N/A')}")
       
       # Validate expected persona selections
       expected_personas = [
           ExpertPersonaType.PYTHON_GURU,           # Code implementation
           ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT,  # Architecture design  
           ExpertPersonaType.SENIOR_PARTNER          # Strategic planning
       ]
       
       actual_personas = [
           switching_context_1.target_persona,
           switching_context_2.target_persona,
           switching_context_3.target_persona
       ]
       
       success = actual_personas == expected_personas
       
       if success:
           print("\n  🎯 All persona selections optimal!")
           print("     ✅ Python implementation → Python Guru")
           print("     ✅ Architecture design → System Architect Expert")
           print("     ✅ Strategic planning → Senior Partner")
       else:
           print(f"\n  ❌ Some persona selections unexpected:")
           for i, (expected, actual) in enumerate(zip(expected_personas, actual_personas)):
               status = "✅" if expected == actual else "❌"
               print(f"     {status} Scenario {i+1}: Expected {expected.value}, got {actual.value}")
       
       return success
       
   except Exception as e:
       print(f"  ❌ Dynamic persona framework demonstration failed: {e}")
       import traceback
       traceback.print_exc()
       return False


if __name__ == "__main__":
   print("🚀 Starting Dynamic Expert Persona Framework Demonstration - Story 3.1")
   
   success = demonstrate_dynamic_persona_framework()
   if success:
       print("\n✅ Story 3.1: Expert Persona Framework - DEMONSTRATED")
   else:
       print("\n❌ Story 3.1: Expert Persona Framework - FAILED")
       exit(1)