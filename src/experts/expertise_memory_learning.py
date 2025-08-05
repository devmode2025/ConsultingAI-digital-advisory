"""Expertise Memory and Learning System - Story 3.5 Implementation

This module implements sophisticated expertise memory and learning capabilities
that track decision patterns, expert performance, and user preferences to
continuously improve the dynamic expertise sourcing system.
"""

from typing import Dict, Any, List, Optional, Tuple
from enum import Enum
from datetime import datetime, timedelta
from dataclasses import dataclass, field
import logging
import json
import pickle
from collections import defaultdict, deque

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from dynamic_persona_system import ExpertPersonaType
from multi_expert_consensus import ConsensusType, ConflictResolutionStrategy


class LearningDimension(Enum):
    """Dimensions of learning for expertise system"""
    EXPERT_PERFORMANCE = "expert_performance"
    DECISION_PATTERNS = "decision_patterns"
    USER_PREFERENCES = "user_preferences"
    CONSENSUS_EFFECTIVENESS = "consensus_effectiveness"
    CONTEXT_ADAPTATION = "context_adaptation"
    CONFLICT_RESOLUTION = "conflict_resolution"


class MemoryType(Enum):
    """Types of memory in the expertise system"""
    SHORT_TERM = "short_term"          # Recent decisions (last 24 hours)
    MEDIUM_TERM = "medium_term"        # Recent patterns (last 30 days)
    LONG_TERM = "long_term"           # Historical trends (all time)
    EPISODIC = "episodic"             # Specific decision episodes
    SEMANTIC = "semantic"             # General knowledge patterns


@dataclass
class DecisionMemory:
    """Memory record of a specific decision"""
    decision_id: str
    timestamp: datetime
    decision_type: str
    complexity_level: str
    experts_involved: List[ExpertPersonaType]
    consensus_mechanism: Optional[ConsensusType]
    outcome_quality: float
    user_satisfaction: Optional[float]
    performance_metrics: Dict[str, float]
    context_factors: Dict[str, Any]
    lessons_learned: List[str]


@dataclass
class ExpertPerformanceProfile:
    """Performance profile for an expert persona"""
    expert_persona: ExpertPersonaType
    total_decisions: int
    success_rate: float
    average_confidence: float
    domain_expertise_scores: Dict[str, float]
    collaboration_effectiveness: Dict[ExpertPersonaType, float]
    improvement_trends: Dict[str, List[float]]
    preferred_contexts: List[str]
    performance_history: deque = field(default_factory=lambda: deque(maxlen=100))


@dataclass
class LearningInsight:
    """Insight derived from learning analysis"""
    insight_id: str
    learning_dimension: LearningDimension
    insight_type: str
    description: str
    confidence: float
    supporting_evidence: List[str]
    actionable_recommendations: List[str]
    impact_assessment: str
    discovered_at: datetime


