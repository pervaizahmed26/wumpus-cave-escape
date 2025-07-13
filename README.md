# Wumpus Cave Escape

A PDDL-based solution for the Wumpus Cave Escape assignment using automated planning.

## Overview

This project implements a complete solution pipeline for the Wumpus Cave Escape problem, from map parsing to solution generation using PDDL (Planning Domain Definition Language) and automated planners. The goal is to help an agent escape from a Wumpus cave by walking off the map boundary.

## Project Structure

```
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── src/
│   ├── __init__.py
│   ├── map_parser.py           # Parse map files
│   ├── pddl_generator.py       # Generate PDDL problem files
│   ├── solution_converter.py   # Convert planner output to required format
│   └── main.py                 # Main execution script
├── domain/
│   └── wumpus.pddl             # PDDL domain file
├── maps/                       # Input map files (to be provided)
├── problems/                   # Generated PDDL problem files
├── solutions/                  # PDDL planner solutions
├── final_solutions/            # Converted solutions in required format
├── scripts/
│   ├── solve_all.py           # Script to solve all maps
│   └── verify_solution.py     # Script to verify solutions
└── tests/
    ├── __init__.py
    └── test_parser.py         # Unit tests
```

## Features

- **Map Parsing**: Converts input map files into structured data (supports S, X, W, A, C, P, -, | symbols)
- **PDDL Generation**: Automatically generates PDDL problem files from maps
- **Solution Conversion**: Transforms planner output into the required format (walk, push, shoot, turn actions)
- **Batch Processing**: Solve multiple maps automatically
- **Solution Verification**: Validate generated solutions
- **Unit Testing**: Comprehensive test suite
- **Correct File Naming**: Follows assignment convention (mapXYZ.txt → mapXYZ.pddl → mapXYZ.pddl.soln → mapXYZ-solution.txt)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd wumpus-cave-escape
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Single Map Processing

```bash
python src/main.py --map maps/map001.txt
```

### Batch Processing

```bash
python scripts/solve_all.py
```

### Solution Verification

```bash
python scripts/verify_solution.py --solution final_solutions/map001-solution.txt
```

## Map Format

Input maps should follow the assignment format:
- `S`: Agent starting position
- `X`: Wall (impassable)
- `W`: Wumpus (can be shot with arrow)
- `A`: Arrow (automatically picked up when walked into)
- `C`: Crate (can be pushed)
- `P`: Pit (can be filled by pushing crates into it)
- `-`: Horizontal turntable (allows east/west movement)
- `|`: Vertical turntable (allows north/south movement)
- ` ` (space): Empty cell

## Action Format

Solutions are generated in the required format:
- `walk [north|east|south|west]`: Move to adjacent cell or escape off map
- `push [north|east|south|west]`: Push crate to adjacent cell
- `shoot [north|east|south|west]`: Shoot wumpus in adjacent cell
- `turn [north|east|south|west]`: Turn turntable 90 degrees

## Goal

The agent must escape the cave by walking off the map boundary (i.e., walking outside the grid boundaries).

## Dependencies

- Python 3.8+
- See `requirements.txt` for complete list
- PDDL planner (Fast-Forward, Fast-Downward, or similar) - not included, must be installed separately

## File Naming Convention

The project follows the assignment's file naming convention:
- Input map: `mapXYZ.txt`
- PDDL problem: `mapXYZ.pddl`
- PDDL solution: `mapXYZ.pddl.soln`
- Final solution: `mapXYZ-solution.txt`

## Testing

Run the test suite:
```bash
python -m pytest tests/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 