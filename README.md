#  Connect 4 AI: Minimax & Alpha-Beta Pruning

###  Project Overview
This project presents a fully interactive Connect 4 game featuring a custom-built Artificial Intelligence agent. The objective of this project was to implement and optimize adversarial search algorithms from scratch, allowing the AI to make strategic, forward-thinking decisions in real-time. 

The project encompasses the core game logic, a custom heuristic evaluation function, and a seamless Graphical User Interface (GUI) for an engaging human-vs-AI experience.

---

###  The Interactive Game Environment (GUI)
We developed a user-friendly graphical interface using **Pygame** to visualize the board state, handle user mouse inputs smoothly, and display real-time feedback when the AI is calculating its next move.

https://github.com/user-attachments/assets/80186667-1db8-47ba-a537-90f274bd7865

---

###  Technical Methodology & Algorithms

**1. Core AI: The Minimax Algorithm**
The foundation of the AI's decision-making is the Minimax algorithm. It simulates all possible future moves (up to a specified depth) to build a game tree, assuming the human player will also play optimally, and selects the move that maximizes the AI's chances of winning.

**2. Optimization: Alpha-Beta Pruning**
To make the AI computationally viable at deeper search levels, **Alpha-Beta Pruning** was integrated. 
* **Performance:** This significantly reduced the search space by eliminating branches of the game tree that are mathematically guaranteed to be suboptimal.
* **Key Insight:** Allowed the AI to search deeper (e.g., Depth 6+) within milliseconds, whereas standard Minimax would cause noticeable lag.

**3. Heuristic Evaluation Function**
Since the game rarely reaches a terminal state (win/loss/draw) within the search depth, a custom evaluation function was designed to score intermediate board states. It assigns strategic weights to different piece formations (e.g., prioritizing 3-in-a-row with an open slot).

---

###  Performance Insights & Optimization

<img width="854" height="533" alt="Screenshot from 2026-04-24 16-16-26" src="https://github.com/user-attachments/assets/125afe6b-f0b9-49f4-8c98-e60862b03f9f" />


1. **Computational Efficiency:** Integrating Alpha-Beta Pruning dropped the number of evaluated nodes exponentially compared to the brute-force Minimax approach.
2. **Dynamic Difficulty:** The AI's strength is fully adjustable. Users can input the desired "Search Depth" at the start of the game, directly controlling how many steps ahead the AI predicts.

---

### 💻 Tech Stack

* **Language:** Python
* **GUI Framework:** Pygame
* **Data Structures & Logic:** NumPy (Matrix manipulation), Math 
* **Algorithms:** Minimax, Alpha-Beta Pruning

---


⚙️ How to Run Locally
Run the following commands in your terminal to set up and play the game:

1. Clone the repository:
   
   ```
   git clone https://github.com/Hamza-Qabbari/Connect4-Python-AI.git
   ```
3. Navigate to the project directory:
   
   ```
   cd Connect4-Python-AI
   ```
5. Install the required dependencies:
   
   ```
   pip install numpy pygame
   ```
7. Run the game:
   
   ```
   python connect4.py
   ```