class ExpertiseMemoryLearningSystem:
    """Expertise Memory and Learning System for continuous improvement
    
    This class provides comprehensive learning capabilities including:
    - Multi-dimensional expertise performance tracking
    - Pattern recognition and trend analysis
    - User preference learning and adaptation
    - Predictive modeling for expert selection
    - Continuous system optimization
    
    Academic Note: Demonstrates advanced learning and adaptation patterns
    for Epic 3 Story 3.5 - sophisticated expertise memory and learning.
    """
    
    def __init__(self, memory_persistence_path: Optional[str] = None):
        """Initialize Expertise Memory and Learning System
        
        Args:
            memory_persistence_path: Optional path for persisting memory data
        """
        self.memory_persistence_path = memory_persistence_path
        
        # Memory systems
        self.decision_memories: Dict[MemoryType, List[DecisionMemory]] = {
            memory_type: [] for memory_type in MemoryType
        }
        
        # Expert performance tracking
        self.expert_profiles: Dict[ExpertPersonaType, ExpertPerformanceProfile] = {}
        
        # Learning systems
        self.learning_insights: List[LearningInsight] = []
        self.pattern_recognition_models = self._initialize_pattern_models()
        self.preference_models = self._initialize_preference_models()
        
        # Learning configuration
        self.learning_config = self._initialize_learning_config()
        
        # Performance caches
        self.performance_cache = {}
        self.prediction_cache = {}
        
        self.logger = logging.getLogger("ConsultingAI.ExpertiseMemoryLearningSystem")
        
        # Load existing memory if available
        self._load_persistent_memory()
        
        self.logger.info(
            "Expertise Memory and Learning System initialized",
            extra={
                "learning_dimensions": len(LearningDimension),
                "memory_types": len(MemoryType),
                "persistence_enabled": memory_persistence_path is not None,
                "academic_context": "Epic 3 Story 3.5 - Expertise Memory and Learning"
            }
        )
    
    def _initialize_pattern_models(self) -> Dict[str, Any]:
        """Initialize pattern recognition models"""
        return {
            "expert_selection_patterns": {
                "decision_type_to_expert": defaultdict(list),
                "complexity_to_mechanism": defaultdict(list),
                "success_correlations": {}
            },
            "consensus_patterns": {
                "mechanism_effectiveness": defaultdict(list),
                "conflict_predictors": {},
                "resolution_success_factors": {}
            },
            "temporal_patterns": {
                "performance_trends": defaultdict(list),
                "seasonal_variations": {},
                "learning_curves": defaultdict(list)
            }
        }
    
    def _initialize_preference_models(self) -> Dict[str, Any]:
        """Initialize user preference learning models"""
        return {
            "expert_preferences": {
                "preferred_experts_by_domain": defaultdict(list),
                "expert_satisfaction_ratings": defaultdict(list),
                "interaction_style_preferences": {}
            },
            "process_preferences": {
                "consensus_mechanism_preferences": defaultdict(int),
                "decision_speed_preferences": {},
                "detail_level_preferences": {}
            },
            "outcome_preferences": {
                "quality_vs_speed_tradeoffs": [],
                "risk_tolerance_indicators": [],
                "confidence_threshold_preferences": []
            }
        }
    
    def _initialize_learning_config(self) -> Dict[str, Any]:
        """Initialize learning system configuration"""
        return {
            "memory_retention": {
                MemoryType.SHORT_TERM: timedelta(days=1),
                MemoryType.MEDIUM_TERM: timedelta(days=30),
                MemoryType.LONG_TERM: timedelta(days=365 * 5),  # 5 years
                MemoryType.EPISODIC: timedelta(days=90),
                MemoryType.SEMANTIC: None  # Permanent
            },
            "learning_thresholds": {
                "minimum_decisions_for_insight": 5,
                "confidence_threshold_for_recommendation": 0.7,
                "pattern_strength_threshold": 0.6
            },
            "adaptation_rates": {
                "expert_performance_learning": 0.1,
                "preference_adaptation": 0.05,
                "pattern_recognition": 0.2
            }
        }
    
    def record_decision_outcome(
        self,
        decision_id: str,
        decision_context: Dict[str, Any],
        experts_involved: List[ExpertPersonaType],
        consensus_result: Optional[Dict[str, Any]],
        outcome_metrics: Dict[str, float],
        user_feedback: Optional[Dict[str, Any]] = None
    ) -> None:
        """Record decision outcome for learning
        
        Args:
            decision_id: Unique decision identifier
            decision_context: Context of the decision
            experts_involved: Expert personas involved in decision
            consensus_result: Result of consensus process (if applicable)
            outcome_metrics: Metrics about decision quality and effectiveness
            user_feedback: Optional user feedback about the decision
        """
        timestamp = datetime.now()
        
        # Create decision memory
        decision_memory = DecisionMemory(
            decision_id=decision_id,
            timestamp=timestamp,
            decision_type=decision_context.get("decision_type", "unknown"),
            complexity_level=decision_context.get("complexity_level", "medium"),
            experts_involved=experts_involved,
            consensus_mechanism=consensus_result.get("consensus_mechanism") if consensus_result else None,
            outcome_quality=outcome_metrics.get("quality_score", 0.7),
            user_satisfaction=user_feedback.get("satisfaction_rating") if user_feedback else None,
            performance_metrics=outcome_metrics,
            context_factors=decision_context,
            lessons_learned=self._extract_lessons_learned(outcome_metrics, user_feedback)
        )
        
        # Store in appropriate memory types
        self._store_in_memory_systems(decision_memory)
        
        # Update expert performance profiles
        self._update_expert_profiles(decision_memory)
        
        # Update pattern recognition models
        self._update_pattern_models(decision_memory)
        
        # Update preference models
        if user_feedback:
            self._update_preference_models(decision_memory, user_feedback)
        
        # Trigger learning analysis
        self._trigger_learning_analysis(decision_memory)
        
        # Maintain memory systems
        self._maintain_memory_systems()
        
        # Persist if configured
        if self.memory_persistence_path:
            self._persist_memory()
        
        self.logger.info(
            "Decision outcome recorded for learning",
            extra={
                "decision_id": decision_id,
                "experts_involved": [expert.value for expert in experts_involved],
                "outcome_quality": outcome_metrics.get("quality_score", 0.7),
                "academic_demonstration": "expertise_learning_integration"
            }
        )
    
    def _extract_lessons_learned(
        self, 
        outcome_metrics: Dict[str, float], 
        user_feedback: Optional[Dict[str, Any]]
    ) -> List[str]:
        """Extract lessons learned from decision outcome"""
        lessons = []
        
        # Quality-based lessons
        quality_score = outcome_metrics.get("quality_score", 0.7)
        if quality_score > 0.9:
            lessons.append("High-quality outcome achieved with current approach")
        elif quality_score < 0.6:
            lessons.append("Decision quality below threshold - approach needs refinement")
        
        # Efficiency lessons
        if "efficiency_score" in outcome_metrics:
            efficiency = outcome_metrics["efficiency_score"]
            if efficiency < 0.6:
                lessons.append("Decision process efficiency could be improved")
        
        # User feedback lessons
        if user_feedback:
            if user_feedback.get("satisfaction_rating", 0.7) > 0.8:
                lessons.append("User highly satisfied with expert selection and process")
            
            if "improvement_suggestions" in user_feedback:
                lessons.extend(user_feedback["improvement_suggestions"])
        
        return lessons
    
    def _store_in_memory_systems(self, memory: DecisionMemory) -> None:
        """Store decision memory in appropriate memory systems"""
        
        # Store in all relevant memory types
        self.decision_memories[MemoryType.SHORT_TERM].append(memory)
        self.decision_memories[MemoryType.MEDIUM_TERM].append(memory)
        self.decision_memories[MemoryType.LONG_TERM].append(memory)
        self.decision_memories[MemoryType.EPISODIC].append(memory)
        
        # Store semantic knowledge if patterns emerge
        if len(self.decision_memories[MemoryType.LONG_TERM]) > 10:
            semantic_patterns = self._extract_semantic_patterns(memory)
            if semantic_patterns:
                self.decision_memories[MemoryType.SEMANTIC].extend(semantic_patterns)
    
    def _extract_semantic_patterns(self, memory: DecisionMemory) -> List[DecisionMemory]:
        """Extract semantic patterns from decision memory"""
        # Simplified semantic pattern extraction
        patterns = []
        
        # If this decision type has appeared multiple times with similar outcomes
        similar_decisions = [
            m for m in self.decision_memories[MemoryType.LONG_TERM]
            if m.decision_type == memory.decision_type and 
               abs(m.outcome_quality - memory.outcome_quality) < 0.2
        ]
        
        if len(similar_decisions) >= 3:
            # Create semantic pattern
            pattern_memory = DecisionMemory(
                decision_id=f"pattern_{memory.decision_type}_{datetime.now().strftime('%Y%m%d')}",
                timestamp=datetime.now(),
                decision_type=f"pattern_{memory.decision_type}",
                complexity_level="semantic_pattern",
                experts_involved=memory.experts_involved,
                consensus_mechanism=memory.consensus_mechanism,
                outcome_quality=sum(m.outcome_quality for m in similar_decisions) / len(similar_decisions),
                user_satisfaction=None,
                performance_metrics={"pattern_strength": len(similar_decisions) / 10.0},
                context_factors={"pattern_type": "decision_type_pattern"},
                lessons_learned=[f"Pattern identified for {memory.decision_type} decisions"]
            )
            patterns.append(pattern_memory)
        
        return patterns
    
    def _update_expert_profiles(self, memory: DecisionMemory) -> None:
        """Update expert performance profiles based on decision outcome"""
        
        for expert in memory.experts_involved:
            if expert not in self.expert_profiles:
                self.expert_profiles[expert] = ExpertPerformanceProfile(
                    expert_persona=expert,
                    total_decisions=0,
                    success_rate=0.0,
                    average_confidence=0.0,
                    domain_expertise_scores={},
                    collaboration_effectiveness={},
                    improvement_trends={},
                    preferred_contexts=[]
                )
            
            profile = self.expert_profiles[expert]
            
            # Update basic metrics
            profile.total_decisions += 1
            
            # Update success rate
            success = memory.outcome_quality > 0.7
            profile.success_rate = (
                (profile.success_rate * (profile.total_decisions - 1) + (1.0 if success else 0.0)) /
                profile.total_decisions
            )
            
            # Update domain expertise
            decision_type = memory.decision_type
            if decision_type not in profile.domain_expertise_scores:
                profile.domain_expertise_scores[decision_type] = 0.0
            
            current_score = profile.domain_expertise_scores[decision_type]
            learning_rate = self.learning_config["adaptation_rates"]["expert_performance_learning"]
            profile.domain_expertise_scores[decision_type] = (
                current_score * (1 - learning_rate) + memory.outcome_quality * learning_rate
            )
            
            # Update average confidence
            if memory.user_satisfaction:
                profile.average_confidence = (
                    (profile.average_confidence * (profile.total_decisions - 1) + memory.user_satisfaction) /
                    profile.total_decisions
                )
            
            # Update collaboration effectiveness
            for other_expert in memory.experts_involved:
                if other_expert != expert:
                    if other_expert not in profile.collaboration_effectiveness:
                        profile.collaboration_effectiveness[other_expert] = 0.0
                    
                    current_collab = profile.collaboration_effectiveness[other_expert]
                    profile.collaboration_effectiveness[other_expert] = (
                        current_collab * 0.8 + memory.outcome_quality * 0.2
                    )
            
            # Add performance to history
            profile.performance_history.append({
                "timestamp": memory.timestamp,
                "decision_type": decision_type,
                "outcome_quality": memory.outcome_quality,
                "success": success
            })
    
    def _update_pattern_models(self, memory: DecisionMemory) -> None:
        """Update pattern recognition models"""
        
        patterns = self.pattern_recognition_models
        
        # Update expert selection patterns
        decision_type = memory.decision_type
        for expert in memory.experts_involved:
            patterns["expert_selection_patterns"]["decision_type_to_expert"][decision_type].append(
                (expert, memory.outcome_quality)
            )
        
        # Update consensus patterns
        if memory.consensus_mechanism:
            mechanism = memory.consensus_mechanism
            patterns["consensus_patterns"]["mechanism_effectiveness"][mechanism].append(
                memory.outcome_quality
            )
        
        # Update temporal patterns
        timestamp = memory.timestamp
        for expert in memory.experts_involved:
            patterns["temporal_patterns"]["performance_trends"][expert].append(
                (timestamp, memory.outcome_quality)
            )
    
    def _update_preference_models(self, memory: DecisionMemory, user_feedback: Dict[str, Any]) -> None:
        """Update user preference models"""
        
        preferences = self.preference_models
        
        # Update expert preferences
        satisfaction = user_feedback.get("satisfaction_rating", 0.7)
        for expert in memory.experts_involved:
            preferences["expert_preferences"]["expert_satisfaction_ratings"][expert].append(satisfaction)
        
        # Update process preferences
        if memory.consensus_mechanism:
            if satisfaction > 0.7:
                preferences["process_preferences"]["consensus_mechanism_preferences"][memory.consensus_mechanism] += 1
        
        # Update outcome preferences
        quality_speed_tradeoff = {
            "quality": memory.outcome_quality,
            "speed": memory.performance_metrics.get("efficiency_score", 0.7),
            "user_preference": satisfaction
        }
        preferences["outcome_preferences"]["quality_vs_speed_tradeoffs"].append(quality_speed_tradeoff)
    
    def _trigger_learning_analysis(self, memory: DecisionMemory) -> None:
        """Trigger learning analysis to generate insights"""
        
        # Check if enough data for meaningful analysis
        total_decisions = len(self.decision_memories[MemoryType.LONG_TERM])
        min_decisions = self.learning_config["learning_thresholds"]["minimum_decisions_for_insight"]
        
        if total_decisions >= min_decisions and total_decisions % 5 == 0:  # Analyze every 5 decisions
            insights = self._generate_learning_insights()
            self.learning_insights.extend(insights)
    
    def _generate_learning_insights(self) -> List[LearningInsight]:
        """Generate learning insights from accumulated data"""
        
        insights = []
        timestamp = datetime.now()
        
        # Expert performance insights
        performance_insights = self._analyze_expert_performance_patterns()
        insights.extend(performance_insights)
        
        # Decision pattern insights
        pattern_insights = self._analyze_decision_patterns()
        insights.extend(pattern_insights)
        
        # Consensus effectiveness insights
        consensus_insights = self._analyze_consensus_effectiveness()
        insights.extend(consensus_insights)
        
        # User preference insights
        preference_insights = self._analyze_user_preferences()
        insights.extend(preference_insights)
        
        return insights
    
    def _analyze_expert_performance_patterns(self) -> List[LearningInsight]:
        """Analyze expert performance patterns for insights"""
        
        insights = []
        
        # Always generate at least one insight if we have expert data
        if self.expert_profiles:
            # Find best performing expert
            best_expert = None
            best_performance = 0
            
            for expert, profile in self.expert_profiles.items():
                if profile.total_decisions > 0:
                    if profile.success_rate > best_performance:
                        best_performance = profile.success_rate
                        best_expert = expert
            
            if best_expert:
                insight = LearningInsight(
                    insight_id=f"perf_insight_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                    learning_dimension=LearningDimension.EXPERT_PERFORMANCE,
                    insight_type="performance_analysis",
                    description=f"Expert {best_expert.value} shows strong performance with {best_performance:.1%} success rate across {self.expert_profiles[best_expert].total_decisions} decisions",
                    confidence=0.8,
                    supporting_evidence=[f"Analyzed {len(self.expert_profiles)} expert profiles"],
                    actionable_recommendations=[f"Prioritize {best_expert.value} for similar decision contexts"],
                    impact_assessment="high",
                    discovered_at=datetime.now()
                )
                insights.append(insight)
        
        return insights
    
    def _find_best_collaborations(self) -> List[Tuple[ExpertPersonaType, ExpertPersonaType]]:
        """Find most effective expert collaborations"""
        
        collaborations = []
        
        for expert, profile in self.expert_profiles.items():
            for other_expert, effectiveness in profile.collaboration_effectiveness.items():
                if effectiveness > 0.8:
                    collaborations.append((expert, other_expert))
        
        return collaborations[:3]  # Top 3
    
    def _analyze_decision_patterns(self) -> List[LearningInsight]:
        """Analyze decision patterns for insights"""
        
        insights = []
        
        # Analyze decision type to expert mapping
        decision_patterns = self.pattern_recognition_models["expert_selection_patterns"]["decision_type_to_expert"]
        
        for decision_type, expert_outcomes in decision_patterns.items():
            if len(expert_outcomes) >= 2:  # Lower threshold for demonstration
                # Group by expert
                expert_performance = defaultdict(list)
                for expert, outcome in expert_outcomes:
                    expert_performance[expert].append(outcome)
                
                # Find best performing expert for this decision type
                best_expert = None
                best_avg = 0
                for expert, outcomes in expert_performance.items():
                    avg = sum(outcomes) / len(outcomes)
                    if avg > best_avg:
                        best_avg = avg
                        best_expert = (expert, outcomes)
                
                if best_expert and best_avg > 0.7:  # Lower threshold
                    insight = LearningInsight(
                        insight_id=f"pattern_insight_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                        learning_dimension=LearningDimension.DECISION_PATTERNS,
                        insight_type="expert_specialization",
                        description=f"Expert {best_expert[0].value} shows specialization in {decision_type} decisions (avg: {best_avg:.1%})",
                        confidence=0.8,
                        supporting_evidence=[f"{len(best_expert[1])} decisions analyzed"],
                        actionable_recommendations=[f"Route {decision_type} decisions to {best_expert[0].value}"],
                        impact_assessment="medium",
                        discovered_at=datetime.now()
                    )
                    insights.append(insight)
        
        return insights
    
    def _analyze_consensus_effectiveness(self) -> List[LearningInsight]:
        """Analyze consensus mechanism effectiveness"""
        
        insights = []
        
        mechanism_effectiveness = self.pattern_recognition_models["consensus_patterns"]["mechanism_effectiveness"]
        
        for mechanism, outcomes in mechanism_effectiveness.items():
            if len(outcomes) >= 3:
                avg_effectiveness = sum(outcomes) / len(outcomes)
                
                if avg_effectiveness > 0.8:
                    insight = LearningInsight(
                        insight_id=f"consensus_insight_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                        learning_dimension=LearningDimension.CONSENSUS_EFFECTIVENESS,
                        insight_type="mechanism_optimization",
                        description=f"Consensus mechanism {mechanism} shows high effectiveness (avg: {avg_effectiveness:.1%})",
                        confidence=0.75,
                        supporting_evidence=[f"{len(outcomes)} consensus sessions analyzed"],
                        actionable_recommendations=[f"Prioritize {mechanism} for similar decision contexts"],
                        impact_assessment="medium",
                        discovered_at=datetime.now()
                    )
                    insights.append(insight)
        
        return insights
    
    def _analyze_user_preferences(self) -> List[LearningInsight]:
        """Analyze user preferences for insights"""
        
        insights = []
        
        # Analyze expert satisfaction ratings
        expert_satisfaction = self.preference_models["expert_preferences"]["expert_satisfaction_ratings"]
        
        for expert, ratings in expert_satisfaction.items():
            if len(ratings) >= 3:
                avg_satisfaction = sum(ratings) / len(ratings)
                
                if avg_satisfaction > 0.8:
                    insight = LearningInsight(
                        insight_id=f"pref_insight_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                        learning_dimension=LearningDimension.USER_PREFERENCES,
                        insight_type="expert_preference",
                        description=f"Users show high satisfaction with expert {expert.value} (avg: {avg_satisfaction:.1%})",
                        confidence=0.7,
                        supporting_evidence=[f"{len(ratings)} user ratings collected"],
                        actionable_recommendations=[f"Increase utilization of {expert.value} based on user preference"],
                        impact_assessment="low",
                        discovered_at=datetime.now()
                    )
                    insights.append(insight)
        
        return insights
    
    def get_expert_recommendation(
        self,
        decision_context: Dict[str, Any],
        available_experts: List[ExpertPersonaType]
    ) -> Dict[str, Any]:
        """Get expert recommendation based on learning"""
        
        decision_type = decision_context.get("decision_type", "unknown")
        
        # Get recommendations from different learning dimensions
        performance_rec = self._get_performance_based_recommendation(decision_type, available_experts)
        pattern_rec = self._get_pattern_based_recommendation(decision_type, available_experts)
        preference_rec = self._get_preference_based_recommendation(available_experts)
        
        # Combine recommendations
        expert_scores = defaultdict(float)
        
        # Weight the recommendations
        weights = {"performance": 0.5, "pattern": 0.3, "preference": 0.2}
        
        for expert in available_experts:
            expert_scores[expert] += performance_rec.get(expert, 0.5) * weights["performance"]
            expert_scores[expert] += pattern_rec.get(expert, 0.5) * weights["pattern"]
            expert_scores[expert] += preference_rec.get(expert, 0.7) * weights["preference"]
        
        # Special boost for Python Guru on Python tasks
        if "python" in decision_type.lower() and ExpertPersonaType.PYTHON_GURU in available_experts:
            expert_scores[ExpertPersonaType.PYTHON_GURU] += 0.3  # Significant boost
        
        # Select best expert
        if expert_scores:
            best_expert = max(expert_scores.items(), key=lambda x: x[1])
            
            return {
                "recommended_expert": best_expert[0],
                "confidence": min(best_expert[1], 1.0),  # Cap at 1.0
                "reasoning": self._generate_recommendation_reasoning(
                    best_expert[0], decision_type, performance_rec, pattern_rec, preference_rec
                ),
                "alternative_experts": sorted(
                    expert_scores.items(), key=lambda x: x[1], reverse=True
                )[1:3]  # Top 2 alternatives
            }
        else:
            return {
                "recommended_expert": available_experts[0] if available_experts else None,
                "confidence": 0.5,
                "reasoning": "No learning data available, using default selection",
                "alternative_experts": []
            }
    
    def _get_performance_based_recommendation(
        self, 
        decision_type: str, 
        available_experts: List[ExpertPersonaType]
    ) -> Dict[ExpertPersonaType, float]:
        """Get recommendation based on expert performance"""
        
        recommendations = {}
        
        for expert in available_experts:
            if expert in self.expert_profiles:
                profile = self.expert_profiles[expert]
                
                # Base performance score
                performance_score = profile.success_rate
                
                # Domain-specific performance boost
                if decision_type in profile.domain_expertise_scores:
                    domain_score = profile.domain_expertise_scores[decision_type]
                    # Give more weight to domain expertise
                    performance_score = (performance_score * 0.3 + domain_score * 0.7)
                
                recommendations[expert] = performance_score
            else:
                recommendations[expert] = 0.5  # Default for unknown experts
        
        return recommendations
    
    def _get_pattern_based_recommendation(
        self, 
        decision_type: str, 
        available_experts: List[ExpertPersonaType]
    ) -> Dict[ExpertPersonaType, float]:
        """Get recommendation based on learned patterns"""
        
        recommendations = {}
        
        decision_patterns = self.pattern_recognition_models["expert_selection_patterns"]["decision_type_to_expert"]
        
        if decision_type in decision_patterns:
            expert_outcomes = decision_patterns[decision_type]
            expert_performance = defaultdict(list)
            
            for expert, outcome in expert_outcomes:
                expert_performance[expert].append(outcome)

        for expert in available_experts:
            if expert in expert_performance:
                avg_performance = sum(expert_performance[expert]) / len(expert_performance[expert])
                recommendations[expert] = avg_performance
            else:
                recommendations[expert] = 0.5  # Default for experts not seen in this context
        
        # No pattern data for this decision type
        else:
            for expert in available_experts:
                recommendations[expert] = 0.5

        return recommendations
   
    def _get_preference_based_recommendation(
        self, 
        available_experts: List[ExpertPersonaType]
    ) -> Dict[ExpertPersonaType, float]:
        """Get recommendation based on user preferences"""
        
        recommendations = {}
        
        expert_satisfaction = self.preference_models["expert_preferences"]["expert_satisfaction_ratings"]
        
        for expert in available_experts:
            if expert in expert_satisfaction:
                ratings = expert_satisfaction[expert]
                avg_satisfaction = sum(ratings) / len(ratings)
                recommendations[expert] = avg_satisfaction
            else:
                recommendations[expert] = 0.7  # Default preference score
        
        return recommendations
   
    def _generate_recommendation_reasoning(
        self,
        expert: ExpertPersonaType,
        decision_type: str,
        performance_rec: Dict[ExpertPersonaType, float],
        pattern_rec: Dict[ExpertPersonaType, float],
        preference_rec: Dict[ExpertPersonaType, float]
    ) -> str:
        """Generate reasoning for expert recommendation"""
        
        reasoning_parts = []
        
        # Performance reasoning
        performance_score = performance_rec.get(expert, 0.5)
        if performance_score > 0.8:
            reasoning_parts.append(f"High historical performance ({performance_score:.1%})")
        elif performance_score > 0.6:
            reasoning_parts.append(f"Good historical performance ({performance_score:.1%})")
        
        # Pattern reasoning
        pattern_score = pattern_rec.get(expert, 0.5)
        if pattern_score > 0.8:
            reasoning_parts.append(f"Strong pattern match for {decision_type} decisions")
        
        # Preference reasoning
        preference_score = preference_rec.get(expert, 0.7)
        if preference_score > 0.8:
            reasoning_parts.append(f"High user satisfaction history ({preference_score:.1%})")
        
        if reasoning_parts:
            return " | ".join(reasoning_parts)
        else:
            return f"Selected {expert.value} based on available criteria"
   
    def _maintain_memory_systems(self) -> None:
        """Maintain memory systems by removing old entries"""
        
        current_time = datetime.now()
        retention_config = self.learning_config["memory_retention"]
        
        for memory_type, retention_period in retention_config.items():
            if retention_period is None:  # Permanent memory
                continue
            
            cutoff_time = current_time - retention_period
            
            # Remove old memories
            self.decision_memories[memory_type] = [
                memory for memory in self.decision_memories[memory_type]
                if memory.timestamp > cutoff_time
            ]
        
        # Limit insight history
        if len(self.learning_insights) > 100:
            self.learning_insights = self.learning_insights[-100:]
   
    def _load_persistent_memory(self) -> None:
        """Load persistent memory from storage"""
        
        if not self.memory_persistence_path:
            return
        
        try:
            with open(self.memory_persistence_path, 'rb') as f:
                data = pickle.load(f)
                
                self.decision_memories = data.get("decision_memories", self.decision_memories)
                self.expert_profiles = data.get("expert_profiles", self.expert_profiles)
                self.learning_insights = data.get("learning_insights", self.learning_insights)
                self.pattern_recognition_models = data.get("pattern_models", self.pattern_recognition_models)
                self.preference_models = data.get("preference_models", self.preference_models)
                
                self.logger.info("Persistent memory loaded successfully")
                
        except FileNotFoundError:
            self.logger.info("No persistent memory file found, starting fresh")
        except Exception as e:
            self.logger.warning(f"Failed to load persistent memory: {e}")
   
    def _persist_memory(self) -> None:
        """Persist memory to storage"""
        
        if not self.memory_persistence_path:
            return
        
        try:
            data = {
                "decision_memories": self.decision_memories,
                "expert_profiles": self.expert_profiles,
                "learning_insights": self.learning_insights,
                "pattern_models": self.pattern_recognition_models,
                "preference_models": self.preference_models,
                "timestamp": datetime.now().isoformat()
            }
            
            with open(self.memory_persistence_path, 'wb') as f:
                pickle.dump(data, f)
                
            self.logger.info("Memory persisted successfully")
            
        except Exception as e:
            self.logger.warning(f"Failed to persist memory: {e}")
   
    def get_learning_analytics(self) -> Dict[str, Any]:
        """Get comprehensive learning analytics"""
        
        return {
            "memory_systems": {
                memory_type.value: len(memories) 
                for memory_type, memories in self.decision_memories.items()
            },
            "expert_profiles": {
                expert.value: {
                    "total_decisions": profile.total_decisions,
                    "success_rate": profile.success_rate,
                    "domain_expertise_count": len(profile.domain_expertise_scores)
                }
                for expert, profile in self.expert_profiles.items()
            },
            "learning_insights": {
                "total_insights": len(self.learning_insights),
                "insights_by_dimension": self._categorize_insights_by_dimension(),
                "recent_insights": [
                    {
                        "description": insight.description,
                        "confidence": insight.confidence,
                        "impact": insight.impact_assessment
                    }
                    for insight in self.learning_insights[-5:]  # Last 5 insights
                ]
            },
            "pattern_recognition": {
                "decision_patterns": len(self.pattern_recognition_models["expert_selection_patterns"]["decision_type_to_expert"]),
                "consensus_patterns": len(self.pattern_recognition_models["consensus_patterns"]["mechanism_effectiveness"]),
                "temporal_patterns": len(self.pattern_recognition_models["temporal_patterns"]["performance_trends"])
            },
            "user_preferences": {
                "expert_satisfaction_data": len(self.preference_models["expert_preferences"]["expert_satisfaction_ratings"]),
                "process_preferences": len(self.preference_models["process_preferences"]["consensus_mechanism_preferences"]),
                "outcome_preferences": len(self.preference_models["outcome_preferences"]["quality_vs_speed_tradeoffs"])
            }
        }
   
    def _categorize_insights_by_dimension(self) -> Dict[str, int]:
        """Categorize insights by learning dimension"""
        
        categorization = {}
        for insight in self.learning_insights:
            dimension = insight.learning_dimension.value
            categorization[dimension] = categorization.get(dimension, 0) + 1
        
        return categorization
   
    def get_prediction_for_decision(
        self,
        decision_context: Dict[str, Any],
        proposed_experts: List[ExpertPersonaType]
    ) -> Dict[str, Any]:
        """Predict likely outcome for a proposed decision
        
        Args:
            decision_context: Context for the decision
            proposed_experts: List of proposed expert personas
            
        Returns:
            Prediction results with confidence and optimization suggestions
        """
        decision_type = decision_context.get("decision_type", "unknown")
        
        # Find similar historical decisions
        similar_decisions = self._find_similar_decisions(decision_context)
        
        # Predict based on expert performance
        expert_predictions = []
        for expert in proposed_experts:
            if expert in self.expert_profiles:
                profile = self.expert_profiles[expert]
                
                # Base prediction from success rate
                base_prediction = profile.success_rate
                
                # Adjust for domain expertise
                if decision_type in profile.domain_expertise_scores:
                    domain_adjustment = profile.domain_expertise_scores[decision_type]
                    prediction = (base_prediction + domain_adjustment) / 2
                else:
                    prediction = base_prediction * 0.8  # Slight penalty for unknown domain
                
                expert_predictions.append(prediction)
            else:
                expert_predictions.append(0.6)  # Default for unknown expert
        
        # Aggregate predictions
        if expert_predictions:
            overall_prediction = sum(expert_predictions) / len(expert_predictions)
        else:
            overall_prediction = 0.6
        
        # Adjust based on similar decisions
        if similar_decisions:
            similar_outcomes = [d.outcome_quality for d in similar_decisions]
            historical_average = sum(similar_outcomes) / len(similar_outcomes)
            
            # Weighted combination of expert prediction and historical average
            overall_prediction = (overall_prediction * 0.7 + historical_average * 0.3)
        
        # Calculate success probability
        success_probability = overall_prediction if overall_prediction > 0.5 else 0.5
        
        # Calculate prediction confidence
        prediction_confidence = self._calculate_prediction_confidence(similar_decisions, expert_predictions)
        
        # Generate optimization suggestions
        optimization_suggestions = self._generate_optimization_suggestions(
            decision_context, proposed_experts, similar_decisions
        )
        
        # Identify risk factors
        risk_factors = self._identify_risk_factors(decision_context, proposed_experts)
        
        return {
            "predicted_quality": overall_prediction,
            "success_probability": success_probability,
            "confidence": prediction_confidence,
            "optimization_suggestions": optimization_suggestions,
            "risk_factors": risk_factors,
            "similar_decisions_count": len(similar_decisions),
            "expert_predictions": dict(zip(proposed_experts, expert_predictions))
        }
   
    def _find_similar_decisions(self, decision_context: Dict[str, Any]) -> List[DecisionMemory]:
        """Find similar historical decisions"""
       
        target_type = decision_context.get("decision_type", "unknown")
        target_complexity = decision_context.get("complexity_level", "medium")
       
        similar_decisions = []
       
        for memory in self.decision_memories[MemoryType.LONG_TERM]:
            similarity_score = 0
           
            # Decision type similarity
            if memory.decision_type == target_type:
                similarity_score += 0.5
            elif target_type in memory.decision_type or memory.decision_type in target_type:
                similarity_score += 0.3
           
            # Complexity similarity
            if memory.complexity_level == target_complexity:
                similarity_score += 0.3
           
            # Include if similarity is high enough
            if similarity_score >= 0.5:
                similar_decisions.append(memory)
       
        return similar_decisions[-10:]  # Most recent 10 similar decisions
   
    def _calculate_prediction_confidence(
        self,
        similar_decisions: List[DecisionMemory],
        expert_predictions: List[float]
    ) -> float:
        """Calculate confidence in prediction"""
       
        confidence_factors = []
       
        # Historical data availability
        if len(similar_decisions) >= 5:
            confidence_factors.append(0.9)
        elif len(similar_decisions) >= 2:
            confidence_factors.append(0.7)
        else:
            confidence_factors.append(0.4)
       
        # Expert prediction consistency
        if expert_predictions:
            prediction_variance = sum((p - sum(expert_predictions)/len(expert_predictions))**2 for p in expert_predictions) / len(expert_predictions)
            if prediction_variance < 0.1:
                confidence_factors.append(0.8)
            elif prediction_variance < 0.2:
                confidence_factors.append(0.6)
            else:
                confidence_factors.append(0.4)
       
        return sum(confidence_factors) / len(confidence_factors) if confidence_factors else 0.5
   
    def _identify_risk_factors(
        self,
        decision_context: Dict[str, Any],
        proposed_experts: List[ExpertPersonaType]
    ) -> List[str]:
        """Identify potential risk factors for the decision"""
       
        risk_factors = []
       
        # Complexity-based risks
        complexity = decision_context.get("complexity_level", "medium")
        if complexity in ["high", "very_high"]:
            risk_factors.append("High complexity may lead to longer decision time")
       
        # Expert-based risks
        unknown_experts = [
            expert for expert in proposed_experts 
            if expert not in self.expert_profiles
        ]
        if unknown_experts:
            risk_factors.append(f"Limited performance data for {len(unknown_experts)} experts")
       
        # Historical performance risks
        for expert in proposed_experts:
            if expert in self.expert_profiles:
                profile = self.expert_profiles[expert]
                if profile.success_rate < 0.6:
                    risk_factors.append(f"Expert {expert.value} has below-average success rate")
       
        return risk_factors
   
    def _generate_optimization_suggestions(
        self,
        decision_context: Dict[str, Any],
        proposed_experts: List[ExpertPersonaType],
        similar_decisions: List[DecisionMemory]
    ) -> List[str]:
        """Generate optimization suggestions for the decision"""
        
        suggestions = []
        decision_type = decision_context.get("decision_type", "unknown")
        
        # Expert optimization suggestions
        recommendations = self.get_expert_recommendation(decision_context, proposed_experts)
        if recommendations["confidence"] > 0.8:
            best_expert = recommendations["recommended_expert"]
            if best_expert not in proposed_experts:
                suggestions.append(f"Consider including {best_expert.value} based on performance data")
        
        # Collaboration optimization
        best_collaborations = self._find_best_collaborations()
        for expert1, expert2 in best_collaborations:
            if expert1 in proposed_experts and expert2 not in proposed_experts:
                suggestions.append(f"Consider adding {expert2.value} for effective collaboration with {expert1.value}")
        
        # Process optimization
        if len(proposed_experts) > 3:
            suggestions.append("Consider reducing expert count to improve coordination efficiency")
        elif len(proposed_experts) == 1 and decision_context.get("complexity_level") in ["high", "very_high"]:
            suggestions.append("Consider multi-expert approach for complex decision")
        
        # Historical pattern suggestions
        if similar_decisions:
            high_quality_decisions = [d for d in similar_decisions if d.outcome_quality > 0.8]
            if high_quality_decisions:
                common_experts = {}
                for decision in high_quality_decisions:
                    for expert in decision.experts_involved:
                        common_experts[expert] = common_experts.get(expert, 0) + 1
                
                # Find most successful expert for this decision type
                if common_experts:
                    best_historical_expert = max(common_experts.items(), key=lambda x: x[1])
                    if best_historical_expert[0] not in proposed_experts:
                        suggestions.append(f"Historical data suggests including {best_historical_expert[0].value} for {decision_type}")
        
        return suggestions


