# Code Review

I will be covering [this repo](https://github.com/codertheashish/Space-Shooter-Game/blob/main/space_shooter_game.py) by **Ashish Kumar Prajapati**.  

The project is a simple space shooter game. You move left and right across the bottom while shooting enemy ships that slowly descend from the top of the screen (see Fig 1), while stars fly by in the background.  

Although the game is fully functional, while playing I encountered some glaring issues:  
- You only lose lives when enemy ships crash into yours, not when they reach the bottom of the screen (like space invaders). After analysing the code it seems this was intentional.  
- You gain score for every shot you take, not every shot you hit, which is completely backwards, especially with infinite ammo. This gives no incentive to attack or do anything. 

![showcase](https://github.com/juroimoh/techBasics1_JASPER_STEINBERG/blob/main/assignments/week11/space_shooter.PNG)
`Fig 1`

The within the code written by Ashish have been kept. All comments from me are outside the code blocks. Ashish does provide surface level comments, explaining the general application of different functions. 

The code begins as follows:  
```
import pygame
import sys
import random

pygame.init()

  # Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter - Final Version")
```
All necessary libraries are installed, and the screen size is setup with a application title.  
