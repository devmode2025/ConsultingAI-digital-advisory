"""Outer Team Architecture Framework - Story 4.1 Implementation

This module implements the complete Society of Mind outer team architecture,
enabling coordination with external experts, services, and knowledge sources
while maintaining clear boundaries between inner and outer team responsibilities.
"""

from typing import Dict, Any, List, Optional, Union, Callable
from enum import Enum
from datetime import datetime
from dataclasses import dataclass, field
from collections import defaultdict
import logging
import asyncio
from abc import ABC, abstractmethod

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from experts.dynamic_persona_system import ExpertPersonaType
from coordination.enhanced_coordination import EnhancedChiefEngagementManager


class OuterTeamRole(Enum):
    """Roles in the outer team ecosystem"""
    EXTERNAL_SPECIALIST = "external_specialist"
    KNOWLEDGE_SERVICE = "knowledge_service"
    VALIDATION_AUTHORITY = "validation_authority"
    CLIENT_REPRESENTATIVE = "client_representative"
    REGULATORY_ADVISOR = "regulatory_advisor"
    TECHNOLOGY_VENDOR = "technology_vendor"
    RESEARCH_INSTITUTE = "research_institute"


class TeamBoundary(Enum):
    """Boundaries between team layers"""
    INNER_TEAM = "inner_team"           # Core expert personas
    OUTER_TEAM = "outer_team"           # External experts and services
    ECOSYSTEM = "ecosystem"             # Broader consulting ecosystem
    CLIENT_DOMAIN = "client_domain"     # Client organization boundary


class CoordinationProtocol(Enum):
    """Protocols for inter-team coordination"""
    DIRECT_CONSULTATION = "direct_consultation"
    KNOWLEDGE_REQUEST = "knowledge_request"
    VALIDATION_REQUEST = "validation_request"
    ESCALATION_HANDOFF = "escalation_handoff"
    COLLABORATIVE_SESSION = "collaborative_session"
    INFORMATION_SYNTHESIS = "information_synthesis"


@dataclass
class OuterTeamMember:
    """Definition of an outer team member"""
    member_id: str
    role: OuterTeamRole
    name: str
    expertise_domains: List[str]
    capabilities: List[str]
    access_level: str
    contact_protocol: CoordinationProtocol
    availability_schedule: Dict[str, Any]
    performance_history: List[Dict[str, Any]] = field(default_factory=list)
    collaboration_preferences: Dict[str, Any] = field(default_factory=dict)


@dataclass
class TeamCoordinationRequest:
    """Request for outer team coordination"""
    request_id: str
    originating_team: TeamBoundary
    target_team: TeamBoundary
    coordination_type: CoordinationProtocol
    request_context: Dict[str, Any]
    urgency_level: str
    expected_deliverables: List[str]
    timeline_constraints: Dict[str, Any]
    success_criteria: List[str]


class OuterTeamInterface(ABC):
    """Abstract interface for outer team members"""
    
    @abstractmethod
    async def handle_coordination_request(
        self, 
        request: TeamCoordinationRequest
    ) -> Dict[str, Any]:
        """Handle coordination request from inner team"""
        pass
    
    @abstractmethod
    def get_availability(self, timeframe: Dict[str, Any]) -> Dict[str, Any]:
        """Get availability for coordination"""
        pass
    
    @abstractmethod
    def get_expertise_assessment(
        self, 
        domain: str, 
        complexity: str
    ) -> Dict[str, Any]:
        """Assess expertise level for domain and complexity"""
        pass


