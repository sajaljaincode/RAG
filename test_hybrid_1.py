#!/usr/bin/env python3
"""Test wrapper for Hybrid_1.py with automated input"""

import sys
import os
from io import StringIO

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Hybrid Search'))

def test_hybrid_search():
    print("Testing Hybrid_1.py with sample query...")
    
    original_input = input
    
    def mock_input(prompt=""):
        print(f"{prompt}machine learning")
        return "machine learning"
    
    try:
        import builtins
        builtins.input = mock_input
        
        import Hybrid_1
        print("✓ Hybrid_1.py executed successfully")
        
    except Exception as e:
        print(f"✗ Hybrid_1.py failed: {e}")
        import traceback
        traceback.print_exc()
    finally:
        builtins.input = original_input

if __name__ == "__main__":
    test_hybrid_search()
