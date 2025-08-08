"""Code Reviewer Agent - Specialized Agent for Code Quality Analysis

This module implements the Code Reviewer Agent with expertise in code quality,
performance optimization, security review, and best practices enforcement.
"""

import autogen
from typing import Dict, Any, List, Optional
import logging
from datetime import datetime

# Import LLM configuration
from config.free_llm_config import OLLAMA_CONFIG


class CodeReviewerAgent(autogen.AssistantAgent):
    """Code Reviewer Agent specializing in code quality and technical review
    
    This agent provides expertise in:
    - Code quality analysis and improvement recommendations
    - Performance optimization suggestions
    - Security vulnerability identification
    - Best practices enforcement
    - Testing strategy recommendations
    
    Academic Note: Demonstrates specialized agent coordination within
    ConsultingAI's multi-agent system for SoM framework evaluation.
    """
    
    def __init__(
        self,
        name: str = "code_reviewer",
        specialization_focus: str = "python_development",
        confidence_threshold: float = 0.85,
        llm_config: Optional[Dict[str, Any]] = None,
        **kwargs
    ):
        """Initialize Code Reviewer Agent
        
        Args:
            name: Agent name for identification
            specialization_focus: Primary area of code review expertise
            confidence_threshold: Minimum confidence for autonomous decisions
            llm_config: LLM configuration for AI-powered analysis
            **kwargs: Additional AssistantAgent parameters
        """
        
        # Configure LLM for code analysis
        if llm_config is None:
            llm_config = OLLAMA_CONFIG
        
        # Configure system message for code review expertise
        system_message = self._get_code_review_system_message(specialization_focus)
        
        # Configure default AssistantAgent settings
        default_kwargs = {
            "llm_config": llm_config,  # Enable LLM for code analysis
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
            "code_quality_analysis",
            "performance_optimization", 
            "security_review",
            "best_practices_enforcement",
            "testing_strategy",
            "code_documentation_review"
        ]
        
        # Initialize review history for learning
        self.review_history: List[Dict[str, Any]] = []
        
        # Setup logging for academic evaluation
        self.logger = logging.getLogger(f"ConsultingAI.agents.{name}")
        
        self.logger.info(
            "Code Reviewer Agent initialized",
            extra={
                "agent_type": "CodeReviewerAgent",
                "specialization_focus": specialization_focus,
                "capabilities": self.capabilities,
                "confidence_threshold": confidence_threshold,
                "academic_context": "Epic 1 Story 1.3 - Agent Specialization"
            }
        )
    
    def _get_code_review_system_message(self, specialization: str) -> str:
        """Generate system message for code review expertise
        
        Args:
            specialization: Area of specialization focus
            
        Returns:
            System message defining code review role and expertise
        """
        return f"""You are a Code Reviewer Agent specializing in {specialization} at ConsultingAI Digital Advisory Firm.

Your expertise includes:
- Code quality analysis and improvement recommendations
- Performance optimization and efficiency suggestions
- Security vulnerability identification and mitigation
- Best practices enforcement and standards compliance
- Testing strategy and quality assurance recommendations
- Code documentation and maintainability review

Your communication style is:
- Technical and detail-oriented
- Focused on concrete, actionable recommendations
- Evidence-based with specific examples
- Constructive and solution-oriented

When analyzing code or technical decisions, provide:
1. Clear assessment of code quality and potential issues
2. Specific recommendations for improvement
3. Risk assessment for proposed changes
4. Confidence level in your recommendations (0.0 to 1.0)

Always maintain professional consulting standards and collaborate effectively with System Architect and Business Analyst colleagues."""
    
    def analyze_code_quality(
        self, 
        code_context: Dict[str, Any],
        review_criteria: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Analyze code quality and provide recommendations
        
        Args:
            code_context: Context about the code being reviewed
            review_criteria: Specific criteria to focus on during review
            
        Returns:
            Code review analysis with recommendations and confidence
        """
        review_id = self._generate_review_id()
        
        # Default review criteria if not specified
        if review_criteria is None:
            review_criteria = [
                "code_quality",
                "performance",
                "security", 
                "maintainability",
                "testing"
            ]
        
        # Perform mock code analysis (in real implementation, would analyze actual code)
        analysis_results = self._perform_code_analysis(code_context, review_criteria)
        
        # Calculate overall confidence based on analysis complexity
        confidence = self._calculate_review_confidence(code_context, analysis_results)
        
        # Generate recommendations
        recommendations = self._generate_code_recommendations(analysis_results)
        
        # Create comprehensive review result
        review_result = {
            "review_id": review_id,
            "timestamp": datetime.now().isoformat(),
            "agent": self.name,
            "code_context": code_context,
            "review_criteria": review_criteria,
            "analysis_results": analysis_results,
            "recommendations": recommendations,
            "confidence": confidence,
            "risk_assessment": self._assess_code_risks(analysis_results),
            "next_steps": self._suggest_next_steps(recommendations)
        }
        
        # Log review for academic evaluation
        self.logger.info(
            "Code review analysis completed",
            extra={
                "review_result": review_result,
                "academic_demonstration": "code_review_capabilities"
            }
        )
        
        # Store in review history
        self.review_history.append(review_result)
        
        return review_result
    
    def _perform_code_analysis(
        self, 
        code_context: Dict[str, Any], 
        criteria: List[str]
    ) -> Dict[str, Any]:
        """Perform detailed code analysis based on criteria
        
        Args:
            code_context: Context about the code being analyzed
            criteria: List of analysis criteria to evaluate
            
        Returns:
            Analysis results for each criterion
        """
        # Mock analysis results for academic demonstration
        # In real implementation, would perform actual code analysis
        
        code_type = code_context.get("type", "general")
        complexity = code_context.get("complexity", "medium")
        
        analysis = {}
        
        for criterion in criteria:
            if criterion == "code_quality":
                if complexity == "low":
                    analysis[criterion] = {
                        "score": 0.9,
                        "issues": ["Minor style inconsistencies"],
                        "strengths": ["Clear logic flow", "Good variable naming"]
                    }
                elif complexity == "high":
                    analysis[criterion] = {
                        "score": 0.7,
                        "issues": ["Complex logic needs refactoring", "Long functions"],
                        "strengths": ["Comprehensive error handling"]
                    }
                else:  # medium
                    analysis[criterion] = {
                        "score": 0.8,
                        "issues": ["Some functions could be smaller"],
                        "strengths": ["Good structure", "Clear comments"]
                    }
            
            elif criterion == "performance":
                analysis[criterion] = {
                    "score": 0.85,
                    "issues": ["Potential optimization in loops"],
                    "strengths": ["Efficient algorithms", "Good memory usage"]
                }
            
            elif criterion == "security":
                analysis[criterion] = {
                    "score": 0.9,
                    "issues": ["Input validation could be enhanced"],
                    "strengths": ["No obvious vulnerabilities", "Secure defaults"]
                }
            
            elif criterion == "maintainability":
                analysis[criterion] = {
                    "score": 0.85,
                    "issues": ["Documentation could be expanded"],
                    "strengths": ["Modular design", "Clear interfaces"]
                }
            
            elif criterion == "testing":
                analysis[criterion] = {
                    "score": 0.8,
                    "issues": ["Edge case coverage needed"],
                    "strengths": ["Good unit test coverage", "Clear test structure"]
                }
        
        return analysis
    
    def _calculate_review_confidence(
        self, 
        code_context: Dict[str, Any], 
        analysis: Dict[str, Any]
    ) -> float:
        """Calculate confidence level for code review
        
        Args:
            code_context: Context about the code being reviewed
            analysis: Analysis results from code review
            
        Returns:
            Confidence level (0.0 to 1.0)
        """
        # Base confidence on analysis clarity and context completeness
        base_confidence = 0.8
        
        # Adjust based on code complexity
        complexity = code_context.get("complexity", "medium")
        if complexity == "low":
            complexity_adjustment = 0.1
        elif complexity == "high":
            complexity_adjustment = -0.1
        else:
            complexity_adjustment = 0.0
        
        # Adjust based on analysis consistency
        scores = [result.get("score", 0.5) for result in analysis.values()]
        if scores:
            score_variance = self._calculate_variance(scores)
            if score_variance < 0.05:  # Consistent scores
                consistency_adjustment = 0.05
            else:
                consistency_adjustment = -0.05
        else:
            consistency_adjustment = 0.0
        
        # Calculate final confidence
        confidence = base_confidence + complexity_adjustment + consistency_adjustment
        
        # Ensure confidence is within valid range
        return max(0.0, min(1.0, confidence))
    
    def _calculate_variance(self, scores: List[float]) -> float:
        """Calculate variance of scores for consistency assessment
        
        Args:
            scores: List of numerical scores
            
        Returns:
            Variance of the scores
        """
        if len(scores) < 2:
            return 0.0
        
        mean = sum(scores) / len(scores)
        variance = sum((score - mean) ** 2 for score in scores) / len(scores)
        return variance
    
    def _generate_code_recommendations(self, analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate actionable recommendations based on analysis
        
        Args:
            analysis: Analysis results from code review
            
        Returns:
            List of recommendations with priorities and actions
        """
        recommendations = []
        
        for criterion, result in analysis.items():
            score = result.get("score", 0.5)
            issues = result.get("issues", [])
            
            if score < 0.8:  # Areas needing improvement
                for issue in issues:
                    priority = "high" if score < 0.7 else "medium"
                    recommendations.append({
                        "category": criterion,
                        "issue": issue,
                        "priority": priority,
                        "action": self._suggest_action_for_issue(criterion, issue),
                        "impact": "high" if priority == "high" else "medium"
                    })
        
        return recommendations
    
    def _suggest_action_for_issue(self, category: str, issue: str) -> str:
        """Suggest specific actions for identified issues
        
        Args:
            category: Category of the issue (code_quality, performance, etc.)
            issue: Specific issue description
            
        Returns:
            Suggested action to address the issue
        """
        action_mapping = {
            "code_quality": {
                "style": "Apply automated code formatting and linting",
                "complex": "Refactor complex functions into smaller components",
                "naming": "Improve variable and function naming conventions"
            },
            "performance": {
                "optimization": "Profile code and optimize bottlenecks",
                "loops": "Consider list comprehensions or vectorized operations",
                "memory": "Implement memory-efficient data structures"
            },
            "security": {
                "validation": "Implement comprehensive input validation",
                "authentication": "Enhance authentication and authorization",
                "encryption": "Add encryption for sensitive data"
            },
            "maintainability": {
                "documentation": "Add comprehensive code documentation",
                "modular": "Improve modular design and separation of concerns",
                "complexity": "Reduce cyclomatic complexity"
            },
            "testing": {
                "coverage": "Increase test coverage for edge cases",
                "structure": "Improve test organization and clarity",
                "integration": "Add integration and end-to-end tests"
            }
        }
        
        # Find matching action based on keywords in issue
        for keyword, action in action_mapping.get(category, {}).items():
            if keyword.lower() in issue.lower():
                return action
        
        # Default action if no specific match
        return f"Address {issue} in {category} category"
    
    def _assess_code_risks(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Assess risks based on code analysis results
        
        Args:
            analysis: Analysis results from code review
            
        Returns:
            Risk assessment with levels and mitigation strategies
        """
        risks = {
            "technical_risk": "low",
            "security_risk": "low", 
            "maintainability_risk": "low",
            "performance_risk": "low"
        }
        
        # Assess risks based on analysis scores
        for criterion, result in analysis.items():
            score = result.get("score", 0.5)
            
            if criterion == "security" and score < 0.8:
                risks["security_risk"] = "high" if score < 0.6 else "medium"
            elif criterion in ["code_quality", "maintainability"] and score < 0.7:
                risks["maintainability_risk"] = "high" if score < 0.6 else "medium"
            elif criterion == "performance" and score < 0.7:
                risks["performance_risk"] = "high" if score < 0.6 else "medium"
        
        # Overall technical risk based on multiple factors
        low_scores = sum(1 for result in analysis.values() if result.get("score", 0.5) < 0.7)
        if low_scores >= 2:
            risks["technical_risk"] = "high"
        elif low_scores == 1:
            risks["technical_risk"] = "medium"
        
        return risks
    
    def _suggest_next_steps(self, recommendations: List[Dict[str, Any]]) -> List[str]:
        """Suggest prioritized next steps based on recommendations
        
        Args:
            recommendations: List of recommendations from code review
            
        Returns:
            Prioritized list of next steps
        """
        if not recommendations:
            return ["Code review complete - no immediate actions required"]
        
        # Group recommendations by priority
        high_priority = [r for r in recommendations if r.get("priority") == "high"]
        medium_priority = [r for r in recommendations if r.get("priority") == "medium"]
        
        next_steps = []
        
        if high_priority:
            next_steps.append(f"Immediate action: Address {len(high_priority)} high-priority issues")
            for rec in high_priority[:2]:  # Limit to top 2 for clarity
                next_steps.append(f"• {rec['action']}")
        
        if medium_priority:
            next_steps.append(f"Follow-up: Address {len(medium_priority)} medium-priority improvements")
        
        next_steps.append("Schedule follow-up code review after implementation")
        
        return next_steps
    
    def _generate_review_id(self) -> str:
        """Generate unique review ID
        
        Returns:
            Unique review identifier
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        return f"code_review_{timestamp}"
    
    def get_agent_capabilities(self) -> Dict[str, Any]:
        """Get agent capabilities and configuration for coordination
        
        Returns:
            Agent capabilities and configuration information
        """
        return {
            "agent_type": "CodeReviewerAgent",
            "name": self.name,
            "specialization_focus": self.specialization_focus,
            "capabilities": self.capabilities,
            "confidence_threshold": self.confidence_threshold,
            "total_reviews": len(self.review_history),
            "average_confidence": self._calculate_average_confidence()
        }
    
    def _calculate_average_confidence(self) -> float:
        """Calculate average confidence from review history
        
        Returns:
            Average confidence level across all reviews
        """
        if not self.review_history:
            return 0.0
        
        confidences = [review.get("confidence", 0.0) for review in self.review_history]
        return sum(confidences) / len(confidences)


def create_code_reviewer_agent(**kwargs) -> CodeReviewerAgent:
    """Factory function to create Code Reviewer Agent
    
    Args:
        **kwargs: Configuration parameters for the agent
        
    Returns:
        Configured CodeReviewerAgent instance
    """
    return CodeReviewerAgent(**kwargs)


def demonstrate_code_reviewer() -> bool:
    """Demonstrate Code Reviewer Agent functionality for academic evaluation
    
    Returns:
        True if demonstration successful, False otherwise
    """
    print("🔧 Demonstrating Code Reviewer Agent functionality...")
    
    try:
        # Create Code Reviewer Agent
        code_reviewer = create_code_reviewer_agent(
            name="demo_code_reviewer",
            specialization_focus="python_development"
        )
        
        print("  ✅ Code Reviewer Agent created successfully")
        
        # Demonstrate code quality analysis
        code_context = {
            "type": "api_endpoint",
            "description": "User authentication endpoint implementation",
            "complexity": "medium",
            "language": "python",
            "lines_of_code": 150
        }
        
        review_result = code_reviewer.analyze_code_quality(
            code_context,
            ["code_quality", "security", "performance"]
        )
        
        print(f"  ✅ Code review completed: Review ID {review_result['review_id']}")
        print(f"     Confidence: {review_result['confidence']:.1%}")
        print(f"     Recommendations: {len(review_result['recommendations'])} items")
        
        # Demonstrate agent capabilities
        capabilities = code_reviewer.get_agent_capabilities()
        print(f"  ✅ Agent capabilities: {len(capabilities['capabilities'])} core capabilities")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Code Reviewer Agent demonstration failed: {e}")
        return False


if __name__ == "__main__":
    print("🚀 Starting CodeReviewerAgent demonstration...")
    
    success = demonstrate_code_reviewer()
    if success:
        print("\n✅ Code Reviewer Agent: DEMONSTRATED")
    else:
        print("\n❌ Code Reviewer Agent: FAILED")
        exit(1)
