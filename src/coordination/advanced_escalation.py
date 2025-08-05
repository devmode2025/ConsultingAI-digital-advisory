"""Advanced Escalation Logic - Story 2.2 Implementation

This module implements sophisticated escalation decision-making that considers
multiple factors including complexity, risk, consensus quality, and business impact.
"""

from typing import Dict, Any, List, Optional, Tuple
from enum import Enum
from datetime import datetime
import logging

try:
    from .escalation_system import EscalationSystem, EscalationTier
except ImportError:
    # Handle direct execution
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from coordination.escalation_system import EscalationSystem, EscalationTier


class ComplexityFactor(Enum):
    """Complexity factors for escalation decisions"""
    TECHNICAL_COMPLEXITY = "technical_complexity"
    STAKEHOLDER_COMPLEXITY = "stakeholder_complexity"
    BUSINESS_IMPACT = "business_impact"
    TIMELINE_PRESSURE = "timeline_pressure"
    INTEGRATION_COMPLEXITY = "integration_complexity"
    REGULATORY_REQUIREMENTS = "regulatory_requirements"


class ExpertiseType(Enum):
    """Types of expertise required for escalation"""
    TECHNICAL_EXPERT = "technical_expert"
    ARCHITECTURE_EXPERT = "architecture_expert"
    BUSINESS_EXPERT = "business_expert"
    COMPLIANCE_EXPERT = "compliance_expert"
    SENIOR_PARTNER = "senior_partner"


