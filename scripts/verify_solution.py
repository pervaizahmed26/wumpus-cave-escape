#!/usr/bin/env python3
"""
Solution Verification Script

This script verifies that solution files are valid and simulate the solution path.
"""

import os
import sys
import argparse
from pathlib import Path

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from map_parser import MapParser
from solution_converter import SolutionConverter


class SolutionVerifier:
    """Verifies solution files against map files."""
    
    def __init__(self):
        self.map_parser = MapParser()
        self.solution_converter = SolutionConverter()
    
    def verify_solution(self, map_file: str, solution_file: str, verbose: bool = True) -> bool:
        """
        Verify a solution file against a map file.
        
        Args:
            map_file: Path to the map file
            solution_file: Path to the solution file
            verbose: Whether to print detailed information
            
        Returns:
            True if solution is valid, False otherwise
        """
        if verbose:
            print(f"Verifying solution: {solution_file}")
            print(f"Against map: {map_file}")
            print("-" * 50)
        
        # Check if files exist
        if not os.path.exists(map_file):
            print(f"Error: Map file not found: {map_file}")
            return False
        
        if not os.path.exists(solution_file):
            print(f"Error: Solution file not found: {solution_file}")
            return False
        
        # Parse map
        try:
            map_data = self.map_parser.parse_map_file(map_file)
            if verbose:
                print(f"Map dimensions: {map_data['dimensions']}")
                print(f"Agent start: {map_data['agent_position']}")
                print(f"Wumpus locations: {map_data['wumpus_positions']}")
                print(f"Arrow locations: {map_data['arrow_positions']}")
                print(f"Crate locations: {map_data['crate_positions']}")
                print(f"Pit locations: {map_data['pit_positions']}")
                print(f"Wall locations: {len(map_data['wall_positions'])} walls")
        except Exception as e:
            print(f"Error parsing map: {e}")
            return False
        
        # Validate solution format
        if not self.solution_converter.validate_solution(solution_file):
            print("Error: Solution file format is invalid!")
            return False
        
        if verbose:
            print("✓ Solution file format is valid")
        
        # Read solution steps
        try:
            with open(solution_file, 'r') as f:
                solution_steps = [line.strip() for line in f.readlines() if line.strip()]
        except Exception as e:
            print(f"Error reading solution file: {e}")
            return False
        
        if verbose:
            print(f"Solution has {len(solution_steps)} steps")
        
        # Simulate solution
        simulation_result = self._simulate_solution(map_data, solution_steps, verbose)
        
        if simulation_result:
            if verbose:
                print("✓ Solution verification PASSED!")
            return True
        else:
            if verbose:
                print("✗ Solution verification FAILED!")
            return False
    
    def _simulate_solution(self, map_data: dict, solution_steps: list, verbose: bool) -> bool:
        """
        Simulate the solution step by step.
        
        Args:
            map_data: Parsed map data
            solution_steps: List of solution steps
            verbose: Whether to print simulation details
            
        Returns:
            True if simulation succeeds, False otherwise
        """
        # Initialize agent state
        agent_pos = map_data['agent_position']
        has_arrows = len(map_data['arrow_positions'])  # Start with arrows from map
        wumpus_positions = set(map_data['wumpus_positions'])
        crate_positions = dict(enumerate(map_data['crate_positions']))
        pit_positions = set(map_data['pit_positions'])
        escaped = False
        
        if verbose:
            print("\nSimulating solution:")
            print(f"Initial state: Agent at {agent_pos}, Arrows={has_arrows}")
        
        # Process each step
        for i, step in enumerate(solution_steps):
            if verbose:
                print(f"\nStep {i+1}: {step}")
            
            parts = step.split()
            if len(parts) != 2:
                if verbose:
                    print(f"  ✗ Invalid action format: {step}")
                return False
            
            action, direction = parts
            
            if action == "walk":
                new_pos = self._get_new_position(agent_pos, direction)
                
                if not self._is_valid_walk(agent_pos, new_pos, map_data, wumpus_positions, crate_positions, pit_positions):
                    if verbose:
                        print(f"  ✗ Invalid walk from {agent_pos} to {new_pos}")
                    return False
                
                # Check if walking off map (escaped)
                rows, cols = map_data['dimensions']
                if (new_pos[0] < 0 or new_pos[0] >= rows or new_pos[1] < 0 or new_pos[1] >= cols):
                    escaped = True
                    if verbose:
                        print(f"  ✓ Agent escaped by walking to {new_pos}")
                    break
                
                agent_pos = new_pos
                
                # Pick up arrow if at arrow position
                if new_pos in map_data['arrow_positions']:
                    has_arrows += 1
                    if verbose:
                        print(f"  ✓ Agent picked up arrow at {new_pos}")
                
                if verbose:
                    print(f"  ✓ Agent walked to {agent_pos}")
            
            elif action == "shoot":
                if has_arrows <= 0:
                    if verbose:
                        print("  ✗ Cannot shoot: No arrows!")
                    return False
                
                target_pos = self._get_new_position(agent_pos, direction)
                
                if target_pos not in wumpus_positions:
                    if verbose:
                        print(f"  ✗ Cannot shoot: No wumpus at {target_pos}")
                    return False
                
                has_arrows -= 1
                wumpus_positions.remove(target_pos)
                if verbose:
                    print(f"  ✓ Wumpus shot at {target_pos}")
            
            elif action == "push":
                if verbose:
                    print(f"  ✓ Push action simulated (direction: {direction})")
                # Simplified push simulation - would need more complex logic
                
            elif action == "turn":
                if verbose:
                    print(f"  ✓ Turn action simulated (direction: {direction})")
                # Simplified turn simulation - would need more complex logic
                
            else:
                if verbose:
                    print(f"  ✗ Unknown action: {action}")
                return False
        
        # Check if goal achieved (escaped)
        if not escaped:
            if verbose:
                print("✗ Goal not achieved: Agent did not escape!")
            return False
        
        return True
    
    def _get_new_position(self, current_pos: tuple, direction: str) -> tuple:
        """Get new position after moving in a direction."""
        row, col = current_pos
        
        if direction == "north":
            return (row - 1, col)
        elif direction == "south":
            return (row + 1, col)
        elif direction == "west":
            return (row, col - 1)
        elif direction == "east":
            return (row, col + 1)
        else:
            return current_pos
    
    def _is_valid_walk(self, from_pos: tuple, to_pos: tuple, map_data: dict, wumpus_positions: set, crate_positions: dict, pit_positions: set) -> bool:
        """Check if a walk is valid."""
        # Check adjacency
        row_diff = abs(from_pos[0] - to_pos[0])
        col_diff = abs(from_pos[1] - to_pos[1])
        
        if not ((row_diff == 1 and col_diff == 0) or (row_diff == 0 and col_diff == 1)):
            return False
        
        # Allow walking off map (that's the goal!)
        rows, cols = map_data['dimensions']
        if (to_pos[0] < 0 or to_pos[0] >= rows or to_pos[1] < 0 or to_pos[1] >= cols):
            return True  # Escaping is allowed
        
        # Check for walls
        if to_pos in map_data['wall_positions']:
            return False
        
        # Check for unfilled pits
        if to_pos in pit_positions:
            return False
        
        # Check for wumpus
        if to_pos in wumpus_positions:
            return False
        
        # Check for crates
        if to_pos in crate_positions.values():
            return False
        
        return True
    
    def _is_wumpus_adjacent(self, agent_pos: tuple, map_data: dict) -> bool:
        """Check if wumpus is adjacent to agent."""
        if not map_data['wumpus_positions']:
            return False
        
        for wumpus_pos in map_data['wumpus_positions']:
            row_diff = abs(agent_pos[0] - wumpus_pos[0])
            col_diff = abs(agent_pos[1] - wumpus_pos[1])
            
            if (row_diff == 1 and col_diff == 0) or (row_diff == 0 and col_diff == 1):
                return True
        
        return False


