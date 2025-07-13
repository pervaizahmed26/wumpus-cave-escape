"""
Solution Converter Module

Converts PDDL planner output to the required solution format for Wumpus Cave Escape assignment.
Output format: walk [north|east|south|west], push [direction], shoot [direction], turn [direction]
"""

import re
import os
from typing import List, Dict, Tuple


class SolutionConverter:
    """Converts PDDL planner solutions to required format."""
    
    def __init__(self):
        self.actions = []
        self.path = []
    
    def convert_solution(self, pddl_solution_file: str, output_file: str) -> None:
        """
        Convert PDDL solution to required format.
        
        Args:
            pddl_solution_file: Path to the PDDL planner solution file
            output_file: Path for the converted solution file
        """
        if not os.path.exists(pddl_solution_file):
            raise FileNotFoundError(f"Solution file not found: {pddl_solution_file}")
        
        # Parse PDDL solution
        actions = self._parse_pddl_solution(pddl_solution_file)
        
        # Convert to required format
        converted_solution = self._convert_actions_to_path(actions)
        
        # Write output
        self._write_solution_file(converted_solution, output_file)
    
    def _parse_pddl_solution(self, solution_file: str) -> List[Dict]:
        """Parse PDDL solution file and extract actions."""
        actions = []
        
        with open(solution_file, 'r') as f:
            content = f.read()
        
        # Look for action patterns in PDDL solution
        # New patterns for Wumpus Cave Escape: walk, push, shoot, turn
        action_patterns = [
            r'\(walk\s+agent\s+loc_(-?\d+)_(-?\d+)\s+loc_(-?\d+)_(-?\d+)\s+(\w+)\)',
            r'\(push\s+agent\s+crate_(\d+)\s+loc_(-?\d+)_(-?\d+)\s+loc_(-?\d+)_(-?\d+)\s+loc_(-?\d+)_(-?\d+)\s+(\w+)\)',
            r'\(shoot\s+agent\s+loc_(-?\d+)_(-?\d+)\s+loc_(-?\d+)_(-?\d+)\s+(\w+)\)',
            r'\(turn\s+agent\s+loc_(-?\d+)_(-?\d+)\s+loc_(-?\d+)_(-?\d+)\s+(\w+)\)'
        ]
        
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if not line or line.startswith(';'):
                continue
                
            # Try to match different action patterns
            for i, pattern in enumerate(action_patterns):
                match = re.search(pattern, line)
                if match:
                    action_types = ['walk', 'push', 'shoot', 'turn']
                    actions.append({
                        'type': action_types[i],
                        'params': match.groups(),
                        'raw': line
                    })
                    break
        
        return actions
    
    def _convert_actions_to_path(self, actions: List[Dict]) -> List[str]:
        """Convert parsed actions to path format."""
        path = []
        
        for action in actions:
            action_type = action['type']
            params = action['params']
            
            if action_type == 'walk':
                # Walk: (walk agent loc_from_row loc_from_col loc_to_row loc_to_col direction)
                # params: (from_row, from_col, to_row, to_col, direction)
                direction = params[4]
                path.append(f"walk {direction}")
                
            elif action_type == 'push':
                # Push: (push agent crate_id loc_from_row loc_from_col loc_crate_row loc_crate_col loc_dest_row loc_dest_col direction)
                # params: (crate_id, from_row, from_col, crate_row, crate_col, dest_row, dest_col, direction)
                direction = params[7]
                path.append(f"push {direction}")
                
            elif action_type == 'shoot':
                # Shoot: (shoot agent loc_from_row loc_from_col loc_to_row loc_to_col direction)
                # params: (from_row, from_col, to_row, to_col, direction)
                direction = params[4]
                path.append(f"shoot {direction}")
                
            elif action_type == 'turn':
                # Turn: (turn agent loc_from_row loc_from_col loc_to_row loc_to_col direction)
                # params: (from_row, from_col, to_row, to_col, direction)
                direction = params[4]
                path.append(f"turn {direction}")
        
        return path
    
    def _get_direction(self, from_pos: Tuple[int, int], to_pos: Tuple[int, int]) -> str:
        """Determine direction of movement."""
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        
        if to_row < from_row:
            return "UP"
        elif to_row > from_row:
            return "DOWN"
        elif to_col < from_col:
            return "LEFT"
        elif to_col > from_col:
            return "RIGHT"
        else:
            return None
    
    def _write_solution_file(self, solution: List[str], output_file: str) -> None:
        """Write converted solution to file."""
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        with open(output_file, 'w') as f:
            for action in solution:
                f.write(f"{action}\n")
    
    def validate_solution(self, solution_file: str) -> bool:
        """
        Validate that a solution file is in the correct format.
        
        Args:
            solution_file: Path to the solution file to validate
            
        Returns:
            True if valid, False otherwise
        """
        if not os.path.exists(solution_file):
            return False
        
        valid_actions = {
            'walk north', 'walk south', 'walk east', 'walk west',
            'push north', 'push south', 'push east', 'push west',
            'shoot north', 'shoot south', 'shoot east', 'shoot west',
            'turn north', 'turn south', 'turn east', 'turn west'
        }
        
        try:
            with open(solution_file, 'r') as f:
                lines = f.readlines()
            
            for line in lines:
                action = line.strip()
                if action and action not in valid_actions:
                    return False
            
            return True
        except Exception:
            return False


def main():
    """Example usage of the SolutionConverter."""
    converter = SolutionConverter()
    
    try:
        # Example conversion
        converter.convert_solution(
            "solutions/example_solution.pddl.soln",
            "final_solutions/example-solution.txt"
        )
        print("Solution converted successfully!")
        
        # Validate the converted solution
        if converter.validate_solution("final_solutions/example-solution.txt"):
            print("Solution validation passed!")
        else:
            print("Solution validation failed!")
            
    except FileNotFoundError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main() 