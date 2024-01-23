import unittest
import io
import unittest.mock  
from src.timeline import Timeline
from src.exploration import explore_timeline  
# Update the import path
from src.utils import calculate_paradox_risk
class TestExploration(unittest.TestCase):
    def test_explore_timeline(self):
        timeline = Timeline()
        timeline.add_event(0, "Start")
        timeline.add_event(10, "Event A")
        timeline.add_event(20, "Event B")
        timeline.add_relationship(0, 10)
        timeline.add_relationship(10, 20)
        
        
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            explore_timeline(timeline, exploration_depth=3, energy_budget=15)
        
        
        self.assertIn("Moved to timestamp 10", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()