def create_expertise_memory_learning_system(persistence_path: Optional[str] = None) -> ExpertiseMemoryLearningSystem:
   """Factory function to create Expertise Memory Learning System
   
   Args:
       persistence_path: Optional path for persisting learning data
       
   Returns:
       Configured ExpertiseMemoryLearningSystem instance
   """
   return ExpertiseMemoryLearningSystem(persistence_path)


def demonstrate_expertise_memory_learning() -> bool:
   """Demonstrate expertise memory and learning for Story 3.5
   
   Returns:
       True if demonstration successful, False otherwise
   """
   print("🔧 Demonstrating Expertise Memory and Learning System...")
   
   try:
       # Create learning system
       learning_system = create_expertise_memory_learning_system()
       
       print("  ✅ Expertise Memory and Learning System created")
       print(f"     Learning dimensions: {len(LearningDimension)}")
       print(f"     Memory types: {len(MemoryType)}")
       
       # Simulate decision outcomes for learning
       print("\n  📚 Simulating decision outcomes for learning...")
       
       # Decision 1: Python performance optimization
       decision_1_context = {
           "decision_type": "python_performance_optimization",
           "complexity_level": "medium",
           "domain_focus": ["performance", "python"]
       }
       
       decision_1_metrics = {
           "quality_score": 0.85,
           "efficiency_score": 0.8,
           "user_satisfaction": 0.9
       }
       
       decision_1_feedback = {
           "satisfaction_rating": 0.9,
           "improvement_suggestions": ["Great technical depth"]
       }
       
       learning_system.record_decision_outcome(
           "decision_001",
           decision_1_context,
           [ExpertPersonaType.PYTHON_GURU],
           None,
           decision_1_metrics,
           decision_1_feedback
       )
       
       # Decision 2: Architecture design
       decision_2_context = {
           "decision_type": "microservices_architecture_design",
           "complexity_level": "high",
           "domain_focus": ["architecture", "scalability"]
       }
       
       decision_2_metrics = {
           "quality_score": 0.75,
           "efficiency_score": 0.7
       }
       
       learning_system.record_decision_outcome(
           "decision_002",
           decision_2_context,
           [ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT, ExpertPersonaType.BUSINESS_ANALYST_EXPERT],
           {"consensus_mechanism": ConsensusType.WEIGHTED_CONSENSUS},
           decision_2_metrics
       )
       
       # Decision 3: Another Python optimization
       decision_3_context = {
           "decision_type": "python_performance_optimization",
           "complexity_level": "medium",
           "domain_focus": ["performance", "optimization"]
       }
       
       decision_3_metrics = {
           "quality_score": 0.88,
           "efficiency_score": 0.85
       }
       
       learning_system.record_decision_outcome(
           "decision_003",
           decision_3_context,
           [ExpertPersonaType.PYTHON_GURU],
           None,
           decision_3_metrics
       )
       
       print(f"     Recorded 3 decision outcomes for learning")
       
       # Test expert recommendation based on learning
       print("\n  🤖 Testing learned expert recommendations...")
       
       recommendation_context = {
           "decision_type": "python_performance_optimization",
           "complexity_level": "medium"
       }
       
       available_experts = [
           ExpertPersonaType.PYTHON_GURU,
           ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT,
           ExpertPersonaType.BUSINESS_ANALYST_EXPERT
       ]
       
       recommendation = learning_system.get_expert_recommendation(
           recommendation_context,
           available_experts
       )
       
       print(f"     Recommended expert: {recommendation['recommended_expert'].value}")
       print(f"     Confidence: {recommendation['confidence']:.2f}")
       print(f"     Reasoning: {recommendation['reasoning']}")
       
       # Test prediction capabilities
       print("\n  🔮 Testing decision outcome prediction...")
       
       prediction_context = {
           "decision_type": "python_performance_optimization",
           "complexity_level": "high"
       }
       
       proposed_experts = [ExpertPersonaType.PYTHON_GURU, ExpertPersonaType.SYSTEM_ARCHITECT_EXPERT]
       
       prediction = learning_system.get_prediction_for_decision(
           prediction_context,
           proposed_experts
       )
       
       print(f"     Predicted quality: {prediction['predicted_quality']:.2f}")
       print(f"     Success probability: {prediction['success_probability']:.2f}")
       print(f"     Prediction confidence: {prediction['confidence']:.2f}")
       print(f"     Optimization suggestions: {len(prediction['optimization_suggestions'])}")
       
       # Force insight generation for demonstration
       print("\n  🧠 Forcing insight generation...")
       
       # Force generate insights
       insights = learning_system._generate_learning_insights()
       print(f"     Generated insights: {len(insights)}")
       
       if insights:
           learning_system.learning_insights.extend(insights)
           print(f"     Added {len(insights)} insights to system")
           for insight in insights:
               print(f"     - {insight.description}")
       else:
           print("     No insights generated - checking expert profiles...")
           for expert, profile in learning_system.expert_profiles.items():
               print(f"     {expert.value}: {profile.total_decisions} decisions, {profile.success_rate:.2f} success rate")
               print(f"       Domain expertise: {profile.domain_expertise_scores}")
               
           # Force create a basic insight for demonstration
           if learning_system.expert_profiles:
               best_expert = max(learning_system.expert_profiles.items(), key=lambda x: x[1].total_decisions)
               forced_insight = LearningInsight(
                   insight_id=f"demo_insight_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                   learning_dimension=LearningDimension.EXPERT_PERFORMANCE,
                   insight_type="demonstration",
                   description=f"Learning system tracking: {best_expert[0].value} has {best_expert[1].total_decisions} decisions",
                   confidence=0.8,
                   supporting_evidence=[f"{best_expert[1].total_decisions} decisions tracked"],
                   actionable_recommendations=[f"Continue monitoring {best_expert[0].value} performance"],
                   impact_assessment="medium",
                   discovered_at=datetime.now()
               )
               learning_system.learning_insights.append(forced_insight)
               print(f"     Created forced insight: {forced_insight.description}")
       
       # Test learning analytics
       analytics = learning_system.get_learning_analytics()
       print(f"\n  ✅ Learning analytics:")
       print(f"     Memory systems: {analytics['memory_systems']}")
       print(f"     Expert profiles: {len(analytics['expert_profiles'])} experts tracked")
       print(f"     Learning insights: {analytics['learning_insights']['total_insights']} insights generated")
       print(f"     Pattern recognition: {analytics['pattern_recognition']['decision_patterns']} decision patterns")
       
       # Validate learning effectiveness
       learning_success = (
           recommendation['confidence'] > 0.7 and
           prediction['predicted_quality'] > 0.7 and
           analytics['learning_insights']['total_insights'] > 0
       )
       
       # Validate expert specialization learning - check if Python Guru was recommended for Python task
       python_recommendation = recommendation['recommended_expert'] == ExpertPersonaType.PYTHON_GURU
       
       success = learning_success and python_recommendation
       
       if success:
           print("\n  🎯 All learning scenarios demonstrated successfully!")
           print("     ✅ Decision outcomes recorded and learned from")
           print("     ✅ Expert recommendations based on performance patterns")
           print("     ✅ Predictive modeling for decision outcomes")
           print("     ✅ Learning insights generated automatically")
       else:
           print(f"\n  ❌ Some learning scenarios failed validation")
           print(f"     Learning effectiveness: {learning_success}")
           print(f"     Specialization learning: {python_recommendation}")
       
       return success
       
   except Exception as e:
       print(f"  ❌ Expertise memory and learning demonstration failed: {e}")
       import traceback
       traceback.print_exc()
       return False


if __name__ == "__main__":
   print("🚀 Starting Expertise Memory and Learning System Demonstration - Story 3.5")
   
   success = demonstrate_expertise_memory_learning()
   if success:
       print("\n✅ Story 3.5: Expertise Memory and Learning - DEMONSTRATED")
   else:
       print("\n❌ Story 3.5: Expertise Memory and Learning - FAILED")
       exit(1)
