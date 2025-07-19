#!/usr/bin/env python3
"""Test wrapper for keyword_1.py with automated input"""

import sys
import os
from io import StringIO

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Keyword Search'))

def test_keyword_search():
    print("Testing keyword_1.py with sample query...")
    
    original_input = input
    
    def mock_input(prompt=""):
        print(f"{prompt}machine learning")
        return "machine learning"
    
    try:
        import builtins
        builtins.input = mock_input
        
        import keyword_1
        print("✓ keyword_1.py executed successfully")
        
    except Exception as e:
        print(f"✗ keyword_1.py failed: {e}")
        import traceback
        traceback.print_exc()
    finally:
        builtins.input = original_input

if __name__ == "__main__":
    test_keyword_search()