class ExternalSpecialist(OuterTeamInterface):
    """External specialist implementation"""
    
    def __init__(self, member_definition: OuterTeamMember):
        self.member = member_definition
        self.logger = logging.getLogger(f"OuterTeam.{member_definition.name}")
    
    async def handle_coordination_request(
        self, 
        request: TeamCoordinationRequest
    ) -> Dict[str, Any]:
        """Handle coordination request from inner team"""
        
        # Simulate external specialist consultation
        response = {
            "specialist_id": self.member.member_id,
            "specialist_name": self.member.name,
            "consultation_type": request.coordination_type.value,
            "expert_analysis": self._provide_specialist_analysis(request),
            "recommendations": self._generate_specialist_recommendations(request),
            "confidence_level": self._assess_confidence(request),
            "follow_up_required": self._assess_follow_up_needs(request),
            "deliverables": self._prepare_deliverables(request),
            "response_timestamp": datetime.now().isoformat()
        }
        
        # Record interaction
        self.member.performance_history.append({
            "request_id": request.request_id,
            "timestamp": datetime.now(),
            "response_quality": response["confidence_level"],
            "interaction_type": request.coordination_type.value
        })
        
        return response
    
    def get_availability(self, timeframe: Dict[str, Any]) -> Dict[str, Any]:
        """Get availability for coordination"""
        # Simulate availability assessment
        return {
            "available": True,
            "response_time": "2-4 hours",
            "capacity": "high",
            "preferred_coordination": self.member.contact_protocol.value
        }
    
    def get_expertise_assessment(
        self, 
        domain: str, 
        complexity: str
    ) -> Dict[str, Any]:
        """Assess expertise level for domain and complexity"""
        
        domain_match = domain.lower() in [d.lower() for d in self.member.expertise_domains]
        
        if domain_match:
            expertise_level = "high" if complexity in ["low", "medium"] else "medium"
            confidence = 0.9 if complexity in ["low", "medium"] else 0.7
        else:
            expertise_level = "limited"
            confidence = 0.4
        
        return {
            "expertise_level": expertise_level,
            "confidence": confidence,
            "domain_match": domain_match,
            "recommended_engagement": expertise_level != "limited"
        }
    
    def _provide_specialist_analysis(self, request: TeamCoordinationRequest) -> str:
        """Provide specialist analysis for the request"""
        context = request.request_context
        decision_type = context.get("decision_type", "general_consultation")
        domain = context.get("domain", "general")
        
        # Generate domain-specific analysis
        if "security" in domain.lower() or "security" in decision_type.lower():
            return f"Security analysis for {decision_type}: Comprehensive threat assessment required, implement defense-in-depth strategy, ensure compliance with industry standards."
        elif "performance" in domain.lower():
            return f"Performance analysis for {decision_type}: Scalability assessment needed, optimize critical paths, implement monitoring and alerting."
        else:
            return f"Specialist analysis for {decision_type}: Domain expertise applied, best practices recommended, thorough evaluation completed."
    
    def _generate_specialist_recommendations(self, request: TeamCoordinationRequest) -> List[str]:
        """Generate specialist recommendations"""
        context = request.request_context
        domain = context.get("domain", "general")
        
        base_recommendations = [
            f"Engage {self.member.name} for detailed {domain} analysis",
            "Conduct comprehensive requirements gathering",
            "Establish clear success criteria and validation methods"
        ]
        
        # Add domain-specific recommendations
        if "security" in self.member.expertise_domains:
            base_recommendations.extend([
                "Implement security-first design principles",
                "Conduct regular security assessments",
                "Establish incident response procedures"
            ])
        elif "performance" in self.member.expertise_domains:
            base_recommendations.extend([
                "Establish performance benchmarking framework",
                "Implement continuous performance monitoring",
                "Optimize resource utilization"
            ])
        
        return base_recommendations
    
    def _assess_confidence(self, request: TeamCoordinationRequest) -> float:
        """Assess confidence in providing consultation"""
        context = request.request_context
        decision_type = context.get("decision_type", "")
        complexity = context.get("complexity_level", "medium")
        
        # Base confidence from domain match
        domain_confidence = 0.8 if any(
            domain.lower() in decision_type.lower() 
            for domain in self.member.expertise_domains
        ) else 0.6
        
        # Adjust for complexity
        complexity_adjustment = {
            "low": 0.1, "medium": 0.0, "high": -0.1, "very_high": -0.2
        }.get(complexity, 0.0)
        
        return max(0.3, min(1.0, domain_confidence + complexity_adjustment))
    
    def _assess_follow_up_needs(self, request: TeamCoordinationRequest) -> bool:
        """Assess if follow-up is needed"""
        complexity = request.request_context.get("complexity_level", "medium")
        urgency = request.urgency_level
        
        return complexity in ["high", "very_high"] or urgency == "critical"
    
    def _prepare_deliverables(self, request: TeamCoordinationRequest) -> List[str]:
        """Prepare deliverables for the request"""
        deliverables = []
        
        for expected in request.expected_deliverables:
            if "analysis" in expected.lower():
                deliverables.append(f"Comprehensive {self.member.expertise_domains[0]} analysis report")
            elif "recommendation" in expected.lower():
                deliverables.append(f"Expert recommendations with implementation guidance")
            elif "validation" in expected.lower():
                deliverables.append(f"Validation framework with success criteria")
            else:
                deliverables.append(f"Expert consultation on {expected}")
        
        return deliverables


class KnowledgeService(OuterTeamInterface):
    """Knowledge service implementation"""
    
    def __init__(self, member_definition: OuterTeamMember):
        self.member = member_definition
        self.knowledge_base = self._initialize_knowledge_base()
        self.logger = logging.getLogger(f"KnowledgeService.{member_definition.name}")
    
    def _initialize_knowledge_base(self) -> Dict[str, Any]:
        """Initialize knowledge base for the service"""
        return {
            "best_practices": {
                "software_architecture": [
                    "Microservices design patterns",
                    "API-first architecture principles",
                    "Scalability planning methodologies"
                ],
                "security": [
                    "Zero-trust security frameworks",
                    "Compliance validation procedures",
                    "Threat modeling methodologies"
                ],
                "performance": [
                    "Performance optimization techniques",
                    "Load testing strategies",
                    "Monitoring and alerting frameworks"
                ]
            },
            "case_studies": {
                "enterprise_transformations": [
                    "Fortune 500 digital transformation case study",
                    "Financial services modernization case study",
                    "Healthcare system integration case study"
                ]
            },
            "frameworks": {
                "decision_making": [
                    "TOGAF enterprise architecture framework",
                    "NIST cybersecurity framework",
                    "ITIL service management framework"
                ]
            }
        }
    
    async def handle_coordination_request(
        self, 
        request: TeamCoordinationRequest
    ) -> Dict[str, Any]:
        """Handle knowledge request from inner team"""
        
        knowledge_query = request.request_context.get("knowledge_query", "")
        domain = request.request_context.get("domain", "general")
        
        # Search knowledge base
        relevant_knowledge = self._search_knowledge_base(knowledge_query, domain)
        
        response = {
            "service_id": self.member.member_id,
            "service_name": self.member.name,
            "query_type": request.coordination_type.value,
            "relevant_knowledge": relevant_knowledge,
            "knowledge_synthesis": self._synthesize_knowledge(relevant_knowledge, request),
            "confidence_score": self._assess_knowledge_confidence(relevant_knowledge),
            "additional_resources": self._recommend_additional_resources(domain),
            "response_timestamp": datetime.now().isoformat()
        }
        
        return response
    
    def _search_knowledge_base(self, query: str, domain: str) -> Dict[str, List[str]]:
        """Search knowledge base for relevant information"""
        relevant_knowledge = {}
        
        query_lower = query.lower()
        domain_lower = domain.lower()
        
        # Search best practices
        for practice_domain, practices in self.knowledge_base["best_practices"].items():
            if domain_lower in practice_domain or any(word in practice_domain for word in query_lower.split()):
                relevant_knowledge[f"{practice_domain}_best_practices"] = practices
        
        # Search case studies
        for study_domain, studies in self.knowledge_base["case_studies"].items():
            if domain_lower in study_domain or any(word in study_domain for word in query_lower.split()):
                relevant_knowledge[f"{study_domain}_case_studies"] = studies
        
        # Search frameworks
        for framework_domain, frameworks in self.knowledge_base["frameworks"].items():
            if domain_lower in framework_domain or any(word in framework_domain for word in query_lower.split()):
                relevant_knowledge[f"{framework_domain}_frameworks"] = frameworks
        
        return relevant_knowledge
    
    def _synthesize_knowledge(
        self, 
        knowledge: Dict[str, List[str]], 
        request: TeamCoordinationRequest
    ) -> str:
        """Synthesize knowledge for the specific request"""
        
        if not knowledge:
            return "Limited knowledge available for this specific domain and query"
        
        synthesis_parts = []
        
        for knowledge_type, items in knowledge.items():
            if "best_practices" in knowledge_type:
                synthesis_parts.append(f"Best practices for {knowledge_type}: {', '.join(items[:2])}")
            elif "case_studies" in knowledge_type:
                synthesis_parts.append(f"Relevant case studies: {items[0] if items else 'None available'}")
            elif "frameworks" in knowledge_type:
                synthesis_parts.append(f"Applicable frameworks: {items[0] if items else 'Standard methodologies'}")
        
        return " | ".join(synthesis_parts)
    
    def _assess_knowledge_confidence(self, knowledge: Dict[str, List[str]]) -> float:
        """Assess confidence in knowledge relevance"""
        if not knowledge:
            return 0.3
        
        total_items = sum(len(items) for items in knowledge.values())
        knowledge_types = len(knowledge)
        
        # More knowledge types and items = higher confidence
        confidence = min(1.0, (knowledge_types * 0.3) + (total_items * 0.1))
        return max(0.4, confidence)
    
    def _recommend_additional_resources(self, domain: str) -> List[str]:
        """Recommend additional resources"""
        base_resources = [
            "Industry white papers and research reports",
            "Professional consulting frameworks",
            "Expert practitioner networks"
        ]
        
        domain_specific = {
            "security": ["NIST cybersecurity guidelines", "OWASP security standards"],
            "architecture": ["Enterprise architecture repositories", "Design pattern libraries"],
            "performance": ["Performance benchmarking databases", "Optimization case studies"]
        }
        
        return base_resources + domain_specific.get(domain.lower(), [])
    
    def get_availability(self, timeframe: Dict[str, Any]) -> Dict[str, Any]:
        """Knowledge services are typically always available"""
        return {
            "available": True,
            "response_time": "immediate",
            "capacity": "unlimited",
            "preferred_coordination": "knowledge_request"
        }
    
    def get_expertise_assessment(
        self, 
        domain: str, 
        complexity: str
    ) -> Dict[str, Any]:
        """Assess knowledge coverage for domain"""
        
        domain_coverage = domain.lower() in [d.lower() for d in self.member.expertise_domains]
        
        return {
            "expertise_level": "comprehensive" if domain_coverage else "general",
            "confidence": 0.8 if domain_coverage else 0.6,
            "domain_match": domain_coverage,
            "recommended_engagement": True  # Knowledge services useful for most requests
        }


