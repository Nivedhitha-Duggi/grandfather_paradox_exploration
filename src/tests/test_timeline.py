import unittest
from src.timeline import Timeline

class TestTimeline(unittest.TestCase):
    def test_add_event(self):
        timeline = Timeline()
        timeline.add_event(0, "Start")
        self.assertIn(0, timeline.graph.nodes)

    def test_add_relationship(self):
        timeline = Timeline()
        timeline.add_event(0, "Start")
        timeline.add_event(10, "Event A")
        timeline.add_relationship(0, 10)
        self.assertTrue(timeline.graph.has_edge(0, 10))

if __name__ == '__main__':
    unittest.main()

