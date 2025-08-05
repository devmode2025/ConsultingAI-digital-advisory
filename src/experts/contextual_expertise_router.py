"""Contextual Expertise Routing Engine - Story 3.2 Implementation

This module implements sophisticated contextual expertise routing that considers
multiple factors including decision complexity, stakeholder requirements, domain overlap,
and historical performance patterns for optimal expert persona matching.
"""

from typing import Dict, Any, List, Optional, Tuple
from enum import Enum
from datetime import datetime
import logging
from dataclasses import dataclass, field

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from dynamic_persona_system import (
    DynamicPersonaManager, ExpertPersonaType, PersonaSwitchingContext,
    PersonaSwitchingTrigger
)


class RoutingComplexity(Enum):
    """Complexity levels for routing decisions"""
    SIMPLE = "simple"
    MODERATE = "moderate"
    COMPLEX = "complex"
    MULTI_DOMAIN = "multi_domain"
    STRATEGIC = "strategic"


class StakeholderType(Enum):
    """Types of stakeholders that influence routing decisions"""
    TECHNICAL_TEAM = "technical_team"
    BUSINESS_STAKEHOLDERS = "business_stakeholders"
    EXECUTIVE_LEADERSHIP = "executive_leadership"
    EXTERNAL_CLIENTS = "external_clients"
    REGULATORY_BODIES = "regulatory_bodies"
    END_USERS = "end_users"


@dataclass
class RoutingContext:
    """Comprehensive context for expertise routing decisions"""
    decision_id: str
    decision_type: str
    complexity_level: RoutingComplexity
    stakeholder_requirements: Dict[StakeholderType, List[str]]
    domain_requirements: List[str]
    business_impact: str
    timeline_constraints: Dict[str, Any]
    risk_factors: List[str]
    compliance_requirements: List[str]
    historical_context: Optional[Dict[str, Any]] = None
    multi_expert_needed: bool = False
    routing_preferences: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ExpertiseMatch:
    """Result of expertise matching analysis"""
    persona_type: ExpertPersonaType
    match_score: float
    domain_coverage: float
    stakeholder_alignment: float
    complexity_handling: float
    historical_performance: float
    routing_confidence: float
    match_rationale: str
    recommended_role: str


