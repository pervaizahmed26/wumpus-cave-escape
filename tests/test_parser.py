"""
Unit tests for the map parser module.
"""

import unittest
import tempfile
import os
import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from map_parser import MapParser


class TestMapParser(unittest.TestCase):
    """Test cases for the MapParser class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.parser = MapParser()
    
    def test_parse_simple_map(self):
        """Test parsing a simple map."""
        map_content = """A.G
...
.W."""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write(map_content)
            temp_file = f.name
        
        try:
            result = self.parser.parse_map_file(temp_file)
            
            # Check dimensions
            self.assertEqual(result['dimensions'], (3, 3))
            
            # Check positions
            self.assertEqual(result['agent_position'], (0, 0))
            self.assertEqual(result['gold_position'], (0, 2))
            self.assertEqual(result['wumpus_position'], (2, 1))
            
            # Check empty lists
            self.assertEqual(result['pits'], [])
            self.assertEqual(result['breezes'], [])
            self.assertEqual(result['stenches'], [])
            
        finally:
            os.unlink(temp_file)
    
    def test_parse_complex_map(self):
        """Test parsing a complex map with all elements."""
        map_content = """A.SG
.BP.
.W.."""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write(map_content)
            temp_file = f.name
        
        try:
            result = self.parser.parse_map_file(temp_file)
            
            # Check dimensions
            self.assertEqual(result['dimensions'], (3, 4))
            
            # Check positions
            self.assertEqual(result['agent_position'], (0, 0))
            self.assertEqual(result['gold_position'], (0, 3))
            self.assertEqual(result['wumpus_position'], (2, 1))
            
            # Check lists
            self.assertEqual(result['pits'], [(1, 2)])
            self.assertEqual(result['breezes'], [(1, 1)])
            self.assertEqual(result['stenches'], [(0, 2)])
            
        finally:
            os.unlink(temp_file)
    
    def test_file_not_found(self):
        """Test handling of non-existent files."""
        with self.assertRaises(FileNotFoundError):
            self.parser.parse_map_file("nonexistent_file.txt")
    
    def test_empty_file(self):
        """Test handling of empty files."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write("")
            temp_file = f.name
        
        try:
            result = self.parser.parse_map_file(temp_file)
            self.assertEqual(result['dimensions'], (0, 0))
            
        finally:
            os.unlink(temp_file)
    
    def test_is_valid_position(self):
        """Test position validation."""
        # Set up a 3x3 map
        self.parser.dimensions = (3, 3)
        
        # Valid positions
        self.assertTrue(self.parser.is_valid_position((0, 0)))
        self.assertTrue(self.parser.is_valid_position((1, 1)))
        self.assertTrue(self.parser.is_valid_position((2, 2)))
        
        # Invalid positions
        self.assertFalse(self.parser.is_valid_position((-1, 0)))
        self.assertFalse(self.parser.is_valid_position((0, -1)))
        self.assertFalse(self.parser.is_valid_position((3, 0)))
        self.assertFalse(self.parser.is_valid_position((0, 3)))
    
    def test_get_adjacent_positions(self):
        """Test getting adjacent positions."""
        # Set up a 3x3 map
        self.parser.dimensions = (3, 3)
        
        # Test corner position (0,0)
        adjacent = self.parser.get_adjacent_positions((0, 0))
        expected = [(1, 0), (0, 1)]
        self.assertEqual(set(adjacent), set(expected))
        
        # Test center position (1,1)
        adjacent = self.parser.get_adjacent_positions((1, 1))
        expected = [(0, 1), (2, 1), (1, 0), (1, 2)]
        self.assertEqual(set(adjacent), set(expected))
        
        # Test edge position (0,1)
        adjacent = self.parser.get_adjacent_positions((0, 1))
        expected = [(1, 1), (0, 0), (0, 2)]
        self.assertEqual(set(adjacent), set(expected))
    
    def test_multiple_pits(self):
        """Test parsing maps with multiple pits."""
        map_content = """A.G
P.P
.W."""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write(map_content)
            temp_file = f.name
        
        try:
            result = self.parser.parse_map_file(temp_file)
            
            # Check multiple pits
            self.assertEqual(set(result['pits']), {(1, 0), (1, 2)})
            
        finally:
            os.unlink(temp_file)
    
    def test_whitespace_handling(self):
        """Test handling of whitespace in map files."""
        map_content = """  A.G  
  ...  
  .W.  """
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write(map_content)
            temp_file = f.name
        
        try:
            result = self.parser.parse_map_file(temp_file)
            
            # Should still parse correctly despite whitespace
            self.assertEqual(result['dimensions'], (3, 3))
            self.assertEqual(result['agent_position'], (0, 0))
            self.assertEqual(result['gold_position'], (0, 2))
            self.assertEqual(result['wumpus_position'], (2, 1))
            
        finally:
            os.unlink(temp_file)


class TestMapParserIntegration(unittest.TestCase):
    """Integration tests for the map parser."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.parser = MapParser()
    
    def test_realistic_wumpus_map(self):
        """Test parsing a realistic Wumpus world map."""
        map_content = """A.SG
.BP.
SW.."""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write(map_content)
            temp_file = f.name
        
        try:
            result = self.parser.parse_map_file(temp_file)
            
            # Verify all expected elements are present
            self.assertIsNotNone(result['agent_position'])
            self.assertIsNotNone(result['gold_position'])
            self.assertIsNotNone(result['wumpus_position'])
            self.assertTrue(len(result['pits']) > 0)
            self.assertTrue(len(result['breezes']) > 0)
            self.assertTrue(len(result['stenches']) > 0)
            
            # Verify logical consistency
            # There should be stenches adjacent to wumpus
            wumpus_pos = result['wumpus_position']
            adjacent_positions = self.parser.get_adjacent_positions(wumpus_pos)
            
            # At least one adjacent position should have a stench
            stench_positions = set(result['stenches'])
            self.assertTrue(any(pos in stench_positions for pos in adjacent_positions))
            
        finally:
            os.unlink(temp_file)


if __name__ == '__main__':
    unittest.main() 