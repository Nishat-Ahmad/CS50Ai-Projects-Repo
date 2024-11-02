# Tic Tac Toe Game with AI and GUI
This project was built ontop of the code base provided by CS50Ai.
This project is a Tic Tac Toe game implemented in Python using the Pygame library for the 
graphical user interface (GUI) and an AI opponent powered by the minimax algorithm. 
The game allows you to play as either "X" or "O" against the AI, which makes optimal moves.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Gameplay](#gameplay)
- [License](#license)

## features

- **Graphical User Interface**: Built using Pygame to provide a visually appealing and interactive experience.
- **AI Opponent**: The AI uses the minimax algorithm to play optimally, making it challenging to beat.
- **Two Modes**: Play as either "X" or "O".

## Installation
To run this game, you'll need Python and Pygame installed on your system.

### Step-by-Step Installation
1. **Install Python**:  
   If you haven't already, download and install Python from [python.org](https://www.python.org/).

2. **Install Pygame**:  
   Open your terminal or command prompt and run the following command:

   ```bash
   pip install pygame
   
3. Clone the Repository:
   Clone this repository to your local machine using:
   ```bash
   git clone https://github.com/Nishat-Ahmad/Tic-Tac-Toe.git

 4. Download Fonts:
   Download the OpenSans-Regular.ttf font from the repo and place it in the same directory as the script.

 5. Run the Game:
   Execute the script with:
      ```bash
      python runner.py

## Usage
1. Game Controls
Choose Your Player: Click "Play as X" or "Play as O" to start the game as the respective player.
Make a Move: Click on an empty cell to place your mark ("X" or "O") on the board.
AI Move: The AI will automatically make its move after you.
Play Again: After a game is over, click "Play Again" to start a new game.

## Gameplay
1. Starting the Game
When the game starts, you will be prompted to select whether you want to play as "X" or "O".
After selecting your player, the game board will be displayed.

2. Playing the Game
You take turns with the AI to place your mark on the board.
The first player to get three of their marks in a row, column, or diagonal wins the game.
If the board is filled and no player has won, the game is a draw.

3. Ending the Game
The game ends when a player wins or the board is full.
A message will be displayed indicating the winner or if it's a tie.
Click "Play Again" to start a new game.

## License
This project is licensed under the Apache 2.0 License. Feel free to use, modify, and distribute the code.

Enjoy playing Tic Tac Toe with an intelligent AI opponent!
