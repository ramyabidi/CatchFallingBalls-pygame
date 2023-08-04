<div align="center">
  <img src="https://i.ibb.co/4sHQPxD/Screenshot-from-2023-08-03-15-46-16-1.png" alt="Catch Falling Balls" width="600px">
</div>

# Catch Falling Balls Game

Catch Falling Balls is a simple arcade game developed using the Pygame library in Python. The objective of the game is to move the basket left and right to catch falling balls, earning points for each successful catch. The game has two versions with slightly different gameplay and features.

## 🎮 Game Versions

### Version 1 (game1.py)

- In Version 1 of the game, falling balls have varying speeds (between 1 and 5).
- The game runs for a total of 60 seconds, and the player's score is recorded.
- At the end of the game, the player's score is displayed along with the top five high scores.
- If the player achieves a new high score, it is highlighted in the end-game message box.

### Version 2 (game2.py)

- Version 2 of the game features falling balls with reduced or fixed speeds (can be adjusted).
- Instead of a fixed time limit, the game continues until the player misses three balls.
- The end-game message box appears when the player misses three balls, showing the final score and top five high scores.
- After the game is over, the player can choose to restart the game or quit.

## 🚀 How to Play

1. **Installation**: Make sure you have Python and Pygame installed on your system. If Pygame is not installed, you can install it using pip:

```bash
pip install pygame
```

2. **Downloading the Game**: Clone or download this repository to your local machine.


3. **Running the Game**: Open a terminal or command prompt, navigate to the folder containing the game files, and execute the desired version's script:

```bash
python game1.py
```
or
```bash
python game2.py
```

4. **Game Controls**: Use the left and right arrow keys to move the basket and catch the falling balls.

5. **Scoring**: Each successful catch increases your score. In Version 1, the game runs for 60 seconds, while in Version 2, it continues until you miss three balls.

6. **Game Over**: In Version 1, the game ends after 60 seconds, and the final score is displayed. In Version 2, the game ends after you miss three balls, and the final score is displayed along with the top five high scores.

## 🎮 Gameplay Screenshots

**Version 1**

![Gameplay Screenshot - Version 1](https://i.ibb.co/6Pm1bnX/Screenshot-from-2023-08-04-11-46-20.png)

**Version 2**

![Gameplay Screenshot - Version 2](https://i.ibb.co/wYjmH1q/Screenshot-from-2023-08-04-11-47-44.png)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- The Pygame library made it easy to develop this simple game.
- The graphics/assets files are located in the `graphics/` folder of the game:
   - `sky.png`: Background image for the game's sky.
   - `ground.png`: Background image for the game's ground.
   - `basket.png`: Image of the basket used to catch the falling balls.
   - `ball_1.png`, `ball_2.png`, ..., `ball_9.png`: Images of the falling balls.
- The graphics used in the game are from [OpenGameArt](https://opengameart.org/), created by various artists.

## 📙 About the Developer

This game was developed by [Ramy Abidi](https://github.com/ramyabidi). Feel free to connect with me on [LinkedIn](https://linkedin.com/in/ramyabidi).