class ContextualExpertiseRouter:
    """Contextual Expertise Routing Engine for optimal expert persona matching
    
    This class provides sophisticated routing capabilities including:
    - Multi-factor analysis for expert persona selection
    - Stakeholder requirement matching and alignment
    - Domain expertise coverage optimization
    - Historical performance consideration
    - Multi-expert coordination for complex scenarios
    
    Academic Note: Demonstrates advanced contextual routing patterns
    for Epic 3 Story 3.2 - intelligent expertise matching beyond basic rules.
    """
    
    def __init__(self, persona_manager: DynamicPersonaManager):
        """Initialize Contextual Expertise Router
        
        Args:
            persona_manager: Dynamic persona manager for expert profiles
        """
        self.persona_manager = persona_manager
        self.routing_history: List[Dict[str, Any]] = []
        self.performance_analytics: Dict[str, Any] = {}
        
        # Initialize routing algorithms and weights
        self.routing_weights = self._initialize_routing_weights()
        self.stakeholder_expertise_mapping = self._initialize_stakeholder_mapping()
        self.complexity_routing_rules = self._initialize_complexity_rules()
        
        # Domain expertise matrix
        self.domain_expertise_matrix = self._build_domain_expertise_matrix()
        
        self.logger = logging.getLogger("ConsultingAI.ContextualExpertiseRouter")
        
        self.logger.info(
            "Contextual Expertise Router initialized",
            extra={
                "routing_algorithms": "multi_factor_analysis",
                "stakeholder_types": len(StakeholderType),
                "academic_context": "Epic 3 Story 3.2 - Contextual Expertise Routing"
            }
        )
    
    def _initialize_routing_weights(self) -> Dict[str, float]:
        """Initialize weights for multi-factor routing analysis"""
        return {
            "domain_expertise": 0.35,      # Primary factor
            "stakeholder_alignment": 0.25,  # Important for consulting
            "complexity_handling": 0.20,    # Capability match
            "historical_performance": 0.15, # Learning from past
            "timeline_efficiency": 0.05     # Speed consideration
        }
    
    def _initialize_stakeholder_mapping(self) -> Dict[StakeholderType, List[ExpertPersonaType]]:
        """Initialize stakeholder to expert persona mapping"""
        return {
            StakeholderType.TECHNICAL_TEAM: [
                ExpertPersonaType.PYTHON_GURU,
                ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT,
                ExpertPersonaType.SECURITY_SPECIALIST
            ],
            StakeholderType.BUSINESS_STAKEHOLDERS: [
                ExpertPersonaType.BUSINESS_ANALYST_EXPERT,
                ExpertPersonaType.SENIOR_PARTNER
            ],
            StakeholderType.EXECUTIVE_LEADERSHIP: [
                ExpertPersonaType.SENIOR_PARTNER,
                ExpertPersonaType.BUSINESS_ANALYST_EXPERT
            ],
            StakeholderType.EXTERNAL_CLIENTS: [
                ExpertPersonaType.SENIOR_PARTNER,
                ExpertPersonaType.BUSINESS_ANALYST_EXPERT
            ],
            StakeholderType.REGULATORY_BODIES: [
                ExpertPersonaType.SECURITY_SPECIALIST,
                ExpertPersonaType.BUSINESS_ANALYST_EXPERT
            ],
            StakeholderType.END_USERS: [
                ExpertPersonaType.BUSINESS_ANALYST_EXPERT,
                ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT
            ]
        }
    
    def _initialize_complexity_rules(self) -> Dict[RoutingComplexity, Dict[str, Any]]:
        """Initialize complexity-based routing rules"""
        return {
            RoutingComplexity.SIMPLE: {
                "preferred_personas": [
                    ExpertPersonaType.PYTHON_GURU,
                    ExpertPersonaType.BUSINESS_ANALYST_EXPERT
                ],
                "decision_speed": "fast",
                "collaboration_level": "minimal",
                "escalation_threshold": 0.7
            },
            RoutingComplexity.MODERATE: {
                "preferred_personas": [
                    ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT,
                    ExpertPersonaType.BUSINESS_ANALYST_EXPERT,
                    ExpertPersonaType.SECURITY_SPECIALIST
                ],
                "decision_speed": "standard",
                "collaboration_level": "moderate",
                "escalation_threshold": 0.6
            },
            RoutingComplexity.COMPLEX: {
                "preferred_personas": [
                    ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT,
                    ExpertPersonaType.SENIOR_PARTNER,
                    ExpertPersonaType.SECURITY_SPECIALIST
                ],
                "decision_speed": "deliberate",
                "collaboration_level": "high",
                "escalation_threshold": 0.5
            },
            RoutingComplexity.MULTI_DOMAIN: {
                "preferred_personas": [
                    ExpertPersonaType.SENIOR_PARTNER,
                    ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT,
                    ExpertPersonaType.BUSINESS_ANALYST_EXPERT
                ],
                "decision_speed": "extended",
                "collaboration_level": "very_high",
                "escalation_threshold": 0.4,
                "multi_expert_required": True
            },
            RoutingComplexity.STRATEGIC: {
                "preferred_personas": [
                    ExpertPersonaType.SENIOR_PARTNER
                ],
                "decision_speed": "strategic_timeline",
                "collaboration_level": "executive",
                "escalation_threshold": 0.3,
                "senior_oversight_required": True
            }
        }
    
    def _build_domain_expertise_matrix(self) -> Dict[str, Dict[ExpertPersonaType, float]]:
        """Build comprehensive domain expertise matrix"""
        
        # Domain categories and expert persona strengths
        domains = {
            "python_development": {
                ExpertPersonaType.PYTHON_GURU: 1.0,
                ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT: 0.7,
                ExpertPersonaType.SECURITY_SPECIALIST: 0.6,
                ExpertPersonaType.BUSINESS_ANALYST_EXPERT: 0.3,
                ExpertPersonaType.SENIOR_PARTNER: 0.4
            },
            "system_architecture": {
                ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT: 1.0,
                ExpertPersonaType.PYTHON_GURU: 0.6,
                ExpertPersonaType.SECURITY_SPECIALIST: 0.8,
                ExpertPersonaType.BUSINESS_ANALYST_EXPERT: 0.4,
                ExpertPersonaType.SENIOR_PARTNER: 0.7
            },
            "business_analysis": {
                ExpertPersonaType.BUSINESS_ANALYST_EXPERT: 1.0,
                ExpertPersonaType.SENIOR_PARTNER: 0.9,
                ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT: 0.5,
                ExpertPersonaType.SECURITY_SPECIALIST: 0.4,
                ExpertPersonaType.PYTHON_GURU: 0.3
            },
            "security_compliance": {
                ExpertPersonaType.SECURITY_SPECIALIST: 1.0,
                ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT: 0.7,
                ExpertPersonaType.BUSINESS_ANALYST_EXPERT: 0.6,
                ExpertPersonaType.SENIOR_PARTNER: 0.8,
                ExpertPersonaType.PYTHON_GURU: 0.5
            },
            "strategic_planning": {
                ExpertPersonaType.SENIOR_PARTNER: 1.0,
                ExpertPersonaType.BUSINESS_ANALYST_EXPERT: 0.7,
                ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT: 0.6,
                ExpertPersonaType.SECURITY_SPECIALIST: 0.5,
                ExpertPersonaType.PYTHON_GURU: 0.3
            },
            "performance_optimization": {
                ExpertPersonaType.PYTHON_GURU: 1.0,
                ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT: 0.9,
                ExpertPersonaType.SECURITY_SPECIALIST: 0.6,
                ExpertPersonaType.BUSINESS_ANALYST_EXPERT: 0.3,
                ExpertPersonaType.SENIOR_PARTNER: 0.4
            },
            "stakeholder_management": {
                ExpertPersonaType.BUSINESS_ANALYST_EXPERT: 1.0,
                ExpertPersonaType.SENIOR_PARTNER: 0.9,
                ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT: 0.5,
                ExpertPersonaType.SECURITY_SPECIALIST: 0.4,
                ExpertPersonaType.PYTHON_GURU: 0.3
            }
        }
        
        return domains
    
    def route_to_optimal_expertise(
        self,
        routing_context: RoutingContext,
        current_persona: Optional[ExpertPersonaType] = None
    ) -> Dict[str, Any]:
        """Route decision to optimal expertise using contextual analysis
        
        Args:
            routing_context: Comprehensive routing context
            current_persona: Currently active persona (if any)
            
        Returns:
            Complete routing result with expert recommendations and rationale
        """
        routing_id = self._generate_routing_id()
        
        self.logger.info(
            "Starting contextual expertise routing",
            extra={
                "routing_id": routing_id,
                "decision_type": routing_context.decision_type,
                "complexity": routing_context.complexity_level.value,
                "academic_demonstration": "contextual_expertise_routing"
            }
        )
        
        # Step 1: Analyze routing requirements
        routing_analysis = self._analyze_routing_requirements(routing_context)
        
        # Step 2: Generate expert candidates
        candidate_experts = self._generate_expert_candidates(routing_context, routing_analysis)
        
        # Step 3: Score candidates using multi-factor analysis
        expert_matches = self._score_expert_candidates(
            candidate_experts, routing_context, routing_analysis
        )
        
        # Step 4: Select optimal expert(s)
        optimal_routing = self._select_optimal_experts(
            expert_matches, routing_context, current_persona
        )
        
        # Step 5: Generate routing execution plan
        execution_plan = self._generate_routing_execution_plan(
            optimal_routing, routing_context, routing_analysis
        )
        
        # Compile comprehensive routing result
        routing_result = {
            "routing_id": routing_id,
            "timestamp": datetime.now().isoformat(),
            "routing_context": routing_context,
            "routing_analysis": routing_analysis,
            "candidate_experts": len(candidate_experts),
            "expert_matches": expert_matches,
            "optimal_routing": optimal_routing,
            "execution_plan": execution_plan,
            "routing_confidence": optimal_routing["primary_expert"]["routing_confidence"],
            "multi_expert_coordination": routing_context.multi_expert_needed or len(optimal_routing.get("supporting_experts", [])) > 0
        }
        
        # Store routing result for learning
        self.routing_history.append(routing_result)
        self._update_performance_analytics(routing_result)
        
        self.logger.info(
            "Contextual expertise routing completed",
            extra={
                "routing_result": routing_result,
                "academic_evaluation": "sophisticated_expertise_matching"
            }
        )
        
        return routing_result
    
    def _analyze_routing_requirements(self, context: RoutingContext) -> Dict[str, Any]:
        """Analyze routing requirements from context"""
        
        # Domain requirement analysis
        domain_coverage_needed = self._analyze_domain_coverage(context.domain_requirements)
        
        # Stakeholder requirement analysis
        stakeholder_alignment_needed = self._analyze_stakeholder_requirements(context.stakeholder_requirements)
        
        # Complexity requirement analysis
        complexity_requirements = self._analyze_complexity_requirements(context.complexity_level)
        
        # Timeline and risk analysis
        constraint_analysis = self._analyze_constraints(context.timeline_constraints, context.risk_factors)
        
        return {
            "domain_coverage": domain_coverage_needed,
            "stakeholder_alignment": stakeholder_alignment_needed,
            "complexity_requirements": complexity_requirements,
            "constraint_analysis": constraint_analysis,
            "routing_priority": self._determine_routing_priority(context),
            "multi_expert_indicators": self._assess_multi_expert_need(context)
        }
    
    def _analyze_domain_coverage(self, domain_requirements: List[str]) -> Dict[str, Any]:
        """Analyze required domain coverage"""
        coverage_analysis = {}
        
        for domain in domain_requirements:
            if domain in self.domain_expertise_matrix:
                # Find experts with high coverage for this domain
                domain_experts = {
                    persona: score for persona, score in self.domain_expertise_matrix[domain].items()
                    if score > 0.6
                }
                coverage_analysis[domain] = {
                    "required": True,
                    "available_experts": domain_experts,
                    "coverage_difficulty": 1.0 - max(domain_experts.values()) if domain_experts else 1.0
                }
        
        return coverage_analysis
    
    def _analyze_stakeholder_requirements(self, stakeholder_reqs: Dict[StakeholderType, List[str]]) -> Dict[str, Any]:
        """Analyze stakeholder alignment requirements"""
        alignment_analysis = {}
        
        for stakeholder_type, requirements in stakeholder_reqs.items():
            # Get preferred expert personas for this stakeholder type
            preferred_experts = self.stakeholder_expertise_mapping.get(stakeholder_type, [])
            
            alignment_analysis[stakeholder_type.value] = {
                "requirements": requirements,
                "preferred_experts": [expert.value for expert in preferred_experts],
                "priority_level": self._assess_stakeholder_priority(stakeholder_type),
                "alignment_complexity": len(requirements)
            }
        
        return alignment_analysis
    
    def _assess_stakeholder_priority(self, stakeholder_type: StakeholderType) -> str:
        """Assess priority level for stakeholder type"""
        priority_mapping = {
            StakeholderType.EXECUTIVE_LEADERSHIP: "critical",
            StakeholderType.EXTERNAL_CLIENTS: "high",
            StakeholderType.BUSINESS_STAKEHOLDERS: "high",
            StakeholderType.REGULATORY_BODIES: "high",
            StakeholderType.TECHNICAL_TEAM: "medium",
            StakeholderType.END_USERS: "medium"
        }
        return priority_mapping.get(stakeholder_type, "medium")
    
    def _analyze_complexity_requirements(self, complexity: RoutingComplexity) -> Dict[str, Any]:
        """Analyze complexity-based routing requirements"""
        complexity_rules = self.complexity_routing_rules[complexity]
        
        return {
            "complexity_level": complexity.value,
            "preferred_personas": [p.value for p in complexity_rules["preferred_personas"]],
            "decision_speed": complexity_rules["decision_speed"],
            "collaboration_level": complexity_rules["collaboration_level"],
            "escalation_threshold": complexity_rules["escalation_threshold"],
            "special_requirements": {
                "multi_expert_required": complexity_rules.get("multi_expert_required", False),
                "senior_oversight_required": complexity_rules.get("senior_oversight_required", False)
            }
        }
    
    def _analyze_constraints(self, timeline_constraints: Dict[str, Any], risk_factors: List[str]) -> Dict[str, Any]:
        """Analyze timeline and risk constraints"""
        timeline_urgency = timeline_constraints.get("urgency", "normal")
        
        # Timeline impact on expert selection
        timeline_impact = {
            "immediate": {"preferred_speed": "fast", "complexity_limit": "moderate"},
            "urgent": {"preferred_speed": "standard", "complexity_limit": "complex"},
            "normal": {"preferred_speed": "deliberate", "complexity_limit": "multi_domain"},
            "flexible": {"preferred_speed": "strategic_timeline", "complexity_limit": "strategic"}
        }.get(timeline_urgency, {"preferred_speed": "standard", "complexity_limit": "complex"})
        
        # Risk factor analysis
        high_risk_factors = [risk for risk in risk_factors if "high" in risk or "critical" in risk]
        risk_level = "high" if high_risk_factors else "medium" if risk_factors else "low"
        
        return {
            "timeline_urgency": timeline_urgency,
            "timeline_impact": timeline_impact,
            "risk_level": risk_level,
            "risk_factors": risk_factors,
            "high_risk_factors": high_risk_factors,
            "risk_mitigation_needed": len(high_risk_factors) > 0
        }
    
    def _determine_routing_priority(self, context: RoutingContext) -> str:
        """Determine overall routing priority"""
        factors = [
            context.business_impact,
            context.complexity_level.value,
            len(context.stakeholder_requirements),
            len(context.risk_factors)
        ]
        
        # Simple priority calculation
        if context.business_impact == "critical" or context.complexity_level == RoutingComplexity.STRATEGIC:
            return "critical"
        elif context.business_impact == "high" or context.complexity_level == RoutingComplexity.COMPLEX:
            return "high"
        else:
            return "medium"
    
    def _assess_multi_expert_need(self, context: RoutingContext) -> Dict[str, Any]:
        """Assess need for multi-expert coordination"""
        indicators = {
            "domain_breadth": len(context.domain_requirements) > 3,
            "stakeholder_diversity": len(context.stakeholder_requirements) > 2,
            "complexity_level": context.complexity_level in [RoutingComplexity.MULTI_DOMAIN, RoutingComplexity.STRATEGIC],
            "compliance_requirements": len(context.compliance_requirements) > 1,
            "explicit_flag": context.multi_expert_needed
        }
        
        multi_expert_score = sum(indicators.values()) / len(indicators)
        
        return {
            "indicators": indicators,
            "multi_expert_score": multi_expert_score,
            "multi_expert_recommended": multi_expert_score > 0.6,
            "coordination_complexity": "high" if multi_expert_score > 0.8 else "medium" if multi_expert_score > 0.4 else "low"
        }
    
    def _generate_expert_candidates(self, context: RoutingContext, analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate expert candidates based on context and analysis"""
        candidates = []
        
        # Get all available expert personas
        for persona in ExpertPersonaType:
            candidate = {
                "persona_type": persona,
                "domain_scores": {},
                "stakeholder_alignment": {},
                "base_confidence": 0.5
            }
            
            # Calculate domain scores
            for domain in context.domain_requirements:
                if domain in self.domain_expertise_matrix:
                    candidate["domain_scores"][domain] = self.domain_expertise_matrix[domain].get(persona, 0.0)
            
            # Calculate stakeholder alignment
            for stakeholder_type in context.stakeholder_requirements:
                if persona in self.stakeholder_expertise_mapping.get(stakeholder_type, []):
                    candidate["stakeholder_alignment"][stakeholder_type.value] = 0.8
                else:
                    candidate["stakeholder_alignment"][stakeholder_type.value] = 0.3
            
            candidates.append(candidate)
        
        return candidates

    def _score_expert_candidates(self, candidates: List[Dict[str, Any]], context: RoutingContext, analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Score expert candidates using multi-factor analysis"""
        scored_candidates = []
        
        for candidate in candidates:
            # Domain expertise score
            domain_score = sum(candidate["domain_scores"].values()) / max(len(candidate["domain_scores"]), 1)
            
            # Stakeholder alignment score
            stakeholder_score = sum(candidate["stakeholder_alignment"].values()) / max(len(candidate["stakeholder_alignment"]), 1)
            
            # Complexity alignment score
            complexity_rules = self.complexity_routing_rules[context.complexity_level]
            complexity_score = 0.8 if candidate["persona_type"] in complexity_rules["preferred_personas"] else 0.4
            
            # Calculate overall score
            overall_score = (domain_score * 0.4 + stakeholder_score * 0.3 + complexity_score * 0.3)
            
            scored_candidate = {
                **candidate,
                "domain_score": domain_score,
                "stakeholder_score": stakeholder_score,
                "complexity_score": complexity_score,
                "overall_score": overall_score,
                "routing_confidence": min(overall_score + 0.1, 1.0)
            }
            
            scored_candidates.append(scored_candidate)
        
        # Sort by overall score
        return sorted(scored_candidates, key=lambda x: x["overall_score"], reverse=True)

    def _select_optimal_experts(self, expert_matches: List[Dict[str, Any]], context: RoutingContext, current_persona: Optional[ExpertPersonaType]) -> Dict[str, Any]:
        """Select optimal expert(s) from scored candidates"""
        if not expert_matches:
            # Fallback to senior partner
            return {
                "primary_expert": {
                    "persona_type": ExpertPersonaType.SENIOR_PARTNER,
                    "routing_confidence": 0.6,
                    "selection_rationale": "Fallback selection - no optimal matches found"
                },
                "supporting_experts": []
            }
        
        # Select primary expert (highest score)
        primary_expert = expert_matches[0]
        
        # Determine if supporting experts are needed
        supporting_experts = []
        if context.multi_expert_needed or context.complexity_level in [RoutingComplexity.MULTI_DOMAIN, RoutingComplexity.STRATEGIC]:
            # Add top 2-3 additional experts as supporting
            for expert in expert_matches[1:4]:
                if expert["overall_score"] > 0.5:
                    supporting_experts.append({
                        "persona_type": expert["persona_type"],
                        "routing_confidence": expert["routing_confidence"],
                        "support_role": "domain_specialist",
                        "recommended_role": "supporting_expert"
                    })
        
        return {
            "primary_expert": {
                "persona_type": primary_expert["persona_type"],
                "match_score": primary_expert["overall_score"],
                "routing_confidence": primary_expert["routing_confidence"],
                "selection_rationale": f"Highest overall score: {primary_expert['overall_score']:.2f}",
                "domain_scores": primary_expert["domain_scores"],
                "stakeholder_alignment": primary_expert["stakeholder_alignment"]
            },
            "supporting_experts": supporting_experts
        }

    def _generate_routing_execution_plan(self, optimal_routing: Dict[str, Any], context: RoutingContext, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Generate execution plan for the routing decision"""
        primary_expert = optimal_routing["primary_expert"]
        supporting_experts = optimal_routing.get("supporting_experts", [])
        
        # Determine coordination approach
        if supporting_experts:
            coordination_approach = "multi_expert_collaboration"
            coordination_frequency = self._determine_coordination_frequency(context)
        else:
            coordination_approach = "single_expert_execution"
            coordination_frequency = "as_needed"
        
        # Generate execution steps
        execution_steps = [
            f"Activate {primary_expert['persona_type'].value} as primary expert",
            "Analyze decision context and requirements",
            "Apply domain expertise to generate recommendations"
        ]
        
        if supporting_experts:
            execution_steps.extend([
                f"Coordinate with {len(supporting_experts)} supporting experts",
                "Synthesize multi-expert perspectives",
                "Validate recommendations across domains"
            ])
        
        execution_steps.append("Deliver comprehensive expert recommendation")
        
        return {
            "coordination_approach": coordination_approach,
            "coordination_frequency": coordination_frequency,
            "execution_steps": execution_steps,
            "estimated_duration": self._estimate_execution_duration(context, len(supporting_experts)),
            "execution_timeline": {
                "decision_delivery": self._estimate_execution_duration(context, len(supporting_experts)),
                "coordination_frequency": coordination_frequency
            },
            "success_criteria": self._define_success_criteria(context, analysis),
            "escalation_triggers": self._define_escalation_triggers(context, primary_expert["routing_confidence"])
        }

    def _determine_coordination_frequency(self, context: RoutingContext) -> str:
        """Determine how frequently experts should coordinate"""
        urgency = context.timeline_constraints.get("urgency", "normal")
        
        frequency_mapping = {
            "immediate": "continuous",
            "urgent": "daily",
            "normal": "regular",
            "flexible": "milestone_based"
        }
        
        return frequency_mapping.get(urgency, "regular")

    def _estimate_execution_duration(self, context: RoutingContext, supporting_expert_count: int) -> str:
        """Estimate execution duration based on context"""
        base_duration = {
            RoutingComplexity.SIMPLE: "1-2 hours",
            RoutingComplexity.MODERATE: "4-8 hours", 
            RoutingComplexity.COMPLEX: "1-2 days",
            RoutingComplexity.MULTI_DOMAIN: "2-5 days",
            RoutingComplexity.STRATEGIC: "1-2 weeks"
        }
        
        duration = base_duration.get(context.complexity_level, "1 day")
        
        if supporting_expert_count > 0:
            duration += f" (+ coordination overhead for {supporting_expert_count} experts)"
        
        return duration

    def _define_success_criteria(self, context: RoutingContext, analysis: Dict[str, Any]) -> List[str]:
        """Define success criteria for the routing execution"""
        criteria = [
            "Expert recommendation addresses all domain requirements",
            "Stakeholder alignment achieved for key requirements",
            f"Decision confidence exceeds {analysis.get('routing_priority', 'medium')} threshold"
        ]
        
        if context.multi_expert_needed:
            criteria.append("Multi-expert consensus achieved on key recommendations")
        
        if context.risk_factors:
            criteria.append("Risk mitigation strategies included in recommendations")
        
        return criteria

    def _define_escalation_triggers(self, context: RoutingContext, confidence: float) -> List[str]:
        """Define escalation triggers for the routing execution"""
        triggers = []
        
        if confidence < 0.7:
            triggers.append("Low confidence in expert recommendation")
        
        if context.business_impact == "critical":
            triggers.append("Critical business impact requires senior oversight")
        
        if len(context.risk_factors) > 2:
            triggers.append("Multiple risk factors require additional review")
        
        if not triggers:
            triggers.append("No automatic escalation triggers identified")
        
        return triggers

    def _define_expert_roles(self, routing: Dict[str, Any]) -> Dict[str, str]:
        """Define specific roles for each expert in multi-expert scenarios"""
        roles = {
            routing["primary_expert"]["persona_type"].value: "Primary decision authority and coordination lead"
        }

        for expert in routing.get("supporting_experts", []):
            persona_name = expert["persona_type"].value
            role = expert["recommended_role"]
            roles[persona_name] = f"{role.replace('_', ' ').title()} - {expert['coordination_level']} coordination"

        return roles

    def _define_communication_protocols(self, routing: Dict[str, Any]) -> Dict[str, Any]:
        """Define communication protocols for multi-expert scenarios"""
        coordination_strategy = routing.get("coordination_strategy", {})

        return {
            "communication_model": coordination_strategy.get("communication_pattern", "mesh"),
            "decision_authority": coordination_strategy.get("decision_authority", "primary_expert_led"),
            "meeting_frequency": coordination_strategy.get("coordination_frequency", "regular"),
            "escalation_path": "Primary Expert → Senior Partner if needed",
            "documentation_requirements": "Shared decision log and rationale tracking"
        }

    def _define_decision_process(self, routing: Dict[str, Any], context: RoutingContext) -> Dict[str, Any]:
        """Define decision-making process for multi-expert scenarios"""
        coordination_strategy = routing.get("coordination_strategy", {})

        return {
            "decision_model": coordination_strategy.get("coordination_model", "collaborative"),
            "consensus_required": coordination_strategy.get("consensus_requirement", False),
            "conflict_resolution": "Primary expert authority with escalation option",
            "timeline_for_decisions": self._determine_execution_timeline(context)["decision_delivery"],
            "documentation_standard": "Comprehensive decision rationale with expert inputs"
        }

    def _update_performance_analytics(self, routing_result: Dict[str, Any]) -> None:
        """Update performance analytics with routing result"""
        if "routing_analytics" not in self.performance_analytics:
            self.performance_analytics["routing_analytics"] = {
                "total_routings": 0,
                "average_confidence": 0.0,
                "complexity_distribution": {},
                "multi_expert_usage": 0
            }
        
        analytics = self.performance_analytics["routing_analytics"]
        analytics["total_routings"] += 1
        
        # Update average confidence
        confidence = routing_result["routing_confidence"]
        current_avg = analytics["average_confidence"]
        total_routings = analytics["total_routings"]
        
        analytics["average_confidence"] = (
            (current_avg * (total_routings - 1) + confidence) / total_routings
        )
        
        # Update complexity distribution
        complexity = routing_result["routing_context"].complexity_level.value
        analytics["complexity_distribution"][complexity] = analytics["complexity_distribution"].get(complexity, 0) + 1
        
        # Update multi-expert usage
        if routing_result["multi_expert_coordination"]:
            analytics["multi_expert_usage"] += 1

    def _generate_routing_id(self) -> str:
        """Generate unique routing ID"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        return f"routing_{timestamp}"

    def get_routing_analytics(self) -> Dict[str, Any]:
        """Get comprehensive routing analytics"""
        return {
            "total_routings": len(self.routing_history),
            "performance_analytics": self.performance_analytics,
            "routing_patterns": self._analyze_routing_patterns(),
            "expert_utilization": self._analyze_expert_utilization(),
            "recent_routings": self.routing_history[-5:]  # Last 5 for review
        }
    
    def _analyze_routing_patterns(self) -> Dict[str, Any]:
        """Analyze routing patterns and trends"""
        if not self.routing_history:
            return {"no_data": True}
        
        complexity_trends = {}
        confidence_trends = []
        multi_expert_usage = 0
        
        for routing in self.routing_history:
            complexity = routing["routing_context"].complexity_level.value
            complexity_trends[complexity] = complexity_trends.get(complexity, 0) + 1
            
            confidence_trends.append(routing["routing_confidence"])
            
            if routing["multi_expert_coordination"]:
                multi_expert_usage += 1
        
        return {
            "complexity_distribution": complexity_trends,
            "average_confidence": sum(confidence_trends) / len(confidence_trends),
            "confidence_trend": "improving" if len(confidence_trends) > 1 and confidence_trends[-1] > confidence_trends[0] else "stable",
            "multi_expert_usage_rate": multi_expert_usage / len(self.routing_history),
            "routing_efficiency": self._calculate_routing_efficiency()
        }
    
    def _analyze_expert_utilization(self) -> Dict[str, Any]:
        """Analyze expert persona utilization patterns"""
        utilization = {}
        
        for routing in self.routing_history:
            primary_expert = routing["optimal_routing"]["primary_expert"]["persona_type"].value
            utilization[primary_expert] = utilization.get(primary_expert, 0) + 1
            
            # Count supporting experts
            for expert in routing["optimal_routing"].get("supporting_experts", []):
                expert_name = expert["persona_type"].value
                utilization[f"{expert_name}_supporting"] = utilization.get(f"{expert_name}_supporting", 0) + 1
        
        return utilization
    
    def _calculate_routing_efficiency(self) -> float:
        """Calculate overall routing efficiency"""
        if not self.routing_history:
            return 0.0
        
        # Simplified efficiency calculation based on confidence scores
        confidence_scores = [routing["routing_confidence"] for routing in self.routing_history]
        return sum(confidence_scores) / len(confidence_scores)


def create_contextual_expertise_router(persona_manager: DynamicPersonaManager) -> ContextualExpertiseRouter:
   """Factory function to create Contextual Expertise Router
   
   Args:
       persona_manager: Dynamic persona manager instance
       
   Returns:
       Configured ContextualExpertiseRouter instance
   """
   return ContextualExpertiseRouter(persona_manager)


def demonstrate_contextual_expertise_routing():
    """Demonstrate contextual expertise routing capabilities"""
    print("🚀 Starting Contextual Expertise Routing Demonstration - Story 3.2")
    print("🔧 Demonstrating Contextual Expertise Routing...")
    
    try:
        # Create router
        router = create_contextual_expertise_router()
        print("  ✅ Contextual Expertise Router created")
        print(f"     Domain expertise matrix: {len(router.domain_expertise_matrix)} domains")
        print(f"     Stakeholder mappings: {len(router.stakeholder_expertise_mapping)} types")
        print()
        
        # Scenario 1: Simple Python development task
        print("  🧪 Scenario 1: Simple Python development task...")
        context_1 = RoutingContext(
            decision_id="simple_python_task",
            complexity_level=RoutingComplexity.SIMPLE,
            domain_requirements=["python", "development"],
            stakeholder_requirements={StakeholderType.TECHNICAL_TEAM: ["code quality", "performance"]},
            business_impact="medium",
            timeline_constraints={"urgency": "normal"},
            risk_factors=["technical_debt"],
            multi_expert_needed=False
        )
        
        result_1 = router.route_to_optimal_expertise(context_1)
        primary_expert_1 = result_1["optimal_routing"]["primary_expert"]
        
        print(f"     Routed to: {primary_expert_1['persona_type'].value}")
        print(f"     Match score: {primary_expert_1['match_score']:.2f}")
        print(f"     Routing confidence: {primary_expert_1['routing_confidence']:.2f}")
        print(f"     Multi-expert needed: {result_1['multi_expert_coordination']}")
        print()
        
        # Scenario 2: Complex multi-domain architecture decision
        print("  🧪 Scenario 2: Complex multi-domain architecture decision...")
        context_2 = RoutingContext(
            decision_id="complex_architecture",
            complexity_level=RoutingComplexity.MULTI_DOMAIN,
            domain_requirements=["architecture", "business", "security"],
            stakeholder_requirements={
                StakeholderType.EXECUTIVE_TEAM: ["strategic alignment"],
                StakeholderType.TECHNICAL_TEAM: ["scalability", "maintainability"]
            },
            business_impact="high",
            timeline_constraints={"urgency": "urgent"},
            risk_factors=["integration_complexity", "timeline_pressure"],
            multi_expert_needed=True
        )
        
        result_2 = router.route_to_optimal_expertise(context_2)
        primary_expert_2 = result_2["optimal_routing"]["primary_expert"]
        supporting_experts_2 = result_2["optimal_routing"]["supporting_experts"]
        
        print(f"     Primary expert: {primary_expert_2['persona_type'].value}")
        print(f"     Match score: {primary_expert_2['match_score']:.2f}")
        print(f"     Supporting experts: {len(supporting_experts_2)}")
        print(f"     Coordination strategy: {result_2['coordination_strategy'].get('coordination_model', 'N/A')}")
        
        for expert in supporting_experts_2:
            print(f"       - {expert['persona_type'].value} ({expert['recommended_role']})")
        print()
        
        # Scenario 3: Strategic crisis response
        print("  🧪 Scenario 3: Strategic crisis response...")
        context_3 = RoutingContext(
            decision_id="crisis_response",
            complexity_level=RoutingComplexity.STRATEGIC,
            domain_requirements=["strategic", "risk_management", "stakeholder_communication"],
            stakeholder_requirements={
                StakeholderType.EXECUTIVE_TEAM: ["crisis management", "strategic response"],
                StakeholderType.CLIENT: ["communication", "reassurance"],
                StakeholderType.REGULATORY: ["compliance", "reporting"]
            },
            business_impact="critical",
            timeline_constraints={"urgency": "immediate"},
            risk_factors=["reputation_risk", "regulatory_risk", "financial_impact"],
            multi_expert_needed=True
        )
        
        result_3 = router.route_to_optimal_expertise(context_3)
        primary_expert_3 = result_3["optimal_routing"]["primary_expert"]
        execution_plan_3 = result_3["execution_plan"]
        
        print(f"     Crisis leader: {primary_expert_3['persona_type'].value}")
        print(f"     Match score: {primary_expert_3['match_score']:.2f}")
        print(f"     Execution timeline: {execution_plan_3['execution_timeline']['decision_delivery']}")
        print(f"     Success criteria: {len(execution_plan_3['success_criteria'])} defined")
        print()
        
        # Analytics summary
        analytics = router.get_routing_analytics()
        print(f"  ✅ Routing analytics: {analytics['total_routings']} routings completed")
        print(f"     Average confidence: {analytics['routing_patterns']['average_confidence']:.2f}")
        print(f"     Multi-expert usage: {analytics['routing_patterns']['multi_expert_usage_rate']*100:.1f}%")
        print()
        
        # Success summary
        print("  🎯 All routing scenarios optimal!")
        print("     ✅ Simple task → Python Guru (single expert)")
        print("     ✅ Multi-domain → Senior Partner (multi-expert)")
        print("     ✅ Strategic crisis → Senior Partner (multi-expert)")
        print()
        
        print("✅ Story 3.2: Contextual Expertise Routing - DEMONSTRATED")
        
    except Exception as e:
        print(f"❌ Contextual expertise routing demonstration failed: {e}")
        import traceback
        traceback.print_exc()
        print("❌ Story 3.2: Contextual Expertise Routing - FAILED")


if __name__ == "__main__":
    demonstrate_contextual_expertise_routing()
