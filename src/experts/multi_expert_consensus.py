"""Multi-Expert Consensus Mechanisms - Story 3.4 Implementation

This module implements sophisticated multi-expert consensus mechanisms for
complex cross-functional decisions, enabling coordination of multiple expert
perspectives with conflict resolution and consensus building capabilities.
"""

from typing import Dict, Any, List, Optional, Tuple
from enum import Enum
from datetime import datetime
from dataclasses import dataclass, field
import logging
from collections import defaultdict

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from dynamic_persona_system import ExpertPersonaType
from contextual_expertise_router import ContextualExpertiseRouter, RoutingContext, RoutingComplexity
sys.path.append(str(Path(__file__).parent.parent / "interfaces"))
from interfaces.expertise_decision_interfaces import ExpertiseDecisionInterfaceManager, DecisionContext


class ConsensusType(Enum):
    """Types of consensus mechanisms"""
    UNANIMOUS = "unanimous"
    MAJORITY = "majority"
    WEIGHTED_CONSENSUS = "weighted_consensus"
    EXPERT_HIERARCHY = "expert_hierarchy"
    DOMAIN_SPECIALIST = "domain_specialist"


class ConflictResolutionStrategy(Enum):
    """Strategies for resolving expert conflicts"""
    SENIOR_ARBITRATION = "senior_arbitration"
    EVIDENCE_BASED = "evidence_based"
    STAKEHOLDER_PRIORITY = "stakeholder_priority"
    RISK_MINIMIZATION = "risk_minimization"
    COMPROMISE_SOLUTION = "compromise_solution"


class ConsensusPhase(Enum):
    """Phases of multi-expert consensus process"""
    EXPERT_SELECTION = "expert_selection"
    INITIAL_ANALYSIS = "initial_analysis"
    PERSPECTIVE_SHARING = "perspective_sharing"
    CONFLICT_IDENTIFICATION = "conflict_identification"
    CONSENSUS_BUILDING = "consensus_building"
    FINAL_VALIDATION = "final_validation"


@dataclass
class ExpertPerspective:
    """Individual expert perspective on a decision"""
    expert_persona: ExpertPersonaType
    decision_analysis: Dict[str, Any]
    recommendation: str
    confidence_level: float
    key_considerations: List[str]
    risk_assessment: Dict[str, Any]
    supporting_evidence: List[str]
    concerns_raised: List[str]
    collaboration_notes: Optional[str] = None


@dataclass
class ConsensusAnalysis:
    """Analysis of consensus across expert perspectives"""
    consensus_type: ConsensusType
    consensus_strength: float
    agreement_areas: List[str]
    disagreement_areas: List[str]
    conflicting_perspectives: List[Tuple[ExpertPersonaType, ExpertPersonaType]]
    consensus_recommendation: str
    confidence_score: float
    resolution_strategy: Optional[ConflictResolutionStrategy] = None


@dataclass
class MultiExpertSession:
    """Multi-expert consensus session"""
    session_id: str
    decision_context: DecisionContext
    participating_experts: List[ExpertPersonaType]
    consensus_mechanism: ConsensusType
    expert_perspectives: List[ExpertPerspective] = field(default_factory=list)
    consensus_phases: List[Dict[str, Any]] = field(default_factory=list)
    final_consensus: Optional[ConsensusAnalysis] = None
    session_metadata: Dict[str, Any] = field(default_factory=dict)