class RiskLevel(Enum):
    """Risk level enumeration for escalation decisions"""
    VERY_LOW = "very_low"
    LOW = "low" 
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class AdvancedEscalationEngine(EscalationSystem):
    """Advanced escalation engine with multi-factor decision analysis
    
    This class extends the base EscalationSystem to provide sophisticated
    escalation logic that considers:
    - Multiple complexity factors beyond confidence scores
    - Risk assessment and business impact analysis
    - Consensus quality and agent agreement patterns
    - Required expertise type identification
    - Historical decision patterns and learning
    
    Academic Note: Demonstrates advanced UserProxyAgent decision-making
    for Epic 2 Story 2.2 - sophisticated escalation beyond basic thresholds.
    """
    
    def __init__(self, escalation_config: Optional[Dict[str, float]] = None):
        """Initialize Advanced Escalation Engine"""
        super().__init__(escalation_config)
        
        # Advanced escalation configuration
        self.complexity_weights = {
            ComplexityFactor.TECHNICAL_COMPLEXITY: 0.25,
            ComplexityFactor.STAKEHOLDER_COMPLEXITY: 0.20,
            ComplexityFactor.BUSINESS_IMPACT: 0.30,
            ComplexityFactor.TIMELINE_PRESSURE: 0.10,
            ComplexityFactor.INTEGRATION_COMPLEXITY: 0.10,
            ComplexityFactor.REGULATORY_REQUIREMENTS: 0.05
        }
        
        # Risk impact multipliers
        self.risk_multipliers = {
            RiskLevel.VERY_LOW: 0.9,
            RiskLevel.LOW: 1.0,
            RiskLevel.MEDIUM: 1.1,
            RiskLevel.HIGH: 1.3,
            RiskLevel.CRITICAL: 1.5
        }
        
        # Decision patterns for learning
        self.decision_patterns = {}
        
        self.logger.info("Advanced Escalation Engine initialized")
    
    def evaluate_advanced_escalation(
        self,
        agent_responses: List[Dict[str, Any]],
        decision_context: Dict[str, Any],
        consensus_analysis: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Evaluate escalation using advanced multi-factor analysis
        
        Args:
            agent_responses: List of responses from specialized agents
            decision_context: Context information about the decision
            consensus_analysis: Optional consensus analysis from discussion rounds
            
        Returns:
            Advanced escalation decision with detailed analysis and reasoning
        """
        escalation_id = self._generate_evaluation_id()
        
        self.logger.info(
            "Starting advanced escalation evaluation",
            extra={
                "escalation_id": escalation_id,
                "agents_involved": len(agent_responses),
                "consensus_provided": consensus_analysis is not None,
                "academic_demonstration": "advanced_escalation_logic"
            }
        )
        
        # Step 1: Basic confidence analysis
        confidence_analysis = self._analyze_confidence_patterns(agent_responses)
        
        # Step 2: Multi-factor complexity assessment
        complexity_assessment = self._assess_multi_factor_complexity(decision_context)
        
        # Step 3: Risk analysis and business impact
        risk_analysis = self._analyze_risk_and_impact(decision_context, agent_responses)
        
        # Step 4: Consensus quality evaluation
        consensus_quality = self._evaluate_consensus_quality(
            agent_responses, consensus_analysis
        )
        
        # Step 5: Calculate composite escalation score
        composite_score = self._calculate_composite_escalation_score(
            confidence_analysis, complexity_assessment, risk_analysis, consensus_quality
        )
        
        # Step 6: Determine escalation tier and required expertise
        escalation_decision = self._make_advanced_escalation_decision(
            composite_score, complexity_assessment, risk_analysis, decision_context
        )
        
        # Step 7: Generate sophisticated reasoning
        escalation_reasoning = self._generate_advanced_reasoning(
            escalation_decision, confidence_analysis, complexity_assessment, 
            risk_analysis, consensus_quality
        )
        
        # Compile comprehensive result
        advanced_result = {
            "escalation_id": escalation_id,
            "timestamp": datetime.now().isoformat(),
            "escalation_tier": escalation_decision["tier"],
            "escalation_tier_name": escalation_decision["tier"].name,
            "escalation_needed": escalation_decision["tier"] != EscalationTier.AGENT_ONLY,
            "required_expertise": escalation_decision["expertise"],
            "confidence_analysis": confidence_analysis,
            "complexity_assessment": complexity_assessment,
            "risk_analysis": risk_analysis,
            "consensus_quality": consensus_quality,
            "composite_score": composite_score,
            "escalation_reasoning": escalation_reasoning,
            "escalation_priority": escalation_decision["priority"],
            "estimated_resolution_time": escalation_decision["estimated_time"],
            "recommended_actions": escalation_decision["actions"],
            "decision_context": decision_context,
            "agent_responses": agent_responses
        }
        
        # Store for pattern learning
        self.escalation_history.append(advanced_result)
        self._update_decision_patterns(advanced_result)
        
        self.logger.info(
            "Advanced escalation evaluation completed",
            extra={
                "escalation_result": advanced_result,
                "academic_evaluation": "sophisticated_escalation_analysis"
            }
        )
        
        return advanced_result
    
    def _analyze_confidence_patterns(self, agent_responses: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze confidence patterns from agent responses"""
        if not agent_responses:
            return {"overall_confidence": 0.0, "confidence_variance": 0.0, "agent_agreement": "no_data"}
        
        confidences = [resp.get("confidence", 0.5) for resp in agent_responses]
        overall_confidence = sum(confidences) / len(confidences)
        confidence_variance = self._calculate_variance(confidences)
        
        # Determine agreement level
        if confidence_variance < 0.05:
            agreement = "strong_agreement"
        elif confidence_variance < 0.15:
            agreement = "moderate_agreement"
        else:
            agreement = "low_agreement"
        
        return {
            "overall_confidence": overall_confidence,
            "confidence_variance": confidence_variance,
            "agent_agreement": agreement,
            "individual_confidences": confidences
        }
    
    def _assess_multi_factor_complexity(self, decision_context: Dict[str, Any]) -> Dict[str, Any]:
        """Assess complexity using multiple factors"""
        complexity_scores = {}
        
        # Technical complexity
        tech_complexity = decision_context.get("technical_complexity", "medium")
        complexity_scores[ComplexityFactor.TECHNICAL_COMPLEXITY] = self._map_complexity_to_score(tech_complexity)
        
        # Business impact
        business_impact = decision_context.get("business_impact", "medium")
        complexity_scores[ComplexityFactor.BUSINESS_IMPACT] = self._map_complexity_to_score(business_impact)
        
        # Stakeholder complexity
        stakeholders = decision_context.get("stakeholders", [])
        complexity_scores[ComplexityFactor.STAKEHOLDER_COMPLEXITY] = min(1.0, len(stakeholders) * 0.2)
        
        # Timeline pressure
        timeline = decision_context.get("timeline", "normal")
        timeline_scores = {"urgent": 0.9, "tight": 0.7, "normal": 0.4, "flexible": 0.2}
        complexity_scores[ComplexityFactor.TIMELINE_PRESSURE] = timeline_scores.get(timeline, 0.4)
        
        # Integration complexity
        dependencies = decision_context.get("dependencies", [])
        complexity_scores[ComplexityFactor.INTEGRATION_COMPLEXITY] = min(1.0, len(dependencies) * 0.15)
        
        # Regulatory requirements
        regulatory = decision_context.get("regulatory_requirements", False)
        complexity_scores[ComplexityFactor.REGULATORY_REQUIREMENTS] = 0.8 if regulatory else 0.1
        
        # Calculate weighted score
        weighted_score = sum(
            score * self.complexity_weights[factor]
            for factor, score in complexity_scores.items()
        )
        
        # Determine complexity level
        if weighted_score < 0.3:
            complexity_level = "low"
        elif weighted_score < 0.6:
            complexity_level = "medium"
        else:
            complexity_level = "high"
        
        return {
            "complexity_scores": complexity_scores,
            "weighted_complexity_score": weighted_score,
            "complexity_level": complexity_level,
            "primary_complexity_factors": [
                factor.value for factor, score in complexity_scores.items() if score > 0.6
            ]
        }
    
    def _map_complexity_to_score(self, complexity_str: str) -> float:
        """Map complexity string to numerical score"""
        mapping = {
            "very_low": 0.1, "low": 0.3, "medium": 0.5, 
            "medium_high": 0.7, "high": 0.8, "very_high": 0.9
        }
        return mapping.get(complexity_str, 0.5)
    
    def _categorize_complexity(self, score: float) -> str:
        """Categorize complexity score into levels"""
        if score < 0.3:
            return "low"
        elif score < 0.5:
            return "medium_low"
        elif score < 0.7:
            return "medium"
        elif score < 0.8:
            return "medium_high"
        else:
            return "high"
    
    def _analyze_risk_and_impact(
        self, 
        decision_context: Dict[str, Any], 
        agent_responses: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Analyze risk and business impact factors
        
        Args:
            decision_context: Context information about the decision
            agent_responses: Agent responses for risk analysis
            
        Returns:
            Risk and impact analysis
        """
        # Business impact assessment
        business_impact = decision_context.get("business_impact", "medium")
        financial_impact = decision_context.get("financial_impact", "medium")
        customer_impact = decision_context.get("customer_impact", "medium")
        
        # Technical risk assessment
        technical_risk = self._assess_technical_risk(decision_context, agent_responses)
        
        # Implementation risk
        implementation_risk = self._assess_implementation_risk(decision_context)
        
        # Timeline risk
        timeline_risk = self._assess_timeline_risk(decision_context)
        
        # Overall risk calculation
        risk_factors = [technical_risk, implementation_risk, timeline_risk]
        overall_risk_score = sum(risk_factors) / len(risk_factors)
        overall_risk_level = self._categorize_risk_level(overall_risk_score)
        
        return {
            "business_impact": business_impact,
            "financial_impact": financial_impact,
            "customer_impact": customer_impact,
            "technical_risk": technical_risk,
            "implementation_risk": implementation_risk,
            "timeline_risk": timeline_risk,
            "overall_risk_score": overall_risk_score,
            "overall_risk_level": overall_risk_level,
            "risk_mitigation_required": overall_risk_score > 0.6
        }
    
    def _assess_technical_risk(
        self, 
        context: Dict[str, Any], 
        agent_responses: List[Dict[str, Any]]
    ) -> float:
        """Assess technical risk based on context and agent input"""
        base_risk = 0.3
        
        # Adjust based on technical complexity
        tech_complexity = context.get("technical_complexity", "medium")
        if tech_complexity == "high":
            base_risk += 0.3
        elif tech_complexity == "very_high":
            base_risk += 0.5
        
        # Adjust based on agent disagreement on technical aspects
        tech_agents = [resp for resp in agent_responses if "technical" in resp.get("agent_type", "").lower()]
        if len(tech_agents) > 1:
            tech_confidences = [resp.get("confidence", 0.5) for resp in tech_agents]
            tech_variance = self._calculate_variance(tech_confidences)
            if tech_variance > 0.15:
                base_risk += 0.2
        
        return min(1.0, base_risk)

    def _assess_implementation_risk(self, context: Dict[str, Any]) -> float:
        """Assess implementation risk"""
        base_risk = 0.2
        
        # Dependencies increase risk
        dependencies = context.get("dependencies", [])
        base_risk += len(dependencies) * 0.1
        
        # Regulatory requirements increase risk
        if context.get("regulatory_requirements", False):
            base_risk += 0.3
        
        return min(1.0, base_risk)

    def _assess_timeline_risk(self, context: Dict[str, Any]) -> float:
        """Assess timeline risk"""
        timeline = context.get("timeline", "normal")
        timeline_risks = {
            "urgent": 0.8,
            "tight": 0.6,
            "normal": 0.3,
            "flexible": 0.1
        }
        return timeline_risks.get(timeline, 0.3)

    def _categorize_risk_level(self, risk_score: float) -> RiskLevel:
        """Categorize numerical risk score into risk level"""
        if risk_score < 0.2:
            return RiskLevel.VERY_LOW
        elif risk_score < 0.4:
            return RiskLevel.LOW
        elif risk_score < 0.6:
            return RiskLevel.MEDIUM
        elif risk_score < 0.8:
            return RiskLevel.HIGH
        else:
            return RiskLevel.CRITICAL
    
    def _evaluate_consensus_quality(
        self,
        agent_responses: List[Dict[str, Any]],
        consensus_analysis: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Evaluate quality of consensus among agents
        
        Args:
            agent_responses: List of agent responses
            consensus_analysis: Optional consensus analysis from discussion rounds
            
        Returns:
            Consensus quality evaluation
        """
        if consensus_analysis:
            # Use provided consensus analysis
            consensus_level = consensus_analysis.get("level", "no_consensus")
            consensus_improvement = consensus_analysis.get("consensus_improvement", 0.0)
            
            quality_score = {
                "strong_consensus": 0.9,
                "moderate_consensus": 0.7,
                "no_consensus": 0.4,
                "conflicting": 0.2
            }.get(consensus_level, 0.4)
            
            # Bonus for improvement
            if consensus_improvement > 0:
                quality_score = min(1.0, quality_score + (consensus_improvement * 0.5))
            
        else:
            # Calculate consensus quality from agent responses
            if not agent_responses:
                return {"quality_score": 0.0, "consensus_strength": "no_data"}
            
            # Analyze recommendation similarity
            recommendations = [resp.get("recommendation", "") for resp in agent_responses]
            unique_recommendations = len(set(recommendations))
            
            if unique_recommendations == 1:
                quality_score = 0.9
                consensus_strength = "strong"
            elif unique_recommendations <= len(agent_responses) // 2:
                quality_score = 0.7
                consensus_strength = "moderate"
            else:
                quality_score = 0.3
                consensus_strength = "weak"
            
            consensus_level = consensus_strength + "_consensus"
            consensus_improvement = 0.0
        
        return {
            "quality_score": quality_score,
            "consensus_level": consensus_level,
            "consensus_strength": consensus_strength if not consensus_analysis else consensus_analysis.get("strength", "unknown"),
            "consensus_improvement": consensus_improvement
        }
    
    def _calculate_composite_escalation_score(
        self,
        confidence_analysis: Dict[str, Any],
        complexity_assessment: Dict[str, Any],
        risk_analysis: Dict[str, Any],
        consensus_quality: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Calculate composite escalation score from all factors"""
        # Component weights for composite score
        weights = {
            "confidence": 0.35,
            "complexity": 0.25,
            "risk": 0.25,
            "consensus": 0.15
        }
        
        # Extract component scores
        confidence_score = 1.0 - confidence_analysis["overall_confidence"]  # Invert (lower confidence = higher escalation need)
        complexity_score = complexity_assessment["weighted_complexity_score"]
        risk_score = risk_analysis["overall_risk_score"]
        consensus_score = 1.0 - consensus_quality["quality_score"]  # Invert (poor consensus = higher escalation need)
        
        # Calculate weighted composite score
        composite_score = (
            confidence_score * weights["confidence"] +
            complexity_score * weights["complexity"] +
            risk_score * weights["risk"] +
            consensus_score * weights["consensus"]
        )
        
        return {
            "composite_score": composite_score,
            "component_scores": {
                "confidence_factor": confidence_score,
                "complexity_factor": complexity_score,
                "risk_factor": risk_score,
                "consensus_factor": consensus_score
            },
            "weights_used": weights,
            "primary_escalation_drivers": self._identify_primary_drivers(
                confidence_score, complexity_score, risk_score, consensus_score
            )
        }

    def _identify_primary_drivers(
        self, confidence_score: float, complexity_score: float, 
        risk_score: float, consensus_score: float
    ) -> List[str]:
        """Identify primary drivers for escalation"""
        drivers = []
        threshold = 0.6
        
        if confidence_score > threshold:
            drivers.append("low_confidence")
        if complexity_score > threshold:
            drivers.append("high_complexity")
        if risk_score > threshold:
            drivers.append("high_risk")
        if consensus_score > threshold:
            drivers.append("poor_consensus")
        
        return drivers if drivers else ["moderate_factors"]
    
    def _make_advanced_escalation_decision(
        self,
        composite_score: Dict[str, Any],
        complexity_assessment: Dict[str, Any],
        risk_analysis: Dict[str, Any],
        decision_context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Make advanced escalation decision with tier, expertise, and actions"""
        score = composite_score["composite_score"]
        primary_drivers = composite_score["primary_escalation_drivers"]
        
        # Determine escalation tier based on composite score
        if score < 0.3:
            tier = EscalationTier.AGENT_ONLY
            priority = "low"
        elif score < 0.6:
            tier = EscalationTier.JUNIOR_SPECIALIST
            priority = "medium"
        else:
            tier = EscalationTier.SENIOR_PARTNER
            priority = "high"
        
        # Adjust tier based on risk level
        risk_level = risk_analysis["overall_risk_level"]
        if risk_level in [RiskLevel.HIGH, RiskLevel.CRITICAL] and tier == EscalationTier.AGENT_ONLY:
            tier = EscalationTier.JUNIOR_SPECIALIST
            priority = "medium"
        elif risk_level == RiskLevel.CRITICAL and tier == EscalationTier.JUNIOR_SPECIALIST:
            tier = EscalationTier.SENIOR_PARTNER
            priority = "high"
        
        # Determine required expertise
        required_expertise = self._determine_required_expertise(
            decision_context, complexity_assessment, risk_analysis, tier
        )
        
        # Estimate resolution time
        estimated_time = self._estimate_resolution_time(tier, complexity_assessment, risk_analysis)
        
        # Recommend actions
        recommended_actions = self._recommend_escalation_actions(
            tier, primary_drivers, risk_analysis, complexity_assessment
        )
        
        return {
            "tier": tier,
            "priority": priority,
            "expertise": required_expertise,
            "estimated_time": estimated_time,
            "actions": recommended_actions,
            "escalation_rationale": self._create_escalation_rationale(
                tier, score, primary_drivers, risk_level
            )
        }

    def _determine_required_expertise(
        self,
        context: Dict[str, Any],
        complexity: Dict[str, Any],
        risk: Dict[str, Any],
        tier: EscalationTier
    ) -> List[ExpertiseType]:
        """Determine what types of expertise are required"""
        required_expertise = []
        
        if tier == EscalationTier.AGENT_ONLY:
            return []
        
        # Based on decision type
        decision_type = context.get("type", "general")
        if "technical" in decision_type.lower():
            required_expertise.append(ExpertiseType.TECHNICAL_EXPERT)
        if "architecture" in decision_type.lower():
            required_expertise.append(ExpertiseType.ARCHITECTURE_EXPERT)
        if "business" in decision_type.lower():
            required_expertise.append(ExpertiseType.BUSINESS_EXPERT)
        
        # Based on complexity factors
        primary_factors = complexity.get("primary_complexity_factors", [])
        if "regulatory_requirements" in primary_factors:
            required_expertise.append(ExpertiseType.COMPLIANCE_EXPERT)
        
        # Based on risk level
        if risk["overall_risk_level"] in [RiskLevel.HIGH, RiskLevel.CRITICAL]:
            if ExpertiseType.SENIOR_PARTNER not in required_expertise:
                required_expertise.append(ExpertiseType.SENIOR_PARTNER)
        
        # Senior partner for Tier 3
        if tier == EscalationTier.SENIOR_PARTNER:
            if ExpertiseType.SENIOR_PARTNER not in required_expertise:
                required_expertise.append(ExpertiseType.SENIOR_PARTNER)
        
        return required_expertise if required_expertise else [ExpertiseType.TECHNICAL_EXPERT]

    def _estimate_resolution_time(
        self, tier: EscalationTier, complexity: Dict[str, Any], risk: Dict[str, Any]
    ) -> str:
        """Estimate resolution time based on tier and complexity"""
        base_times = {
            EscalationTier.AGENT_ONLY: "2-4 hours",
            EscalationTier.JUNIOR_SPECIALIST: "1-2 days",
            EscalationTier.SENIOR_PARTNER: "3-5 days"
        }
        
        base_time = base_times.get(tier, "1-2 days")
        
        # Adjust for high complexity or risk
        if complexity["complexity_level"] == "high" or risk["overall_risk_level"] in [RiskLevel.HIGH, RiskLevel.CRITICAL]:
            if tier == EscalationTier.AGENT_ONLY:
                base_time = "4-8 hours"
            elif tier == EscalationTier.JUNIOR_SPECIALIST:
                base_time = "2-3 days"
            else:
                base_time = "5-7 days"
        
        return base_time

    def _recommend_escalation_actions(
        self,
        tier: EscalationTier,
        primary_drivers: List[str],
        risk: Dict[str, Any],
        complexity: Dict[str, Any]
    ) -> List[str]:
        """Recommend specific actions for escalation"""
        actions = []
        
        if tier == EscalationTier.AGENT_ONLY:
            actions.append("Proceed with agent recommendation")
            actions.append("Monitor implementation progress")
        
        elif tier == EscalationTier.JUNIOR_SPECIALIST:
            actions.append("Engage junior specialist for review")
            
            if "poor_consensus" in primary_drivers:
                actions.append("Facilitate consensus building session")
            if "high_complexity" in primary_drivers:
                actions.append("Break down decision into smaller components")
            if "high_risk" in primary_drivers:
                actions.append("Conduct risk mitigation planning")
        
        else:  # SENIOR_PARTNER
            actions.append("Escalate to senior partner for strategic oversight")
            actions.append("Conduct comprehensive stakeholder alignment")
            
            if risk["overall_risk_level"] in [RiskLevel.HIGH, RiskLevel.CRITICAL]:
                actions.append("Implement enhanced risk management protocols")
            if complexity["complexity_level"] in ["medium_high", "high"]:
                actions.append("Establish expert working group")
        
        return actions

    def _create_escalation_rationale(
        self,
        tier: EscalationTier,
        score: float,
        drivers: List[str],
        risk_level: RiskLevel
    ) -> str:
        """Create clear rationale for escalation decision"""
        rationale = f"Composite escalation score: {score:.2f}/1.0. "
        
        if tier == EscalationTier.AGENT_ONLY:
            rationale += "Low complexity and risk enable autonomous agent execution."
        elif tier == EscalationTier.JUNIOR_SPECIALIST:
            rationale += "Moderate complexity or risk requires specialist review. "
            rationale += f"Primary drivers: {', '.join(drivers)}."
        else:
            rationale += "High complexity or risk requires senior strategic oversight. "
            rationale += f"Risk level: {risk_level.value}. Primary drivers: {', '.join(drivers)}."
        
        return rationale
    
    def _generate_advanced_reasoning(
        self,
        escalation_decision: Dict[str, Any],
        confidence: Dict[str, Any],
        complexity: Dict[str, Any],
        risk: Dict[str, Any],
        consensus: Dict[str, Any]
    ) -> str:
        """Generate sophisticated reasoning for escalation decision"""
        tier = escalation_decision["tier"]
        reasoning_parts = []
        
        # Start with tier decision
        reasoning_parts.append(f"Escalation Tier: {tier.name}")
        reasoning_parts.append(escalation_decision["escalation_rationale"])
        
        # Add factor analysis
        reasoning_parts.append(
            f"Confidence Analysis: {confidence['agent_agreement']} "
            f"(avg: {confidence['overall_confidence']:.1%}, variance: {confidence['confidence_variance']:.3f})"
        )
        
        reasoning_parts.append(
            f"Complexity: {complexity['complexity_level']} "
            f"(score: {complexity['weighted_complexity_score']:.2f})"
        )
        
        reasoning_parts.append(
            f"Risk: {risk['overall_risk_level'].value} "
            f"(score: {risk['overall_risk_score']:.2f})"
        )
        
        reasoning_parts.append(
            f"Consensus Quality: {consensus['quality_score']:.2f}"
        )
        
        # Add expertise and timeline
        if escalation_decision["expertise"]:
            expertise_names = [exp.value for exp in escalation_decision["expertise"]]
            reasoning_parts.append(f"Required expertise: {', '.join(expertise_names)}")
        
        reasoning_parts.append(f"Estimated resolution time: {escalation_decision['estimated_time']}")
        
        return " | ".join(reasoning_parts)

    def _update_decision_patterns(self, escalation_result: Dict[str, Any]) -> None:
        """Update decision patterns for learning"""
        decision_type = escalation_result["decision_context"].get("type", "general")
        
        if decision_type not in self.decision_patterns:
            self.decision_patterns[decision_type] = {
                "total_decisions": 0,
                "escalation_distribution": {},
                "average_complexity": 0.0,
                "average_risk": 0.0
            }
        
        pattern = self.decision_patterns[decision_type]
        pattern["total_decisions"] += 1
        
        # Update escalation distribution
        tier_name = escalation_result["escalation_tier_name"]
        pattern["escalation_distribution"][tier_name] = pattern["escalation_distribution"].get(tier_name, 0) + 1
        
        # Update averages
        complexity_score = escalation_result["complexity_assessment"]["weighted_complexity_score"]
        risk_score = escalation_result["risk_analysis"]["overall_risk_score"]
        
        pattern["average_complexity"] = (
            (pattern["average_complexity"] * (pattern["total_decisions"] - 1) + complexity_score) /
            pattern["total_decisions"]
        )
        
        pattern["average_risk"] = (
            (pattern["average_risk"] * (pattern["total_decisions"] - 1) + risk_score) /
            pattern["total_decisions"]
        )

    def get_advanced_escalation_analytics(self) -> Dict[str, Any]:
        """Get comprehensive analytics for advanced escalation patterns"""
        return {
            "total_advanced_escalations": len(self.escalation_history),
            "decision_patterns": self.decision_patterns,
            "escalation_distribution": self._calculate_escalation_distribution(),
            "average_complexity": self._calculate_average_complexity(),
            "average_risk": self._calculate_average_risk()
        }

    def _calculate_escalation_distribution(self) -> Dict[str, int]:
        """Calculate distribution of escalation tiers"""
        distribution = {}
        for result in self.escalation_history:
            tier = result.get("escalation_tier_name", "unknown")
            distribution[tier] = distribution.get(tier, 0) + 1
        return distribution

    def _calculate_average_complexity(self) -> float:
        """Calculate average complexity score"""
        if not self.escalation_history:
            return 0.0
        scores = [r["complexity_assessment"]["weighted_complexity_score"] for r in self.escalation_history]
        return sum(scores) / len(scores)

    def _calculate_average_risk(self) -> float:
        """Calculate average risk score"""
        if not self.escalation_history:
            return 0.0
        scores = [r["risk_analysis"]["overall_risk_score"] for r in self.escalation_history]
        return sum(scores) / len(scores)

    def _generate_evaluation_id(self) -> str:
        """Generate unique evaluation ID"""
        return f"adv_esc_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"

def create_advanced_escalation_engine(**kwargs) -> AdvancedEscalationEngine:
   """Factory function to create Advanced Escalation Engine
   
   Args:
       **kwargs: Configuration parameters for the engine
       
   Returns:
       Configured AdvancedEscalationEngine instance
   """
   return AdvancedEscalationEngine(**kwargs)


def demonstrate_advanced_escalation() -> bool:
    """Demonstrate advanced escalation logic capabilities"""
    try:
        print("  🔧 Demonstrating Advanced Escalation Engine...")
        
        # Initialize advanced escalation engine
        engine = AdvancedEscalationEngine()
        
        # Test scenario 1: High complexity scenario
        print("\n  🧪 Scenario 1: High complexity decision...")
        
        complex_context = {
            "type": "system_architecture_migration",
            "description": "Migrate legacy monolith to microservices",
            "technical_complexity": "very_high",
            "business_impact": "high",
            "stakeholders": ["engineering", "product", "business", "operations"],
            "timeline": "urgent",
            "dependencies": ["database_migration", "api_redesign", "deployment_pipeline"],
            "regulatory_requirements": True,
            "financial_impact": "high",
            "customer_impact": "medium"
        }
        
        complex_responses = [
            {
                "agent": "senior_architect",
                "agent_type": "SystemArchitectAgent",
                "recommendation": "Phased microservices migration with hybrid approach",
                "confidence": 0.65,
                "rationale": "Complex migration requires careful phasing"
            },
            {
                "agent": "lead_developer",
                "agent_type": "CodeReviewerAgent", 
                "recommendation": "Maintain current architecture with incremental improvements",
                "confidence": 0.55,
                "rationale": "High risk of disruption with major changes"
            },
            {
                "agent": "business_director",
                "agent_type": "BusinessAnalystAgent",
                "recommendation": "Cloud-native architecture for competitive advantage",
                "confidence": 0.70,
                "rationale": "Business needs require modern, scalable solution"
            }
        ]
        
        complex_result = engine.evaluate_advanced_escalation(
            complex_responses, complex_context
        )
        
        print(f"     Escalation tier: {complex_result['escalation_tier_name']}")
        print(f"     Composite score: {complex_result['composite_score']['composite_score']:.2f}")
        print(f"     Risk level: {complex_result['risk_analysis']['overall_risk_level'].value}")
        print(f"     Required expertise: {[exp.value for exp in complex_result['required_expertise']]}")
        print(f"     Estimated time: {complex_result['estimated_resolution_time']}")
        
        # Test scenario 2: Medium complexity scenario
        print("\n  🧪 Scenario 2: Medium complexity decision...")
        
        medium_context = {
            "type": "api_enhancement",
            "description": "Add new features to existing API",
            "technical_complexity": "medium",
            "business_impact": "medium",
            "stakeholders": ["engineering", "product"],
            "timeline": "normal",
            "regulatory_requirements": False
        }
        
        medium_responses = [
            {
                "agent": "api_architect",
                "agent_type": "SystemArchitectAgent",
                "recommendation": "RESTful API extension with versioning",
                "confidence": 0.82,
                "rationale": "Standard approach with proven patterns"
            },
            {
                "agent": "backend_developer",
                "agent_type": "CodeReviewerAgent",
                "recommendation": "RESTful API with comprehensive testing",
                "confidence": 0.85,
                "rationale": "Well-established implementation approach"
            },
            {
                "agent": "product_analyst",
                "agent_type": "BusinessAnalystAgent", 
                "recommendation": "API enhancement with user feedback integration",
                "confidence": 0.80,
                "rationale": "Balances technical and business requirements"
            }
        ]
        
        medium_result = engine.evaluate_advanced_escalation(
            medium_responses, medium_context
        )
        
        print(f"     Escalation tier: {medium_result['escalation_tier_name']}")
        print(f"     Composite score: {medium_result['composite_score']['composite_score']:.2f}")
        print(f"     Risk level: {medium_result['risk_analysis']['overall_risk_level'].value}")
        print(f"     Required expertise: {[exp.value for exp in medium_result['required_expertise']]}")
        print(f"     Estimated time: {medium_result['estimated_resolution_time']}")
        
        # Test scenario 3: Low complexity scenario
        print("\n  🧪 Scenario 3: Low complexity decision...")
        
        simple_context = {
            "type": "code_style_update",
            "description": "Update code formatting standards",
            "technical_complexity": "low",
            "business_impact": "low",
            "stakeholders": ["engineering"],
            "timeline": "flexible"
        }
        
        simple_responses = [
            {
                "agent": "code_reviewer",
                "agent_type": "CodeReviewerAgent",
                "recommendation": "Adopt Black formatter with pre-commit hooks",
                "confidence": 0.92,
                "rationale": "Industry standard with excellent tooling"
            },
            {
                "agent": "tech_lead",
                "agent_type": "SystemArchitectAgent",
                "recommendation": "Black formatter for consistency",
                "confidence": 0.90,
                "rationale": "Supports team productivity and code quality"
            },
            {
                "agent": "team_manager",
                "agent_type": "BusinessAnalystAgent",
                "recommendation": "Standardize on Black formatter",
                "confidence": 0.88,
                "rationale": "Reduces code review overhead"
            }
        ]
        
        simple_result = engine.evaluate_advanced_escalation(
            simple_responses, simple_context
        )
        
        print(f"     Escalation tier: {simple_result['escalation_tier_name']}")
        print(f"     Composite score: {simple_result['composite_score']['composite_score']:.2f}")
        print(f"     Risk level: {simple_result['risk_analysis']['overall_risk_level'].value}")
        print(f"     Escalation needed: {simple_result['escalation_needed']}")
        
        # Display analytics
        analytics = engine.get_advanced_escalation_analytics()
        print(f"\n  ✅ Advanced escalation analytics: {analytics['total_advanced_escalations']} decisions analyzed")
        
        # Validate results
        expected_tiers = [
            EscalationTier.SENIOR_PARTNER,  # High complexity/risk
            EscalationTier.JUNIOR_SPECIALIST,  # Medium complexity
            EscalationTier.AGENT_ONLY  # Low complexity/risk
        ]
        
        actual_tiers = [
            complex_result['escalation_tier'],
            medium_result['escalation_tier'], 
            simple_result['escalation_tier']
        ]
        
        success = actual_tiers == expected_tiers
        
        if success:
            print("\n  🎯 All escalation scenarios demonstrated correctly!")
            print("     ✅ High complexity/risk → Senior Partner")
            print("     ✅ Medium complexity → Junior Specialist")
            print("     ✅ Low complexity/risk → Agent Only")
        else:
            print(f"\n  ❌ Escalation results unexpected:")
            for i, (expected, actual) in enumerate(zip(expected_tiers, actual_tiers)):
                status = "✅" if expected == actual else "❌"
                print(f"     {status} Scenario {i+1}: Expected {expected.name}, got {actual.name}")
        
        return success
        
    except Exception as e:
        print(f"  ❌ Advanced escalation demonstration failed: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
   print("🚀 Starting Advanced Escalation Logic Demonstration - Story 2.2")
   
   success = demonstrate_advanced_escalation()
   if success:
       print("\n✅ Story 2.2: Advanced Escalation Logic - DEMONSTRATED")
   else:
       print("\n❌ Story 2.2: Advanced Escalation Logic - FAILED")
       exit(1)
