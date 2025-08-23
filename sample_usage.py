#!/usr/bin/env python3
"""
Sample Usage Script for LangGraph Email Agent

This script demonstrates how to interact with the deployed email agent API.
"""

import requests
import json
import time
from typing import Dict, Any

class EmailAgentClient:
    """Client for interacting with the LangGraph Email Agent API"""
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
    
    def health_check(self) -> Dict[str, Any]:
        """Check if the service is healthy"""
        try:
            response = self.session.get(f"{self.base_url}/health")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e), "status": "unhealthy"}
    
    def process_email(self, email_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process an email through the agent workflow"""
        try:
            # Initialize the workflow state
            initial_state = {
                "emails": [email_data],
                "current_email": email_data,
                "email_category": "",
                "generated_email": "",
                "rag_queries": [],
                "retrieved_documents": "",
                "writer_messages": [],
                "sendable": False,
                "trials": 0
            }
            
            # Stream the workflow execution
            response = self.session.post(
                f"{self.base_url}/stream",
                json={"input": initial_state},
                stream=True
            )
            response.raise_for_status()
            
            results = []
            for line in response.iter_lines():
                if line:
                    try:
                        data = json.loads(line.decode('utf-8'))
                        results.append(data)
                    except json.JSONDecodeError:
                        continue
            
            return {"status": "success", "results": results}
            
        except requests.RequestException as e:
            return {"error": str(e), "status": "failed"}
    
    def get_workflow_info(self) -> Dict[str, Any]:
        """Get information about the available workflow"""
        try:
            response = self.session.get(f"{self.base_url}/")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e), "status": "failed"}

def main():
    """Main function demonstrating usage"""
    print("🚀 LangGraph Email Agent - Sample Usage")
    print("=" * 50)
    
    # Initialize client
    client = EmailAgentClient()
    
    # Check health
    print("\n1. Health Check:")
    health = client.health_check()
    print(f"   Status: {health}")
    
    # Get workflow info
    print("\n2. Workflow Information:")
    workflow_info = client.get_workflow_info()
    print(f"   Info: {json.dumps(workflow_info, indent=2)}")
    
    # Sample email data
    sample_email = {
        "id": "sample_123",
        "threadId": "thread_456",
        "messageId": "msg_789",
        "references": "",
        "sender": "customer@example.com",
        "subject": "Product Inquiry - Pricing Information",
        "body": "Hi, I'm interested in your product. Can you please provide pricing information and availability? Thanks!"
    }
    
    print(f"\n3. Processing Sample Email:")
    print(f"   From: {sample_email['sender']}")
    print(f"   Subject: {sample_email['subject']}")
    print(f"   Body: {sample_email['body']}")
    
    # Process the email
    print("\n4. Processing through AI Agent...")
    result = client.process_email(sample_email)
    
    if result.get("status") == "success":
        print("   ✅ Email processed successfully!")
        print("   📊 Results:")
        for i, step_result in enumerate(result.get("results", [])):
            print(f"      Step {i+1}: {step_result}")
    else:
        print(f"   ❌ Processing failed: {result.get('error', 'Unknown error')}")
    
    print("\n" + "=" * 50)
    print("🎯 Sample usage completed!")
    print("\nTo use with your own emails:")
    print("1. Deploy the API using: python deploy_api.py")
    print("2. Update the base_url in EmailAgentClient")
    print("3. Call process_email() with your email data")

if __name__ == "__main__":
    main()
