# Dynamic Pong

Dynamic Pong is a modern rendition of the classic arcade game Pong, crafted with Python using the Pygame library. It offers an engaging and interactive gaming experience, featuring responsive paddle controls and dynamic game speed adjustments. This project is an excellent showcase of Python programming skills, game design, and software development principles.

## Features

- **Adaptive Gameplay**: The game's difficulty increases as you progress, offering a challenging and engaging experience.
- **Collision Detection**: Implements collision logic for paddles and game boundaries.
- **Score Tracking**: Real-time score display for both the player and the computer-controlled opponent.
- **Customizability**: Adjustable game window size and element proportions to fit various screens.

## Installation

To install and play Dynamic Pong, follow these simple steps:

1. Open a terminal or command prompt.
2. Run the command:
   ```sh
   pip install dynamic_pong
   ```
3. Wait for the installation to complete.

## How to Play

1. After installation, run the command:
   ```sh
   dynamic_pong
   ```
2. Control the left paddle using the `Up` and `Down` arrow keys or the `W` and `S` keys.
3. The game continues indefinitely until manually exited.

## Code Examples

```python
# Creating a block representing a paddle
block = Block("white", 20, 100, 50, 300)
```

```python
# Initializing a player paddle
player = Player("white", 20, 140, 5)
```

```python
# Handling a ball collision with the top edge of the screen
ball = Ball("white", 30, 30, paddle_group)
ball.rect.top = -5
ball.speed_y = -5
ball.collisions()
```

## Contributing

Contributions to Dynamic Pong are welcome! If you have suggestions for improvements or encounter any issues, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## About the Author

Adamya Singh - Software developer with a passion for machine learning and functional programming. Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/adamya-singh-0a8746184/).
