#!/usr/bin/env python3
"""
Build script to compile Mermaid diagrams from markdown files to SVG.
Usage: python build-diagrams.py
"""

import os
import re
from pathlib import Path
from mermaid import Mermaid

# Directories
DOCS_DIR = Path("docs")
DIAGRAMS_DIR = Path("docs/diagrams")

def ensure_dirs():
    """Create necessary directories."""
    DIAGRAMS_DIR.mkdir(parents=True, exist_ok=True)

def extract_mermaid_blocks(md_file):
    """Extract Mermaid code blocks from a markdown file."""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match ```mermaid ... ``` blocks
    pattern = r'```mermaid\n(.*?)```'
    matches = re.findall(pattern, content, re.DOTALL)
    
    return matches

def compile_diagram(mermaid_code, output_name):
    """Compile a single Mermaid diagram to SVG."""
    try:
        m = Mermaid(mermaid_code)
        svg = m.svg_response.text
        
        output_file = DIAGRAMS_DIR / f"{output_name}.svg"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(svg)
        
        print(f"  OK Compiled: {output_file}")
        return True
    except Exception as e:
        print(f"  FAIL Failed: {output_name} - {e}")
        return False

def process_markdown_file(md_file):
    """Process a single markdown file and compile its diagrams."""
    print(f"\nProcessing: {md_file}")
    
    blocks = extract_mermaid_blocks(md_file)
    if not blocks:
        print("  No Mermaid diagrams found")
        return 0
    
    success_count = 0
    for i, block in enumerate(blocks):
        # Generate a unique name from the file and block index
        stem = md_file.stem
        name = f"{stem}_diagram_{i+1}"
        if compile_diagram(block, name):
            success_count += 1
    
    return success_count

def main():
    """Main build function."""
    print("=" * 60)
    print("Mermaid Diagram Builder")
    print("=" * 60)
    
    ensure_dirs()
    
    # Find all markdown files in docs/
    md_files = list(DOCS_DIR.rglob("*.md"))
    
    if not md_files:
        print("No markdown files found in docs/")
        return
    
    print(f"\nFound {len(md_files)} markdown files")
    
    total_success = 0
    total_diagrams = 0
    
    for md_file in md_files:
        count = process_markdown_file(md_file)
        total_success += count
        total_diagrams += count
    
    print("\n" + "=" * 60)
    print(f"Results: {total_success}/{total_diagrams} diagrams compiled successfully")
    print("=" * 60)

if __name__ == "__main__":
    main()
