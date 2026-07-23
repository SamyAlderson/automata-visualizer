# main.py
"""
Main entry point for the automata visualizer.
"""

import numpy as np
from automata import Automaton

def draw_automaton(automaton, width=800, height=600):
    """
    Draw the automaton on a canvas.
    
    Parameters:
        automaton (Automaton): Finite automaton to visualize.
        width (int): Width of the canvas.
        height (int): Height of the canvas.
    """
    # Calculate the maximum number of states to determine the canvas size
    max_states = max(len(state) for state in automaton.states)
    
    # Create a 2D grid to represent the canvas
    canvas = np.full((height, width), ' ', dtype=object)
    
    # Iterate over each state
    for i, (state, transitions) in enumerate(automaton.states.items()):
        # Calculate the y-coordinate for this state
        y = height // 2 - len(state) // 2
        
        # Iterate over each symbol in the state
        for j, symbol in enumerate(state):
            # Calculate the x-coordinate for this symbol
            x = width // 2 + j - len(state) // 2
            
            # Draw the symbol on the canvas
            canvas[y, x] = symbol
    
    # Print the canvas
    for row in canvas:
        print(' '.join(row))

def main():
    # Create an instance of the finite automaton
    automaton = Automaton()
    
    # Define the states and transitions for the automaton
    automaton.add_state('A', {'a': 'B', 'b': 'C'})
    automaton.add_state('B', {'a': 'A', 'b': 'D'})
    automaton.add_state('C', {'a': 'A', 'b': 'B'})
    automaton.add_state('D', {'a': 'A', 'b': 'C'})
    
    # Draw the automaton on a canvas
    draw_automaton(automaton)

if __name__ == '__main__':
    main()