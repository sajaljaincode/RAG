#!/usr/bin/env python3
"""Test wrapper for rag_with_context.py with automated input"""

import sys
import os
from io import StringIO

def test_rag_with_context():
    print("Testing rag_with_context.py with sample query...")
    
    original_input = input
    
    def mock_input(prompt=""):
        if "quit" in prompt.lower() or "exit" in prompt.lower():
            print(f"{prompt}quit")
            return "quit"
        else:
            print(f"{prompt}What is machine learning?")
            return "What is machine learning?"
    
    try:
        import builtins
        builtins.input = mock_input
        
        import rag_with_context
        print("✓ rag_with_context.py executed successfully")
        
    except Exception as e:
        print(f"✗ rag_with_context.py failed: {e}")
        import traceback
        traceback.print_exc()
    finally:
        builtins.input = original_input

if __name__ == "__main__":
    test_rag_with_context()
