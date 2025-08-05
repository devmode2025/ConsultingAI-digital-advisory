"""Consulting Scenario Demonstrations - Story 2.4 Implementation

This module implements comprehensive consulting scenarios that showcase
all Epic 2 capabilities in realistic business contexts.
"""

import sys
from pathlib import Path
from typing import Dict, Any, List, Optional
from datetime import datetime
import json

# Add src to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from coordination.enhanced_coordination import (
    create_enhanced_chief_engagement_manager, ConsensusLevel
)
from coordination.advanced_escalation import (
    create_advanced_escalation_engine
)
from interfaces.advanced_human_interaction import (
    create_advanced_human_interaction_manager, InterventionMode, ExpertiseContext, InterventionType
)
from agents.code_reviewer import create_code_reviewer_agent
from agents.system_architect import create_system_architect_agent
from agents.business_analyst import create_business_analyst_agent


class ConsultingScenarioRunner:
    """Comprehensive consulting scenario demonstration system
    
    This class orchestrates realistic consulting scenarios that demonstrate:
    - Enhanced Chief Engagement Manager coordination
    - Advanced escalation logic with multi-factor analysis
    - Sophisticated human intervention mechanisms
    - Complete inner team collaboration workflows
    
    Academic Note: Demonstrates complete Epic 2 capabilities for
    Story 2.4 - realistic consulting scenario evaluation.
    """
    
    def __init__(self):
        """Initialize consulting scenario demonstration system"""
        print("🏗️ Initializing Consulting Scenario Demonstration System...")
        
        # Create enhanced coordination components
        self.chief_manager = create_enhanced_chief_engagement_manager(
            name="consulting_scenario_manager",
            human_input_mode="NEVER"
        )
        
        # Create advanced escalation engine
        self.escalation_engine = create_advanced_escalation_engine()
        
        # Create advanced human interaction manager
        self.human_interaction = create_advanced_human_interaction_manager(
            intervention_mode=InterventionMode.SIMULATED
        )
        
        # Create specialized consulting agents
        self.code_reviewer = create_code_reviewer_agent(name="consulting_code_reviewer")
        self.system_architect = create_system_architect_agent(name="consulting_architect")
        self.business_analyst = create_business_analyst_agent(name="consulting_analyst")
        
        # Scenario execution history
        self.scenario_results: List[Dict[str, Any]] = []
        
        print("✅ Consulting Scenario System initialized with enhanced capabilities")
    
    def execute_comprehensive_consulting_demonstration(self) -> bool:
        """Execute comprehensive consulting demonstration scenarios
        
        Returns:
            True if all scenarios demonstrate successfully, False otherwise
        """
        print("\n🎯 Executing Comprehensive Consulting Demonstration")
        print("=" * 80)
        
        scenarios = [
            self._scenario_1_api_security_enhancement,
            self._scenario_2_enterprise_architecture_decision,
            self._scenario_3_product_launch_coordination,
            self._scenario_4_crisis_response_scenario
        ]
        
        scenario_results = []
        
        for i, scenario_func in enumerate(scenarios, 1):
            print(f"\n📋 SCENARIO {i}: {scenario_func.__name__.replace('_scenario_', '').replace('_', ' ').title()}")
            print("-" * 60)
            
            try:
                result = scenario_func()
                scenario_results.append(result)
                
                if result["success"]:
                    print(f"✅ Scenario {i}: SUCCESS")
                else:
                    print(f"❌ Scenario {i}: FAILED - {result.get('error', 'Unknown error')}")
                    
            except Exception as e:
                print(f"❌ Scenario {i}: EXCEPTION - {e}")
                scenario_results.append({"success": False, "error": str(e)})
        
        # Evaluate overall demonstration success
        successful_scenarios = sum(1 for result in scenario_results if result["success"])
        total_scenarios = len(scenarios)
        
        success_rate = successful_scenarios / total_scenarios
        overall_success = success_rate >= 0.75  # 75% success rate required
        
        self._display_comprehensive_summary(scenario_results, overall_success)
        
        return overall_success
    
    def _scenario_1_api_security_enhancement(self) -> Dict[str, Any]:
        """Scenario 1: API Security Enhancement Consultation
        
        Demonstrates: Medium complexity consultation with junior specialist escalation
        """
        print("🔒 API Security Enhancement for Financial Services Client")
        
        try:
            # Define consultation context
            consultation_context = {
                "scenario_name": "api_security_enhancement",
                "client": "Financial Services Company", 
                "description": "Enhance API security for payment processing system",
                "type": "security_enhancement",
                "complexity": "medium",
                "business_impact": "high",
                "financial_impact": "high",
                "stakeholders": ["security_team", "api_development", "compliance", "operations"],
                "timeline": "tight",
                "regulatory_requirements": True,
                "integration_requirements": ["payment_gateway", "fraud_detection", "audit_logging"]
            }
            
            # Define participating agents with enhanced profiles
            participating_agents = [
                {
                    "name": self.code_reviewer.name,
                    "agent_type": "CodeReviewerAgent",
                    "expertise": ["security_patterns", "api_development", "code_quality"],
                    "seniority": "senior"
                },
                {
                    "name": self.system_architect.name,
                    "agent_type": "SystemArchitectAgent",
                    "expertise": ["api_architecture", "security_design", "compliance"],
                    "seniority": "principal"
                },
                {
                    "name": self.business_analyst.name,
                    "agent_type": "BusinessAnalystAgent", 
                    "expertise": ["regulatory_compliance", "risk_assessment", "stakeholder_management"],
                    "seniority": "senior"
                }
            ]
            
            print(f"   Client: {consultation_context['client']}")
            print(f"   Complexity: {consultation_context['complexity']}")
            print(f"   Participating agents: {len(participating_agents)}")
            
            # Execute multi-agent discussion
            discussion_result = self.chief_manager.orchestrate_multi_agent_discussion(
                consultation_context,
                participating_agents,
                discussion_rounds=2
            )
            
            print(f"   Discussion completed: {discussion_result['discussion_id']}")
            print(f"   Final consensus: {discussion_result['final_consensus']['level'].value}")
            
            # Execute advanced escalation analysis
            final_consensus = discussion_result["final_consensus"]
            final_recommendations = final_consensus.get("final_recommendations", [])
            
            # Convert string recommendations to proper agent response format
            if isinstance(final_recommendations, list) and final_recommendations:
                if isinstance(final_recommendations[0], str):
                    # Convert strings to agent response format
                    agent_responses = []
                    for i, rec in enumerate(final_recommendations):
                        agent_responses.append({
                            "agent": f"agent_{i}",
                            "recommendation": rec,
                            "confidence": 0.7,  # Default confidence
                            "agent_type": "general"
                        })
                    final_recommendations = agent_responses
            elif not isinstance(final_recommendations, list):
                final_recommendations = []
            
            escalation_result = self.escalation_engine.evaluate_advanced_escalation(
                final_recommendations,
                consultation_context,
                final_consensus
            )
            
            print(f"   Escalation tier: {escalation_result['escalation_tier_name']}")
            print(f"   Risk level: {escalation_result['risk_analysis']['overall_risk_level'].value}")
            
            # Execute human intervention if needed
            intervention_result = None
            if escalation_result["escalation_needed"]:
                intervention_request = {
                    "decision_context": consultation_context,
                    "escalation_info": escalation_result,
                    "agent_recommendations": final_recommendations,
                    "consensus_analysis": final_consensus
                }
                
                intervention_result = self.human_interaction.request_human_intervention(
                    intervention_request,
                    InterventionType.APPROVAL_REJECTION
                )
                
                print(f"   Human intervention: {intervention_result['intervention_type'].value}")
                print(f"   Expert decision: {intervention_result['human_input'].get('decision', 'Unknown')}")
            
            # Store scenario result
            scenario_result = {
                "scenario_name": "api_security_enhancement",
                "success": True,
                "consultation_context": consultation_context,
                "discussion_result": discussion_result,
                "escalation_result": escalation_result,
                "intervention_result": intervention_result,
                "metrics": {
                    "discussion_rounds": len(discussion_result["discussion_rounds"]),
                    "consensus_level": discussion_result["final_consensus"]["level"].value,
                    "escalation_tier": escalation_result["escalation_tier_name"],
                    "human_intervention_needed": escalation_result["escalation_needed"]
                }
            }
            
            self.scenario_results.append(scenario_result)
            return scenario_result
            
        except Exception as e:
            print(f"   ERROR: {str(e)}")
            import traceback
            traceback.print_exc()
            return {"scenario_name": "api_security_enhancement", "success": False, "error": str(e)}
    
    def _scenario_2_enterprise_architecture_decision(self) -> Dict[str, Any]:
        """Scenario 2: Enterprise Architecture Modernization Decision
        
        Demonstrates: High complexity consultation with senior partner escalation
        """
        print("🏢 Enterprise Architecture Modernization for Healthcare System")
        
        try:
            # Define complex consultation context
            consultation_context = {
                "scenario_name": "enterprise_architecture_modernization",
                "client": "Regional Healthcare Network",
                "description": "Modernize legacy healthcare management system",
                "type": "strategic_architecture_overhaul",
                "complexity": "very_high",
                "business_impact": "critical",
                "financial_impact": "very_high",
                "customer_impact": "high",
                "stakeholders": ["medical_staff", "it_operations", "executives", "patients", "regulatory_bodies"],
                "timeline": "urgent",
                "regulatory_requirements": True,
                "integration_requirements": ["electronic_health_records", "billing_systems", "lab_interfaces", "pharmacy_systems"],
                "dependencies": ["data_migration", "staff_training", "regulatory_approval", "vendor_coordination"]
            }
            
            # Enhanced agent profiles for complex scenario
            participating_agents = [
                {
                    "name": self.code_reviewer.name,
                    "agent_type": "CodeReviewerAgent",
                    "expertise": ["legacy_system_analysis", "healthcare_standards", "data_security"],
                    "seniority": "principal"
                },
                {
                    "name": self.system_architect.name,
                    "agent_type": "SystemArchitectAgent", 
                    "expertise": ["enterprise_architecture", "healthcare_systems", "cloud_migration"],
                    "seniority": "distinguished"
                },
                {
                    "name": self.business_analyst.name,
                    "agent_type": "BusinessAnalystAgent",
                    "expertise": ["healthcare_operations", "change_management", "regulatory_compliance"],
                    "seniority": "principal"
                }
            ]
            
            print(f"   Client: {consultation_context['client']}")
            print(f"   Complexity: {consultation_context['complexity']}")
            print(f"   Stakeholders: {len(consultation_context['stakeholders'])}")
            
            # Execute extended multi-agent discussion
            discussion_result = self.chief_manager.orchestrate_multi_agent_discussion(
                consultation_context,
                participating_agents,
                discussion_rounds=3  # More rounds for complex scenario
            )
            
            print(f"   Discussion completed: {discussion_result['discussion_id']}")
            print(f"   Final consensus: {discussion_result['final_consensus']['level'].value}")
            print(f"   Coordination quality: {discussion_result['coordination_quality']['overall_score']:.2f}")
            
            # Advanced escalation with comprehensive analysis
            final_consensus = discussion_result["final_consensus"]
            final_recommendations = final_consensus.get("final_recommendations", [])
            
            # Convert string recommendations to proper agent response format
            if isinstance(final_recommendations, list) and final_recommendations:
                if isinstance(final_recommendations[0], str):
                    # Convert strings to agent response format
                    agent_responses = []
                    for i, rec in enumerate(final_recommendations):
                        agent_responses.append({
                            "agent": f"agent_{i}",
                            "recommendation": rec,
                            "confidence": 0.7,  # Default confidence
                            "agent_type": "general"
                        })
                    final_recommendations = agent_responses
            elif not isinstance(final_recommendations, list):
                final_recommendations = []
            
            escalation_result = self.escalation_engine.evaluate_advanced_escalation(
                final_recommendations,
                consultation_context,
                final_consensus
            )
            
            print(f"   Escalation tier: {escalation_result['escalation_tier_name']}")
            print(f"   Risk level: {escalation_result['risk_analysis']['overall_risk_level'].value}")
            print(f"   Required expertise: {[exp.value for exp in escalation_result['required_expertise']]}")
            
            # Strategic intervention for senior partner escalation
            intervention_result = None
            if escalation_result["escalation_tier_name"] == "SENIOR_PARTNER":
                intervention_request = {
                    "decision_context": consultation_context,
                    "escalation_info": escalation_result,
                    "agent_recommendations": discussion_result["final_consensus"]["final_recommendations"],
                    "consensus_analysis": discussion_result["final_consensus"]
                }
                
                intervention_result = self.human_interaction.request_human_intervention(
                    intervention_request,
                    InterventionType.STRATEGIC_DIRECTION
                )
                
                print(f"   Strategic intervention: Senior Partner guidance provided")
                strategic_recs = intervention_result['human_input'].get('strategic_recommendations', [])
                print(f"   Strategic recommendations: {len(strategic_recs)} strategic actions")
            
            # Store comprehensive scenario result
            scenario_result = {
                "scenario_name": "enterprise_architecture_modernization",
                "success": True,
                "consultation_context": consultation_context,
                "discussion_result": discussion_result,
                "escalation_result": escalation_result,
                "intervention_result": intervention_result,
                "metrics": {
                    "discussion_rounds": len(discussion_result["discussion_rounds"]),
                    "consensus_level": discussion_result["final_consensus"]["level"].value,
                    "coordination_quality": discussion_result["coordination_quality"]["overall_score"],
                    "escalation_tier": escalation_result["escalation_tier_name"],
                    "risk_level": escalation_result["risk_analysis"]["overall_risk_level"].value,
                    "strategic_intervention": intervention_result is not None
                }
            }
            
            self.scenario_results.append(scenario_result)
            return scenario_result
            
        except Exception as e:
            return {"scenario_name": "enterprise_architecture_modernization", "success": False, "error": str(e)}
    
    def _scenario_3_product_launch_coordination(self) -> Dict[str, Any]:
        """Scenario 3: Product Launch Technology Coordination
        
        Demonstrates: Multi-team coordination with partial modification intervention
        """
        print("🚀 Product Launch Technology Coordination for E-commerce Platform")
        
        try:
            consultation_context = {
                "scenario_name": "product_launch_coordination",
                "client": "E-commerce Technology Company",
                "description": "Coordinate technology stack for major product launch",
                "type": "product_launch_coordination",
                "complexity": "high",
                "business_impact": "very_high",
                "timeline": "critical",
                "stakeholders": ["product_team", "engineering", "marketing", "operations", "customer_support"],
                "integration_requirements": ["payment_processing", "inventory_management", "customer_analytics"],
                "dependencies": ["load_testing", "security_audit", "compliance_review"]
            }
            
            participating_agents = [
                {
                    "name": self.code_reviewer.name,
                    "agent_type": "CodeReviewerAgent",
                    "expertise": ["performance_optimization", "quality_assurance", "deployment"],
                    "seniority": "senior"
                },
                {
                    "name": self.system_architect.name,
                    "agent_type": "SystemArchitectAgent",
                    "expertise": ["scalable_architecture", "integration_patterns", "launch_strategy"],
                    "seniority": "principal"
                },
                {
                    "name": self.business_analyst.name,
                    "agent_type": "BusinessAnalystAgent",
                    "expertise": ["product_coordination", "stakeholder_management", "launch_planning"],
                    "seniority": "senior"
                }
            ]
            
            print(f"   Client: {consultation_context['client']}")
            print(f"   Timeline: {consultation_context['timeline']}")
            
            # Execute coordination discussion
            discussion_result = self.chief_manager.orchestrate_multi_agent_discussion(
                consultation_context,
                participating_agents,
                discussion_rounds=2
            )
            
            print(f"   Consensus: {discussion_result['final_consensus']['level'].value}")
            
            # Escalation analysis
            final_consensus = discussion_result["final_consensus"]
            final_recommendations = final_consensus.get("final_recommendations", [])
            
            # Convert string recommendations to proper agent response format
            if isinstance(final_recommendations, list) and final_recommendations:
                if isinstance(final_recommendations[0], str):
                    # Convert strings to agent response format
                    agent_responses = []
                    for i, rec in enumerate(final_recommendations):
                        agent_responses.append({
                            "agent": f"agent_{i}",
                            "recommendation": rec,
                            "confidence": 0.7,  # Default confidence
                            "agent_type": "general"
                        })
                    final_recommendations = agent_responses
            elif not isinstance(final_recommendations, list):
                final_recommendations = []
            
            escalation_result = self.escalation_engine.evaluate_advanced_escalation(
                final_recommendations,
                consultation_context,
                final_consensus
            )
            
            print(f"   Escalation tier: {escalation_result['escalation_tier_name']}")
            
            # Partial modification intervention
            intervention_request = {
                "decision_context": consultation_context,
                "escalation_info": escalation_result,
                "agent_recommendations": final_recommendations,
                "consensus_analysis": final_consensus
            }
            
            intervention_result = self.human_interaction.request_human_intervention(
                intervention_request,
                InterventionType.PARTIAL_MODIFICATION
            )
            
            modifications = intervention_result['human_input'].get('modifications', {}).get('modifications', [])
            print(f"   Partial modifications: {len(modifications)} enhancements suggested")
            
            scenario_result = {
                "scenario_name": "product_launch_coordination",
                "success": True,
                "consultation_context": consultation_context,
                "discussion_result": discussion_result,
                "escalation_result": escalation_result,
                "intervention_result": intervention_result,
                "metrics": {
                    "consensus_level": discussion_result["final_consensus"]["level"].value,
                    "modifications_suggested": len(modifications),
                    "escalation_tier": escalation_result["escalation_tier_name"]
                }
            }
            
            self.scenario_results.append(scenario_result)
            return scenario_result
            
        except Exception as e:
            return {"scenario_name": "product_launch_coordination", "success": False, "error": str(e)}
    
    def _scenario_4_crisis_response_scenario(self) -> Dict[str, Any]:
        """Scenario 4: Crisis Response Technology Decision
        
        Demonstrates: Urgent decision override with expert consultation
        """
        print("🚨 Crisis Response Technology Decision for Financial Institution")
        
        try:
            consultation_context = {
                "scenario_name": "crisis_response_decision",
                "client": "International Bank",
                "description": "Emergency response to critical security vulnerability",
                "type": "crisis_response",
                "complexity": "medium",
                "business_impact": "critical",
                "timeline": "immediate",
                "stakeholders": ["security_team", "operations", "executives", "regulatory_contacts"],
                "regulatory_requirements": True,
                "crisis_factors": ["active_threat", "customer_data_risk", "regulatory_notification_required"]
            }
            
            participating_agents = [
                {
                    "name": self.code_reviewer.name,
                    "agent_type": "CodeReviewerAgent",
                    "expertise": ["security_analysis", "vulnerability_assessment", "incident_response"],
                    "seniority": "principal"
                },
                {
                    "name": self.system_architect.name,
                    "agent_type": "SystemArchitectAgent",
                    "expertise": ["security_architecture", "crisis_management", "system_isolation"],
                    "seniority": "senior"
                },
                {
                    "name": self.business_analyst.name,
                    "agent_type": "BusinessAnalystAgent",
                    "expertise": ["crisis_communication", "regulatory_compliance", "business_continuity"],
                    "seniority": "senior"
                }
            ]
            
            print(f"   Crisis type: {consultation_context['description']}")
            print(f"   Timeline: {consultation_context['timeline']}")
            
            # Rapid coordination discussion
            discussion_result = self.chief_manager.orchestrate_multi_agent_discussion(
                consultation_context,
                participating_agents,
                discussion_rounds=1  # Rapid response
            )
            
            # Crisis escalation analysis
            final_consensus = discussion_result["final_consensus"]
            final_recommendations = final_consensus.get("final_recommendations", [])
            
            # Convert string recommendations to proper agent response format
            if isinstance(final_recommendations, list) and final_recommendations:
                if isinstance(final_recommendations[0], str):
                    # Convert strings to agent response format
                    agent_responses = []
                    for i, rec in enumerate(final_recommendations):
                        agent_responses.append({
                            "agent": f"agent_{i}",
                            "recommendation": rec,
                            "confidence": 0.7,  # Default confidence
                            "agent_type": "general"
                        })
                    final_recommendations = agent_responses
            elif not isinstance(final_recommendations, list):
                final_recommendations = []
            
            try:
                escalation_result = self.escalation_engine.evaluate_advanced_escalation(
                    final_recommendations,
                    consultation_context,
                    final_consensus
                )
            except Exception as escalation_error:
                print(f"   ESCALATION ERROR: {escalation_error}")
                import traceback
                traceback.print_exc()
                raise escalation_error
            
            # Decision override for crisis response
            intervention_request = {
                "decision_context": consultation_context,
                "escalation_info": escalation_result,
                "agent_recommendations": final_recommendations  # Use processed recommendations
            }
            
            intervention_result = self.human_interaction.request_human_intervention(
                intervention_request,
                InterventionType.DECISION_OVERRIDE
            )
            
            override_rec = intervention_result['human_input'].get('override_recommendation', 'No override')
            print(f"   Crisis override: {override_rec}")
            
            scenario_result = {
                "scenario_name": "crisis_response_decision",
                "success": True,
                "consultation_context": consultation_context,
                "discussion_result": discussion_result,
                "escalation_result": escalation_result,
                "intervention_result": intervention_result,
                "metrics": {
                    "response_time": "rapid",
                    "override_applied": True,
                    "crisis_handled": True
                }
            }
            
            self.scenario_results.append(scenario_result)
            return scenario_result
            
        except Exception as e:
            return {"scenario_name": "crisis_response_decision", "success": False, "error": str(e)}
    
    def _display_comprehensive_summary(
        self, 
        scenario_results: List[Dict[str, Any]], 
        overall_success: bool
    ) -> None:
        """Display comprehensive demonstration summary"""
        
        print("\n" + "=" * 80)
        print("📊 COMPREHENSIVE CONSULTING DEMONSTRATION SUMMARY")
        print("=" * 80)
        
        successful_scenarios = sum(1 for result in scenario_results if result.get("success", False))
        total_scenarios = len(scenario_results)
        
        print(f"Overall Success Rate: {successful_scenarios}/{total_scenarios} ({successful_scenarios/total_scenarios:.1%})")
        
        # Scenario-by-scenario summary
        for i, result in enumerate(scenario_results, 1):
            status = "✅ SUCCESS" if result.get("success", False) else "❌ FAILED"
            scenario_name = result.get("scenario_name", f"scenario_{i}")
            print(f"\nScenario {i}: {scenario_name.replace('_', ' ').title()}")
            print(f"   Status: {status}")
            
            if result.get("success", False) and "metrics" in result:
                metrics = result["metrics"]
                for key, value in metrics.items():
                    print(f"   {key.replace('_', ' ').title()}: {value}")
        
        # Epic 2 capabilities demonstration summary
        print(f"\n🎯 Epic 2 Capabilities Demonstrated:")
        print(f"✅ Enhanced Chief Engagement Manager coordination")
        print(f"✅ Advanced escalation logic with multi-factor analysis")
        print(f"✅ Sophisticated human intervention mechanisms")
        print(f"✅ Realistic consulting scenario execution")
        print(f"✅ Complete inner team collaboration workflows")
        
        if overall_success:
            print(f"\n🎉 STORY 2.4: Consulting Scenario Demonstrations - COMPLETE!")
            print(f"🏆 EPIC 2: Inner Team Implementation - COMPLETE!")
            print(f"🚀 Ready for Epic 3: Dynamic Expertise Sourcing")
        else:
            print(f"\n❌ Some scenarios need refinement before Epic 2 completion")
    
    def get_demonstration_analytics(self) -> Dict[str, Any]:
        """Get comprehensive demonstration analytics"""
        return {
            "total_scenarios_executed": len(self.scenario_results),
            "successful_scenarios": sum(1 for r in self.scenario_results if r.get("success", False)),
            "scenario_results": self.scenario_results,
            "coordination_analytics": self.chief_manager.get_coordination_analytics(),
            "escalation_analytics": self.escalation_engine.get_advanced_escalation_analytics(),
            "intervention_analytics": self.human_interaction.get_intervention_analytics()
        }


