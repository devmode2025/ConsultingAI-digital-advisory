#!/usr/bin/env python3
"""Quick verification that ConsultingAI LLM setup is complete"""

import subprocess
import sys

def check_ollama_service():
    """Check if Ollama service is running"""
    try:
        result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
        if 'ollama serve' in result.stdout:
            print("✅ Ollama service is running")
            return True
        else:
            print("❌ Ollama service not found")
            return False
    except Exception as e:
        print(f"❌ Error checking service: {e}")
        return False

def check_model_available():
    """Check if llama3.2:3b is downloaded"""
    try:
        result = subprocess.run(['ollama', 'list'], capture_output=True, text=True)
        if 'llama3.2:3b' in result.stdout:
            print("✅ Llama 3.2:3b model is available")
            return True
        else:
            print("❌ Llama 3.2:3b model not found")
            print("   Run: ollama pull llama3.2:3b")
            return False
    except Exception as e:
        print(f"❌ Error checking models: {e}")
        return False

def test_model_response():
    """Test model can generate responses"""
    try:
        result = subprocess.run([
            'ollama', 'run', 'llama3.2:3b', 
            'Respond with exactly: ConsultingAI setup successful'
        ], capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0 and 'successful' in result.stdout:
            print("✅ Model responding correctly")
            return True
        else:
            print("❌ Model test failed")
            return False
    except subprocess.TimeoutExpired:
        print("⚠️  Model response timeout (may still be loading)")
        return False
    except Exception as e:
        print(f"❌ Model test error: {e}")
        return False

if __name__ == "__main__":
    print("🧪 ConsultingAI Setup Verification")
    print("=" * 40)
    
    all_good = True
    
    # Check service
    if not check_ollama_service():
        all_good = False
    
    # Check model
    if not check_model_available():
        all_good = False
    
    # Test model (only if available)
    if all_good:
        if not test_model_response():
            all_good = False
    
    print("\n" + "=" * 40)
    if all_good:
        print("🎉 Setup complete! ConsultingAI is ready.")
        print("   Next: python src/main.py")
    else:
        print("⚠️  Setup incomplete. Follow the steps above.")
    
    sys.exit(0 if all_good else 1)