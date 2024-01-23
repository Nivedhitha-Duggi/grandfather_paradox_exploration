from visualization import dynamic_visualization_enhanced
from exploration import explore_timeline
from timeline import Timeline


timeline = Timeline()
timeline.add_event(0, "Start")
timeline.add_event(10, "Event A")
timeline.add_event(20, "Event B")
timeline.add_event(30, "Event C")
timeline.add_relationship(0, 10)
timeline.add_relationship(10, 20)
timeline.add_relationship(20, 30)

ethical_constraints = [15, 25]

print("\nDynamic Visualization:")
dynamic_visualization_enhanced(timeline, exploration_depth=3, energy_budget=15)

print("\nExploration with Ethical Constraints:")
explore_timeline(timeline, exploration_depth=5, energy_budget=20, ethical_constraints=ethical_constraints)

