# Time Warp: Exploring Timelines and Ethics in Python

This project simulates the exploration of timelines, with a focus on the Grandfather Paradox and ethical considerations in time travel scenarios. It offers functionalities for:

    Timeline representation: A Timeline class using NetworkX to model events and relationships over time.
    
    Exploration logic: An explore_timeline function to simulate exploration based on depth and energy budget.
    
    Visualization: A dynamic_visualization_enhanced function using Matplotlib to visualize exploration, emphasizing paradox risk.
    
    Ethical constraints: Integration of ethical considerations into the exploration process.
    
    Testing: Test cases to ensure correctness.
    
    Utility functions: A calculate_paradox_risk function to determine paradox risk at a timestamp.

# Programming Language and Libraries:

    Python
    NetworkX
    Matplotlib
    unittest
    unittest.mock

# Project Structure:

├── exploration.py

├── tests

│   ├── __init__.py

│   └── test_exploration.py

├── visualization.py

├── utils.py

├── README.md

├── requirements.txt

# Key Files:

    exploration.py: Contains the explore_timeline function for simulation.
    visualization.py: Contains the dynamic_visualization_enhanced function for visualization.
    utils.py: Contains utility functions, including calculate_paradox_risk.
    tests/test_exploration.py: Contains test cases for the exploration logic.

# Installation:

    Clone the repository: https://github.com/Nivedhitha-Duggi/grandfather_paradox_exploration.git
    
    Install dependencies: pip install -r requirements.txt

# Usage:

1.Create a Timeline object:
    

    timeline = Timeline()
    timeline.add_event("Birth of traveler", timestamp=0)



2.Explore the timeline:


results = explore_timeline(timeline, depth=3, energy_budget=100)


3.Visualize the exploration:


dynamic_visualization_enhanced(timeline, results)
