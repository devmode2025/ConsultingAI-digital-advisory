"""Enhanced Chief Engagement Manager - Story 2.1 Implementation

This module extends the Chief Engagement Manager with sophisticated
multi-agent discussion orchestration and intelligent consensus detection.
"""

import autogen
from typing import Dict, Any, List, Optional, Tuple
import logging
from datetime import datetime
from enum import Enum
import json

# Import base functionality
from .chief_engagement_manager import ChiefEngagementManager
from .escalation_system import EscalationSystem, EscalationTier


class ConsensusLevel(Enum):
    """Enum for agent consensus levels"""
    STRONG_CONSENSUS = "strong_consensus"      # All agents agree
    MODERATE_CONSENSUS = "moderate_consensus"  # Majority agreement
    NO_CONSENSUS = "no_consensus"             # Significant disagreement
    CONFLICTING = "conflicting"               # Opposing recommendations


class DiscussionPhase(Enum):
    """Enum for multi-agent discussion phases"""
    INITIAL_ANALYSIS = "initial_analysis"
    CONSENSUS_BUILDING = "consensus_building"  
    CONFLICT_RESOLUTION = "conflict_resolution"
    FINAL_RECOMMENDATION = "final_recommendation"


class EnhancedChiefEngagementManager(ChiefEngagementManager):
    """Enhanced Chief Engagement Manager with sophisticated coordination capabilities
    
    This class extends the base Chief Engagement Manager to provide:
    - Complex multi-agent discussion orchestration
    - Consensus detection and conflict resolution
    - Context-rich escalation with detailed reasoning
    - Decision history tracking and pattern learning
    
    Academic Note: Demonstrates advanced UserProxyAgent coordination patterns
    for Epic 2 Story 2.1 - sophisticated inner team collaboration.
    """
    
    def __init__(self, **kwargs):
        """Initialize Enhanced Chief Engagement Manager"""
        super().__init__(**kwargs)
        
        # Enhanced coordination capabilities
        self.discussion_history = []
        self.consensus_patterns = {}
        
        # Initialize enhanced escalation system
        self.enhanced_escalation = EscalationSystem()
        
        self.logger.info("Enhanced Chief Engagement Manager initialized")
    
    def orchestrate_multi_agent_discussion(
        self,
        consultation_context: Dict[str, Any],
        participating_agents: List[Dict[str, Any]],
        discussion_rounds: int = 2
    ) -> Dict[str, Any]:
        """Orchestrate complex multi-agent discussion with multiple rounds
        
        Args:
            consultation_context: Context for the consultation discussion
            participating_agents: List of agent information and capabilities
            discussion_rounds: Number of discussion rounds to conduct
            
        Returns:
            Complete discussion result with consensus analysis and recommendations
        """
        discussion_id = self._generate_discussion_id()
        
        self.logger.info(
            "Starting multi-agent discussion orchestration",
            extra={
                "discussion_id": discussion_id,
                "participating_agents": len(participating_agents),
                "discussion_rounds": discussion_rounds,
                "academic_demonstration": "multi_agent_coordination"
            }
        )
        
        # Initialize discussion
        discussion_result = {
            "discussion_id": discussion_id,
            "timestamp": datetime.now().isoformat(),
            "consultation_context": consultation_context,
            "participating_agents": participating_agents,
            "discussion_rounds": [],
            "final_consensus": None,
            "escalation_decision": None,
            "coordination_quality": None
        }
        
        # Conduct discussion rounds
        for round_num in range(1, discussion_rounds + 1):
            round_result = self._conduct_discussion_round(
                round_num, consultation_context, participating_agents, discussion_result
            )
            discussion_result["discussion_rounds"].append(round_result)
        
        # Analyze final consensus
        final_consensus = self._analyze_final_consensus(discussion_result["discussion_rounds"])
        discussion_result["final_consensus"] = final_consensus
        
        # Make escalation decision based on consensus and confidence
        escalation_decision = self._make_enhanced_escalation_decision(
            final_consensus, consultation_context
        )
        discussion_result["escalation_decision"] = escalation_decision
        
        # Evaluate coordination quality
        coordination_quality = self._evaluate_coordination_quality(discussion_result)
        discussion_result["coordination_quality"] = coordination_quality
        
        # Store discussion for learning
        self.discussion_history.append(discussion_result)
        self._update_consensus_patterns(discussion_result)
        
        self.logger.info(
            "Multi-agent discussion completed",
            extra={
                "discussion_result": discussion_result,
                "academic_evaluation": "sophisticated_coordination"
            }
        )
        
        return discussion_result
    
    def _conduct_discussion_round(
        self,
        round_num: int,
        context: Dict[str, Any],
        agents: List[Dict[str, Any]],
        previous_discussion: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Conduct a single round of multi-agent discussion
        
        Args:
            round_num: Current discussion round number
            context: Consultation context
            agents: Participating agents
            previous_discussion: Results from previous rounds
            
        Returns:
            Round result with agent responses and consensus analysis
        """
        round_result = {
            "round_number": round_num,
            "phase": self._determine_discussion_phase(round_num, previous_discussion),
            "agent_responses": [],
            "consensus_level": None,
            "conflicts_identified": [],
            "consensus_building_attempts": []
        }
        
        # Get agent responses for this round
        for agent_info in agents:
            agent_response = self._simulate_agent_response(agent_info, context, round_num, previous_discussion)
            round_result["agent_responses"].append(agent_response)
        
        # Analyze consensus for this round
        consensus_analysis = self._analyze_round_consensus(round_result["agent_responses"])
        round_result["consensus_level"] = consensus_analysis["level"]
        round_result["conflicts_identified"] = consensus_analysis["conflicts"]
        
        # Attempt consensus building if needed
        if consensus_analysis["level"] in [ConsensusLevel.NO_CONSENSUS, ConsensusLevel.CONFLICTING]:
            consensus_building = self._attempt_consensus_building(
                round_result["agent_responses"], context
            )
            round_result["consensus_building_attempts"] = consensus_building
        
        return round_result
    
    def _simulate_agent_response(
        self,
        agent_info: Dict[str, Any],
        context: Dict[str, Any],
        round_num: int,
        previous_discussion: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Simulate agent response based on agent type and context
        
        Args:
            agent_info: Information about the responding agent
            context: Consultation context
            round_num: Current round number
            previous_discussion: Previous discussion results
            
        Returns:
            Simulated agent response with recommendation and confidence
        """
        agent_type = agent_info.get("agent_type", "unknown")
        agent_name = agent_info.get("name", "unknown_agent")
        
        # Simulate responses based on agent specialization and context
        if agent_type == "CodeReviewerAgent":
            return self._simulate_code_reviewer_response(agent_name, context, round_num)
        elif agent_type == "SystemArchitectAgent":
            return self._simulate_architect_response(agent_name, context, round_num)
        elif agent_type == "BusinessAnalystAgent":
            return self._simulate_analyst_response(agent_name, context, round_num)
        else:
            return self._simulate_generic_response(agent_name, context, round_num)
    
    def _simulate_code_reviewer_response(
        self, agent_name: str, context: Dict[str, Any], round_num: int
    ) -> Dict[str, Any]:
        """Simulate Code Reviewer Agent response"""
        scenario_type = context.get("type", "general")
        
        if "code" in scenario_type.lower() or "technical" in scenario_type.lower():
            # High confidence for code-related decisions
            return {
                "agent": agent_name,
                "agent_type": "CodeReviewerAgent",
                "recommendation": "Implement secure coding standards with comprehensive testing",
                "confidence": 0.88 if round_num == 1 else 0.90,
                "rationale": "Technical implementation follows established best practices",
                "focus_areas": ["code_quality", "security", "testing"],
                "round_number": round_num
            }
        else:
            # Lower confidence for non-technical decisions
            return {
                "agent": agent_name,
                "agent_type": "CodeReviewerAgent", 
                "recommendation": "Support technical feasibility of proposed solution",
                "confidence": 0.70 if round_num == 1 else 0.75,
                "rationale": "Limited technical context but no obvious implementation barriers",
                "focus_areas": ["technical_feasibility"],
                "round_number": round_num
            }
    
    def _simulate_architect_response(
        self, agent_name: str, context: Dict[str, Any], round_num: int
    ) -> Dict[str, Any]:
        """Simulate System Architect Agent response"""
        scenario_type = context.get("type", "general")
        complexity = context.get("complexity", "medium")
        
        if "architecture" in scenario_type.lower() or "design" in scenario_type.lower():
            confidence = 0.85 if complexity == "low" else 0.75 if complexity == "medium" else 0.65
            
            return {
                "agent": agent_name,
                "agent_type": "SystemArchitectAgent",
                "recommendation": "Adopt microservices architecture with API-first design",
                "confidence": confidence + (0.05 if round_num > 1 else 0),
                "rationale": f"Architecture approach suitable for {complexity} complexity requirements",
                "focus_areas": ["scalability", "maintainability", "integration"],
                "round_number": round_num
            }
        else:
            return {
                "agent": agent_name,
                "agent_type": "SystemArchitectAgent",
                "recommendation": "Ensure solution aligns with overall system architecture",
                "confidence": 0.72 if round_num == 1 else 0.78,
                "rationale": "Architectural considerations support proposed approach",
                "focus_areas": ["system_integration"],
                "round_number": round_num
            }
    
    def _simulate_analyst_response(
        self, agent_name: str, context: Dict[str, Any], round_num: int
    ) -> Dict[str, Any]:
        """Simulate Business Analyst Agent response"""
        scenario_type = context.get("type", "general")
        business_impact = context.get("business_impact", "medium")
        
        if business_impact == "high":
            return {
                "agent": agent_name,
                "agent_type": "BusinessAnalystAgent",
                "recommendation": "Prioritize stakeholder alignment and business value delivery",
                "confidence": 0.85 if round_num == 1 else 0.88,
                "rationale": "High business impact requires careful stakeholder management",
                "focus_areas": ["stakeholder_management", "business_value", "risk_mitigation"],
                "round_number": round_num
            }
        else:
            return {
                "agent": agent_name,
                "agent_type": "BusinessAnalystAgent",
                "recommendation": "Support balanced approach with measured implementation",
                "confidence": 0.75 if round_num == 1 else 0.78,
                "rationale": "Standard business considerations apply",
                "focus_areas": ["requirements", "process_optimization"],
                "round_number": round_num
            }
    
    def _simulate_generic_response(
        self, agent_name: str, context: Dict[str, Any], round_num: int
    ) -> Dict[str, Any]:
        """Simulate generic agent response"""
        return {
            "agent": agent_name,
            "agent_type": "GenericAgent",
            "recommendation": "Support collaborative decision-making approach",
            "confidence": 0.65 if round_num == 1 else 0.70,
            "rationale": "General support for team consensus",
            "focus_areas": ["collaboration"],
            "round_number": round_num
        }
    
    def _analyze_round_consensus(self, agent_responses: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze consensus level for a discussion round
        
        Args:
            agent_responses: List of agent responses for the round
            
        Returns:
            Consensus analysis with level and identified conflicts
        """
        if not agent_responses:
            return {"level": ConsensusLevel.NO_CONSENSUS, "conflicts": []}
        
        # Analyze confidence levels
        confidences = [response.get("confidence", 0.5) for response in agent_responses]
        avg_confidence = sum(confidences) / len(confidences)
        confidence_variance = self._calculate_variance(confidences)
        
        # Analyze recommendation similarity
        recommendations = [response.get("recommendation", "") for response in agent_responses]
        unique_recommendations = len(set(recommendations))
        
        # Determine consensus level
        if unique_recommendations == 1 and confidence_variance < 0.05:
            consensus_level = ConsensusLevel.STRONG_CONSENSUS
        elif unique_recommendations <= len(agent_responses) // 2 and avg_confidence > 0.75:
            consensus_level = ConsensusLevel.MODERATE_CONSENSUS
        elif confidence_variance > 0.15 or unique_recommendations == len(agent_responses):
            consensus_level = ConsensusLevel.CONFLICTING
        else:
            consensus_level = ConsensusLevel.NO_CONSENSUS
        
        # Identify specific conflicts
        conflicts = []
        if consensus_level in [ConsensusLevel.NO_CONSENSUS, ConsensusLevel.CONFLICTING]:
            for i, response1 in enumerate(agent_responses):
                for j, response2 in enumerate(agent_responses[i+1:], i+1):
                    if response1["recommendation"] != response2["recommendation"]:
                        conflicts.append({
                            "agents": [response1["agent"], response2["agent"]],
                            "conflict_type": "recommendation_disagreement",
                            "details": {
                                "agent1_rec": response1["recommendation"],
                                "agent2_rec": response2["recommendation"],
                                "confidence_diff": abs(response1["confidence"] - response2["confidence"])
                            }
                        })
        
        return {
            "level": consensus_level,
            "avg_confidence": avg_confidence,
            "confidence_variance": confidence_variance,
            "unique_recommendations": unique_recommendations,
            "conflicts": conflicts
        }
    
    def _calculate_variance(self, values: List[float]) -> float:
        """Calculate variance of a list of values"""
        if len(values) < 2:
            return 0.0
        
        mean = sum(values) / len(values)
        variance = sum((x - mean) ** 2 for x in values) / len(values)
        return variance
    
    def _determine_discussion_phase(
        self, round_num: int, previous_discussion: Dict[str, Any]
    ) -> DiscussionPhase:
        """Determine the current phase of discussion"""
        if round_num == 1:
            return DiscussionPhase.INITIAL_ANALYSIS
        
        # Analyze previous rounds to determine phase
        previous_rounds = previous_discussion.get("discussion_rounds", [])
        if previous_rounds:
            last_round = previous_rounds[-1]
            last_consensus = last_round.get("consensus_level")
            
            if last_consensus == ConsensusLevel.STRONG_CONSENSUS:
                return DiscussionPhase.FINAL_RECOMMENDATION
            elif last_consensus in [ConsensusLevel.NO_CONSENSUS, ConsensusLevel.CONFLICTING]:
                return DiscussionPhase.CONFLICT_RESOLUTION
            else:
                return DiscussionPhase.CONSENSUS_BUILDING
        
        return DiscussionPhase.CONSENSUS_BUILDING
    
    def _attempt_consensus_building(
        self, agent_responses: List[Dict[str, Any]], context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Attempt to build consensus when agents disagree
        
        Args:
            agent_responses: Agent responses showing disagreement
            context: Consultation context
            
        Returns:
            List of consensus building attempts and their outcomes
        """
        consensus_attempts = []
        
        # Identify the main areas of disagreement
        recommendations = [resp.get("recommendation", "") for resp in agent_responses]
        unique_recs = list(set(recommendations))
        
        if len(unique_recs) > 1:
            # Attempt to find common ground
            attempt = {
                "strategy": "find_common_elements",
                "disagreement_areas": unique_recs,
                "common_ground": self._find_common_ground(agent_responses),
                "success_probability": self._estimate_consensus_probability(agent_responses)
            }
            consensus_attempts.append(attempt)
            
            # Suggest compromise approach
            compromise = {
                "strategy": "compromise_approach",
                "suggested_compromise": self._suggest_compromise(agent_responses, context),
                "rationale": "Hybrid approach incorporating key elements from each perspective"
            }
            consensus_attempts.append(compromise)
        
        return consensus_attempts
    
    def _find_common_ground(self, agent_responses: List[Dict[str, Any]]) -> List[str]:
        """Identify common elements across agent responses"""
        all_focus_areas = []
        for response in agent_responses:
            focus_areas = response.get("focus_areas", [])
            all_focus_areas.extend(focus_areas)
        
        # Find focus areas mentioned by multiple agents
        from collections import Counter
        focus_counts = Counter(all_focus_areas)
        common_ground = [area for area, count in focus_counts.items() if count > 1]
        
        return common_ground
    
    def _suggest_compromise(
        self, agent_responses: List[Dict[str, Any]], context: Dict[str, Any]
    ) -> str:
        """Suggest a compromise approach based on agent responses"""
        # Simple compromise suggestion based on agent types
        agent_types = [resp.get("agent_type", "") for resp in agent_responses]
        
        if "CodeReviewerAgent" in agent_types and "SystemArchitectAgent" in agent_types:
            return "Implement technically sound solution with strong architectural foundation"
        elif "BusinessAnalystAgent" in agent_types:
            return "Balance technical requirements with business value and stakeholder needs"
        else:
            return "Adopt phased approach incorporating elements from all perspectives"
    
    def _estimate_consensus_probability(self, agent_responses: List[Dict[str, Any]]) -> float:
        """Estimate probability of reaching consensus"""
        confidences = [resp.get("confidence", 0.5) for resp in agent_responses]
        variance = self._calculate_variance(confidences)
        
        # Lower variance suggests higher probability of consensus
        if variance < 0.05:
            return 0.8
        elif variance < 0.10:
            return 0.6
        elif variance < 0.15:
            return 0.4
        else:
            return 0.2
    
    def _analyze_final_consensus(self, discussion_rounds: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze final consensus across all discussion rounds"""
        if not discussion_rounds:
            return {"level": ConsensusLevel.NO_CONSENSUS, "progression": []}
        
        # Track consensus progression
        consensus_progression = []
        for round_result in discussion_rounds:
            consensus_progression.append({
                "round": round_result["round_number"],
                "level": round_result["consensus_level"],
                "avg_confidence": round_result.get("avg_confidence", 0.5)
            })
        
        # Final consensus is from last round
        final_round = discussion_rounds[-1]
        final_level = final_round["consensus_level"]
        
        return {
            "level": final_level,
            "progression": consensus_progression,
            "consensus_improvement": self._calculate_consensus_improvement(consensus_progression),
            "final_confidences": [
                round_result.get("agent_responses", [{}])[-1].get("confidence", 0.5)
                for round_result in discussion_rounds
                if round_result.get("agent_responses")
            ],
            "final_recommendations": [
                round_result.get("agent_responses", [{}])[-1].get("recommendation", "")
                for round_result in discussion_rounds
                if round_result.get("agent_responses")
            ]
        }
    
    def _calculate_consensus_improvement(self, progression: List[Dict[str, Any]]) -> float:
        """Calculate how much consensus improved over discussion rounds"""
        if len(progression) < 2:
            return 0.0
        
        first_confidence = progression[0]["avg_confidence"]
        last_confidence = progression[-1]["avg_confidence"]
        
        return last_confidence - first_confidence
    
    def _make_enhanced_escalation_decision(
        self, consensus: Dict[str, Any], context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Make enhanced escalation decision based on consensus and context"""
        consensus_level = consensus["level"]
        final_confidences = consensus.get("final_confidences", [])
        
        if not final_confidences:
            overall_confidence = 0.5
        else:
            overall_confidence = sum(final_confidences) / len(final_confidences)
        
        # Adjust confidence based on consensus level
        if consensus_level == ConsensusLevel.STRONG_CONSENSUS:
            adjusted_confidence = overall_confidence * 1.1
        elif consensus_level == ConsensusLevel.MODERATE_CONSENSUS:
            adjusted_confidence = overall_confidence * 1.0
        elif consensus_level == ConsensusLevel.NO_CONSENSUS:
            adjusted_confidence = overall_confidence * 0.9
        else:  # CONFLICTING
            adjusted_confidence = overall_confidence * 0.8
        
        # Ensure confidence stays in valid range
        adjusted_confidence = max(0.0, min(1.0, adjusted_confidence))
        
        # Use enhanced escalation system
        mock_agent_responses = [
            {"confidence": conf, "recommendation": rec} 
            for conf, rec in zip(final_confidences, consensus.get("final_recommendations", []))
        ]
        
        escalation_result = self.enhanced_escalation.evaluate_escalation(
            mock_agent_responses, context
        )
        
        # Add consensus information to escalation decision
        escalation_result["consensus_analysis"] = {
            "consensus_level": consensus_level.value,
            "consensus_improvement": consensus.get("consensus_improvement", 0.0),
            "discussion_rounds_needed": len(consensus.get("progression", [])),
            "adjusted_confidence": adjusted_confidence
        }
        
        return escalation_result
    
    def _evaluate_coordination_quality(self, discussion_result: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate the quality of coordination process"""
        rounds = discussion_result.get("discussion_rounds", [])
        consensus = discussion_result.get("final_consensus", {})
        
        quality_metrics = {
            "efficiency": self._calculate_efficiency(rounds),
            "consensus_achievement": self._rate_consensus_achievement(consensus),
            "agent_participation": self._evaluate_agent_participation(rounds),
            "conflict_resolution": self._rate_conflict_resolution(rounds),
            "overall_score": 0.0
        }
        
        # Calculate overall coordination quality score
        overall_score = (
            quality_metrics["efficiency"] * 0.25 +
            quality_metrics["consensus_achievement"] * 0.35 +
            quality_metrics["agent_participation"] * 0.20 +
            quality_metrics["conflict_resolution"] * 0.20
        )
        
        quality_metrics["overall_score"] = overall_score
        
        return quality_metrics
    
    def _calculate_efficiency(self, rounds: List[Dict[str, Any]]) -> float:
        """Calculate coordination efficiency (fewer rounds = higher efficiency)"""
        if not rounds:
            return 0.0
        
        num_rounds = len(rounds)
        if num_rounds == 1:
            return 1.0
        elif num_rounds == 2:
            return 0.8
        elif num_rounds == 3:
            return 0.6
        else:
            return 0.4
    
    def _rate_consensus_achievement(self, consensus: Dict[str, Any]) -> float:
        """Rate how well consensus was achieved"""
        level = consensus.get("level", ConsensusLevel.NO_CONSENSUS)
        improvement = consensus.get("consensus_improvement", 0.0)
        
        base_score = {
            ConsensusLevel.STRONG_CONSENSUS: 1.0,
            ConsensusLevel.MODERATE_CONSENSUS: 0.8,
            ConsensusLevel.NO_CONSENSUS: 0.4,
            ConsensusLevel.CONFLICTING: 0.2
        }.get(level, 0.3)
        
        # Bonus for improvement over rounds
        improvement_bonus = min(0.2, improvement * 2)
        
        return min(1.0, base_score + improvement_bonus)
    
    def _evaluate_agent_participation(self, rounds: List[Dict[str, Any]]) -> float:
        """Evaluate quality of agent participation"""
        if not rounds:
            return 0.0
        
        total_responses = 0
        total_rounds = len(rounds)
        
        for round_result in rounds:
            total_responses += len(round_result.get("agent_responses", []))
        
        expected_responses = total_rounds * 3  # Assuming 3 agents typically
        participation_rate = total_responses / expected_responses if expected_responses > 0 else 0
        
        return min(1.0, participation_rate)
    
    def _rate_conflict_resolution(self, rounds: List[Dict[str, Any]]) -> float:
        """Rate how well conflicts were resolved"""
        if not rounds:
            return 0.0
        
        conflicts_identified = 0
        conflicts_resolved = 0
        
        for round_result in rounds:
            round_conflicts = len(round_result.get("conflicts_identified", []))
            conflicts_identified += round_conflicts
            
            # Check if consensus building attempts were made
            if round_conflicts > 0 and round_result.get("consensus_building_attempts"):
                conflicts_resolved += round_conflicts * 0.7  # Assume 70% resolution rate
        
        if conflicts_identified == 0:
            return 1.0  # No conflicts to resolve
        
        resolution_rate = conflicts_resolved / conflicts_identified
        return min(1.0, resolution_rate)
    
    def _update_consensus_patterns(self, discussion_result: Dict[str, Any]) -> None:
        """Update learned consensus patterns based on discussion results"""
        consensus = discussion_result.get("final_consensus", {})
        context = discussion_result.get("consultation_context", {})
        
        pattern_key = context.get("type", "general")
        
        if pattern_key not in self.consensus_patterns:
            self.consensus_patterns[pattern_key] = {
                "total_discussions": 0,
                "consensus_levels": [],
                "average_rounds": 0.0,
                "success_rate": 0.0
            }
        
        pattern = self.consensus_patterns[pattern_key]
        pattern["total_discussions"] += 1
        pattern["consensus_levels"].append(consensus.get("level", ConsensusLevel.NO_CONSENSUS))
        
        rounds_needed = len(discussion_result.get("discussion_rounds", []))
        pattern["average_rounds"] = (
            (pattern["average_rounds"] * (pattern["total_discussions"] - 1) + rounds_needed) /
            pattern["total_discussions"]
        )
        
        # Calculate success rate (strong or moderate consensus)
        successful_consensus = [
            level for level in pattern["consensus_levels"]
            if level in [ConsensusLevel.STRONG_CONSENSUS, ConsensusLevel.MODERATE_CONSENSUS]
        ]
        pattern["success_rate"] = len(successful_consensus) / len(pattern["consensus_levels"])
    
    def _generate_discussion_id(self) -> str:
        """Generate unique discussion ID"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        return f"discussion_{timestamp}"
    
    def get_coordination_analytics(self) -> Dict[str, Any]:
        """Get comprehensive coordination analytics for academic evaluation"""
        return {
            "total_discussions": len(self.discussion_history),
            "consensus_patterns": self.consensus_patterns,
            "average_coordination_quality": self._calculate_average_coordination_quality(),
            "escalation_statistics": self.enhanced_escalation.get_escalation_statistics(),
            "discussion_history": self.discussion_history[-5:]  # Last 5 for brevity
        }
    
    def _calculate_average_coordination_quality(self) -> float:
        """Calculate average coordination quality across all discussions"""
        if not self.discussion_history:
            return 0.0
        
        quality_scores = [
            discussion.get("coordination_quality", {}).get("overall_score", 0.0)
            for discussion in self.discussion_history
        ]
        
        return sum(quality_scores) / len(quality_scores)


def create_enhanced_chief_engagement_manager(**kwargs) -> EnhancedChiefEngagementManager:
    """Factory function to create Enhanced Chief Engagement Manager
    
    Args:
        **kwargs: Configuration parameters for the manager
        
    Returns:
        Configured EnhancedChiefEngagementManager instance
    """
    return EnhancedChiefEngagementManager(**kwargs)


def demonstrate_enhanced_coordination() -> bool:
    """Demonstrate enhanced coordination capabilities for Story 2.1
    
    Returns:
        True if demonstration successful, False otherwise
    """
    print("🔧 Demonstrating Enhanced Chief Engagement Manager Coordination...")
    
    try:
        # Create enhanced manager
        manager = create_enhanced_chief_engagement_manager(
            name="enhanced_demo_manager",
            human_input_mode="NEVER"
        )
        
        print("  ✅ Enhanced Chief Engagement Manager created")
        
        # Set up complex consultation scenario
        consultation_context = {
            "scenario_name": "complex_api_architecture_decision",
            "description": "Design API architecture for multi-tenant SaaS platform",
            "type": "complex_architecture_decision",
            "complexity": "high",
            "business_impact": "high",
            "stakeholders": ["engineering", "product", "customers", "operations"],
            "timeline": "urgent"
        }
        
        # Define participating agents
        participating_agents = [
            {
                "name": "senior_code_reviewer",
                "agent_type": "CodeReviewerAgent",
                "expertise": ["security", "performance", "code_quality"],
                "seniority": "senior"
            },
            {
                "name": "lead_system_architect", 
                "agent_type": "SystemArchitectAgent",
                "expertise": ["scalability", "distributed_systems", "api_design"],
                "seniority": "lead"
            },
            {
                "name": "principal_business_analyst",
                "agent_type": "BusinessAnalystAgent", 
                "expertise": ["stakeholder_management", "requirements", "roi_analysis"],
                "seniority": "principal"
            }
        ]
       
        print(f"  📋 Consultation: {consultation_context['description']}")
        print(f"     Participating agents: {len(participating_agents)}")
        
        # Orchestrate multi-agent discussion
        discussion_result = manager.orchestrate_multi_agent_discussion(
            consultation_context,
            participating_agents,
            discussion_rounds=2
        )
        
        print(f"  ✅ Multi-agent discussion completed: {discussion_result['discussion_id']}")
        
        # Display discussion results
        final_consensus = discussion_result["final_consensus"]
        escalation_decision = discussion_result["escalation_decision"]
        coordination_quality = discussion_result["coordination_quality"]
        
        print(f"     Discussion rounds: {len(discussion_result['discussion_rounds'])}")
        print(f"     Final consensus: {final_consensus['level'].value}")
        print(f"     Consensus improvement: {final_consensus.get('consensus_improvement', 0.0):.2f}")
        print(f"     Escalation tier: {escalation_decision['escalation_tier'].name}")
        print(f"     Escalation needed: {escalation_decision['escalation_needed']}")
        print(f"     Coordination quality: {coordination_quality['overall_score']:.2f}")
        
        # Test coordination analytics
        analytics = manager.get_coordination_analytics()
        print(f"  ✅ Coordination analytics: {analytics['total_discussions']} discussions tracked")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Enhanced coordination demonstration failed: {e}")
        return False


if __name__ == "__main__":
    print("🚀 Starting Enhanced Coordination Demonstration - Story 2.1")
    
    success = demonstrate_enhanced_coordination()
    if success:
        print("\n✅ Story 2.1: Chief Engagement Manager Coordination - DEMONSTRATED")
    else:
        print("\n❌ Story 2.1: Enhanced Coordination - FAILED")
        exit(1)