class MultiExpertConsensusManager:
    """Multi-Expert Consensus Management System
    
    This class provides sophisticated multi-expert consensus capabilities including:
    - Automated expert selection for complex decisions
    - Parallel and sequential expert consultation processes
    - Advanced conflict detection and resolution mechanisms
    - Weighted consensus building based on expertise relevance
    - Quality assurance through multi-perspective validation
    
    Academic Note: Demonstrates advanced multi-expert coordination patterns
    for Epic 3 Story 3.4 - sophisticated consensus mechanisms.
    """
    
    def __init__(self, router: ContextualExpertiseRouter, interface_manager: ExpertiseDecisionInterfaceManager):
        """Initialize Multi-Expert Consensus Manager
        
        Args:
            router: Contextual expertise router for expert selection
            interface_manager: Interface manager for expert-specific interactions
        """
        self.router = router
        self.interface_manager = interface_manager
        self.consensus_sessions: List[MultiExpertSession] = []
        self.consensus_patterns: Dict[str, Any] = {}
        
        # Consensus mechanism configurations
        self.consensus_configs = self._initialize_consensus_configs()
        self.conflict_resolution_strategies = self._initialize_conflict_strategies()
        
        # Expert weighting and compatibility
        self.expert_weights = self._initialize_expert_weights()
        self.expert_compatibility = self._initialize_expert_compatibility()
        
        self.logger = logging.getLogger("ConsultingAI.MultiExpertConsensusManager")
        
        self.logger.info(
            "Multi-Expert Consensus Manager initialized",
            extra={
                "consensus_mechanisms": len(ConsensusType),
                "conflict_strategies": len(ConflictResolutionStrategy),
                "academic_context": "Epic 3 Story 3.4 - Multi-Expert Consensus Mechanisms"
            }
        )
    
    def _initialize_consensus_configs(self) -> Dict[ConsensusType, Dict[str, Any]]:
        """Initialize consensus mechanism configurations"""
        return {
            ConsensusType.UNANIMOUS: {
                "threshold": 1.0,
                "min_experts": 2,
                "max_experts": 4,
                "conflict_tolerance": 0.0,
                "use_cases": ["critical_decisions", "high_risk_scenarios"]
            },
            ConsensusType.MAJORITY: {
                "threshold": 0.6,
                "min_experts": 3,
                "max_experts": 5,
                "conflict_tolerance": 0.3,
                "use_cases": ["standard_decisions", "moderate_complexity"]
            },
            ConsensusType.WEIGHTED_CONSENSUS: {
                "threshold": 0.7,
                "min_experts": 2,
                "max_experts": 6,
                "conflict_tolerance": 0.4,
                "use_cases": ["domain_specific_decisions", "expertise_hierarchy"]
            },
            ConsensusType.EXPERT_HIERARCHY: {
                "threshold": 0.8,
                "min_experts": 2,
                "max_experts": 4,
                "conflict_tolerance": 0.2,
                "use_cases": ["strategic_decisions", "senior_oversight_required"]
            },
            ConsensusType.DOMAIN_SPECIALIST: {
                "threshold": 0.9,
                "min_experts": 1,
                "max_experts": 3,
                "conflict_tolerance": 0.1,
                "use_cases": ["technical_specialization", "domain_expertise_critical"]
            }
        }
    
    def _initialize_conflict_strategies(self) -> Dict[ConflictResolutionStrategy, Dict[str, Any]]:
        """Initialize conflict resolution strategies"""
        return {
            ConflictResolutionStrategy.SENIOR_ARBITRATION: {
                "approach": "escalate_to_senior_partner",
                "criteria": ["strategic_importance", "organizational_impact"],
                "timeline": "extended_for_review"
            },
            ConflictResolutionStrategy.EVIDENCE_BASED: {
                "approach": "require_additional_evidence",
                "criteria": ["data_quality", "proof_of_concept", "validation"],
                "timeline": "extended_for_analysis"
            },
            ConflictResolutionStrategy.STAKEHOLDER_PRIORITY: {
                "approach": "prioritize_stakeholder_value",
                "criteria": ["stakeholder_impact", "business_value"],
                "timeline": "stakeholder_consultation"
            },
            ConflictResolutionStrategy.RISK_MINIMIZATION: {
                "approach": "choose_lowest_risk_option",
                "criteria": ["risk_assessment", "mitigation_feasibility"],
                "timeline": "risk_analysis_period"
            },
            ConflictResolutionStrategy.COMPROMISE_SOLUTION: {
                "approach": "develop_hybrid_approach",
                "criteria": ["feasibility", "stakeholder_satisfaction"],
                "timeline": "solution_development"
            }
        }
    
    def _initialize_expert_weights(self) -> Dict[ExpertPersonaType, Dict[str, float]]:
        """Initialize expert weighting for different decision domains"""
        return {
            ExpertPersonaType.PYTHON_GURU: {
                "technical_implementation": 1.0,
                "performance_optimization": 1.0,
                "code_quality": 1.0,
                "system_architecture": 0.7,
                "business_analysis": 0.3,
                "security_compliance": 0.6,
                "strategic_planning": 0.2
            },
            ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT: {
                "technical_implementation": 0.8,
                "performance_optimization": 0.8,
                "system_architecture": 1.0,
                "scalability_design": 1.0,
                "integration_strategy": 1.0,
                "business_analysis": 0.6,
                "security_compliance": 0.7,
                "strategic_planning": 0.5
            },
            ExpertPersonaType.BUSINESS_ANALYST_EXPERT: {
                "business_analysis": 1.0,
                "stakeholder_management": 1.0,
                "process_optimization": 1.0,
                "requirements_analysis": 1.0,
                "technical_implementation": 0.4,
                "system_architecture": 0.5,
                "security_compliance": 0.6,
                "strategic_planning": 0.8
            },
            ExpertPersonaType.SECURITY_SPECIALIST: {
                "security_compliance": 1.0,
                "risk_assessment": 1.0,
                "threat_analysis": 1.0,
                "compliance_review": 1.0,
                "technical_implementation": 0.7,
                "system_architecture": 0.8,
                "business_analysis": 0.6,
                "strategic_planning": 0.7
            },
            ExpertPersonaType.SENIOR_PARTNER: {
                "strategic_planning": 1.0,
                "organizational_impact": 1.0,
                "executive_oversight": 1.0,
                "stakeholder_alignment": 1.0,
                "business_analysis": 0.9,
                "system_architecture": 0.6,
                "technical_implementation": 0.4,
                "security_compliance": 0.8
            }
        }
    
    def _initialize_expert_compatibility(self) -> Dict[ExpertPersonaType, List[ExpertPersonaType]]:
        """Initialize expert compatibility matrix for effective collaboration"""
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
                ExpertPersonaType.SENIOR_PARTNER,
                ExpertPersonaType.PYTHON_GURU
            ],
            ExpertPersonaType.SENIOR_PARTNER: [
                ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT,
                ExpertPersonaType.BUSINESS_ANALYST_EXPERT,
                ExpertPersonaType.SECURITY_SPECIALIST
            ]
        }
    

    def _generate_session_id(self) -> str:
        """Generate unique session ID"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        return f"consensus_{timestamp}"
    
    def initiate_multi_expert_consensus(
        self,
        decision_context: DecisionContext,
        preferred_consensus_type: Optional[ConsensusType] = None
    ) -> MultiExpertSession:
        """Initiate multi-expert consensus process
        
        Args:
            decision_context: Context for the decision requiring consensus
            preferred_consensus_type: Optional preferred consensus mechanism
            
        Returns:
            Configured multi-expert consensus session
        """
        session_id = self._generate_session_id()
        
        # Determine optimal consensus mechanism
        consensus_type = preferred_consensus_type or self._select_optimal_consensus_mechanism(decision_context)
        
        # Select participating experts
        participating_experts = self._select_consensus_experts(decision_context, consensus_type)
        
        # Create consensus session
        consensus_session = MultiExpertSession(
            session_id=session_id,
            decision_context=decision_context,
            participating_experts=participating_experts,
            consensus_mechanism=consensus_type,
            session_metadata={
                "initiated_at": datetime.now().isoformat(),
                "decision_complexity": decision_context.complexity_level,
                "domain_focus": decision_context.domain_focus,
                "expert_count": len(participating_experts)
            }
        )
        
        self.logger.info(
            "Multi-expert consensus session initiated",
            extra={
                "session_id": session_id,
                "consensus_type": consensus_type.value,
                "participating_experts": [expert.value for expert in participating_experts],
                "academic_demonstration": "multi_expert_consensus_initiation"
            }
        )
        
        return consensus_session
    
    def execute_consensus_process(
        self,
        consensus_session: MultiExpertSession,
        simulate_expert_input: bool = True
    ) -> Dict[str, Any]:
        """Execute complete multi-expert consensus process
        
        Args:
            consensus_session: Configured consensus session
            simulate_expert_input: Whether to simulate expert input for demonstration
            
        Returns:
            Complete consensus result with expert perspectives and final consensus
        """
        session_id = consensus_session.session_id
        
        self.logger.info(
            "Starting multi-expert consensus process",
            extra={
                "session_id": session_id,
                "academic_demonstration": "multi_expert_consensus_execution"
            }
        )
        
        # Phase 1: Initial Expert Analysis
        initial_analysis = self._conduct_initial_expert_analysis(
            consensus_session, simulate_expert_input
        )
        consensus_session.consensus_phases.append({
            "phase": ConsensusPhase.INITIAL_ANALYSIS,
            "result": initial_analysis,
            "timestamp": datetime.now().isoformat()
        })
        
        # Phase 2: Perspective Sharing and Cross-Pollination
        perspective_sharing = self._conduct_perspective_sharing(
            consensus_session, initial_analysis
        )
        consensus_session.consensus_phases.append({
            "phase": ConsensusPhase.PERSPECTIVE_SHARING,
            "result": perspective_sharing,
            "timestamp": datetime.now().isoformat()
        })
        
        # Phase 3: Conflict Identification and Analysis
        conflict_analysis = self._identify_and_analyze_conflicts(
            consensus_session, perspective_sharing
        )
        consensus_session.consensus_phases.append({
            "phase": ConsensusPhase.CONFLICT_IDENTIFICATION,
            "result": conflict_analysis,
            "timestamp": datetime.now().isoformat()
        })
        
        # Phase 4: Consensus Building Process
        consensus_building = self._conduct_consensus_building(
            consensus_session, conflict_analysis
        )
        consensus_session.consensus_phases.append({
            "phase": ConsensusPhase.CONSENSUS_BUILDING,
            "result": consensus_building,
            "timestamp": datetime.now().isoformat()
        })
        
        # Phase 5: Final Validation and Consensus Formation
        final_consensus = self._finalize_consensus(
            consensus_session, consensus_building
        )
        consensus_session.final_consensus = final_consensus
        consensus_session.consensus_phases.append({
            "phase": ConsensusPhase.FINAL_VALIDATION,
            "result": final_consensus,
            "timestamp": datetime.now().isoformat()
        })
        
        # Store session for learning
        self.consensus_sessions.append(consensus_session)
        self._update_consensus_patterns(consensus_session)
        
        # Compile comprehensive result
        consensus_result = {
            "session_id": session_id,
            "completion_timestamp": datetime.now().isoformat(),
            "consensus_session": consensus_session,
            "process_phases": consensus_session.consensus_phases,
            "final_consensus": final_consensus,
            "expert_perspectives": consensus_session.expert_perspectives,
            "consensus_quality": self._assess_consensus_quality(consensus_session),
            "process_efficiency": self._calculate_process_efficiency(consensus_session),
            "learning_insights": self._extract_learning_insights(consensus_session)
        }
        
        self.logger.info(
            "Multi-expert consensus process completed",
            extra={
                "consensus_result": consensus_result,
                "academic_evaluation": "sophisticated_multi_expert_coordination"
            }
        )
        
        return consensus_result
    
    def _select_optimal_consensus_mechanism(self, context: DecisionContext) -> ConsensusType:
        """Select optimal consensus mechanism based on decision context"""
        
        # Analyze decision characteristics
        complexity = context.complexity_level
        domain_count = len(context.domain_focus)
        stakeholder_count = len(context.stakeholder_context)
        business_impact = context.business_requirements.get("impact", "medium")
        
        # Decision logic for consensus mechanism
        if business_impact == "critical" and complexity in ["high", "very_high"]:
            return ConsensusType.UNANIMOUS
        elif domain_count > 3 or complexity == "very_high":
            return ConsensusType.WEIGHTED_CONSENSUS
        elif stakeholder_count > 3:
            return ConsensusType.MAJORITY
        elif "strategic" in context.decision_type.lower():
            return ConsensusType.EXPERT_HIERARCHY
        elif domain_count == 1:
            return ConsensusType.DOMAIN_SPECIALIST
        else:
            return ConsensusType.MAJORITY
    
    def _select_consensus_experts(
        self, 
        context: DecisionContext, 
        consensus_type: ConsensusType
    ) -> List[ExpertPersonaType]:
        """Select experts for consensus based on context and mechanism"""
        
        config = self.consensus_configs[consensus_type]
        min_experts = config["min_experts"]
        max_experts = config["max_experts"]
        
        # Use router to get expert recommendations
        routing_context = RoutingContext(
            decision_id=context.decision_id,
            decision_type=context.decision_type,
            complexity_level=RoutingComplexity.COMPLEX,  # Multi-expert implies complexity
            stakeholder_requirements={},  # Simplified for this method
            domain_requirements=context.domain_focus,
            business_impact=context.business_requirements.get("impact", "medium"),
            timeline_constraints={"urgency": "normal"},
            risk_factors=[],
            compliance_requirements=[],
            multi_expert_needed=True
        )
        
        routing_result = self.router.route_to_optimal_expertise(routing_context)
        
        # Extract experts from routing result
        experts = [routing_result["optimal_routing"]["primary_expert"]["persona_type"]]
        
        # Add supporting experts
        supporting_experts = routing_result["optimal_routing"].get("supporting_experts", [])
        for expert in supporting_experts:
            experts.append(expert["persona_type"])
        
        # Ensure we have enough experts and they're compatible
        experts = self._ensure_expert_compatibility(experts, min_experts, max_experts)
        
        return experts[:max_experts]  # Limit to max allowed
    
    def _ensure_expert_compatibility(
        self, 
        experts: List[ExpertPersonaType], 
        min_experts: int, 
        max_experts: int
    ) -> List[ExpertPersonaType]:
        """Ensure expert list meets compatibility and count requirements"""
        
        # Remove duplicates while preserving order
        unique_experts = []
        seen = set()
        for expert in experts:
            if expert not in seen:
                unique_experts.append(expert)
                seen.add(expert)
        
        # Add compatible experts if we need more
        while len(unique_experts) < min_experts:
            # Find compatible expert not already in list
            for expert in unique_experts:
                compatible = self.expert_compatibility.get(expert, [])
                for comp_expert in compatible:
                    if comp_expert not in unique_experts:
                        unique_experts.append(comp_expert)
                        break
                if len(unique_experts) >= min_experts:
                    break
            
            # Fallback: add any remaining expert type
            if len(unique_experts) < min_experts:
                all_experts = list(ExpertPersonaType)
                for expert in all_experts:
                    if expert not in unique_experts:
                        unique_experts.append(expert)
                        break
        
        return unique_experts
    
    def _conduct_initial_expert_analysis(
        self, 
        session: MultiExpertSession, 
        simulate_expert_input: bool = True
    ) -> Dict[str, Any]:
        """Conduct initial analysis by all participating experts"""
        
        expert_perspectives = []
        analysis_results = {}
        
        for expert in session.participating_experts:
            try:
                if simulate_expert_input:
                    # Generate simulated expert perspective for demonstration
                    perspective = self._generate_simulated_expert_perspective(
                        expert, session.decision_context
                    )
                    expert_perspectives.append(perspective)
                    analysis_results[expert.value] = {
                        "status": "completed",
                        "perspective": perspective,
                        "simulation": True
                    }
                else:
                    # Create actual expert session
                    expert_session = self.interface_manager.create_expert_session(
                        session.decision_context, expert
                    )
                    
                    if expert_session:
                        # Get expert analysis
                        expert_analysis = expert_session.analyze_decision(session.decision_context)
                        
                        # Convert to ExpertPerspective
                        perspective = ExpertPerspective(
                            expert_persona=expert,
                            decision_analysis=expert_analysis.get("analysis", {}),
                            recommendation=expert_analysis.get("recommendation", "No recommendation provided"),
                            confidence_level=expert_analysis.get("confidence", 0.5),
                            key_considerations=expert_analysis.get("considerations", []),
                            risk_assessment=expert_analysis.get("risks", {}),
                            supporting_evidence=expert_analysis.get("evidence", []),
                            concerns_raised=expert_analysis.get("concerns", [])
                        )
                        
                        expert_perspectives.append(perspective)
                        analysis_results[expert.value] = {
                            "status": "completed",
                            "perspective": perspective,
                            "simulation": False
                        }
                    else:
                        print(f"Failed to create session for {expert.value}: No interface available for persona {expert.value}")
                        # Create fallback simulated perspective
                        perspective = self._generate_simulated_expert_perspective(
                            expert, session.decision_context
                        )
                        expert_perspectives.append(perspective)
                        analysis_results[expert.value] = {
                            "status": "fallback_simulation",
                            "perspective": perspective,
                            "simulation": True
                        }
                        
            except Exception as e:
                print(f"Error analyzing with {expert.value}: {e}")
                # Create fallback simulated perspective
                perspective = self._generate_simulated_expert_perspective(
                    expert, session.decision_context
                )
                expert_perspectives.append(perspective)
                analysis_results[expert.value] = {
                    "status": "error_fallback",
                    "perspective": perspective,
                    "error": str(e),
                    "simulation": True
                }
        
        # Store perspectives in session
        session.expert_perspectives = expert_perspectives
        
        return {
            "participating_experts": len(session.participating_experts),
            "perspectives_generated": len(expert_perspectives),
            "analysis_results": analysis_results,
            "consensus_indicators": self._calculate_initial_consensus_indicators(expert_perspectives)
        }
    
    def _calculate_initial_consensus_indicators(self, perspectives: List[ExpertPerspective]) -> Dict[str, Any]:
        """Calculate initial consensus indicators from expert perspectives"""
        
        if not perspectives:
            return {
                "average_confidence": 0.0,
                "confidence_variance": 0.0,
                "recommendation_diversity": 0.0,
                "consensus_likelihood": 0.0
            }
        
        # Calculate confidence metrics
        confidences = [p.confidence_level for p in perspectives]
        average_confidence = sum(confidences) / len(confidences)
        confidence_variance = sum((c - average_confidence) ** 2 for c in confidences) / len(confidences)
        
        # Calculate recommendation diversity
        recommendations = [p.recommendation for p in perspectives]
        unique_recommendations = len(set(recommendations))
        recommendation_diversity = unique_recommendations / len(recommendations)
        
        # Estimate consensus likelihood
        consensus_likelihood = (average_confidence * 0.4) + ((1 - recommendation_diversity) * 0.6)
        
        return {
            "average_confidence": average_confidence,
            "confidence_variance": confidence_variance,
            "recommendation_diversity": recommendation_diversity,
            "consensus_likelihood": consensus_likelihood
        }
    
    def _generate_simulated_expert_perspective(
        self, 
        expert: ExpertPersonaType, 
        context: DecisionContext
    ) -> ExpertPerspective:
        """Generate simulated expert perspective for demonstration purposes"""
        
        # Simulate expert-specific analysis based on persona
        if expert == ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT:
            return ExpertPerspective(
                expert_persona=expert,
                decision_analysis={
                    "architectural_assessment": "Microservices migration requires careful service boundary design",
                    "scalability_analysis": "Current monolith limits horizontal scaling",
                    "integration_strategy": "API-first approach with event-driven architecture"
                },
                recommendation="Implement phased microservices migration with domain-driven design",
                confidence_level=0.85,
                key_considerations=[
                    "Service boundary definition",
                    "Data consistency patterns",
                    "Deployment orchestration",
                    "Monitoring and observability"
                ],
                risk_assessment={
                    "technical_risks": ["service sprawl", "distributed system complexity"],
                    "mitigation_strategies": ["strong governance", "automated testing"]
                },
                supporting_evidence=[
                    "Industry best practices for microservices adoption",
                    "Scalability requirements analysis"
                ],
                concerns_raised=[
                    "Team readiness for distributed systems",
                    "Operational complexity increase"
                ]
            )
        elif expert == ExpertPersonaType.BUSINESS_ANALYST_EXPERT:
            return ExpertPerspective(
                expert_persona=expert,
                decision_analysis={
                    "business_impact": "Migration supports business agility and faster time-to-market",
                    "stakeholder_analysis": "Development teams favor flexibility, operations concerned about complexity",
                    "cost_benefit": "Higher initial investment, long-term operational benefits"
                },
                recommendation="Proceed with migration focusing on business value delivery",
                confidence_level=0.78,
                key_considerations=[
                    "Business continuity during migration",
                    "Team training and skill development",
                    "Customer impact minimization",
                    "ROI timeline expectations"
                ],
                risk_assessment={
                    "business_risks": ["service disruption", "extended timeline"],
                    "mitigation_strategies": ["phased rollout", "rollback procedures"]
                },
                supporting_evidence=[
                    "Business agility requirements",
                    "Competitive advantage analysis"
                ],
                concerns_raised=[
                    "Migration timeline impact on feature delivery",
                    "Resource allocation during transition"
                ]
            )
        elif expert == ExpertPersonaType.SECURITY_SPECIALIST:
            return ExpertPerspective(
                expert_persona=expert,
                decision_analysis={
                    "security_assessment": "Microservices increase attack surface but improve isolation",
                    "compliance_impact": "Enhanced security boundaries support compliance requirements",
                    "threat_analysis": "Service-to-service communication requires robust authentication"
                },
                recommendation="Implement zero-trust security model with service mesh",
                confidence_level=0.82,
                key_considerations=[
                    "Service-to-service authentication",
                    "API security and rate limiting",
                    "Secrets management",
                    "Security monitoring and logging"
                ],
                risk_assessment={
                    "security_risks": ["increased attack surface", "service communication vulnerabilities"],
                    "mitigation_strategies": ["service mesh implementation", "comprehensive monitoring"]
                },
                supporting_evidence=[
                    "Zero-trust security principles",
                    "Microservices security best practices"
                ],
                concerns_raised=[
                    "Complexity of distributed security",
                    "Key management across services"
                ]
            )
        else:
            # Generic expert perspective
            return ExpertPerspective(
                expert_persona=expert,
                decision_analysis={
                    "general_assessment": f"{expert.value} analysis of the decision context",
                    "domain_perspective": f"Specialized {expert.value} viewpoint"
                },
                recommendation=f"Recommendation from {expert.value} perspective",
                confidence_level=0.75,
                key_considerations=[
                    f"{expert.value} specific consideration 1",
                    f"{expert.value} specific consideration 2"
                ],
                risk_assessment={
                    "risks": [f"{expert.value} identified risks"],
                    "mitigations": [f"{expert.value} suggested mitigations"]
                },
                supporting_evidence=[f"{expert.value} supporting evidence"],
                concerns_raised=[f"{expert.value} concerns"]
            )
    
    def _assess_initial_consensus(self, analyses: Dict[str, ExpertPerspective]) -> Dict[str, Any]:
        """Assess initial consensus indicators from expert analyses"""
        
        if len(analyses) < 2:
            return {"consensus_possible": True, "confidence": 1.0}
        
        # Analyze confidence levels
        confidences = [perspective.confidence_level for perspective in analyses.values()]
        avg_confidence = sum(confidences) / len(confidences)
        confidence_variance = sum((c - avg_confidence) ** 2 for c in confidences) / len(confidences)
        
        # Analyze recommendation similarity (simplified)
        recommendations = [perspective.recommendation for perspective in analyses.values()]
        unique_recommendations = len(set(recommendations))
        
        consensus_indicators = {
            "average_confidence": avg_confidence,
            "confidence_variance": confidence_variance,
            "recommendation_diversity": unique_recommendations / len(recommendations),
            "consensus_possible": confidence_variance < 0.1 and unique_recommendations <= len(recommendations) / 2,
            "estimated_consensus_strength": max(0.0, 1.0 - (confidence_variance + unique_recommendations / len(recommendations)) / 2)
        }
        
        return consensus_indicators
    
    def _conduct_perspective_sharing(
        self, 
        session: MultiExpertSession, 
        initial_analysis: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Conduct perspective sharing and cross-pollination between experts"""
        
        shared_insights = defaultdict(list)
        cross_expert_feedback = {}
        
        # Simulate perspective sharing (in real implementation, this would involve actual expert interaction)
        for i, perspective1 in enumerate(session.expert_perspectives):
            for j, perspective2 in enumerate(session.expert_perspectives):
                if i != j:
                    # Generate cross-expert insights
                    insight = self._generate_cross_expert_insight(perspective1, perspective2)
                    shared_insights[perspective1.expert_persona.value].append(insight)
        
        # Update expert perspectives with shared insights
        for perspective in session.expert_perspectives:
            expert_key = perspective.expert_persona.value
            if expert_key in shared_insights:
                perspective.collaboration_notes = f"Insights from {len(shared_insights[expert_key])} expert interactions"
        
        return {
            "perspective_sharing_completed": True,
            "shared_insights": dict(shared_insights),
            "cross_pollination_effects": self._assess_cross_pollination_effects(shared_insights),
            "updated_perspectives": [p.expert_persona.value for p in session.expert_perspectives]
        }
    
    def _generate_cross_expert_insight(
        self, 
        perspective1: ExpertPerspective, 
        perspective2: ExpertPerspective
    ) -> Dict[str, Any]:
        """Generate insight from cross-expert perspective sharing"""
        
        return {
            "from_expert": perspective2.expert_persona.value,
            "to_expert": perspective1.expert_persona.value,
            "insight_type": "domain_complement",
            "insight": f"{perspective2.expert_persona.value} perspective adds {perspective2.key_considerations[0] if perspective2.key_considerations else 'additional considerations'}",
            "relevance": self._calculate_perspective_relevance(perspective1, perspective2)
        }
    
    def _calculate_perspective_relevance(
        self, 
        perspective1: ExpertPerspective, 
        perspective2: ExpertPerspective
    ) -> float:
        """Calculate relevance between two expert perspectives"""
        
        # Check compatibility
        compatible_experts = self.expert_compatibility.get(perspective1.expert_persona, [])
        if perspective2.expert_persona in compatible_experts:
            return 0.8
        
        # Check confidence alignment
        confidence_diff = abs(perspective1.confidence_level - perspective2.confidence_level)
        relevance = max(0.3, 1.0 - confidence_diff)
        
        return relevance
    
    def _assess_cross_pollination_effects(self, shared_insights: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
        """Assess effects of cross-expert perspective sharing"""
        
        total_insights = sum(len(insights) for insights in shared_insights.values())
        
        return {
            "total_insights_shared": total_insights,
            "average_insights_per_expert": total_insights / len(shared_insights) if shared_insights else 0,
            "cross_pollination_effectiveness": min(1.0, total_insights / (len(shared_insights) * 2)) if shared_insights else 0
        }
    
    def _identify_and_analyze_conflicts(
        self, 
        session: MultiExpertSession, 
        perspective_sharing: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Identify and analyze conflicts between expert perspectives"""
        
        conflicts = []
        agreement_areas = []
        
        # Compare expert perspectives pairwise
        perspectives = session.expert_perspectives
        for i in range(len(perspectives)):
            for j in range(i + 1, len(perspectives)):
                conflict_analysis = self._analyze_perspective_conflict(perspectives[i], perspectives[j])
                if conflict_analysis["has_conflict"]:
                    conflicts.append(conflict_analysis)
                else:
                    agreement_areas.extend(conflict_analysis["agreement_areas"])
        
        # Determine conflict resolution strategy
        resolution_strategy = self._determine_conflict_resolution_strategy(conflicts, session)
        
        return {
            "conflicts_identified": len(conflicts),
            "conflict_details": conflicts,
            "agreement_areas": list(set(agreement_areas)),  # Remove duplicates
            "conflict_severity": self._assess_conflict_severity(conflicts),
            "resolution_strategy": resolution_strategy,
            "consensus_feasibility": self._assess_consensus_feasibility(conflicts, session.consensus_mechanism)
        }
    
    def _analyze_perspective_conflict(
        self, 
        perspective1: ExpertPerspective, 
        perspective2: ExpertPerspective
    ) -> Dict[str, Any]:
        """Analyze conflict between two expert perspectives"""
        
        # Compare recommendations
        recommendation_conflict = perspective1.recommendation != perspective2.recommendation
        
        # Compare confidence levels
        confidence_gap = abs(perspective1.confidence_level - perspective2.confidence_level)
        
        # Compare concerns
        common_concerns = set(perspective1.concerns_raised) & set(perspective2.concerns_raised)
        conflicting_concerns = set(perspective1.concerns_raised) ^ set(perspective2.concerns_raised)
        
        has_conflict = recommendation_conflict or confidence_gap > 0.3
        
        return {
            "expert_pair": (perspective1.expert_persona.value, perspective2.expert_persona.value),
           "has_conflict": has_conflict,
           "conflict_types": {
               "recommendation_conflict": recommendation_conflict,
               "confidence_gap": confidence_gap > 0.3,
               "concern_divergence": len(conflicting_concerns) > len(common_concerns)
           },
           "conflict_severity": self._calculate_conflict_severity(
               recommendation_conflict, confidence_gap, len(conflicting_concerns)
           ),
           "agreement_areas": list(common_concerns),
           "disagreement_details": {
               "recommendation_diff": recommendation_conflict,
               "confidence_gap": confidence_gap,
               "conflicting_concerns": list(conflicting_concerns)
           }
       }
   
    def _calculate_conflict_severity(
        self, 
        recommendation_conflict: bool, 
        confidence_gap: float, 
        concern_divergence: int
    ) -> str:
        """Calculate severity of conflict between perspectives"""
        
        severity_score = 0
        if recommendation_conflict:
            severity_score += 3
        if confidence_gap > 0.3:
            severity_score += 2
        if concern_divergence > 2:
            severity_score += 1
        
        if severity_score >= 5:
            return "high"
        elif severity_score >= 3:
            return "medium"
        elif severity_score >= 1:
            return "low"
        else:
            return "minimal"

    def _assess_conflict_severity(self, conflicts: List[Dict[str, Any]]) -> str:
        """Assess overall conflict severity across all expert pairs"""
        
        if not conflicts:
            return "none"
        
        severity_levels = [conflict["conflict_severity"] for conflict in conflicts]
        severity_counts = {"high": 0, "medium": 0, "low": 0, "minimal": 0}
        
        for level in severity_levels:
            severity_counts[level] += 1
        
        if severity_counts["high"] > 0:
            return "high"
        elif severity_counts["medium"] > len(conflicts) / 2:
            return "medium"
        elif severity_counts["low"] > 0:
            return "low"
        else:
            return "minimal"

    def _determine_conflict_resolution_strategy(
        self, 
        conflicts: List[Dict[str, Any]], 
        session: MultiExpertSession
    ) -> ConflictResolutionStrategy:
        """Determine appropriate conflict resolution strategy"""
        
        if not conflicts:
            return ConflictResolutionStrategy.COMPROMISE_SOLUTION
        
        # Analyze conflict characteristics
        high_severity_conflicts = sum(1 for c in conflicts if c["conflict_severity"] == "high")
        business_impact = session.decision_context.business_requirements.get("impact", "medium")
        complexity = session.decision_context.complexity_level
        
        # Strategy selection logic
        if high_severity_conflicts > 0 and business_impact == "critical":
            return ConflictResolutionStrategy.SENIOR_ARBITRATION
        elif high_severity_conflicts > 0:
            return ConflictResolutionStrategy.EVIDENCE_BASED
        elif business_impact in ["high", "critical"]:
            return ConflictResolutionStrategy.STAKEHOLDER_PRIORITY
        elif complexity in ["high", "very_high"]:
            return ConflictResolutionStrategy.RISK_MINIMIZATION
        else:
            return ConflictResolutionStrategy.COMPROMISE_SOLUTION

    def _assess_consensus_feasibility(
        self, 
        conflicts: List[Dict[str, Any]], 
        consensus_mechanism: ConsensusType
    ) -> Dict[str, Any]:
        """Assess feasibility of reaching consensus given conflicts"""
        
        config = self.consensus_configs[consensus_mechanism]
        conflict_tolerance = config["conflict_tolerance"]
        
        if not conflicts:
            return {"feasible": True, "confidence": 1.0, "estimated_effort": "minimal"}
        
        # Calculate conflict intensity
        total_conflicts = len(conflicts)
        high_severity = sum(1 for c in conflicts if c["conflict_severity"] == "high")
        conflict_intensity = (high_severity * 3 + total_conflicts) / (total_conflicts * 3)
        
        feasible = conflict_intensity <= conflict_tolerance
        confidence = max(0.1, 1.0 - conflict_intensity)
        
        if conflict_intensity < 0.2:
            effort = "minimal"
        elif conflict_intensity < 0.5:
            effort = "moderate"
        else:
            effort = "significant"
        
        return {
            "feasible": feasible,
            "confidence": confidence,
            "estimated_effort": effort,
            "conflict_intensity": conflict_intensity,
            "tolerance_threshold": conflict_tolerance
        }

    def _conduct_consensus_building(
        self, 
        session: MultiExpertSession, 
        conflict_analysis: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Conduct consensus building process"""
        
        consensus_mechanism = session.consensus_mechanism
        conflicts = conflict_analysis["conflict_details"]
        resolution_strategy = conflict_analysis["resolution_strategy"]
        
        # Apply resolution strategy
        resolution_result = self._apply_conflict_resolution(
            conflicts, resolution_strategy, session
        )
        
        # Build consensus based on mechanism
        consensus_result = self._build_consensus_by_mechanism(
            session, consensus_mechanism, resolution_result
        )
        
        # Validate consensus quality
        consensus_validation = self._validate_consensus_quality(
            consensus_result, session
        )
        
        return {
            "resolution_applied": resolution_strategy.value,
            "resolution_result": resolution_result,
            "consensus_mechanism_used": consensus_mechanism.value,
            "consensus_result": consensus_result,
            "consensus_validation": consensus_validation,
            "consensus_building_success": consensus_validation["overall_quality_score"] > 0.7
        }

    def _apply_conflict_resolution(
        self, 
        conflicts: List[Dict[str, Any]], 
        strategy: ConflictResolutionStrategy, 
        session: MultiExpertSession
    ) -> Dict[str, Any]:
        """Apply conflict resolution strategy"""
        
        strategy_config = self.conflict_resolution_strategies[strategy]
        
        resolution_actions = []
        resolved_conflicts = 0
        
        for conflict in conflicts:
            # Simulate conflict resolution based on strategy
            resolution_action = self._resolve_specific_conflict(conflict, strategy, session)
            resolution_actions.append(resolution_action)
            
            if resolution_action["resolution_success"]:
                resolved_conflicts += 1
        
        return {
            "strategy_used": strategy.value,
            "strategy_config": strategy_config,
            "total_conflicts": len(conflicts),
            "resolved_conflicts": resolved_conflicts,
            "resolution_success_rate": resolved_conflicts / len(conflicts) if conflicts else 1.0,
            "resolution_actions": resolution_actions
        }

    def _resolve_specific_conflict(
        self, 
        conflict: Dict[str, Any], 
        strategy: ConflictResolutionStrategy, 
        session: MultiExpertSession
    ) -> Dict[str, Any]:
        """Resolve specific conflict using chosen strategy"""
        
        expert_pair = conflict["expert_pair"]
        conflict_severity = conflict["conflict_severity"]
        
        # Simulate resolution based on strategy
        if strategy == ConflictResolutionStrategy.SENIOR_ARBITRATION:
            resolution = {
                "method": "senior_partner_decision",
                "resolution": "Senior partner arbitration applied",
                "success_probability": 0.9 if conflict_severity != "high" else 0.8
            }
        elif strategy == ConflictResolutionStrategy.EVIDENCE_BASED:
            resolution = {
                "method": "additional_evidence_required",
                "resolution": "Request additional evidence and analysis",
                "success_probability": 0.8 if conflict_severity != "high" else 0.7
            }
        elif strategy == ConflictResolutionStrategy.COMPROMISE_SOLUTION:
            resolution = {
                "method": "hybrid_approach_development",
                "resolution": "Develop compromise solution incorporating both perspectives",
                "success_probability": 0.7
            }
        else:
            resolution = {
                "method": "general_resolution",
                "resolution": f"Apply {strategy.value} approach",
                "success_probability": 0.75
            }
        
        # Determine success based on probability
        success = resolution["success_probability"] > 0.6
        
        return {
            "conflict_id": f"{expert_pair[0]}_{expert_pair[1]}",
            "expert_pair": expert_pair,
            "resolution_method": resolution["method"],
            "resolution_description": resolution["resolution"],
            "resolution_success": success,
            "confidence": resolution["success_probability"]
        }

    def _build_consensus_by_mechanism(
        self, 
        session: MultiExpertSession, 
        mechanism: ConsensusType, 
        resolution_result: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Build consensus using specified mechanism"""
        
        perspectives = session.expert_perspectives
        config = self.consensus_configs[mechanism]
        
        if mechanism == ConsensusType.UNANIMOUS:
            return self._build_unanimous_consensus(perspectives, resolution_result)
        elif mechanism == ConsensusType.MAJORITY:
            return self._build_majority_consensus(perspectives, resolution_result)
        elif mechanism == ConsensusType.WEIGHTED_CONSENSUS:
            return self._build_weighted_consensus(perspectives, session.decision_context, resolution_result)
        elif mechanism == ConsensusType.EXPERT_HIERARCHY:
            return self._build_hierarchical_consensus(perspectives, resolution_result)
        elif mechanism == ConsensusType.DOMAIN_SPECIALIST:
            return self._build_specialist_consensus(perspectives, session.decision_context, resolution_result)
        else:
            return self._build_majority_consensus(perspectives, resolution_result)  # Fallback
   
    def _build_unanimous_consensus(
           self, 
           perspectives: List[ExpertPerspective], 
           resolution_result: Dict[str, Any]
       ) -> Dict[str, Any]:
           """Build unanimous consensus"""
           
           # Check if all experts agree after conflict resolution
           recommendations = [p.recommendation for p in perspectives]
           unique_recommendations = set(recommendations)
           
           if len(unique_recommendations) == 1:
               consensus_recommendation = recommendations[0]
               consensus_strength = 1.0
               success = True
           else:
               # Attempt to find common ground
               consensus_recommendation = f"Synthesized approach incorporating {len(unique_recommendations)} expert perspectives"
               consensus_strength = 0.8 if resolution_result["resolution_success_rate"] > 0.8 else 0.6
               success = resolution_result["resolution_success_rate"] > 0.9
           
           return {
               "mechanism": "unanimous",
               "success": success,
               "consensus_recommendation": consensus_recommendation,
               "consensus_strength": consensus_strength,
               "participating_experts": [p.expert_persona.value for p in perspectives],
               "confidence_scores": [p.confidence_level for p in perspectives]
           }
    def _build_majority_consensus(
           self, 
           perspectives: List[ExpertPerspective], 
           resolution_result: Dict[str, Any]
       ) -> Dict[str, Any]:
           """Build majority consensus"""
           
           # Count recommendation frequencies
           recommendations = [p.recommendation for p in perspectives]
           recommendation_counts = {}
           for rec in recommendations:
               recommendation_counts[rec] = recommendation_counts.get(rec, 0) + 1
           
           # Find majority recommendation
           total_experts = len(perspectives)
           majority_threshold = total_experts / 2
           
           majority_recommendation = max(recommendation_counts.items(), key=lambda x: x[1])
           
           if majority_recommendation[1] > majority_threshold:
               consensus_recommendation = majority_recommendation[0]
               consensus_strength = majority_recommendation[1] / total_experts
               success = True
           else:
               # No clear majority, synthesize
               consensus_recommendation = f"Balanced approach considering {len(recommendation_counts)} perspectives"
               consensus_strength = 0.6
               success = resolution_result["resolution_success_rate"] > 0.7
           
           return {
               "mechanism": "majority",
               "success": success,
               "consensus_recommendation": consensus_recommendation,
               "consensus_strength": consensus_strength,
               "vote_distribution": recommendation_counts,
               "majority_threshold": majority_threshold
           }
       
    def _build_weighted_consensus(
        self, 
        perspectives: List[ExpertPerspective], 
        context: DecisionContext, 
        resolution_result: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Build weighted consensus based on expertise relevance"""
        
        # Check if we have any perspectives
        if not perspectives:
            return {
                "mechanism": "weighted_consensus",
                "success": False,
                "consensus_recommendation": "No expert perspectives available",
                "consensus_strength": 0.0,
                "expert_weights": {},
                "weighted_confidence": 0.0,
                "leading_expert": "none"
            }
        
        # Calculate weights for each expert based on domain relevance
        expert_weights = {}
        total_weight = 0
        
        for perspective in perspectives:
            expert = perspective.expert_persona
            domain_weights = self.expert_weights.get(expert, {})
            
            # Calculate relevance to decision domains
            relevance_score = 0
            for domain in context.domain_focus:
                domain_weight = domain_weights.get(domain, 0.5)  # Default weight
                relevance_score += domain_weight
        
            # Normalize by number of domains
            expert_weight = relevance_score / len(context.domain_focus) if context.domain_focus else 0.5
            expert_weights[expert.value] = expert_weight
            total_weight += expert_weight
        
        # Normalize weights
        if total_weight > 0:
            for expert in expert_weights:
                expert_weights[expert] /= total_weight
        
        # Build weighted consensus
        weighted_confidence = sum(
            expert_weights.get(p.expert_persona.value, 0) * p.confidence_level 
            for p in perspectives
        )
        
        # Select recommendation from highest weighted expert
        weighted_scores = [
            (p, expert_weights.get(p.expert_persona.value, 0) * p.confidence_level)
            for p in perspectives
        ]
        
        best_weighted_perspective = max(weighted_scores, key=lambda x: x[1])[0]
        
        return {
            "mechanism": "weighted_consensus",
            "success": weighted_confidence > 0.7,
            "consensus_recommendation": best_weighted_perspective.recommendation,
            "consensus_strength": weighted_confidence,
            "expert_weights": expert_weights,
            "weighted_confidence": weighted_confidence,
            "leading_expert": best_weighted_perspective.expert_persona.value
        }

    def _build_hierarchical_consensus(
        self, 
        perspectives: List[ExpertPerspective], 
        resolution_result: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Build hierarchical consensus based on expert seniority"""
        
        # Define hierarchy order (Senior Partner > System Architect > Others)
        hierarchy_order = [
            ExpertPersonaType.SENIOR_PARTNER,
            ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT,
            ExpertPersonaType.BUSINESS_ANALYST_EXPERT,
            ExpertPersonaType.SECURITY_SPECIALIST,
            ExpertPersonaType.PYTHON_GURU
        ]
        
        # Sort perspectives by hierarchy
        sorted_perspectives = sorted(
            perspectives,
            key=lambda p: hierarchy_order.index(p.expert_persona) if p.expert_persona in hierarchy_order else len(hierarchy_order)
        )
        
        # Senior-most expert's recommendation takes precedence
        senior_perspective = sorted_perspectives[0]
        
        return {
            "mechanism": "expert_hierarchy",
            "success": senior_perspective.confidence_level > 0.7,
            "consensus_recommendation": senior_perspective.recommendation,
            "consensus_strength": senior_perspective.confidence_level,
            "hierarchy_order": [p.expert_persona.value for p in sorted_perspectives],
            "senior_expert": senior_perspective.expert_persona.value
        }

    def _build_specialist_consensus(
        self, 
        perspectives: List[ExpertPerspective], 
        context: DecisionContext, 
        resolution_result: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Build specialist consensus based on domain expertise"""
        
        # Check if we have any perspectives
        if not perspectives:
            return {
                "mechanism": "domain_specialist",
                "success": False,
                "consensus_recommendation": "No expert perspectives available",
                "consensus_strength": 0.0,
                "specialist_expert": "none",
                "domain_relevance": 0.0
            }
        
        # Identify most relevant specialist for the decision context
        domain_specialists = {
            "python": ExpertPersonaType.PYTHON_GURU,
            "architecture": ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT,
            "business": ExpertPersonaType.BUSINESS_ANALYST_EXPERT,
            "security": ExpertPersonaType.SECURITY_SPECIALIST
        }
        
        # Find the most relevant specialist
        specialist_type = None
        for domain in context.domain_focus:
            if domain.lower() in domain_specialists:
                specialist_type = domain_specialists[domain.lower()]
                break
        
        # Find specialist perspective
        specialist_perspective = None
        if specialist_type:
            specialist_perspective = next(
                (p for p in perspectives if p.expert_persona == specialist_type), 
                None
            )
        
        if specialist_perspective:
            consensus_recommendation = specialist_perspective.recommendation
            consensus_strength = specialist_perspective.confidence_level
            success = consensus_strength > 0.8
        else:
            # Fallback to highest confidence expert
            specialist_perspective = max(perspectives, key=lambda p: p.confidence_level)
            consensus_recommendation = specialist_perspective.recommendation
            consensus_strength = specialist_perspective.confidence_level
            success = consensus_strength > 0.7
        
        return {
            "mechanism": "domain_specialist",
            "success": success,
            "consensus_recommendation": consensus_recommendation,
            "consensus_strength": consensus_strength,
            "specialist_expert": specialist_perspective.expert_persona.value,
            "domain_relevance": self._calculate_domain_relevance(specialist_perspective, context)
        }
   
    def _finalize_consensus(
        self, 
        session: MultiExpertSession, 
        consensus_building: Dict[str, Any]
    ) -> ConsensusAnalysis:
        """Finalize consensus analysis and create final consensus object"""
        
        consensus_result = consensus_building["consensus_result"]
        conflicts = session.consensus_phases[2]["result"]["conflict_details"]  # From conflict identification phase
        
        # Determine agreement and disagreement areas
        agreement_areas = session.consensus_phases[2]["result"]["agreement_areas"]
        disagreement_areas = [
            f"{conflict['expert_pair'][0]} vs {conflict['expert_pair'][1]}" 
            for conflict in conflicts
        ]
        
        # Create conflicting perspectives list
        conflicting_perspectives = [
            (ExpertPersonaType(conflict['expert_pair'][0]), ExpertPersonaType(conflict['expert_pair'][1]))
            for conflict in conflicts
        ]
        
        final_consensus = ConsensusAnalysis(
            consensus_type=session.consensus_mechanism,
            consensus_strength=consensus_result["consensus_strength"],
            agreement_areas=agreement_areas,
            disagreement_areas=disagreement_areas,
            conflicting_perspectives=conflicting_perspectives,
            consensus_recommendation=consensus_result["consensus_recommendation"],
            confidence_score=consensus_result.get("weighted_confidence", consensus_result["consensus_strength"]),
            resolution_strategy=session.consensus_phases[3]["result"]["resolution_applied"]
        )
        
        return final_consensus

    def _validate_consensus_quality(
        self, 
        consensus_result: Dict[str, Any], 
        session: MultiExpertSession
    ) -> Dict[str, Any]:
        """Validate quality of consensus achieved"""
        
        # Safe access to consensus phases
        conflict_resolution_rate = 0.0
        if len(session.consensus_phases) > 3:
            phase_result = session.consensus_phases[3].get("result", {})
            resolution_result = phase_result.get("resolution_result", {})
            conflict_resolution_rate = resolution_result.get("resolution_success_rate", 0.0)
        
        quality_factors = {
            "consensus_strength": consensus_result["consensus_strength"],
            "expert_participation": len(session.expert_perspectives) / max(len(session.participating_experts), 1),
            "conflict_resolution_rate": conflict_resolution_rate,
            "confidence_alignment": self._calculate_confidence_alignment(session.expert_perspectives)
        }
        
        # Calculate overall quality score
        overall_quality = sum(quality_factors.values()) / len(quality_factors)
        
        # Determine quality rating
        if overall_quality >= 0.8:
            quality_rating = "excellent"
        elif overall_quality >= 0.6:
            quality_rating = "good"
        elif overall_quality >= 0.4:
            quality_rating = "acceptable"
        else:
            quality_rating = "poor"
        
        return {
            "quality_factors": quality_factors,
            "overall_quality_score": overall_quality,
            "quality_rating": quality_rating,
            "validation_timestamp": datetime.now().isoformat()
        }

    def _calculate_confidence_alignment(self, perspectives: List[ExpertPerspective]) -> float:
        """Calculate confidence alignment among expert perspectives"""
        if not perspectives or len(perspectives) < 2:
            return 1.0
        
        confidences = [p.confidence_level for p in perspectives]
        avg_confidence = sum(confidences) / len(confidences)
        variance = sum((c - avg_confidence) ** 2 for c in confidences) / len(confidences)
        
        # Return alignment score (1.0 = perfect alignment, 0.0 = no alignment)
        return max(0.0, 1.0 - variance)

    def _assess_consensus_quality(self, session: MultiExpertSession) -> Dict[str, Any]:
        """Assess overall quality of consensus process"""
        
        if not session.final_consensus:
            return {"quality": "incomplete", "score": 0.0}
        
        quality_metrics = {
            "consensus_strength": session.final_consensus.consensus_strength,
            "expert_engagement": len(session.expert_perspectives) / len(session.participating_experts),
            "process_efficiency": len(session.consensus_phases) <= 5,  # Ideal process length
            "conflict_resolution": len(session.final_consensus.conflicting_perspectives) == 0
        }
        
        overall_score = sum(
            1.0 if isinstance(metric, bool) and metric else metric if isinstance(metric, float) else 0.0
            for metric in quality_metrics.values()
        ) / len(quality_metrics)
        
        return {
            "quality_metrics": quality_metrics,
            "overall_score": overall_score,
            "quality_rating": "excellent" if overall_score > 0.9 else "good" if overall_score > 0.7 else "satisfactory" if overall_score > 0.5 else "poor"
        }

    def _calculate_process_efficiency(self, session: MultiExpertSession) -> Dict[str, Any]:
        """Calculate efficiency of consensus process"""
        
        phases_completed = len(session.consensus_phases)
        experts_involved = len(session.participating_experts)
        
        # Efficiency factors
        phase_efficiency = min(1.0, 5.0 / phases_completed)  # Ideal: 5 phases
        expert_efficiency = min(1.0, experts_involved / 3.0)  # Ideal: ~3 experts
        
        if session.final_consensus:
            outcome_efficiency = session.final_consensus.consensus_strength
        else:
            outcome_efficiency = 0.0
        
        overall_efficiency = (phase_efficiency + expert_efficiency + outcome_efficiency) / 3
        
        return {
            "phase_efficiency": phase_efficiency,
            "expert_efficiency": expert_efficiency,
            "outcome_efficiency": outcome_efficiency,
            "overall_efficiency": overall_efficiency,
            "phases_completed": phases_completed,
            "experts_involved": experts_involved
        }

    def _extract_learning_insights(self, session: MultiExpertSession) -> List[str]:
        """Extract learning insights from consensus session"""
        
        insights = []
        
        # Analyze consensus mechanism effectiveness
        if session.final_consensus and session.final_consensus.consensus_strength > 0.8:
            insights.append(f"{session.consensus_mechanism.value} mechanism highly effective for this decision type")
        
        # Analyze expert combination effectiveness
        if len(session.expert_perspectives) >= 3:
            insights.append(f"Multi-expert approach with {len(session.participating_experts)} experts provided comprehensive analysis")
        
        # Analyze conflict resolution
        conflicts = len(session.final_consensus.conflicting_perspectives) if session.final_consensus else 0
        if conflicts == 0:
            insights.append("Conflict resolution strategy successfully resolved all expert disagreements")
        
        return insights

    def _update_consensus_patterns(self, session: MultiExpertSession) -> None:
        """Update consensus patterns for learning"""
        
        decision_type = session.decision_context.decision_type
        mechanism = session.consensus_mechanism.value
        
        if decision_type not in self.consensus_patterns:
            self.consensus_patterns[decision_type] = {
                "total_sessions": 0,
                "mechanism_usage": {},
                "success_rates": {},
                "average_quality": 0.0
            }
        
        pattern = self.consensus_patterns[decision_type]
        pattern["total_sessions"] += 1
        pattern["mechanism_usage"][mechanism] = pattern["mechanism_usage"].get(mechanism, 0) + 1
        
        if session.final_consensus:
            success = session.final_consensus.consensus_strength > 0.7
            pattern["success_rates"][mechanism] = pattern["success_rates"].get(mechanism, []) + [success]

    def get_consensus_analytics(self) -> Dict[str, Any]:
        """Get comprehensive consensus analytics"""
        return {
            "total_consensus_sessions": len(self.consensus_sessions),
            "consensus_patterns": self.consensus_patterns,
            "mechanism_effectiveness": self._analyze_mechanism_effectiveness(),
            "average_consensus_quality": self._calculate_average_consensus_quality(),
            "conflict_resolution_success": self._calculate_conflict_resolution_success()
        }

    def _analyze_mechanism_effectiveness(self) -> Dict[str, float]:
        """Analyze effectiveness of different consensus mechanisms"""
        mechanism_scores = {}
        
        for session in self.consensus_sessions:
            mechanism = session.consensus_mechanism.value
            if session.final_consensus:
                score = session.final_consensus.consensus_strength
                if mechanism not in mechanism_scores:
                    mechanism_scores[mechanism] = []
                mechanism_scores[mechanism].append(score)
        
        # Calculate averages
        effectiveness = {}
        for mechanism, scores in mechanism_scores.items():
            effectiveness[mechanism] = sum(scores) / len(scores)
        
        return effectiveness

    def _calculate_average_consensus_quality(self) -> float:
        """Calculate average consensus quality across all sessions"""
        if not self.consensus_sessions:
            return 0.0
        
        quality_scores = []
        for session in self.consensus_sessions:
            if session.final_consensus:
                quality_scores.append(session.final_consensus.consensus_strength)
        
        return sum(quality_scores) / len(quality_scores) if quality_scores else 0.0

    def _calculate_conflict_resolution_success(self) -> float:
        """Calculate conflict resolution success rate"""
        if not self.consensus_sessions:
            return 0.0
        
        total_sessions = len(self.consensus_sessions)
        successful_resolutions = sum(
            1 for session in self.consensus_sessions 
            if session.final_consensus and len(session.final_consensus.conflicting_perspectives) == 0
        )
        
        return successful_resolutions / total_sessions

    def _calculate_domain_relevance(self, perspective: ExpertPerspective, context: DecisionContext) -> float:
        """Calculate domain relevance score for an expert perspective"""
        
        expert = perspective.expert_persona
        expert_weights = self.expert_weights.get(expert, {})
        
        if not context.domain_focus:
            return 0.5  # Default relevance if no domains specified
        
        # Calculate weighted relevance based on decision domains
        total_relevance = 0.0
        for domain in context.domain_focus:
            domain_weight = expert_weights.get(domain, 0.5)  # Default weight
            total_relevance += domain_weight
        
        # Normalize by number of domains
        average_relevance = total_relevance / len(context.domain_focus)
        
        return min(1.0, average_relevance)  # Cap at 1.0


def create_multi_expert_consensus_manager(
   router: ContextualExpertiseRouter,
   interface_manager: ExpertiseDecisionInterfaceManager
) -> MultiExpertConsensusManager:
   """Factory function to create Multi-Expert Consensus Manager
   
   Args:
       router: Contextual expertise router
       interface_manager: Expertise decision interface manager
       
   Returns:
       Configured MultiExpertConsensusManager instance
   """
   return MultiExpertConsensusManager(router, interface_manager)


def demonstrate_multi_expert_consensus() -> bool:
   """Demonstrate multi-expert consensus mechanisms for Story 3.4
   
   Returns:
       True if demonstration successful, False otherwise
   """
   print("🔧 Demonstrating Multi-Expert Consensus Mechanisms...")
   
   try:
       # Import required dependencies
       from dynamic_persona_system import DynamicPersonaManager
       from contextual_expertise_router import create_contextual_expertise_router
       import sys
       from pathlib import Path
       sys.path.append(str(Path(__file__).parent.parent / "interfaces"))
       from interfaces.expertise_decision_interfaces import create_expertise_decision_interface_manager
       
       # Create required components
       persona_manager = DynamicPersonaManager()
       router = create_contextual_expertise_router(persona_manager)
       interface_manager = create_expertise_decision_interface_manager()
       
       # Create consensus manager
       consensus_manager = create_multi_expert_consensus_manager(router, interface_manager)
       
       print("  ✅ Multi-Expert Consensus Manager created")
       print(f"     Consensus mechanisms: {len(ConsensusType)}")
       print(f"     Conflict strategies: {len(ConflictResolutionStrategy)}")
       
       # Test scenario 1: Multi-domain architecture decision
       print("\n  🧪 Scenario 1: Multi-domain architecture decision...")
       
       architecture_context = DecisionContext(
           decision_id="consensus_001",
           decision_type="enterprise_microservices_migration",
           complexity_level="very_high",
           domain_focus=["architecture", "business_analysis", "security", "performance"],
           stakeholder_context={
               "technical_teams": ["architects", "developers"],
               "business_teams": ["product_managers", "stakeholders"],
               "security_team": ["security_specialists"]
           },
           technical_details={"current_state": "monolith", "target_state": "microservices"},
           business_requirements={"impact": "critical", "timeline": "6_months"},
           constraints={"budget": "significant", "team_skills": "mixed"},
           success_criteria=["scalability", "maintainability", "security", "business_value"],
           expert_persona=ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT  # Will be overridden by consensus
       )
       
       consensus_session_1 = consensus_manager.initiate_multi_expert_consensus(
           architecture_context, ConsensusType.WEIGHTED_CONSENSUS
       )
       
       consensus_result_1 = consensus_manager.execute_consensus_process(consensus_session_1)
       
       print(f"     Consensus type: {consensus_session_1.consensus_mechanism.value}")
       print(f"     Participating experts: {len(consensus_session_1.participating_experts)}")
       print(f"     Process phases: {len(consensus_result_1['process_phases'])}")
       print(f"     Final consensus strength: {consensus_result_1['final_consensus'].consensus_strength:.2f}")
       print(f"     Conflicts resolved: {len(consensus_result_1['final_consensus'].conflicting_perspectives) == 0}")
       
       # Test scenario 2: Strategic business decision with unanimous requirement
       print("\n  🧪 Scenario 2: Strategic business decision (unanimous consensus)...")
       strategic_context = DecisionContext(
           decision_id="consensus_002",
           decision_type="strategic_digital_transformation",
           complexity_level="very_high",
           domain_focus=["strategic_planning", "organizational_change", "technology_strategy"],
           stakeholder_context={
               "executives": ["ceo", "cto", "cfo"],
               "board": ["board_members"],
               "employees": ["all_staff"]
           },
           technical_details={"transformation_scope": "enterprise_wide", "technology_overhaul": "complete"},
           business_requirements={"impact": "critical", "timeline": "24_months", "investment": "major"},
           constraints={"organizational_change": "significant", "risk_tolerance": "low"},
           success_criteria=["competitive_advantage", "operational_efficiency", "employee_adoption"],
           expert_persona=ExpertPersonaType.SENIOR_PARTNER
       )
       
       consensus_session_2 = consensus_manager.initiate_multi_expert_consensus(
           strategic_context, ConsensusType.UNANIMOUS
       )
       
       consensus_result_2 = consensus_manager.execute_consensus_process(consensus_session_2)
       
       print(f"     Consensus type: {consensus_session_2.consensus_mechanism.value}")
       print(f"     Participating experts: {len(consensus_session_2.participating_experts)}")
       print(f"     Unanimous achieved: {consensus_result_2['final_consensus'].consensus_strength >= 0.9}")
       print(f"     Consensus confidence: {consensus_result_2['final_consensus'].confidence_score:.2f}")
       
       # Test scenario 3: Technical security decision with domain specialist
       print("\n  🧪 Scenario 3: Security compliance decision (domain specialist)...")
       
       security_context = DecisionContext(
           decision_id="consensus_003",
           decision_type="security_compliance_framework",
           complexity_level="high",
           domain_focus=["security", "compliance", "risk_management"],
           stakeholder_context={
               "security_team": ["security_officers"],
               "compliance": ["compliance_officers"],
               "legal": ["legal_team"]
           },
           technical_details={"compliance_requirements": ["gdpr", "sox", "iso27001"]},
           business_requirements={"impact": "high", "timeline": "urgent"},
           constraints={"regulatory_deadline": "strict", "audit_requirements": "comprehensive"},
           success_criteria=["compliance_achievement", "risk_mitigation", "audit_readiness"],
           expert_persona=ExpertPersonaType.SECURITY_SPECIALIST
       )
       
       consensus_session_3 = consensus_manager.initiate_multi_expert_consensus(
           security_context, ConsensusType.DOMAIN_SPECIALIST
       )
       
       consensus_result_3 = consensus_manager.execute_consensus_process(consensus_session_3)
       
       print(f"     Consensus type: {consensus_session_3.consensus_mechanism.value}")
       print(f"     Domain specialist: {consensus_result_3['final_consensus'].consensus_recommendation[:50]}...")
       print(f"     Specialist confidence: {consensus_result_3['final_consensus'].confidence_score:.2f}")
       print(f"     Quality rating: {consensus_result_3['consensus_quality']['quality_rating']}")
       
       # Test analytics
       analytics = consensus_manager.get_consensus_analytics()
       print(f"\n  ✅ Consensus analytics: {analytics['total_consensus_sessions']} sessions completed")
       print(f"     Average quality: {analytics['average_consensus_quality']:.2f}")
       print(f"     Conflict resolution success: {analytics['conflict_resolution_success']:.1%}")
       
       # Validate consensus mechanisms
       mechanisms_tested = [
           consensus_session_1.consensus_mechanism,
           consensus_session_2.consensus_mechanism,
           consensus_session_3.consensus_mechanism
       ]
       
       expected_mechanisms = [
           ConsensusType.WEIGHTED_CONSENSUS,
           ConsensusType.UNANIMOUS,
           ConsensusType.DOMAIN_SPECIALIST
       ]
       
       mechanisms_success = mechanisms_tested == expected_mechanisms
       
       # Validate consensus achievement
       consensus_strengths = [
           consensus_result_1['final_consensus'].consensus_strength,
           consensus_result_2['final_consensus'].consensus_strength,
           consensus_result_3['final_consensus'].consensus_strength
       ]
       
       consensus_success = all(strength > 0.6 for strength in consensus_strengths)
       
       success = mechanisms_success and consensus_success
       
       if success:
           print("\n  🎯 All consensus scenarios demonstrated successfully!")
           print("     ✅ Multi-domain architecture → Weighted consensus")
           print("     ✅ Strategic transformation → Unanimous consensus")
           print("     ✅ Security compliance → Domain specialist consensus")
       else:
           print(f"\n  ❌ Some consensus scenarios failed validation")
           print(f"     Mechanisms: {mechanisms_success}")
           print(f"     Consensus quality: {consensus_success}")
       
       return success

   except Exception as e:
       print(f"  ❌ Multi-expert consensus demonstration failed: {e}")
       import traceback
       traceback.print_exc()
       return False


if __name__ == "__main__":
   print("🚀 Starting Multi-Expert Consensus Mechanisms Demonstration - Story 3.4")
   
   success = demonstrate_multi_expert_consensus()
   if success:
       print("\n✅ Story 3.4: Multi-Expert Consensus Mechanisms - DEMONSTRATED")
   else:
       print("\n❌ Story 3.4: Multi-Expert Consensus Mechanisms - FAILED")
       exit(1)