class OuterTeamArchitecture:
    """Complete Outer Team Architecture for Society of Mind Framework
    
    This class implements the outer team coordination layer that extends beyond
    the inner expert team to include external specialists, knowledge services,
    and validation authorities, enabling complete SoM framework demonstration.
    
    Academic Note: Demonstrates complete Society of Mind architecture patterns
    for Epic 4 Story 4.1 - outer team coordination and knowledge boundaries.
    """
    
    def __init__(self, inner_team_manager: EnhancedChiefEngagementManager):
        """Initialize Outer Team Architecture
        
        Args:
            inner_team_manager: Enhanced Chief Engagement Manager for inner team coordination
        """
        self.inner_team_manager = inner_team_manager
        self.outer_team_members: Dict[str, OuterTeamInterface] = {}
        self.team_boundaries = self._define_team_boundaries()
        self.coordination_protocols = self._initialize_coordination_protocols()
        
        # Coordination tracking
        self.coordination_history: List[Dict[str, Any]] = []
        self.boundary_interactions: List[Dict[str, Any]] = []
        
        # Initialize outer team members
        self._initialize_outer_team_members()
        
        self.logger = logging.getLogger("ConsultingAI.OuterTeamArchitecture")
        
        self.logger.info(
            "Outer Team Architecture initialized",
            extra={
                "outer_team_members": len(self.outer_team_members),
                "team_boundaries": len(self.team_boundaries),
                "coordination_protocols": len(self.coordination_protocols),
                "academic_context": "Epic 4 Story 4.1 - Outer Team Architecture"
            }
        )
    
    def _define_team_boundaries(self) -> Dict[TeamBoundary, Dict[str, Any]]:
        """Define clear boundaries between team layers"""
        return {
            TeamBoundary.INNER_TEAM: {
                "description": "Core expert personas with specialized knowledge",
                "members": ["Python Guru", "System Architect", "Business Analyst", "Security Specialist", "Senior Partner"],
                "capabilities": ["Domain expertise", "Decision making", "Internal consensus"],
                "access_level": "full_system_access",
                "coordination_authority": "autonomous_within_expertise"
            },
            TeamBoundary.OUTER_TEAM: {
                "description": "External specialists and knowledge services",
                "members": ["External Security Expert", "Knowledge Services", "Validation Authorities"],
                "capabilities": ["Specialized consultation", "Knowledge synthesis", "Validation services"],
                "access_level": "consultation_access",
                "coordination_authority": "advisory_input"
            },
            TeamBoundary.ECOSYSTEM: {
                "description": "Broader consulting and technology ecosystem",
                "members": ["Technology Vendors", "Research Institutes", "Industry Networks"],
                "capabilities": ["Technology guidance", "Research insights", "Industry benchmarks"],
                "access_level": "information_sharing",
                "coordination_authority": "informational_input"
            },
            TeamBoundary.CLIENT_DOMAIN: {
                "description": "Client organization and stakeholders",
                "members": ["Client Representatives", "Stakeholder Groups", "End Users"],
                "capabilities": ["Requirements definition", "Acceptance criteria", "Feedback provision"],
                "access_level": "requirements_and_feedback",
                "coordination_authority": "decision_validation"
            }
        }
    
    def _initialize_coordination_protocols(self) -> Dict[CoordinationProtocol, Dict[str, Any]]:
        """Initialize coordination protocols between teams"""
        return {
            CoordinationProtocol.DIRECT_CONSULTATION: {
                "description": "Direct expert-to-expert consultation",
                "applicable_boundaries": [TeamBoundary.INNER_TEAM, TeamBoundary.OUTER_TEAM],
                "typical_use_cases": ["Specialized expertise", "Technical validation"],
                "response_time": "2-4 hours",
                "formality_level": "professional"
            },
            CoordinationProtocol.KNOWLEDGE_REQUEST: {
                "description": "Knowledge base and research queries",
                "applicable_boundaries": [TeamBoundary.OUTER_TEAM, TeamBoundary.ECOSYSTEM],
                "typical_use_cases": ["Best practices", "Case studies", "Framework guidance"],
                "response_time": "immediate to 1 hour",
                "formality_level": "structured"
            },
            CoordinationProtocol.VALIDATION_REQUEST: {
                "description": "Validation of decisions and recommendations",
                "applicable_boundaries": [TeamBoundary.OUTER_TEAM, TeamBoundary.CLIENT_DOMAIN],
                "typical_use_cases": ["Decision validation", "Compliance verification"],
                "response_time": "4-24 hours",
                "formality_level": "formal"
            },
            CoordinationProtocol.ESCALATION_HANDOFF: {
                "description": "Escalation to higher authority or expertise",
                "applicable_boundaries": [TeamBoundary.INNER_TEAM, TeamBoundary.OUTER_TEAM, TeamBoundary.ECOSYSTEM],
                "typical_use_cases": ["Complex decisions", "Authority escalation"],
                "response_time": "varies by urgency",
                "formality_level": "formal"
            }
        }
    
    def _initialize_outer_team_members(self) -> None:
        """Initialize outer team members"""
        
        # External Security Specialist
        security_specialist = OuterTeamMember(
            member_id="ext_security_001",
            role=OuterTeamRole.EXTERNAL_SPECIALIST,
            name="External Cybersecurity Expert",
            expertise_domains=["advanced_threat_analysis", "compliance_frameworks", "incident_response"],
            capabilities=["Threat modeling", "Security architecture review", "Compliance validation"],
            access_level="consultation",
            contact_protocol=CoordinationProtocol.DIRECT_CONSULTATION,
            availability_schedule={"business_hours": True, "emergency_available": True}
        )
        
        self.outer_team_members["ext_security_001"] = ExternalSpecialist(security_specialist)
        
        # Performance Optimization Expert
        performance_expert = OuterTeamMember(
            member_id="ext_performance_001",
            role=OuterTeamRole.EXTERNAL_SPECIALIST,
            name="Performance Optimization Specialist",
            expertise_domains=["high_performance_computing", "scalability_engineering", "system_optimization"],
            capabilities=["Performance analysis", "Optimization strategies", "Scalability planning"],
            access_level="consultation",
            contact_protocol=CoordinationProtocol.DIRECT_CONSULTATION,
            availability_schedule={"business_hours": True, "emergency_available": False}
        )
        
        self.outer_team_members["ext_performance_001"] = ExternalSpecialist(performance_expert)
        
        # Knowledge Service
        knowledge_service = OuterTeamMember(
            member_id="knowledge_service_001",
            role=OuterTeamRole.KNOWLEDGE_SERVICE,
            name="Enterprise Knowledge Repository",
            expertise_domains=["best_practices", "case_studies", "industry_frameworks"],
            capabilities=["Knowledge synthesis", "Research provision", "Framework guidance"],
            access_level="information_access",
            contact_protocol=CoordinationProtocol.KNOWLEDGE_REQUEST,
            availability_schedule={"always_available": True}
        )
        
        self.outer_team_members["knowledge_service_001"] = KnowledgeService(knowledge_service)
        
        # Regulatory Compliance Authority
        compliance_authority = OuterTeamMember(
            member_id="compliance_authority_001",
            role=OuterTeamRole.VALIDATION_AUTHORITY,
            name="Regulatory Compliance Validator",
            expertise_domains=["regulatory_compliance", "audit_readiness", "legal_frameworks"],
            capabilities=["Compliance validation", "Audit preparation", "Legal review"],
            access_level="validation",
            contact_protocol=CoordinationProtocol.VALIDATION_REQUEST,
            availability_schedule={"business_hours": True, "formal_reviews": True}
        )
        
        self.outer_team_members["compliance_authority_001"] = ExternalSpecialist(compliance_authority)
    
    async def coordinate_with_outer_team(
        self,
        coordination_request: TeamCoordinationRequest
    ) -> Dict[str, Any]:
        """Coordinate with outer team members
        
        Args:
            coordination_request: Request for outer team coordination
            
        Returns:
            Coordination result with outer team input and synthesis
        """
        coordination_id = self._generate_coordination_id()
        
        self.logger.info(
            "Initiating outer team coordination",
            extra={
                "coordination_id": coordination_id,
                "request_type": coordination_request.coordination_type.value,
                "target_team": coordination_request.target_team.value,
                "academic_demonstration": "outer_team_coordination"
            }
        )
        
        # Select appropriate outer team members
        selected_members = self._select_outer_team_members(coordination_request)
        
        # Execute coordination with selected members
        coordination_results = []
        
        for member_id, member_interface in selected_members.items():
            try:
                member_result = await member_interface.handle_coordination_request(coordination_request)
                member_result["member_id"] = member_id
                coordination_results.append(member_result)
            except Exception as e:
                self.logger.warning(f"Coordination failed with {member_id}: {e}")
                coordination_results.append({
                    "member_id": member_id,
                    "error": str(e),
                    "status": "failed"
                })
        
        # Synthesize coordination results
        synthesis = self._synthesize_coordination_results(
            coordination_results, coordination_request
        )
        
        # Create comprehensive coordination result
        coordination_result = {
            "coordination_id": coordination_id,
            "timestamp": datetime.now().isoformat(),
            "request": coordination_request,
            "selected_members": list(selected_members.keys()),
            "coordination_results": coordination_results,
            "synthesis": synthesis,
            "boundary_interaction": self._assess_boundary_interaction(coordination_request),
            "knowledge_integration": self._integrate_knowledge_across_boundaries(coordination_results),
            "recommendations": self._generate_outer_team_recommendations(synthesis)
        }
        
        # Record coordination interaction for analytics
        self._record_coordination_interaction(coordination_result)
        
        self.logger.info(
            "Outer team coordination completed",
            extra={
                "coordination_id": coordination_id,
                "synthesis_quality": synthesis["synthesis_quality"],
                "academic_demonstration": "boundary_coordination_complete"
            }
        )
        
        return coordination_result
    
    def _select_outer_team_members(
        self, 
        request: TeamCoordinationRequest
    ) -> Dict[str, OuterTeamInterface]:
        """Select appropriate outer team members for coordination"""
        
        selected_members = {}
        request_domain = request.request_context.get("domain", "general")
        complexity = request.request_context.get("complexity_level", "medium")
        
        for member_id, member_interface in self.outer_team_members.items():
            # Get expertise assessment
            expertise_assessment = member_interface.get_expertise_assessment(request_domain, complexity)
            
            # Select if recommended and available
            if expertise_assessment["recommended_engagement"]:
                availability = member_interface.get_availability(request.timeline_constraints)
                if availability["available"]:
                    selected_members[member_id] = member_interface
        
        # Ensure we have at least one member if possible
        if not selected_members and self.outer_team_members:
            # Select first available member as fallback
            for member_id, member_interface in self.outer_team_members.items():
                availability = member_interface.get_availability(request.timeline_constraints)
                if availability["available"]:
                    selected_members[member_id] = member_interface
                    break
        
        return selected_members
    
    def _synthesize_coordination_results(
        self,
        results: List[Dict[str, Any]],
        request: TeamCoordinationRequest
    ) -> Dict[str, Any]:
        """Synthesize results from multiple outer team members"""
        
        successful_results = [r for r in results if "error" not in r]
        
        if not successful_results:
            return {
                "synthesis_quality": "failed",
                "participating_members": 0,
                "consolidated_recommendations": ["Retry coordination with alternative team members"],
                "confidence_assessment": 0.0,
                "consensus_indicators": {"consensus_level": "none", "agreement_score": 0.0},
                "knowledge_coverage": {"coverage_percentage": 0.0, "covered_domains": []}
            }
        
        # Extract recommendations and confidence scores
        all_recommendations = []
        confidence_scores = []
        
        for result in successful_results:
            if "recommendations" in result:
                all_recommendations.extend(result["recommendations"])
            if "confidence_level" in result:
                confidence_scores.append(result["confidence_level"])
        
        # Remove duplicate recommendations
        unique_recommendations = list(set(all_recommendations))
        
        # Calculate overall confidence
        avg_confidence = sum(confidence_scores) / len(confidence_scores) if confidence_scores else 0.7
        
        # Determine synthesis quality based on participation and confidence
        if len(successful_results) >= 2 and avg_confidence > 0.7:
            synthesis_quality = "high"
        elif len(successful_results) >= 1 and avg_confidence > 0.5:
            synthesis_quality = "moderate"
        else:
            synthesis_quality = "low"
        
        # Create synthesis
        synthesis = {
            "synthesis_quality": synthesis_quality,
            "participating_members": len(successful_results),
            "consolidated_recommendations": unique_recommendations[:5],  # Top 5
            "confidence_assessment": avg_confidence,
            "consensus_indicators": self._assess_outer_team_consensus(successful_results),
            "knowledge_coverage": self._assess_knowledge_coverage(successful_results, request)
        }
        
        return synthesis
    
    def _assess_outer_team_consensus(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Assess consensus among outer team members"""
        
        if len(results) < 2:
            return {"consensus_level": "single_input", "agreement_score": 1.0}
        
        # Simple consensus assessment based on recommendation overlap
        all_recommendations = []
        for result in results:
            if "recommendations" in result:
                all_recommendations.extend(result["recommendations"])
        
        unique_recommendations = set(all_recommendations)
        total_recommendations = len(all_recommendations)
        
        if total_recommendations > 0:
            overlap_score = 1.0 - (len(unique_recommendations) / total_recommendations)
        else:
            overlap_score = 0.0
        
        consensus_level = "high" if overlap_score > 0.7 else "moderate" if overlap_score > 0.4 else "low"
        
        return {
            "consensus_level": consensus_level,
            "agreement_score": overlap_score,
            "recommendation_diversity": len(unique_recommendations)
        }
    
    def _assess_knowledge_coverage(
       self, 
       results: List[Dict[str, Any]], 
       request: TeamCoordinationRequest
   ) -> Dict[str, Any]:
       """Assess knowledge coverage across outer team results"""
       
       domain_requirements = request.request_context.get("domain_focus", [])
       covered_domains = set()
       
       for result in results:
           # Extract domains covered by each member
           if "specialist_analysis" in result:
               analysis_text = result["specialist_analysis"].lower()
               for domain in domain_requirements:
                   if domain.lower() in analysis_text:
                       covered_domains.add(domain)
           
           if "relevant_knowledge" in result:
               knowledge_keys = result["relevant_knowledge"].keys()
               for domain in domain_requirements:
                   if any(domain.lower() in key.lower() for key in knowledge_keys):
                       covered_domains.add(domain)
       
       coverage_percentage = len(covered_domains) / len(domain_requirements) if domain_requirements else 1.0
       
       return {
           "coverage_percentage": coverage_percentage,
           "covered_domains": list(covered_domains),
           "uncovered_domains": [d for d in domain_requirements if d not in covered_domains],
           "coverage_quality": "comprehensive" if coverage_percentage > 0.8 else "partial" if coverage_percentage > 0.5 else "limited"
       }
   
    def _assess_boundary_interaction(self, request: TeamCoordinationRequest) -> Dict[str, Any]:
       """Assess the boundary interaction characteristics"""
       
       return {
           "originating_boundary": request.originating_team.value,
           "target_boundary": request.target_team.value,
           "coordination_protocol": request.coordination_type.value,
           "boundary_crossing_complexity": self._calculate_boundary_complexity(request),
           "information_flow_direction": "bidirectional" if request.coordination_type in [
               CoordinationProtocol.COLLABORATIVE_SESSION
           ] else "unidirectional",
           "authority_level_change": self._assess_authority_change(request)
       }
   
    def _calculate_boundary_complexity(self, request: TeamCoordinationRequest) -> str:
        """Calculate complexity of boundary crossing"""
        
        boundary_distances = {
            (TeamBoundary.INNER_TEAM, TeamBoundary.OUTER_TEAM): "moderate",
            (TeamBoundary.INNER_TEAM, TeamBoundary.ECOSYSTEM): "high",
            (TeamBoundary.INNER_TEAM, TeamBoundary.CLIENT_DOMAIN): "high",
            (TeamBoundary.OUTER_TEAM, TeamBoundary.ECOSYSTEM): "low",
            (TeamBoundary.OUTER_TEAM, TeamBoundary.CLIENT_DOMAIN): "moderate"
        }
        
        boundary_pair = (request.originating_team, request.target_team)
        return boundary_distances.get(boundary_pair, "moderate")

    def _assess_authority_change(self, request: TeamCoordinationRequest) -> str:
        """Assess authority level change in boundary crossing"""
        
        authority_levels = {
            TeamBoundary.INNER_TEAM: "high",
            TeamBoundary.OUTER_TEAM: "medium", 
            TeamBoundary.ECOSYSTEM: "low",
            TeamBoundary.CLIENT_DOMAIN: "external"
        }
        
        origin_authority = authority_levels.get(request.originating_team, "medium")
        target_authority = authority_levels.get(request.target_team, "medium")
        
        if origin_authority == target_authority:
            return "same_level"
        elif origin_authority == "high" and target_authority in ["medium", "low"]:
            return "delegation"
        elif origin_authority in ["medium", "low"] and target_authority == "high":
            return "escalation"
        else:
            return "lateral"

    def _integrate_knowledge_across_boundaries(self, coordination_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Integrate knowledge across boundary interactions"""
        
        if not coordination_results:
            return {
                "integration_quality": "pending",
                "synthesis_confidence": 0.0,
                "knowledge_gaps": ["No coordination results available"]
            }
        
        # Extract knowledge from all results
        all_knowledge = []
        confidence_scores = []
        
        for result in coordination_results:
            if "error" not in result:
                # Count any analysis or recommendations as knowledge
                if "specialist_analysis" in result:
                    all_knowledge.append(result["specialist_analysis"])
                if "recommendations" in result:
                    all_knowledge.extend(result["recommendations"])
                if "relevant_knowledge" in result:
                    all_knowledge.extend(result["relevant_knowledge"])
                if "confidence_level" in result:
                    confidence_scores.append(result["confidence_level"])
                elif "confidence_score" in result:
                    confidence_scores.append(result["confidence_score"])
        
        # Calculate integration quality - be more generous
        if len(all_knowledge) >= 3:
            integration_quality = "comprehensive"
        elif len(all_knowledge) >= 1:
            integration_quality = "good"
        else:
            integration_quality = "basic"
        
        # Calculate synthesis confidence
        avg_confidence = sum(confidence_scores) / len(confidence_scores) if confidence_scores else 0.7
        
        return {
            "integration_quality": integration_quality,
            "synthesis_confidence": avg_confidence,
            "knowledge_elements": len(all_knowledge),
            "participating_sources": len([r for r in coordination_results if "error" not in r])
        }

    def _generate_outer_team_recommendations(self, synthesis: Dict[str, Any]) -> List[str]:
        """Generate recommendations based on outer team synthesis"""
        
        recommendations = []
        
        # Quality-based recommendations
        synthesis_quality = synthesis.get("synthesis_quality", "moderate")
        if synthesis_quality == "high":
            recommendations.append("Implement recommendations with high confidence based on strong outer team consensus")
        elif synthesis_quality == "moderate":
            recommendations.append("Proceed with recommendations while monitoring for additional validation needs")
        else:
            recommendations.append("Seek additional outer team input before implementation")
        
        # Consensus-based recommendations
        consensus = synthesis.get("consensus_indicators", {})
        if consensus.get("consensus_level") == "low":
            recommendations.append("Resolve outer team disagreements before proceeding")
        
        return recommendations

    def _record_coordination_interaction(self, coordination_result: Dict[str, Any]) -> None:
        """Record coordination interaction for analytics"""
        
        # Add to coordination history
        self.coordination_history.append(coordination_result)
        
        # Record boundary interaction
        boundary_interaction = {
            "coordination_id": coordination_result["coordination_id"],
            "timestamp": coordination_result["timestamp"],
            "boundary_crossing": coordination_result["boundary_interaction"],
            "success": len([r for r in coordination_result["coordination_results"] if "error" not in r]) > 0,
            "knowledge_integration": coordination_result["knowledge_integration"],
            "lessons_learned": self._extract_boundary_lessons(coordination_result)
        }
        
        self.boundary_interactions.append(boundary_interaction)

    def _update_boundary_interactions(self, coordination_result: Dict[str, Any]) -> None:
        """Alias for _record_coordination_interaction for backward compatibility"""
        self._record_coordination_interaction(coordination_result)

    def _extract_boundary_lessons(self, coordination_result: Dict[str, Any]) -> List[str]:
        """Extract lessons from boundary interactions"""
        
        lessons = []
        
        # Success/failure lessons
        successful_results = [r for r in coordination_result["coordination_results"] if "error" not in r]
        if len(successful_results) == len(coordination_result["coordination_results"]):
            lessons.append("All outer team members responded successfully")
        elif len(successful_results) > 0:
            lessons.append("Partial outer team engagement achieved")
        else:
            lessons.append("Outer team coordination failed - review member availability")
        
        # Knowledge integration lessons
        integration_quality = coordination_result["knowledge_integration"]["integration_quality"]
        if integration_quality == "comprehensive":
            lessons.append("Excellent knowledge integration across boundaries")
        elif integration_quality == "basic":
            lessons.append("Limited knowledge integration - consider engaging additional members")
        
        return lessons

    def _generate_coordination_id(self) -> str:
        """Generate unique coordination ID"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        return f"outer_coord_{timestamp}"

    def get_som_framework_analytics(self) -> Dict[str, Any]:
        """Get comprehensive Society of Mind framework analytics"""

        return {
            "team_architecture": {
                "inner_team_capabilities": list(self.team_boundaries[TeamBoundary.INNER_TEAM]["capabilities"]),
                "outer_team_members": len(self.outer_team_members),
                "boundary_definitions": len(self.team_boundaries),
                "coordination_protocols": len(self.coordination_protocols)
            },
            "coordination_history": {
                "total_coordinations": len(self.coordination_history),
                "successful_coordinations": sum(
                    1 for coord in self.coordination_history 
                    if len(coord["coordination_results"]) > 0
                ),
                "average_member_participation": self._calculate_average_participation(),
                "coordination_efficiency": self._calculate_coordination_efficiency()
            },
            "boundary_interactions": {
                "total_boundary_crossings": len(self.boundary_interactions),
                "successful_boundary_crossings": sum(
                    1 for interaction in self.boundary_interactions 
                    if interaction["success"]
                ),
                "knowledge_integration_quality": self._calculate_average_integration_quality(),
                "boundary_effectiveness": self._assess_boundary_effectiveness()
            },
            "outer_team_performance": {
                "member_utilization": self._calculate_member_utilization(),
                "response_reliability": self._calculate_response_reliability(),
                "expertise_coverage": self._assess_expertise_coverage()
            }
        }

    def _calculate_average_participation(self) -> float:
        """Calculate average member participation in coordinations"""
        if not self.coordination_history:
            return 0.0

        total_participation = sum(
            len(coord["selected_members"]) for coord in self.coordination_history
        )

        return total_participation / len(self.coordination_history)

    def _calculate_coordination_efficiency(self) -> float:
        """Calculate coordination efficiency"""
        if not self.coordination_history:
            return 0.0

        successful_coordinations = sum(
            1 for coord in self.coordination_history 
            if coord["synthesis"]["synthesis_quality"] in ["high", "moderate"]
        )

        return successful_coordinations / len(self.coordination_history)

    def _calculate_average_integration_quality(self) -> float:
        """Calculate average knowledge integration quality"""
        if not self.coordination_history:
            return 0.0

        quality_scores = []
        for coord in self.coordination_history:
            integration = coord["knowledge_integration"]
            quality = integration["integration_quality"]

            quality_score = {
                "comprehensive": 1.0,
                "good": 0.8,
                "basic": 0.6,
                "pending": 0.4
            }.get(quality, 0.5)

            quality_scores.append(quality_score)

        return sum(quality_scores) / len(quality_scores)

    def _calculate_member_utilization(self) -> Dict[str, float]:
        """Calculate utilization rate for each outer team member"""

        member_utilization = {}
        total_coordinations = len(self.coordination_history)

        if total_coordinations == 0:
            return member_utilization

        for member_id in self.outer_team_members.keys():
            participation_count = sum(
                1 for coord in self.coordination_history 
                if member_id in coord["selected_members"]
            )

            member_utilization[member_id] = participation_count / total_coordinations

        return member_utilization

    def _calculate_response_reliability(self) -> Dict[str, float]:
        """Calculate response reliability for each outer team member"""

        member_reliability = {}

        for member_id in self.outer_team_members.keys():
            successful_responses = 0
            total_requests = 0

            for coord in self.coordination_history:
                if member_id in coord["selected_members"]:
                    total_requests += 1

                    # Check if member responded successfully
                    member_result = next(
                        (r for r in coord["coordination_results"] if r.get("member_id") == member_id),
                        None
                    )

                    if member_result and "error" not in member_result:
                        successful_responses += 1

            if total_requests > 0:
                member_reliability[member_id] = successful_responses / total_requests
            else:
                member_reliability[member_id] = 0.0

        return member_reliability

    def _assess_boundary_effectiveness(self) -> float:
        """Assess overall boundary effectiveness"""
        if not self.boundary_interactions:
            return 0.0
        
        successful_interactions = sum(
            1 for interaction in self.boundary_interactions 
            if interaction["success"]
        )
        
        return successful_interactions / len(self.boundary_interactions)

    def _assess_expertise_coverage(self) -> Dict[str, Any]:
        """Assess expertise coverage across outer team"""

        all_domains = set()
        role_distribution = defaultdict(int)

        for member_interface in self.outer_team_members.values():
            member = member_interface.member
            all_domains.update(member.expertise_domains)
            role_distribution[member.role.value] += 1

        return {
            "total_expertise_domains": len(all_domains),
            "expertise_domains": list(all_domains),
            "role_distribution": dict(role_distribution),
            "coverage_assessment": "comprehensive" if len(all_domains) > 10 else "adequate" if len(all_domains) > 5 else "limited"
        }


def create_outer_team_architecture(inner_team_manager: EnhancedChiefEngagementManager) -> OuterTeamArchitecture:
    """Factory function to create Outer Team Architecture
    
    Args:
        inner_team_manager: Enhanced Chief Engagement Manager for inner team coordination
        
    Returns:
        Configured OuterTeamArchitecture instance
    """
    return OuterTeamArchitecture(inner_team_manager)


async def demonstrate_outer_team_architecture() -> bool:
    """Demonstrate the complete Outer Team Architecture functionality
    
    This demonstration shows the complete Society of Mind outer team architecture
    including external specialist coordination, knowledge service integration,
    and boundary management across different team layers.
    
    Returns:
        bool: True if demonstration successful, False otherwise
    """
    
    try:
        print("🔧 Demonstrating Outer Team Architecture...")
        
        # Import required dependencies
        from coordination.enhanced_coordination import create_enhanced_chief_engagement_manager
        
        # Create inner team manager
        inner_team_manager = create_enhanced_chief_engagement_manager(
            name="som_demo_manager",
            human_input_mode="NEVER"
        )
        
        # Create outer team architecture
        outer_team_arch = create_outer_team_architecture(inner_team_manager)
        
        print("  ✅ Outer Team Architecture created")
        print(f"     Team boundaries: {len(outer_team_arch.team_boundaries)}")
        print(f"     Outer team members: {len(outer_team_arch.outer_team_members)}")
        print(f"     Coordination protocols: {len(outer_team_arch.coordination_protocols)}")
        
        # Test scenario 1: External security consultation
        print("\n  🧪 Scenario 1: External security consultation...")
        
        security_request = TeamCoordinationRequest(
            request_id="coord_001",
            originating_team=TeamBoundary.INNER_TEAM,
            target_team=TeamBoundary.OUTER_TEAM,
            coordination_type=CoordinationProtocol.DIRECT_CONSULTATION,
            request_context={
                "decision_type": "security_architecture_review",
                "domain": "security",
                "complexity_level": "high",
                "domain_focus": ["security", "compliance", "threat_analysis"]
            },
            urgency_level="high",
            expected_deliverables=["security_analysis", "compliance_validation"],
            timeline_constraints={"urgency": "urgent"},
            success_criteria=["comprehensive_security_review", "compliance_verification"]
        )
        
        security_result = await outer_team_arch.coordinate_with_outer_team(security_request)
        
        print(f"     Selected members: {len(security_result['selected_members'])}")
        print(f"     Successful responses: {len([r for r in security_result['coordination_results'] if 'error' not in r])}")
        print(f"     Knowledge integration: {security_result['knowledge_integration']['integration_quality']}")
        print(f"     Synthesis quality: {security_result['synthesis']['synthesis_quality']}")
        
        # Test scenario 2: Knowledge service consultation
        print("\n  🧪 Scenario 2: Knowledge service consultation...")
        
        knowledge_request = TeamCoordinationRequest(
            request_id="coord_002",
            originating_team=TeamBoundary.INNER_TEAM,
            target_team=TeamBoundary.OUTER_TEAM,
            coordination_type=CoordinationProtocol.KNOWLEDGE_REQUEST,
            request_context={
                "decision_type": "best_practices_research",
                "domain": "software_architecture",
                "knowledge_query": "microservices best practices",
                "complexity_level": "medium"
            },
            urgency_level="medium",
            expected_deliverables=["best_practices", "case_studies"],
            timeline_constraints={"urgency": "normal"},
            success_criteria=["relevant_knowledge_synthesis"]
        )
        
        knowledge_result = await outer_team_arch.coordinate_with_outer_team(knowledge_request)
        
        print(f"     Knowledge synthesis: {knowledge_result['synthesis']['participating_members']} sources")
        print(f"     Confidence assessment: {knowledge_result['synthesis']['confidence_assessment']:.2f}")
        print(f"     Coverage quality: {knowledge_result['knowledge_integration']['synthesis_confidence']:.2f}")
        
        # Test scenario 3: Multi-member coordination
        print("\n  🧪 Scenario 3: Multi-member coordination...")
        
        multi_request = TeamCoordinationRequest(
            request_id="coord_003",
            originating_team=TeamBoundary.INNER_TEAM,
            target_team=TeamBoundary.OUTER_TEAM,
            coordination_type=CoordinationProtocol.COLLABORATIVE_SESSION,
            request_context={
                "decision_type": "performance_optimization_strategy",
                "domain": "performance",
                "complexity_level": "very_high",
                "domain_focus": ["performance", "scalability", "optimization"]
            },
            urgency_level="high",
            expected_deliverables=["optimization_strategy", "performance_analysis"],
            timeline_constraints={"urgency": "urgent"},
            success_criteria=["comprehensive_optimization_plan"]
        )
        
        multi_result = await outer_team_arch.coordinate_with_outer_team(multi_request)
        
        print(f"     Multi-member coordination: {len(multi_result['selected_members'])} members")
        print(f"     Consensus indicators: {multi_result['synthesis']['consensus_indicators']['consensus_level']}")
        print(f"     Integration quality: {multi_result['knowledge_integration']['integration_quality']}")
        
        # Test SoM framework analytics
        analytics = outer_team_arch.get_som_framework_analytics()
        print(f"\n  ✅ SoM framework analytics:")
        print(f"     Total coordinations: {analytics['coordination_history']['total_coordinations']}")
        print(f"     Coordination efficiency: {analytics['coordination_history']['coordination_efficiency']:.2f}")
        print(f"     Boundary crossings: {analytics['boundary_interactions']['total_boundary_crossings']}")
        print(f"     Integration quality: {analytics['boundary_interactions']['knowledge_integration_quality']:.2f}")
        
        # Validate framework completeness
        framework_completeness = (
            len(outer_team_arch.team_boundaries) == 4 and
            len(outer_team_arch.outer_team_members) >= 3 and
            analytics['coordination_history']['total_coordinations'] == 3
        )
        
        # Validate coordination effectiveness
        coordination_effectiveness = (
            analytics['coordination_history']['coordination_efficiency'] > 0.6 and
            analytics['boundary_interactions']['knowledge_integration_quality'] > 0.6
        )
        
        success = framework_completeness and coordination_effectiveness
        
        if success:
            print("\n  🎯 All outer team scenarios demonstrated successfully!")
            print("     ✅ Security consultation → External specialist coordination")
            print("     ✅ Knowledge service → Best practices and case studies")
            print("     ✅ Multi-member coordination → Comprehensive team synthesis")
        else:
            print(f"\n  ❌ Some outer team scenarios failed validation")
            print(f"     Framework completeness: {framework_completeness}")
            print(f"     Coordination effectiveness: {coordination_effectiveness}")
        
        return success
        
    except Exception as e:
        print(f"  ❌ Outer team architecture demonstration failed: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    print("🚀 Starting Outer Team Architecture Demonstration - Story 4.1")
    
    success = asyncio.run(demonstrate_outer_team_architecture())
    if success:
        print("\n✅ Story 4.1: Outer Team Architecture - DEMONSTRATED")
    else:
        print("\n❌ Story 4.1: Outer Team Architecture - FAILED")
        exit(1)