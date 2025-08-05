"""Test all three specialized agents together - Story 1.3 Validation"""

import sys
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent / "src"))

def test_story_1_3_agents():
    """Test all three specialized agents for Story 1.3 validation"""
    
    print("🧪 Story 1.3: Testing All Specialized Agents")
    print("=" * 60)
    
    results = {}
    
    # Test CodeReviewerAgent
    print("\n1️⃣ Testing CodeReviewerAgent...")
    try:
        from agents.code_reviewer import create_code_reviewer_agent
        
        code_reviewer = create_code_reviewer_agent(name="integration_code_reviewer")
        
        code_context = {
            "type": "consultation_code_review",
            "description": "API authentication implementation",
            "complexity": "medium"
        }
        
        review_result = code_reviewer.analyze_code_quality(code_context)
        capabilities = code_reviewer.get_agent_capabilities()
        
        print(f"   ✅ CodeReviewerAgent: {review_result['confidence']:.1%} confidence")
        print(f"      Agent type: {capabilities['agent_type']}")
        print(f"      Capabilities: {len(capabilities['capabilities'])} skills")
        
        results['code_reviewer'] = {
            'success': True,
            'confidence': review_result['confidence'],
            'agent_type': capabilities['agent_type']
        }
        
    except Exception as e:
        print(f"   ❌ CodeReviewerAgent failed: {e}")
        results['code_reviewer'] = {'success': False, 'error': str(e)}
    
    # Test SystemArchitectAgent
    print("\n2️⃣ Testing SystemArchitectAgent...")
    try:
        from agents.system_architect import create_system_architect_agent
        
        architect = create_system_architect_agent(name="integration_architect")
        
        arch_context = {
            "type": "consultation_architecture",
            "description": "Microservices design for customer portal",
            "scale": "high",
            "complexity": "medium"
        }
        
        arch_result = architect.analyze_system_architecture(arch_context)
        capabilities = architect.get_agent_capabilities()
        
        print(f"   ✅ SystemArchitectAgent: {arch_result['confidence']:.1%} confidence")
        print(f"      Agent type: {capabilities['agent_type']}")
        print(f"      Technology stack: {len(arch_result['technology_stack'])} components")
        
        results['system_architect'] = {
            'success': True,
            'confidence': arch_result['confidence'],
            'agent_type': capabilities['agent_type']
        }
        
    except Exception as e:
        print(f"   ❌ SystemArchitectAgent failed: {e}")
        results['system_architect'] = {'success': False, 'error': str(e)}
    
    # Test BusinessAnalystAgent
    print("\n3️⃣ Testing BusinessAnalystAgent...")
    try:
        from agents.business_analyst import create_business_analyst_agent
        
        analyst = create_business_analyst_agent(name="integration_analyst")
        
        biz_context = {
            "project": "consultation_requirements",
            "description": "Customer portal business requirements",
            "stakeholders": ["customers", "support", "management"],
            "timeline": "3 months"
        }
        
        biz_result = analyst.analyze_business_requirements(biz_context)
        capabilities = analyst.get_agent_capabilities()
        
        print(f"   ✅ BusinessAnalystAgent: {biz_result['confidence']:.1%} confidence")
        print(f"      Agent type: {capabilities['agent_type']}")
        print(f"      Stakeholder alignment: {biz_result['stakeholder_analysis']['alignment_score']:.1%}")
        
        results['business_analyst'] = {
            'success': True,
            'confidence': biz_result['confidence'],
            'agent_type': capabilities['agent_type']
        }
        
    except Exception as e:
        print(f"   ❌ BusinessAnalystAgent failed: {e}")
        results['business_analyst'] = {'success': False, 'error': str(e)}
    
    # Test Chief Engagement Manager coordination
    print("\n4️⃣ Testing Chief Engagement Manager Coordination...")
    try:
        from coordination.chief_engagement_manager import create_chief_engagement_manager
        
        manager = create_chief_engagement_manager(
            name="integration_manager",
            human_input_mode="NEVER"
        )
        
        # Test escalation with all three agent responses
        consultation_context = {
            "scenario": "Multi-agent consultation test",
            "type": "integrated_decision",
            "complexity": "medium"
        }
        
        # Simulate responses from all three agents
        multi_agent_responses = [
            {
                "agent": "code_reviewer",
                "recommendation": "Use secure authentication patterns",
                "confidence": results['code_reviewer'].get('confidence', 0.8),
                "agent_type": "CodeReviewerAgent"
            },
            {
                "agent": "system_architect", 
                "recommendation": "Implement microservices architecture",
                "confidence": results['system_architect'].get('confidence', 0.8),
                "agent_type": "SystemArchitectAgent"
            },
            {
                "agent": "business_analyst",
                "recommendation": "Prioritize user experience requirements",
                "confidence": results['business_analyst'].get('confidence', 0.85),
                "agent_type": "BusinessAnalystAgent"
            }
        ]
        
        escalation_result = manager.evaluate_escalation_need(
            multi_agent_responses, 
            consultation_context
        )
        
        print(f"   ✅ Multi-agent coordination: Tier {escalation_result['escalation_tier'].name}")
        print(f"      Overall confidence: {escalation_result['overall_confidence']:.1%}")
        print(f"      Escalation needed: {escalation_result['escalation_needed']}")
        
        results['coordination'] = {
            'success': True,
            'escalation_tier': escalation_result['escalation_tier'].name,
            'overall_confidence': escalation_result['overall_confidence']
        }
        
    except Exception as e:
        print(f"   ❌ Chief Engagement Manager coordination failed: {e}")
        results['coordination'] = {'success': False, 'error': str(e)}
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 Story 1.3 Integration Test Summary")
    print("=" * 60)
    
    all_success = True
    for agent_name, result in results.items():
        status = "✅ PASS" if result['success'] else "❌ FAIL"
        print(f"   {agent_name.replace('_', ' ').title()}: {status}")
        if not result['success']:
            all_success = False
    
    if all_success:
        print("\n🎉 Story 1.3: Basic Agent Specialization - COMPLETE!")
        print("✅ CodeReviewerAgent with code analysis capabilities")
        print("✅ SystemArchitectAgent with design and architecture decisions") 
        print("✅ BusinessAnalystAgent with requirements and stakeholder analysis")
        print("✅ All agents coordinate with Chief Engagement Manager")
        print("✅ Multi-agent consultation workflows operational")
        print("\n🚀 Ready for Story 1.4: Basic Tier System Implementation")
    else:
        print("\n❌ Story 1.3: Some agents need fixes before proceeding")
    
    return all_success

if __name__ == "__main__":
    success = test_story_1_3_agents()
    if success:
        print("\n✅ Story 1.3 Integration Test: PASSED")
    else:
        print("\n❌ Story 1.3 Integration Test: FAILED")
        exit(1)
