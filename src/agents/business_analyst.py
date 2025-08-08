"""Business Analyst Agent - Simplified Version"""

import autogen
from typing import Dict, Any, List
import logging
from datetime import datetime

# Import LLM configuration
from config.free_llm_config import OLLAMA_CONFIG


class BusinessAnalystAgent(autogen.AssistantAgent):
    """Business Analyst Agent specializing in requirements and stakeholder analysis"""
    
    def __init__(self, name: str = "business_analyst", llm_config: Dict[str, Any] = None, **kwargs):
        """Initialize Business Analyst Agent with LLM support
        
        Args:
            name: Agent name for identification
            llm_config: LLM configuration for AI-powered business analysis
            **kwargs: Additional AssistantAgent parameters
        """
        
        # Configure LLM for business analysis
        if llm_config is None:
            llm_config = OLLAMA_CONFIG
            
        system_message = """You are a Business Analyst Agent at ConsultingAI Digital Advisory Firm.
        
Your expertise includes:
- Requirements gathering and analysis
- Stakeholder needs assessment
- Business impact evaluation
- Process optimization recommendations
- Risk and compliance analysis"""
        
        super().__init__(
            name=name,
            system_message=system_message,
            llm_config=llm_config,  # Enable LLM for business analysis
            human_input_mode="NEVER",
            **kwargs
        )
        
        self.capabilities = [
            "requirements_analysis",
            "stakeholder_assessment",
            "business_impact_evaluation",
            "process_optimization",
            "risk_analysis",
            "compliance_review"
        ]
        
        self.analysis_history = []
        self.logger = logging.getLogger(f"ConsultingAI.agents.{name}")
        
        print(f"✅ {name} created successfully with LLM support")
    
    def analyze_business_requirements(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze business requirements and stakeholder needs"""
        
        analysis_id = f"biz_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Mock business analysis results
        result = {
            "analysis_id": analysis_id,
            "timestamp": datetime.now().isoformat(),
            "agent": self.name,
            "context": context,
            "confidence": 0.85,
            "stakeholder_analysis": {
                "primary_stakeholders": ["Product Manager", "Development Team", "End Users"],
                "requirements_clarity": "high",
                "alignment_score": 0.9
            },
            "business_impact": {
                "revenue_impact": "medium",
                "cost_reduction": "high", 
                "risk_level": "low",
                "roi_estimate": "6 months"
            },
            "recommendations": [
                {"category": "requirements", "recommendation": "Prioritize user authentication features", "priority": "high"},
                {"category": "process", "recommendation": "Implement agile development methodology", "priority": "medium"},
                {"category": "risk", "recommendation": "Regular stakeholder check-ins", "priority": "medium"}
            ],
            "next_steps": [
                "Conduct user interviews",
                "Create detailed user stories", 
                "Establish success metrics"
            ]
        }
        
        self.analysis_history.append(result)
        return result
    
    def get_agent_capabilities(self) -> Dict[str, Any]:
        """Get agent capabilities"""
        return {
            "agent_type": "BusinessAnalystAgent",
            "name": self.name,
            "capabilities": self.capabilities,
            "total_analyses": len(self.analysis_history)
        }


def create_business_analyst_agent(**kwargs):
    """Factory function"""
    return BusinessAnalystAgent(**kwargs)


def demonstrate_business_analyst():
    """Demonstration function"""
    print("🔧 Demonstrating Business Analyst Agent functionality...")
    
    try:
        # Create agent
        analyst = create_business_analyst_agent(name="demo_business_analyst")
        
        # Test analysis
        context = {
            "project": "customer_portal",
            "stakeholders": ["customers", "support_team", "management"],
            "timeline": "3 months",
            "budget": "medium"
        }
        
        result = analyst.analyze_business_requirements(context)
        
        print(f"  ✅ Business analysis completed: {result['analysis_id']}")
        print(f"     Confidence: {result['confidence']:.1%}")
        print(f"     Stakeholder alignment: {result['stakeholder_analysis']['alignment_score']:.1%}")
        print(f"     Recommendations: {len(result['recommendations'])} items")
        print(f"     ROI estimate: {result['business_impact']['roi_estimate']}")
        
        # Test capabilities
        capabilities = analyst.get_agent_capabilities()
        print(f"  ✅ Agent capabilities: {len(capabilities['capabilities'])} core capabilities")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Business Analyst demonstration failed: {e}")
        return False


if __name__ == "__main__":
    print("🚀 Starting BusinessAnalystAgent demonstration...")
    
    success = demonstrate_business_analyst()
    if success:
        print("\n✅ Business Analyst Agent: DEMONSTRATED")
    else:
        print("\n❌ Business Analyst Agent: FAILED")
        exit(1)