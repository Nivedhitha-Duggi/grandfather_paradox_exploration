import unittest
import io
import unittest.mock  
from src.timeline import Timeline
from src.visualization import dynamic_visualization_enhanced  
from src.utils import calculate_paradox_risk

class TestVisualization(unittest.TestCase):
    def test_dynamic_visualization_enhanced(self):
        timeline = Timeline()
        timeline.add_event(0, "Start")
        timeline.add_event(10, "Event A")
        timeline.add_event(20, "Event B")
        timeline.add_relationship(0, 10)
        timeline.add_relationship(10, 20)
        
      
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            dynamic_visualization_enhanced(timeline, exploration_depth=3, energy_budget=15)
        
        self.assertIn("Dynamic Visualization - Step 1", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()

