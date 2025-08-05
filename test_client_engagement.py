#!/usr/bin/env python3
"""Test script for Advanced Client Engagement Framework"""

import asyncio
from src.advanced_capabilities.client_engagement_framework import demonstrate_advanced_client_engagement

async def main():
    """Run the client engagement demonstration"""
    print("🧪 Testing Advanced Client Engagement Framework...")
    try:
        await demonstrate_advanced_client_engagement()
        print("✅ Client engagement demonstration completed successfully!")
    except Exception as e:
        print(f"❌ Client engagement demonstration failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())