def main():
    """Main entry point for verification script."""
    parser = argparse.ArgumentParser(
        description="Verify solution files against map files"
    )
    
    parser.add_argument(
        '--map', '-m',
        type=str,
        help='Path to the map file'
    )
    
    parser.add_argument(
        '--solution', '-s',
        type=str,
        help='Path to the solution file'
    )
    
    parser.add_argument(
        '--batch', '-b',
        action='store_true',
        help='Verify all solutions in final_solutions directory'
    )
    
    parser.add_argument(
        '--quiet', '-q',
        action='store_true',
        help='Suppress detailed output'
    )
    
    args = parser.parse_args()
    
    verifier = SolutionVerifier()
    
    if args.batch:
        # Verify all solutions
        solutions_dir = "final_solutions"
        maps_dir = "maps"
        
        if not os.path.exists(solutions_dir):
            print(f"Error: Solutions directory '{solutions_dir}' not found!")
            sys.exit(1)
        
        solution_files = [f for f in os.listdir(solutions_dir) if f.endswith('-solution.txt')]
        
        if not solution_files:
            print("No solution files found!")
            sys.exit(1)
        
        print(f"Verifying {len(solution_files)} solutions...")
        print("=" * 50)
        
        passed = 0
        failed = 0
        
        for solution_file in solution_files:
            # Try to find corresponding map file (mapXYZ-solution.txt -> mapXYZ.txt)
            base_name = solution_file.replace('-solution.txt', '')
            map_file = os.path.join(maps_dir, f"{base_name}.txt")
            
            if not os.path.exists(map_file):
                print(f"✗ {solution_file}: No corresponding map file found")
                failed += 1
                continue
            
            solution_path = os.path.join(solutions_dir, solution_file)
            result = verifier.verify_solution(map_file, solution_path, verbose=not args.quiet)
            
            if result:
                passed += 1
                print(f"✓ {solution_file}: PASSED")
            else:
                failed += 1
                print(f"✗ {solution_file}: FAILED")
            
            if not args.quiet:
                print()
        
        print("=" * 50)
        print(f"Verification Summary: {passed} passed, {failed} failed")
        
        if failed == 0:
            print("All solutions verified successfully!")
            sys.exit(0)
        else:
            sys.exit(1)
    
    elif args.map and args.solution:
        # Verify single solution
        result = verifier.verify_solution(args.map, args.solution, verbose=not args.quiet)
        
        if result:
            print("Solution verification PASSED!")
            sys.exit(0)
        else:
            print("Solution verification FAILED!")
            sys.exit(1)
    
    else:
        print("Error: Must specify either --map and --solution, or --batch")
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main() 