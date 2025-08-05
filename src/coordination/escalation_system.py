"""Escalation System for ConsultingAI

This module implements the core escalation detection and routing logic
for the three-tier escalation system in ConsultingAI.
"""

from typing import Dict, Any, List, Optional
from enum import Enum
import logging
from datetime import datetime


class EscalationTier(Enum):
    """Escalation tier enumeration for type safety"""
    AGENT_ONLY = 1      # Tier 1: >90% confidence
    JUNIOR_SPECIALIST = 2  # Tier 2: 70-90% confidence  
    SENIOR_PARTNER = 3     # Tier 3: <70% confidence


class EscalationSystem:
    """Core escalation detection and routing system
    
    This class implements the three-tier escalation logic that determines
    when and how to route decisions to human experts based on confidence
    levels, complexity analysis, and consultation context.
    """
    
    def __init__(self, escalation_config: Optional[Dict[str, float]] = None):
        """Initialize escalation system
        
        Args:
            escalation_config: Configuration for escalation thresholds
        """
        # Default escalation thresholds for academic demonstration
        self.config = escalation_config or {
            "tier_1_threshold": 0.90,  # Agent-only execution
            "tier_2_threshold": 0.70,  # Junior specialist review
            "tier_3_threshold": 0.50   # Senior partner oversight
        }
        
        self.escalation_history: List[Dict[str, Any]] = []
        self.logger = logging.getLogger("ConsultingAI.EscalationSystem")
        
        self.logger.info(
            "Escalation system initialized",
            extra={
                "escalation_config": self.config,
                "academic_context": "Epic 1 Story 1.2 - Escalation Logic"
            }
        )
    
    def evaluate_escalation(
        self, 
        agent_responses: List[Dict[str, Any]], 
        decision_context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Evaluate escalation requirements for a consultation decision
        
        Args:
            agent_responses: List of responses from specialized agents
            decision_context: Context information about the decision
            
        Returns:
            Complete escalation evaluation with tier, reasoning, and metadata
        """
        # Extract confidence scores from agent responses
        confidence_scores = self._extract_confidence_scores(agent_responses)
        
        # Calculate overall confidence metric
        overall_confidence = self._calculate_overall_confidence(confidence_scores, agent_responses)
        
        # Determine escalation tier
        escalation_tier = self._determine_escalation_tier(overall_confidence)
        
        # Analyze decision complexity factors
        complexity_factors = self._analyze_complexity(decision_context, agent_responses)
        
        # Generate escalation reasoning
        reasoning = self._generate_escalation_reasoning(
            escalation_tier, overall_confidence, complexity_factors, agent_responses
        )
        
        # Create escalation evaluation result
        escalation_result = {
            "escalation_tier": escalation_tier,
            "escalation_tier_name": escalation_tier.name,
            "escalation_needed": escalation_tier != EscalationTier.AGENT_ONLY,
            "overall_confidence": overall_confidence,
            "individual_confidences": confidence_scores,
            "complexity_factors": complexity_factors,
            "reasoning": reasoning,
            "required_expertise": self._determine_required_expertise(escalation_tier, decision_context),
            "decision_context": decision_context,
            "agent_responses": agent_responses,
            "timestamp": datetime.now().isoformat(),
            "evaluation_id": self._generate_evaluation_id()
        }
        
        # Log escalation evaluation for academic assessment
        self.logger.info(
            "Escalation evaluation completed",
            extra={
                "escalation_result": escalation_result,
                "academic_demonstration": "escalation_detection_logic"
            }
        )
        
        # Store in escalation history
        self.escalation_history.append(escalation_result)
        
        return escalation_result
    
    def _extract_confidence_scores(self, agent_responses: List[Dict[str, Any]]) -> List[float]:
        """Extract confidence scores from agent responses
        
        Args:
            agent_responses: List of agent response dictionaries
            
        Returns:
            List of confidence scores (0.0 to 1.0)
        """
        confidence_scores = []
        
        for response in agent_responses:
            if "confidence" in response:
                confidence = response["confidence"]
                # Ensure confidence is in valid range
                confidence = max(0.0, min(1.0, float(confidence)))
                confidence_scores.append(confidence)
            else:
                # Default confidence for responses without explicit confidence
                confidence_scores.append(0.5)
        
        return confidence_scores
    
    def _calculate_overall_confidence(
        self, 
        confidence_scores: List[float], 
        agent_responses: List[Dict[str, Any]]
    ) -> float:
        """Calculate overall confidence from individual agent confidences
        
        Args:
            confidence_scores: List of individual confidence scores
            agent_responses: Original agent responses for context
            
        Returns:
            Overall confidence score (0.0 to 1.0)
        """
        if not confidence_scores:
            return 0.5  # Default medium confidence
        
        # For Story 1.2, use simple average (can be enhanced in later stories)
        overall_confidence = sum(confidence_scores) / len(confidence_scores)
        
        # Apply consensus penalty if agents disagree significantly
        if len(confidence_scores) > 1:
            confidence_variance = self._calculate_variance(confidence_scores)
            if confidence_variance > 0.1:  # High disagreement threshold
                # Reduce overall confidence when agents disagree
                overall_confidence *= 0.85
        
        return max(0.0, min(1.0, overall_confidence))
    
    def _calculate_variance(self, scores: List[float]) -> float:
        """Calculate variance of confidence scores
        
        Args:
            scores: List of confidence scores
            
        Returns:
            Variance of the scores
        """
        if len(scores) < 2:
            return 0.0
        
        mean = sum(scores) / len(scores)
        variance = sum((score - mean) ** 2 for score in scores) / len(scores)
        return variance
    
    def _determine_escalation_tier(self, overall_confidence: float) -> EscalationTier:
        """Determine escalation tier based on overall confidence
        
        Args:
            overall_confidence: Calculated overall confidence score
            
        Returns:
            Appropriate escalation tier
        """
        if overall_confidence >= self.config["tier_1_threshold"]:
            return EscalationTier.AGENT_ONLY
        elif overall_confidence >= self.config["tier_2_threshold"]:
            return EscalationTier.JUNIOR_SPECIALIST
        else:
            return EscalationTier.SENIOR_PARTNER
    
    def _analyze_complexity(
        self, 
        decision_context: Dict[str, Any], 
        agent_responses: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Analyze decision complexity factors
        
        Args:
            decision_context: Context information about the decision
            agent_responses: Agent responses for complexity analysis
            
        Returns:
            Dictionary of complexity factors and their assessments
        """
        complexity_factors = {
            "stakeholder_count": len(decision_context.get("stakeholders", [])),
            "decision_scope": decision_context.get("scope", "unknown"),
            "business_impact": decision_context.get("business_impact", "medium"),
            "technical_complexity": decision_context.get("technical_complexity", "medium"),
            "agent_disagreement": len(set(
                response.get("recommendation", "") for response in agent_responses
            )) > 1,
            "time_sensitivity": decision_context.get("time_sensitivity", "normal")
        }
        
        return complexity_factors
    
    def _generate_escalation_reasoning(
        self, 
        tier: EscalationTier, 
        confidence: float, 
        complexity_factors: Dict[str, Any], 
        agent_responses: List[Dict[str, Any]]
    ) -> str:
        """Generate human-readable reasoning for escalation decision
        
        Args:
            tier: Determined escalation tier
            confidence: Overall confidence score
            complexity_factors: Analyzed complexity factors
            agent_responses: Agent responses for context
            
        Returns:
            Human-readable escalation reasoning
        """
        if tier == EscalationTier.AGENT_ONLY:
            reasoning = f"High confidence ({confidence:.1%}) enables agent-only execution. "
            reasoning += "Specialized agents provided consistent, high-quality recommendations "
            reasoning += "with sufficient certainty for autonomous implementation."
        
        elif tier == EscalationTier.JUNIOR_SPECIALIST:
            reasoning = f"Medium confidence ({confidence:.1%}) requires junior specialist review. "
            
            if complexity_factors.get("agent_disagreement"):
                reasoning += "Agents provided conflicting recommendations requiring human validation. "
            
            reasoning += "Human expertise needed to validate approach and ensure optimal decision quality."
        
        else:  # SENIOR_PARTNER
            reasoning = f"Low confidence ({confidence:.1%}) requires senior partner strategic oversight. "
            
            if complexity_factors.get("business_impact") == "high":
                reasoning += "High business impact requires senior strategic judgment. "
            
            if complexity_factors.get("technical_complexity") == "high":
                reasoning += "Complex technical decision requires experienced oversight. "
            
            reasoning += "Senior expertise essential for strategic decision-making and risk management."
        
        return reasoning
    
    def _determine_required_expertise(
        self, 
        tier: EscalationTier, 
        decision_context: Dict[str, Any]
    ) -> Optional[str]:
        """Determine what type of human expertise is required
        
        Args:
            tier: Escalation tier requiring human intervention
            decision_context: Context about the decision being made
            
        Returns:
            Required expertise type or None for agent-only decisions
        """
        if tier == EscalationTier.AGENT_ONLY:
            return None
        
        # Determine expertise based on decision context
        decision_type = decision_context.get("type", "general")
        
        if "technical" in decision_type.lower() or "code" in decision_type.lower():
            return "python_guru" if tier == EscalationTier.JUNIOR_SPECIALIST else "senior_technical_expert"
        elif "architecture" in decision_type.lower() or "design" in decision_type.lower():
            return "system_architect_expert"
        elif "business" in decision_type.lower() or "requirement" in decision_type.lower():
            return "business_analyst_expert"
        else:
            # Default expertise assignment based on tier
            if tier == EscalationTier.JUNIOR_SPECIALIST:
                return "junior_specialist"
            else:
                return "senior_partner"
   
    def _generate_evaluation_id(self) -> str:
        """Generate unique evaluation ID for tracking
        
        Returns:
            Unique evaluation identifier
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        return f"escalation_{timestamp}"
   
    def get_escalation_statistics(self) -> Dict[str, Any]:
        """Get escalation statistics for academic evaluation
       
        Returns:
            Statistics about escalation patterns and performance
        """
        if not self.escalation_history:
            return {
                "total_evaluations": 0,
                "tier_distribution": {},
                "average_confidence": 0.0,
                "escalation_rate": 0.0
            }
       
        # Calculate tier distribution
        tier_counts = {}
        total_confidence = 0.0
        escalated_count = 0
       
        for evaluation in self.escalation_history:
            tier_name = evaluation["escalation_tier_name"]
            tier_counts[tier_name] = tier_counts.get(tier_name, 0) + 1
            total_confidence += evaluation["overall_confidence"]
           
            if evaluation["escalation_needed"]:
                escalated_count += 1
       
        statistics = {
            "total_evaluations": len(self.escalation_history),
            "tier_distribution": tier_counts,
            "average_confidence": total_confidence / len(self.escalation_history),
            "escalation_rate": escalated_count / len(self.escalation_history),
            "escalation_config": self.config,
            "evaluation_history": self.escalation_history
        }
       
        return statistics


def demonstrate_escalation_system() -> bool:
   """Demonstrate escalation system functionality for academic evaluation
   
   Returns:
       True if demonstration successful, False otherwise
   """
   print("🔧 Demonstrating Escalation System functionality...")
   
   try:
       # Create escalation system
       escalation_system = EscalationSystem()
       print("  ✅ Escalation system created")
       
       # Test Tier 1 (Agent-only) scenario
       print("  🧪 Testing Tier 1 (Agent-only) scenario...")
       tier1_responses = [
           {"agent": "code_reviewer", "recommendation": "Use black formatter", "confidence": 0.95},
           {"agent": "system_architect", "recommendation": "Use black formatter", "confidence": 0.92},
           {"agent": "business_analyst", "recommendation": "Use black formatter", "confidence": 0.90}
       ]
       tier1_context = {"type": "code_formatting", "scope": "minor", "business_impact": "low"}
       
       tier1_result = escalation_system.evaluate_escalation(tier1_responses, tier1_context)
       assert tier1_result["escalation_tier"] == EscalationTier.AGENT_ONLY
       print(f"    ✅ Tier 1 result: {tier1_result['escalation_tier_name']} ({tier1_result['overall_confidence']:.1%} confidence)")
       
       # Test Tier 2 (Junior specialist) scenario
       print("  🧪 Testing Tier 2 (Junior specialist) scenario...")
       tier2_responses = [
           {"agent": "code_reviewer", "recommendation": "REST API", "confidence": 0.80},
           {"agent": "system_architect", "recommendation": "GraphQL", "confidence": 0.75},
           {"agent": "business_analyst", "recommendation": "REST API", "confidence": 0.78}
       ]
       tier2_context = {"type": "api_design", "scope": "medium", "business_impact": "medium"}
       
       tier2_result = escalation_system.evaluate_escalation(tier2_responses, tier2_context)
       assert tier2_result["escalation_tier"] == EscalationTier.JUNIOR_SPECIALIST
       print(f"    ✅ Tier 2 result: {tier2_result['escalation_tier_name']} ({tier2_result['overall_confidence']:.1%} confidence)")
       
       # Test Tier 3 (Senior partner) scenario
       print("  🧪 Testing Tier 3 (Senior partner) scenario...")
       tier3_responses = [
           {"agent": "code_reviewer", "recommendation": "Microservices", "confidence": 0.60},
           {"agent": "system_architect", "recommendation": "Monolith", "confidence": 0.55},
           {"agent": "business_analyst", "recommendation": "Hybrid approach", "confidence": 0.50}
       ]
       tier3_context = {"type": "architecture_pattern", "scope": "major", "business_impact": "high"}
       
       tier3_result = escalation_system.evaluate_escalation(tier3_responses, tier3_context)
       assert tier3_result["escalation_tier"] == EscalationTier.SENIOR_PARTNER
       print(f"    ✅ Tier 3 result: {tier3_result['escalation_tier_name']} ({tier3_result['overall_confidence']:.1%} confidence)")
       
       # Test escalation statistics
       statistics = escalation_system.get_escalation_statistics()
       print(f"  ✅ Escalation statistics: {statistics['total_evaluations']} evaluations, {statistics['escalation_rate']:.1%} escalation rate")
       
       return True
       
   except Exception as e:
       print(f"  ❌ Escalation system demonstration failed: {e}")
       return False


if __name__ == "__main__":
   success = demonstrate_escalation_system()
   if success:
       print("\n✅ Escalation System: DEMONSTRATED")
   else:
       print("\n❌ Escalation System: FAILED")
       exit(1)
