#!/usr/bin/env python3
"""
Solve All Maps Script

This script processes all map files in the maps directory and generates solutions for each.
"""

import os
import sys
import glob
from pathlib import Path

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import WumpusEscapeMain


def solve_all_maps(maps_dir: str = "maps", output_dir: str = ".", verbose: bool = True):
    """
    Solve all maps in the specified directory.
    
    Args:
        maps_dir: Directory containing map files
        output_dir: Directory for output files
        verbose: Whether to print detailed progress
    """
    if not os.path.exists(maps_dir):
        print(f"Error: Maps directory '{maps_dir}' not found!")
        return False
    
    # Find all map files
    map_files = glob.glob(os.path.join(maps_dir, "*.txt"))
    
    if not map_files:
        print(f"No map files found in '{maps_dir}'")
        return False
    
    print(f"Found {len(map_files)} map files to process:")
    for map_file in map_files:
        print(f"  - {os.path.basename(map_file)}")
    print()
    
    # Initialize solver
    solver = WumpusEscapeMain()
    
    # Process each map
    results = []
    successful = 0
    failed = 0
    
    for map_file in map_files:
        map_name = os.path.basename(map_file)
        print(f"Processing {map_name}...")
        print("-" * 50)
        
        try:
            result = solver.process_map(map_file, output_dir)
            if result:
                results.append({
                    'map': map_name,
                    'status': 'SUCCESS',
                    'solution': result
                })
                successful += 1
                if verbose:
                    print(f"✓ {map_name} solved successfully!")
                    print(f"  Solution: {result}")
            else:
                results.append({
                    'map': map_name,
                    'status': 'FAILED',
                    'solution': None
                })
                failed += 1
                if verbose:
                    print(f"✗ {map_name} failed to solve!")
        
        except Exception as e:
            results.append({
                'map': map_name,
                'status': 'ERROR',
                'solution': None,
                'error': str(e)
            })
            failed += 1
            if verbose:
                print(f"✗ {map_name} encountered an error: {e}")
        
        print()
    
    # Print summary
    print("=" * 60)
    print("BATCH PROCESSING SUMMARY")
    print("=" * 60)
    print(f"Total maps processed: {len(map_files)}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Success rate: {successful/len(map_files)*100:.1f}%")
    print()
    
    # Detailed results
    if verbose:
        print("Detailed Results:")
        print("-" * 40)
        for result in results:
            status_symbol = "✓" if result['status'] == 'SUCCESS' else "✗"
            print(f"{status_symbol} {result['map']}: {result['status']}")
            if result['status'] == 'SUCCESS':
                print(f"  Solution: {result['solution']}")
            elif result['status'] == 'ERROR':
                print(f"  Error: {result['error']}")
            print()
    
    return successful == len(map_files)


def main():
    """Main entry point for solve_all script."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Solve all maps in the maps directory"
    )
    
    parser.add_argument(
        '--maps-dir', '-m',
        type=str,
        default='maps',
        help='Directory containing map files (default: maps)'
    )
    
    parser.add_argument(
        '--output-dir', '-o',
        type=str,
        default='.',
        help='Output directory for generated files (default: current directory)'
    )
    
    parser.add_argument(
        '--quiet', '-q',
        action='store_true',
        help='Suppress detailed output'
    )
    
    args = parser.parse_args()
    
    # Solve all maps
    success = solve_all_maps(
        maps_dir=args.maps_dir,
        output_dir=args.output_dir,
        verbose=not args.quiet
    )
    
    if success:
        print("All maps solved successfully!")
        sys.exit(0)
    else:
        print("Some maps failed to solve.")
        sys.exit(1)


if __name__ == "__main__":
    main() 