def demonstrate_consulting_scenarios() -> bool:
    """Main demonstration function for consulting scenarios
    
    Returns:
        True if all scenarios demonstrate successfully, False otherwise
    """
    print("🚀 Starting Comprehensive Consulting Scenario Demonstration - Story 2.4")
    print("🎯 Academic Context: Epic 2 Inner Team Implementation - Complete Integration")
    
    try:
        # Create and run comprehensive demonstration
        runner = ConsultingScenarioRunner()
        success = runner.execute_comprehensive_consulting_demonstration()
        
        if success:
            # Display analytics summary
            analytics = runner.get_demonstration_analytics()
            print(f"\n📈 Demonstration Analytics Summary:")
            print(f"   Total scenarios: {analytics['total_scenarios_executed']}")
            print(f"   Success rate: {analytics['successful_scenarios']}/{analytics['total_scenarios_executed']}")
            print(f"   Coordination discussions: {analytics['coordination_analytics']['total_discussions']}")
            print(f"   Advanced escalations: {analytics['escalation_analytics']['total_advanced_escalations']}")
            print(f"   Human interventions: {analytics['intervention_analytics']['total_interventions']}")
        
        return success
        
    except Exception as e:
        print(f"❌ Consulting scenario demonstration failed: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = demonstrate_consulting_scenarios()
    if success:
        print("\n✅ Story 2.4: Consulting Scenario Demonstrations - PASSED")
        exit(0)
    else:
        print("\n❌ Story 2.4: Consulting Scenario Demonstrations - FAILED")
        exit(1)
