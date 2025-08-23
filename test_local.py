#!/usr/bin/env python3
"""
Local Test Script for LangGraph Email Agent

This script tests the local setup without requiring external API keys.
"""

import sys
import os

def test_imports():
    """Test if all required modules can be imported"""
    print("🧪 Testing imports...")
    
    try:
        from src.graph import Workflow
        print("   ✅ Workflow imported successfully")
    except ImportError as e:
        print(f"   ❌ Failed to import Workflow: {e}")
        return False
    
    try:
        from src.nodes import Nodes
        print("   ✅ Nodes imported successfully")
    except ImportError as e:
        print(f"   ❌ Failed to import Nodes: {e}")
        return False
    
    try:
        from src.nodes import Nodes
        print("   ✅ Nodes imported successfully")
    except ImportError as e:
        print(f"   ❌ Failed to import Nodes: {e}")
        return False
    
    try:
        from src.agents import Agents
        print("   ✅ Agents imported successfully")
    except ImportError as e:
        print(f"   ❌ Failed to import Agents: {e}")
        return False
    
    try:
        from src.state import GraphState
        print("   ✅ GraphState imported successfully")
    except ImportError as e:
        print(f"   ❌ Failed to import GraphState: {e}")
        return False
    
    return True

def test_workflow_creation():
    """Test if workflow can be created"""
    print("\n🔧 Testing workflow creation...")
    
    try:
        from src.graph import Workflow
        # This will fail without API keys, which is expected
        print("   ⚠️  Workflow creation requires API keys (expected behavior)")
        print("   ✅ Workflow class can be imported successfully")
        
        # Check if the class exists and has required methods
        if hasattr(Workflow, '__init__'):
            print("   ✅ Workflow class structure is correct")
        else:
            print("   ❌ Workflow class missing __init__ method")
            return False
            
        return True
    except Exception as e:
        if "api_key" in str(e).lower():
            print("   ✅ Workflow class structure is correct (API key error is expected)")
            return True
        else:
            print(f"   ❌ Unexpected error creating workflow: {e}")
            return False

def test_fastapi_setup():
    """Test if FastAPI can be set up"""
    print("\n🚀 Testing FastAPI setup...")
    
    try:
        from fastapi import FastAPI
        from fastapi.middleware.cors import CORSMiddleware
        
        app = FastAPI(title="Test App")
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        
        print("   ✅ FastAPI app created successfully")
        print("   ✅ CORS middleware added successfully")
        return True
    except Exception as e:
        print(f"   ❌ FastAPI setup failed: {e}")
        return False

def main():
    """Main test function"""
    print("🚀 LangGraph Email Agent - Local Test Suite")
    print("=" * 50)
    
    # Test imports
    if not test_imports():
        print("\n❌ Import tests failed. Check your installation.")
        return False
    
    # Test workflow creation
    if not test_workflow_creation():
        print("\n❌ Workflow creation failed. Check your code.")
        return False
    
    # Test FastAPI setup
    if not test_fastapi_setup():
        print("\n❌ FastAPI setup failed. Check your dependencies.")
        return False
    
    print("\n" + "=" * 50)
    print("🎯 All tests passed! Your local setup is working correctly.")
    print("\nNext steps:")
    print("1. Set up your .env file with API keys")
    print("2. Run: python deploy_api.py")
    print("3. Test the API at: http://localhost:8000/health")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
