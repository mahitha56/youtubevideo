import time
import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def fireworks():
    colors = ['*', '+', 'x', 'o', '@']
    for _ in range(10):
        line = ' ' * random.randint(0, 20)
        line += random.choice(colors)
        print(line)
        time.sleep(0.1)

def countdown(seconds):
    for i in range(seconds, 0, -1):
        clear_screen()
        print(f"🎉 New Year Countdown: {i} 🎉")
        time.sleep(1)
    clear_screen()
    print("🥳🥳 HAPPY NEW YEAR 2026! 🥳🥳\n")
    for _ in range(5):
        fireworks()

if __name__ == "__main__":
    print("Get ready for 2026! Countdown starting in 3 seconds...")
    time.sleep(3)
    countdown(10)  # 10-second countdown
