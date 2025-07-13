"""
PDDL Generator Module

Generates PDDL problem files from parsed map data for Wumpus Cave Escape assignment.
"""

import os
from typing import Dict, List, Tuple
from map_parser import MapParser


class PDDLGenerator:
    """Generator for PDDL problem files from map data."""
    
    def __init__(self, domain_file: str = "domain/wumpus.pddl"):
        self.domain_file = domain_file
        self.map_data = None
    
    def generate_problem_file(self, map_data: Dict, output_file: str) -> None:
        """
        Generate a PDDL problem file from map data.
        
        Args:
            map_data: Dictionary containing parsed map information
            output_file: Path for the output PDDL problem file
        """
        self.map_data = map_data
        
        problem_content = self._generate_problem_content()
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        with open(output_file, 'w') as f:
            f.write(problem_content)
    
    def _generate_problem_content(self) -> str:
        """Generate the complete PDDL problem content."""
        problem_name = "wumpus-cave-escape"
        domain_name = "wumpus-escape"
        
        content = f"""(define (problem {problem_name})
  (:domain {domain_name})
  
  (:objects
{self._generate_objects()}
  )
  
  (:init
{self._generate_initial_state()}
  )
  
  (:goal
{self._generate_goal()}
  )
)
"""
        return content
    
    def _generate_objects(self) -> str:
        """Generate the objects section of the PDDL problem."""
        rows, cols = self.map_data['dimensions']
        objects = []
        
        # Generate location objects (including boundary locations for escape)
        for row in range(-1, rows + 1):
            for col in range(-1, cols + 1):
                objects.append(f"    loc_{row}_{col} - location")
        
        # Add agent
        objects.append("    agent - agent")
        
        # Add directions
        objects.append("    north - direction")
        objects.append("    south - direction")
        objects.append("    east - direction")
        objects.append("    west - direction")
        
        # Add crates
        crate_count = len(self.map_data['crate_positions'])
        for i in range(crate_count):
            objects.append(f"    crate_{i} - crate")
        
        return "\n".join(objects)
    
    def _generate_initial_state(self) -> str:
        """Generate the initial state section."""
        init_facts = []
        
        # Agent position
        if self.map_data['agent_position']:
            row, col = self.map_data['agent_position']
            init_facts.append(f"    (at agent loc_{row}_{col})")
        
        # Direction facts
        init_facts.append("    (north north)")
        init_facts.append("    (south south)")
        init_facts.append("    (east east)")
        init_facts.append("    (west west)")
        
        # Walls
        for row, col in self.map_data['wall_positions']:
            init_facts.append(f"    (wall-at loc_{row}_{col})")
        
        # Wumpus positions
        for row, col in self.map_data['wumpus_positions']:
            init_facts.append(f"    (wumpus-at loc_{row}_{col})")
        
        # Arrow positions
        for row, col in self.map_data['arrow_positions']:
            init_facts.append(f"    (arrow-at loc_{row}_{col})")
        
        # Crate positions
        for i, (row, col) in enumerate(self.map_data['crate_positions']):
            init_facts.append(f"    (crate-at crate_{i} loc_{row}_{col})")
        
        # Pit positions
        for row, col in self.map_data['pit_positions']:
            init_facts.append(f"    (pit-at loc_{row}_{col})")
        
        # Horizontal turntables
        for row, col in self.map_data['horizontal_turntables']:
            init_facts.append(f"    (horizontal-turntable loc_{row}_{col})")
        
        # Vertical turntables
        for row, col in self.map_data['vertical_turntables']:
            init_facts.append(f"    (vertical-turntable loc_{row}_{col})")
        
        # Empty positions
        for row, col in self.map_data['empty_positions']:
            init_facts.append(f"    (empty loc_{row}_{col})")
        
        # Off-map positions (boundary locations)
        rows, cols = self.map_data['dimensions']
        for row in range(-1, rows + 1):
            for col in range(-1, cols + 1):
                if row == -1 or row == rows or col == -1 or col == cols:
                    init_facts.append(f"    (off-map loc_{row}_{col})")
        
        # Adjacent relationships
        init_facts.extend(self._generate_adjacency_facts())
        
        return "\n".join(init_facts)
    
    def _generate_adjacency_facts(self) -> List[str]:
        """Generate adjacency facts for all locations including boundary."""
        facts = []
        rows, cols = self.map_data['dimensions']
        
        # Include boundary locations for escape
        for row in range(-1, rows + 1):
            for col in range(-1, cols + 1):
                current_loc = f"loc_{row}_{col}"
                
                # Check all four directions
                directions = [
                    (row - 1, col, "north"),  # North
                    (row + 1, col, "south"),  # South
                    (row, col - 1, "west"),   # West
                    (row, col + 1, "east")    # East
                ]
                
                for new_row, new_col, direction in directions:
                    if (-1 <= new_row <= rows and -1 <= new_col <= cols):
                        adjacent_loc = f"loc_{new_row}_{new_col}"
                        facts.append(f"    (adjacent {current_loc} {adjacent_loc} {direction})")
        
        return facts
    
    def _generate_goal(self) -> str:
        """Generate the goal section."""
        # Goal is to escape the cave
        return "    (escaped agent)"


def main():
    """Example usage of the PDDLGenerator."""
    # Parse a map first
    parser = MapParser()
    generator = PDDLGenerator()
    
    try:
        # Example map parsing and PDDL generation
        map_data = parser.parse_map_file("maps/example_map.txt")
        generator.generate_problem_file(map_data, "problems/example_problem.pddl")
        print("PDDL problem file generated successfully!")
    except FileNotFoundError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main() 