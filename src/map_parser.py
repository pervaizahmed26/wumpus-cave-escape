"""
Map Parser Module

Parses input map files for the Wumpus Cave Escape assignment.
Map format uses: S (start), X (wall), W (wumpus), A (arrow), C (crate), P (pit), - (horizontal turntable), | (vertical turntable), space (empty)
"""

import os
from typing import Dict, List, Tuple, Optional


class MapParser:
    """Parser for Wumpus Cave Escape map files."""
    
    def __init__(self):
        self.map_data = {}
        self.dimensions = (0, 0)
        self.agent_pos = None
        self.wumpus_positions = []
        self.arrow_positions = []
        self.crate_positions = []
        self.pit_positions = []
        self.wall_positions = []
        self.horizontal_turntables = []
        self.vertical_turntables = []
        self.empty_positions = []
    
    def parse_map_file(self, file_path: str) -> Dict:
        """
        Parse a map file and extract all relevant information.
        
        Args:
            file_path: Path to the map file
            
        Returns:
            Dictionary containing parsed map data
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Map file not found: {file_path}")
        
        with open(file_path, 'r') as f:
            lines = f.readlines()
        
        # Remove trailing newlines but preserve whitespace within lines
        lines = [line.rstrip('\n\r') for line in lines if line.rstrip('\n\r')]
        
        # Parse dimensions
        if not lines:
            self.dimensions = (0, 0)
            return self._create_map_data()
            
        self.dimensions = (len(lines), len(lines[0]) if lines else 0)
        
        # Reset all position lists
        self.agent_pos = None
        self.wumpus_positions = []
        self.arrow_positions = []
        self.crate_positions = []
        self.pit_positions = []
        self.wall_positions = []
        self.horizontal_turntables = []
        self.vertical_turntables = []
        self.empty_positions = []
        
        # Parse map elements
        for row, line in enumerate(lines):
            for col, char in enumerate(line):
                pos = (row, col)
                
                if char == 'S':
                    self.agent_pos = pos
                    self.empty_positions.append(pos)  # Starting position is also empty
                elif char == 'X':
                    self.wall_positions.append(pos)
                elif char == 'W':
                    self.wumpus_positions.append(pos)
                elif char == 'A':
                    self.arrow_positions.append(pos)
                elif char == 'C':
                    self.crate_positions.append(pos)
                elif char == 'P':
                    self.pit_positions.append(pos)
                elif char == '-':
                    self.horizontal_turntables.append(pos)
                elif char == '|':
                    self.vertical_turntables.append(pos)
                elif char == ' ':
                    self.empty_positions.append(pos)
        
        return self._create_map_data()
    
    def _create_map_data(self) -> Dict:
        """Create structured map data dictionary."""
        return {
            'dimensions': self.dimensions,
            'agent_position': self.agent_pos,
            'wumpus_positions': self.wumpus_positions,
            'arrow_positions': self.arrow_positions,
            'crate_positions': self.crate_positions,
            'pit_positions': self.pit_positions,
            'wall_positions': self.wall_positions,
            'horizontal_turntables': self.horizontal_turntables,
            'vertical_turntables': self.vertical_turntables,
            'empty_positions': self.empty_positions
        }
    
    def is_valid_position(self, pos: Tuple[int, int]) -> bool:
        """Check if a position is within map boundaries."""
        row, col = pos
        return 0 <= row < self.dimensions[0] and 0 <= col < self.dimensions[1]
    
    def get_adjacent_positions(self, pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        """Get all valid adjacent positions."""
        row, col = pos
        adjacent = [
            (row - 1, col),  # Up
            (row + 1, col),  # Down
            (row, col - 1),  # Left
            (row, col + 1)   # Right
        ]
        return [p for p in adjacent if self.is_valid_position(p)]


def main():
    """Example usage of the MapParser."""
    parser = MapParser()
    
    # Example: Parse a map file
    try:
        map_data = parser.parse_map_file("maps/example_map.txt")
        print("Map parsed successfully:")
        print(f"Dimensions: {map_data['dimensions']}")
        print(f"Agent position: {map_data['agent_position']}")
        print(f"Wumpus positions: {map_data['wumpus_positions']}")
        print(f"Arrow positions: {map_data['arrow_positions']}")
        print(f"Crate positions: {map_data['crate_positions']}")
        print(f"Pit positions: {map_data['pit_positions']}")
        print(f"Wall positions: {map_data['wall_positions']}")
        print(f"Horizontal turntables: {map_data['horizontal_turntables']}")
        print(f"Vertical turntables: {map_data['vertical_turntables']}")
    except FileNotFoundError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main() 