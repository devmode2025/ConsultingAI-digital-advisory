"""System Architect Agent - Specialized Agent for System Design and Architecture

This module implements the System Architect Agent with expertise in system design,
scalability analysis, integration planning, and technology selection.
"""

import autogen
from typing import Dict, Any, List, Optional
import logging
from datetime import datetime


class SystemArchitectAgent(autogen.AssistantAgent):
    """System Architect Agent specializing in system design and architecture decisions
    
    This agent provides expertise in:
    - System design and architecture patterns
    - Scalability analysis and performance planning
    - Technology selection and integration strategies
    - Infrastructure design and deployment planning
    - API design and service architecture
    
    Academic Note: Demonstrates specialized agent coordination within
    ConsultingAI's multi-agent system for SoM framework evaluation.
    """
    
    def __init__(
        self,
        name: str = "system_architect",
        specialization_focus: str = "distributed_systems",
        confidence_threshold: float = 0.80,
        **kwargs
    ):
        """Initialize System Architect Agent
        
        Args:
            name: Agent name for identification
            specialization_focus: Primary area of architecture expertise
            confidence_threshold: Minimum confidence for autonomous decisions
            **kwargs: Additional AssistantAgent parameters
        """
        
        # Configure system message for architecture expertise
        system_message = self._get_architecture_system_message(specialization_focus)
        
        # Configure default AssistantAgent settings
        default_kwargs = {
            "llm_config": False,  # No LLM for academic demonstration
            "max_consecutive_auto_reply": 2,
            "human_input_mode": "NEVER"
        }
        
        # Merge provided kwargs with defaults
        final_kwargs = {**default_kwargs, **kwargs}
        
        # Initialize parent AssistantAgent
        super().__init__(name=name, system_message=system_message, **final_kwargs)
        
        # Configure agent capabilities and specialization
        self.specialization_focus = specialization_focus
        self.confidence_threshold = confidence_threshold
        self.capabilities = [
            "system_design",
            "scalability_analysis", 
            "integration_planning",
            "technology_selection",
            "api_design",
            "infrastructure_planning"
        ]
        
        # Initialize architecture review history
        self.architecture_history: List[Dict[str, Any]] = []
        
        # Setup logging for academic evaluation
        self.logger = logging.getLogger(f"ConsultingAI.agents.{name}")
        
        self.logger.info(
            "System Architect Agent initialized",
            extra={
                "agent_type": "SystemArchitectAgent",
                "specialization_focus": specialization_focus,
                "capabilities": self.capabilities,
                "confidence_threshold": confidence_threshold,
                "academic_context": "Epic 1 Story 1.3 - Agent Specialization"
            }
        )
    
    def _get_architecture_system_message(self, specialization: str) -> str:
        """Generate system message for architecture expertise
        
        Args:
            specialization: Area of specialization focus
            
        Returns:
            System message defining architecture role and expertise
        """
        return f"""You are a System Architect Agent specializing in {specialization} at ConsultingAI Digital Advisory Firm.

Your expertise includes:
- System design and architecture pattern selection
- Scalability analysis and performance optimization strategies
- Technology stack evaluation and selection
- Integration planning and service communication design
- API design and microservices architecture
- Infrastructure planning and deployment strategies

Your communication style is:
- Strategic and high-level thinking with concrete implementation guidance
- Focused on long-term maintainability and scalability
- Risk-aware with emphasis on proven patterns and best practices
- Collaborative with consideration for business and technical constraints

When analyzing system design decisions, provide:
1. Clear architectural recommendations with trade-off analysis
2. Scalability and performance considerations
3. Integration and maintenance implications
4. Technology selection rationale
5. Confidence level in your recommendations (0.0 to 1.0)

Always maintain professional consulting standards and collaborate effectively with Code Reviewer and Business Analyst colleagues."""
    
    def analyze_system_architecture(
        self, 
        architecture_context: Dict[str, Any],
        analysis_criteria: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Analyze system architecture and provide design recommendations
        
        Args:
            architecture_context: Context about the system being designed
            analysis_criteria: Specific criteria to focus on during analysis
            
        Returns:
            Architecture analysis with recommendations and confidence
        """
        analysis_id = self._generate_analysis_id()
        
        # Default analysis criteria if not specified
        if analysis_criteria is None:
            analysis_criteria = [
                "scalability",
                "maintainability",
                "performance",
                "security",
                "integration"
            ]
        
        # Perform architecture analysis
        analysis_results = self._perform_architecture_analysis(architecture_context, analysis_criteria)
        
        # Calculate confidence based on analysis complexity and clarity
        confidence = self._calculate_architecture_confidence(architecture_context, analysis_results)
        
        # Generate architectural recommendations
        recommendations = self._generate_architecture_recommendations(analysis_results, architecture_context)
        
        # Create comprehensive analysis result
        architecture_result = {
            "analysis_id": analysis_id,
            "timestamp": datetime.now().isoformat(),
            "agent": self.name,
            "architecture_context": architecture_context,
            "analysis_criteria": analysis_criteria,
            "analysis_results": analysis_results,
            "recommendations": recommendations,
            "confidence": confidence,
            "technology_stack": self._suggest_technology_stack(architecture_context),
            "scalability_plan": self._create_scalability_plan(analysis_results),
            "risk_assessment": self._assess_architecture_risks(analysis_results),
            "implementation_phases": self._suggest_implementation_phases(recommendations)
        }
        
        # Log analysis for academic evaluation
        self.logger.info(
            "System architecture analysis completed",
            extra={
                "architecture_result": architecture_result,
                "academic_demonstration": "system_architecture_capabilities"
            }
        )
        
        # Store in architecture history
        self.architecture_history.append(architecture_result)
        
        return architecture_result
    
    def _perform_architecture_analysis(
        self, 
        context: Dict[str, Any], 
        criteria: List[str]
    ) -> Dict[str, Any]:
        """Perform detailed architecture analysis based on criteria
        
        Args:
            context: Context about the system being analyzed
            criteria: List of analysis criteria to evaluate
            
        Returns:
            Analysis results for each criterion
        """
        system_type = context.get("type", "web_application")
        scale = context.get("expected_scale", "medium")
        complexity = context.get("complexity", "medium")
        
        analysis = {}
        
        for criterion in criteria:
            if criterion == "scalability":
                if scale == "high":
                    analysis[criterion] = {
                        "score": 0.7,
                        "concerns": ["Database bottlenecks", "Service coordination complexity"],
                        "recommendations": ["Microservices architecture", "Database sharding", "Caching layers"]
                    }
                elif scale == "low":
                    analysis[criterion] = {
                        "score": 0.9,
                        "concerns": ["Over-engineering risk"],
                        "recommendations": ["Monolithic architecture", "Simple deployment"]
                    }
                else:  # medium
                    analysis[criterion] = {
                        "score": 0.8,
                        "concerns": ["Future growth planning"],
                        "recommendations": ["Modular monolith", "API-first design"]
                    }
            
            elif criterion == "maintainability":
                analysis[criterion] = {
                    "score": 0.85,
                    "concerns": ["Code organization", "Documentation requirements"],
                    "recommendations": ["Clear module boundaries", "Comprehensive documentation", "Automated testing"]
                }
            
            elif criterion == "performance":
                if system_type == "real_time":
                    analysis[criterion] = {
                        "score": 0.75,
                        "concerns": ["Latency requirements", "Concurrent user load"],
                        "recommendations": ["In-memory caching", "CDN integration", "Load balancing"]
                    }
                else:
                    analysis[criterion] = {
                        "score": 0.85,
                        "concerns": ["Database query optimization"],
                        "recommendations": ["Database indexing", "Query optimization", "Caching strategy"]
                    }
            
            elif criterion == "security":
                analysis[criterion] = {
                    "score": 0.8,
                    "concerns": ["Authentication and authorization", "Data protection"],
                    "recommendations": ["OAuth2/JWT implementation", "HTTPS everywhere", "Input validation"]
                }
            
            elif criterion == "integration":
                analysis[criterion] = {
                    "score": 0.8,
                    "concerns": ["API versioning", "Third-party dependencies"],
                    "recommendations": ["RESTful API design", "API versioning strategy", "Circuit breakers"]
                }
        
        return analysis
    
    def _calculate_architecture_confidence(
        self, 
        context: Dict[str, Any], 
        analysis: Dict[str, Any]
    ) -> float:
        """Calculate confidence level for architecture analysis
        
        Args:
            context: Context about the system being analyzed
            analysis: Analysis results from architecture review
            
        Returns:
            Confidence level (0.0 to 1.0)
        """
        # Base confidence for system architecture decisions
        base_confidence = 0.75
        
        # Adjust based on system complexity
        complexity = context.get("complexity", "medium")
        if complexity == "low":
            complexity_adjustment = 0.1
        elif complexity == "high":
            complexity_adjustment = -0.15
        else:
            complexity_adjustment = 0.0
        
        # Adjust based on requirements clarity
        requirements_clarity = context.get("requirements_clarity", "medium")
        if requirements_clarity == "high":
            clarity_adjustment = 0.1
        elif requirements_clarity == "low":
            clarity_adjustment = -0.1
        else:
            clarity_adjustment = 0.0
        
        # Adjust based on analysis consistency
        scores = [result.get("score", 0.5) for result in analysis.values()]
        if scores:
            avg_score = sum(scores) / len(scores)
            if avg_score > 0.8:
                consistency_adjustment = 0.05
            elif avg_score < 0.7:
                consistency_adjustment = -0.05
            else:
                consistency_adjustment = 0.0
        else:
            consistency_adjustment = 0.0
        
        # Calculate final confidence
        confidence = base_confidence + complexity_adjustment + clarity_adjustment + consistency_adjustment
        
        # Ensure confidence is within valid range
        return max(0.0, min(1.0, confidence))
    
    def _generate_architecture_recommendations(
        self, 
        analysis: Dict[str, Any], 
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate actionable architecture recommendations
        
        Args:
            analysis: Analysis results from architecture review
            context: System context for targeted recommendations
            
        Returns:
            List of prioritized architecture recommendations
        """
        recommendations = []
        
        for criterion, result in analysis.items():
            score = result.get("score", 0.5)
            concerns = result.get("concerns", [])
            criterion_recommendations = result.get("recommendations", [])
            
            if score < 0.8:  # Areas needing architectural attention
                priority = "high" if score < 0.7 else "medium"
                
                for i, rec in enumerate(criterion_recommendations):
                    recommendations.append({
                        "category": criterion,
                        "recommendation": rec,
                        "priority": priority,
                        "rationale": concerns[i] if i < len(concerns) else f"Improve {criterion} aspects",
                        "impact": "high" if priority == "high" else "medium",
                        "implementation_effort": self._estimate_implementation_effort(rec),
                        "dependencies": self._identify_dependencies(rec, context)
                    })
        
        # Sort by priority and impact
        recommendations.sort(key=lambda x: (
            0 if x["priority"] == "high" else 1,
            0 if x["impact"] == "high" else 1
        ))
        
        return recommendations
    
    def _estimate_implementation_effort(self, recommendation: str) -> str:
        """Estimate implementation effort for a recommendation
        
        Args:
            recommendation: Architecture recommendation
            
        Returns:
            Effort estimate (low, medium, high)
        """
        high_effort_keywords = ["microservices", "sharding", "migration", "refactor"]
        medium_effort_keywords = ["caching", "load balancing", "api design"]
        
        rec_lower = recommendation.lower()
        
        if any(keyword in rec_lower for keyword in high_effort_keywords):
            return "high"
        elif any(keyword in rec_lower for keyword in medium_effort_keywords):
            return "medium"
        else:
            return "low"
    
    def _identify_dependencies(self, recommendation: str, context: Dict[str, Any]) -> List[str]:
        """Identify dependencies for implementing a recommendation
        
        Args:
            recommendation: Architecture recommendation
            context: System context
            
        Returns:
            List of dependencies
        """
        dependencies = []
        rec_lower = recommendation.lower()
        
        if "microservices" in rec_lower:
            dependencies.extend(["Service discovery", "API gateway", "Container orchestration"])
        elif "caching" in rec_lower:
            dependencies.extend(["Cache infrastructure", "Cache invalidation strategy"])
        elif "database" in rec_lower:
            dependencies.extend(["Database design review", "Migration planning"])
        elif "api" in rec_lower:
            dependencies.extend(["API documentation", "Versioning strategy"])
        
        return dependencies
    
    def _suggest_technology_stack(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Suggest appropriate technology stack based on context
        
        Args:
            context: System context and requirements
            
        Returns:
            Suggested technology stack
        """
        system_type = context.get("type", "web_application")
        scale = context.get("expected_scale", "medium")
        
        # Base technology suggestions
        tech_stack = {
            "backend_framework": "FastAPI" if system_type == "api" else "Django",
            "database": "PostgreSQL",
            "caching": "Redis",
            "web_server": "Nginx",
            "deployment": "Docker + Kubernetes" if scale == "high" else "Docker + Cloud Platform"
        }
        
        # Adjust based on scale and type
        if scale == "high":
            tech_stack.update({
                "message_queue": "RabbitMQ",
                "monitoring": "Prometheus + Grafana",
                "load_balancer": "AWS ALB / GCP Load Balancer"
            })
        
        if system_type == "real_time":
            tech_stack.update({
                "websockets": "Socket.IO",
                "streaming": "Apache Kafka"
            })
        
        return tech_stack
    
    def _create_scalability_plan(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Create scalability plan based on analysis
        
        Args:
            analysis: Architecture analysis results
            
        Returns:
            Scalability plan with phases and metrics
        """
        scalability_analysis = analysis.get("scalability", {})
        score = scalability_analysis.get("score", 0.5)
        
        if score > 0.8:
            plan = {
                "current_state": "Well-positioned for growth",
                "immediate_actions": ["Monitor performance metrics", "Establish baselines"],
                "growth_phases": {
                    "phase_1": "Optimize current architecture",
                    "phase_2": "Horizontal scaling preparation",
                    "phase_3": "Advanced scaling strategies"
                }
            }
        else:
            plan = {
                "current_state": "Requires scalability improvements",
                "immediate_actions": ["Address bottlenecks", "Implement monitoring"],
                "growth_phases": {
                    "phase_1": "Fix current limitations",
                    "phase_2": "Implement scalable patterns",
                    "phase_3": "Advanced distributed architecture"
                }
            }
        
        return plan
    
    def _assess_architecture_risks(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Assess architecture risks based on analysis
        
        Args:
            analysis: Architecture analysis results
            
        Returns:
            Risk assessment with mitigation strategies
        """
        risks = {
            "technical_risk": "low",
            "scalability_risk": "low",
            "maintainability_risk": "low",
            "integration_risk": "low"
        }
        
        # Assess risks based on analysis scores
        for criterion, result in analysis.items():
            score = result.get("score", 0.5)
            
            if criterion == "scalability" and score < 0.7:
                risks["scalability_risk"] = "high" if score < 0.6 else "medium"
            elif criterion == "maintainability" and score < 0.7:
                risks["maintainability_risk"] = "high" if score < 0.6 else "medium"
            elif criterion == "integration" and score < 0.7:
                risks["integration_risk"] = "high" if score < 0.6 else "medium"
        
        # Overall technical risk
        low_scores = sum(1 for result in analysis.values() if result.get("score", 0.5) < 0.7)
        if low_scores >= 2:
            risks["technical_risk"] = "high"
        elif low_scores == 1:
            risks["technical_risk"] = "medium"
        
        return risks
    
    def _suggest_implementation_phases(self, recommendations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Suggest implementation phases for recommendations
        
        Args:
            recommendations: List of architecture recommendations
            
        Returns:
            Phased implementation plan
        """
        if not recommendations:
            return [{"phase": "maintenance", "description": "Monitor and maintain current architecture"}]
        
        # Group recommendations by priority and effort
        high_priority = [r for r in recommendations if r.get("priority") == "high"]
        medium_priority = [r for r in recommendations if r.get("priority") == "medium"]
        
        phases = []
        
        if high_priority:
            phases.append({
                "phase": "immediate",
                "duration": "1-2 months",
                "focus": "Critical architecture improvements",
                "recommendations": high_priority[:3]  # Limit to top 3 for focus
            })
        
        if medium_priority:
            phases.append({
                "phase": "short_term",
                "duration": "3-6 months", 
                "focus": "Architecture optimization and enhancement",
                "recommendations": medium_priority[:3]
            })
        
        phases.append({
            "phase": "long_term",
            "duration": "6+ months",
            "focus": "Continuous improvement and advanced optimizations",
            "recommendations": "Ongoing monitoring and refinement"
        })
        
        return phases
    
    def _generate_analysis_id(self) -> str:
        """Generate unique analysis ID
        
        Returns:
            Unique analysis identifier
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        return f"arch_analysis_{timestamp}"
    
    def get_agent_capabilities(self) -> Dict[str, Any]:
        """Get agent capabilities and configuration for coordination
        
        Returns:
            Agent capabilities and configuration information
        """
        return {
            "agent_type": "SystemArchitectAgent",
            "name": self.name,
            "specialization_focus": self.specialization_focus,
            "capabilities": self.capabilities,
            "confidence_threshold": self.confidence_threshold,
            "analysis_history_count": len(self.analysis_history),
            "average_confidence": self._calculate_average_confidence(),
            "status": "active"
        }

    def _calculate_average_confidence(self) -> float:
        """Calculate average confidence from architecture history
        
        Returns:
            Average confidence level across all analyses
        """
        if not self.architecture_history:
            return 0.0
        
        confidences = [analysis.get("confidence", 0.0) for analysis in self.architecture_history]
        return sum(confidences) / len(confidences)


def create_system_architect_agent(**kwargs) -> SystemArchitectAgent:
    """Factory function to create System Architect Agent
    
    Args:
        **kwargs: Configuration parameters for the agent
        
    Returns:
        Configured SystemArchitectAgent instance
    """
    return SystemArchitectAgent(**kwargs)


def demonstrate_system_architect() -> bool:
    """Demonstrate System Architect Agent functionality for academic evaluation
    
    Returns:
        True if demonstration successful, False otherwise
    """
    print("🔧 Demonstrating System Architect Agent functionality...")
    
    try:
        # Create System Architect Agent
        architect = create_system_architect_agent(
            name="demo_system_architect",
            specialization_focus="distributed_systems"
        )
        
        print("  ✅ System Architect Agent created successfully")
        
        # Demonstrate architecture analysis
        architecture_context = {
            "type": "web_application",
            "description": "E-commerce platform with microservices architecture",
            "expected_scale": "high",
            "complexity": "high",
            "requirements_clarity": "medium"
        }
        
        analysis_result = architect.analyze_system_architecture(
            architecture_context,
            ["scalability", "maintainability", "performance", "integration"]
        )
        
        print(f"  ✅ Architecture analysis completed: Analysis ID {analysis_result['analysis_id']}")
        print(f"     Confidence: {analysis_result['confidence']:.1%}")
        print(f"     Recommendations: {len(analysis_result['recommendations'])} items")
        print(f"     Technology stack suggestions: {len(analysis_result['technology_stack'])} components")
        
        # Demonstrate agent capabilities
        capabilities = architect.get_agent_capabilities()
        print(f"  ✅ Agent capabilities: {len(capabilities['capabilities'])} core capabilities")
        
        return True
        
    except Exception as e:
        print(f"  ❌ System Architect Agent demonstration failed: {e}")
        return False


if __name__ == "__main__":
    print("🚀 Starting SystemArchitectAgent demonstration...")
    
    success = demonstrate_system_architect()
    if success:
        print("\n✅ System Architect Agent: DEMONSTRATED")
    else:
        print("\n❌ System Architect Agent: FAILED")
        exit(1)
