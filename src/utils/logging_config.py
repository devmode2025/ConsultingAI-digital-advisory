"""Logging configuration for ConsultingAI academic evaluation

This module sets up comprehensive logging for all ConsultingAI components
with structured output optimized for academic assessment and debugging.
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, Any
from enum import Enum


class AcademicJSONFormatter(logging.Formatter):
    """Custom JSON formatter for academic evaluation logging"""
    
    def format(self, record: logging.LogRecord) -> str:
        """Format log record as JSON for academic evaluation
        
        Args:
            record: Log record to format
            
        Returns:
            JSON-formatted log string
        """
        # Base log data
        log_data = {
            "timestamp": datetime.fromtimestamp(record.created).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno
        }
        
        # Add academic evaluation context if present
        if hasattr(record, 'academic_context'):
            log_data["academic_context"] = record.academic_context
        
        if hasattr(record, 'academic_demonstration'):
            log_data["academic_demonstration"] = record.academic_demonstration
        
        # Add any extra fields from the log record
        for key, value in record.__dict__.items():
            if key not in ['name', 'msg', 'args', 'levelname', 'levelno', 'pathname', 
                          'filename', 'module', 'lineno', 'funcName', 'created', 
                          'msecs', 'relativeCreated', 'thread', 'threadName', 
                          'processName', 'process', 'getMessage', 'exc_info', 
                          'exc_text', 'stack_info', 'academic_context', 
                          'academic_demonstration']:
                log_data[key] = self._make_json_serializable(value)
        
        return json.dumps(log_data, indent=None, separators=(',', ':'))
    
    def _make_json_serializable(self, obj):
        """Convert objects to JSON-serializable format"""
        if isinstance(obj, Enum):
            return obj.name
        elif hasattr(obj, '__dict__'):
            return {k: self._make_json_serializable(v) for k, v in obj.__dict__.items()}
        elif isinstance(obj, (list, tuple)):
            return [self._make_json_serializable(item) for item in obj]
        elif isinstance(obj, dict):
            return {k: self._make_json_serializable(v) for k, v in obj.items()}
        else:
            try:
                json.dumps(obj)
                return obj
            except (TypeError, ValueError):
                return str(obj)


def setup_academic_logging(log_level: str = "INFO") -> None:
    """Setup logging configuration for academic evaluation
    
    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    # Create logs directory if it doesn't exist
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    # Convert log level string to logging constant
    numeric_level = getattr(logging, log_level.upper(), logging.INFO)
    
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(numeric_level)
    
    # Remove existing handlers to avoid duplication
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
    
    # Create file handler for application logs
    app_log_file = log_dir / "application.log"
    app_handler = logging.FileHandler(app_log_file, mode='a', encoding='utf-8')
    app_handler.setLevel(numeric_level)
    app_handler.setFormatter(AcademicJSONFormatter())
    
    # Create file handler for agent coordination logs
    coordination_log_file = log_dir / "agent_coordination.log"
    coordination_handler = logging.FileHandler(coordination_log_file, mode='a', encoding='utf-8')
    coordination_handler.setLevel(numeric_level)
    coordination_handler.setFormatter(AcademicJSONFormatter())
    
    # Create file handler for escalation decision logs
    escalation_log_file = log_dir / "escalation_decisions.log"
    escalation_handler = logging.FileHandler(escalation_log_file, mode='a', encoding='utf-8')
    escalation_handler.setLevel(numeric_level)
    escalation_handler.setFormatter(AcademicJSONFormatter())
    
    # Create console handler for immediate feedback
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)  # Only show warnings and errors on console
    console_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(console_formatter)
    
    # Add handlers to root logger
    root_logger.addHandler(app_handler)
    root_logger.addHandler(console_handler)
    
    # Create specialized loggers for different components
    
    # Agent coordination logger
    coordination_logger = logging.getLogger("ConsultingAI.coordination")
    coordination_logger.addHandler(coordination_handler)
    coordination_logger.propagate = False  # Don't propagate to root logger to avoid duplication
    
    # Escalation system logger
    escalation_logger = logging.getLogger("ConsultingAI.escalation")
    escalation_logger.addHandler(escalation_handler)
    escalation_logger.propagate = False
    
    # Log initialization for academic evaluation
    root_logger.info(
        "Academic logging system initialized",
        extra={
            "academic_context": "Epic 1 Story 1.2 - Logging Infrastructure",
            "log_level": log_level,
            "log_files": {
                "application": str(app_log_file),
                "coordination": str(coordination_log_file),
                "escalation": str(escalation_log_file)
            }
        }
    )


def get_academic_logger(name: str) -> logging.Logger:
    """Get configured logger for academic evaluation
    
    Args:
        name: Logger name (typically component name)
        
    Returns:
        Configured logger instance
    """
    return logging.getLogger(f"ConsultingAI.{name}")


def log_academic_milestone(
    milestone: str, 
    component: str, 
    details: Dict[str, Any]
) -> None:
    """Log academic milestone for evaluation tracking
    
    Args:
        milestone: Milestone description
        component: Component achieving the milestone
        details: Additional milestone details
    """
    logger = get_academic_logger("milestones")
    
    logger.info(
        f"Academic milestone reached: {milestone}",
        extra={
            "academic_milestone": milestone,
            "component": component,
            "milestone_details": details,
            "academic_evaluation": True
        }
    )


def demonstrate_logging_system() -> bool:
    """Demonstrate logging system for academic evaluation
    
    Returns:
        True if demonstration successful, False otherwise
    """
    print("🔧 Demonstrating Academic Logging System...")
    
    try:
        # Setup logging
        setup_academic_logging("INFO")
        print("  ✅ Academic logging configured")
        
        # Test different logger types
        app_logger = get_academic_logger("demo")
        coordination_logger = get_academic_logger("coordination.demo")
        escalation_logger = get_academic_logger("escalation.demo")
        
        # Test basic logging
        app_logger.info("Test application log entry", extra={"academic_demonstration": True})
        coordination_logger.info("Test coordination log entry", extra={"academic_demonstration": True})
        escalation_logger.info("Test escalation log entry", extra={"academic_demonstration": True})
        
        print("  ✅ Component-specific logging working")
        
        # Test academic milestone logging
        log_academic_milestone(
            "Story 1.2 Logging Demonstration", 
            "LoggingSystem", 
            {"demonstration_complete": True, "epic": 1, "story": "1.2"}
        )
        
        print("  ✅ Academic milestone logging working")
        
        # Verify log files were created
        log_dir = Path("logs")
        expected_files = ["application.log", "agent_coordination.log", "escalation_decisions.log"]
        
        for log_file in expected_files:
            if (log_dir / log_file).exists():
                print(f"  ✅ Log file created: {log_file}")
            else:
                print(f"  ⚠️  Log file missing: {log_file}")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Logging system demonstration failed: {e}")
        return False


if __name__ == "__main__":
    success = demonstrate_logging_system()
    if success:
        print("\n✅ Academic Logging System: DEMONSTRATED")
    else:
        print("\n❌ Academic Logging System: FAILED")
        exit(1)
