import os
import random
import sys
import time
from time import sleep

from rich.console import Console
from rich.text import Text

from romanticCLI.const import frames, gradient_colors

console = Console()


def typing_effect(message, delay=0.1):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)


def heart_animation(count=10):
    for _ in range(count):
        for frame in frames:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear console
            print(frame)
            time.sleep(0.3)


def loading(loading_text="Loading...", delay=2, after_text="Done!"):
    with console.status(f"[bold magenta]{loading_text}"):
        sleep(delay)

    console.print(f"[bold red]{after_text}[/]")


def apply_random_gradient(message: str):
    # Create a Text object from the message
    text = Text(message)

    # Get the length of the message
    message_length = len(message)

    # Randomly apply each color to different parts of the message
    for color in gradient_colors:
        start = random.randint(0, message_length - 1)
        end = random.randint(start + 1, message_length)  # Make sure the end is after the start

        # Apply the color to the chosen range of text
        text.stylize(f"bold {color}", start, end)

    # Print the styled text
    console.print(text)


def print_colored_message(message):
    # Replace literal '\\n' with real newlines
    message = message.replace("\\n", "\n")

    # Create a Text object from the message
    Text(message)

    # Apply random colors to the text
    colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]

    # Print top border
    console.print("**********************************************************************************",
                  style=f"bold {random.choice(colors)}")

    # Split the message into lines, trim whitespace, and apply random colors to each line
    for line in message.split("\n"):
        trimmed_line = line.strip()  # Trim leading/trailing whitespace from each line
        colored_line = Text(trimmed_line)  # Create a Text object for the line
        random_color = random.choice(colors)
        colored_line.stylize(f"bold {random_color}")  # Apply the color styling
        console.print(colored_line)  # Print the trimmed and styled line

    # Print bottom border
    console.print("**********************************************************************************",
                  style=f"bold {random.choice(colors)}")
