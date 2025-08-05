# Classic Pong Game with Python Turtle

This is a simple two-player Pong-style arcade game built using Python's 'turtle' graphics module. It includes basic collision detection, a scoreboard, and keyboard controls, and is structured using object-oriented programming.

---

## How to Play

- Two players control paddles on either side of the screen.
- The objective is to bounce the ball and prevent it from passing your paddle.
- First to reach the score '10' wins.

> You can change the score(number of points) in the 'main.py' file if needed.

### Controls

- **Player 1 (Right Paddle)**
  - Move Up: Arrow Up
  - Move Down: Arrow Down
- **Player 2 (Left Paddle)**
  - Move Up: 'w'
  - Move Down: 's'

> You can change the control keys in the 'main.py' file if needed.

---

## Project Structure

- 'main.py' – Entry point to run the game
- 'arcade_participants.py' – Sets up the game screen and players
- 'ball.py' – Manages the ball's movement and collisions
- 'scoreboard.py' – Displays and updates the player scores

Only the 'main.py' file needs to be run to play the game.

---

## Requirements

- Python 3.12.0
- No external libraries are required
  - Uses built-in 'turtle' and 'random' modules

To run the game: python main.py
