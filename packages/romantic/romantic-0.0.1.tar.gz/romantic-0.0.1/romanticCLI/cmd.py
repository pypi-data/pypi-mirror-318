import os
import random
import time

import click
from asciimatics.screen import Screen
from rich import print as rprint
from rich.console import Console

from romanticCLI.auth import is_logged_in
from romanticCLI.services import apply_random_gradient


@click.command()
@click.option('--mood', type=click.Choice(['happy', 'sad', 'romantic', 'playful'], case_sensitive=False),
              prompt="How are you feeling today?", help="Choose your mood and I'll respond!")
def mood_check(mood):
    """Respond based on her mood."""
    if is_logged_in():
        responses = {
            'happy': "I'm so glad you're happy! Let's make today even brighter 🌞",
            'sad': "Aww, don't worry, love. I'm sending virtual hugs your way 💖",
            'romantic': "Oh my love, I adore you more than words can express 💕",
            'playful': "Oh, feeling playful? Let's have some fun! 😋"
        }
        click.echo(click.style(responses[mood], fg='cyan'))
    else:
        click.echo(click.style("You are not logged in. Please log in to continue.", fg="red"))


# @click.command()
# @click.argument('text1')
# def typing_animation(text1):
#     for char in text1:
#         sys.stdout.write(char)
#         sys.stdout.flush()
#         time.sleep(0.1)


# @click.command()
# def heart_animation():
#     for _ in range(10):
#         for frame in frames:
#             os.system('cls' if os.name == 'nt' else 'clear')  # Clear console
#             print(frame)
#             time.sleep(0.3)


# @click.command()
# def send_love():
#     with console.status("[bold magenta]Sending love..."):
#         sleep(3)
#
#     console.print("[bold red]All my love has been sent![/]")


# @click.command()
# def loading_animation():
#     for _ in track(range(10), description="Thinking about you..."):
#         sleep(0.1)


@click.command()
@click.option('--message', prompt="What's on your mind?", help="Send me a text to be romantic!")
def display_gradient_text(message):
    apply_random_gradient(message)
    click.echo(click.style(f"Sending: {message} 😘", fg='yellow', bold=True))


@click.command()
def text():
    # Simulate gradient by styling different parts of the text
    rprint("[#FF0000 bold]You[/][#FF7F00] are[/][#FFFF00] my[/][#7FFF00] sunshine[/]!")


@click.command()
def surprise():
    """Give her a cute romantic surprise"""
    surprises = [
        "You make my heart skip a beat 💓",
        "Roses are red, violets are blue, I can't stop thinking of you! 🌹",
        """ 
        🌹
        (  *  ) 
         )  (
        """
    ]
    click.echo(click.style(random.choice(surprises), fg='red', bold=True))


console = Console()


@click.command()
def colorful_love():
    """A beautiful colorized love message"""
    console.print("[bold magenta]My love for you is like an eternal flame, burning brighter every day![/] ❤️")


@click.command()
def love_quiz():
    """A fun little love quiz for you!"""
    questions = [
        ("What's my favorite color?", "blue"),
        ("Where did we first meet?", "cafe"),
        ("What's our favorite song?", "perfect")
    ]

    score = 0
    for question, answer in questions:
        user_answer = click.prompt(click.style(question, fg='cyan'))
        if user_answer.lower() == answer:
            score += 1

    click.echo(click.style(f"You scored {score}/{len(questions)}! Love you even more 💖", fg='magenta', bold=True))


@click.command()
@click.option('--note', prompt="Leave a secret note for me", help="Leave a secret love note")
def leave_note(note):
    """Leave a secret note that can be discovered later"""
    with open('secret_note.txt', 'a') as f:
        f.write(note + '\n')
    click.echo(click.style("Note saved! I'll find it later 💌", fg='yellow'))


@click.command()
def read_note():
    """Read the secret notes she's left for you"""
    try:
        with open('secret_note.txt', 'r') as f:
            notes = f.read()
            click.echo(click.style(f"Here are your secret notes:\n{notes}", fg='blue'))
    except FileNotFoundError:
        click.echo(click.style("No notes yet!", fg='red'))


@click.command()
@click.option('--text1', prompt="What's on your mind?", help="Send me a text to be romantic!")
def send_text(text1):
    """Send a text in the most romantic way possible"""
    click.echo(click.style(f"Sending: {text1} 😘", fg='yellow', bold=True))


@click.command()
def animated_heart():
    """Show animated hearts in different colors"""
    for i in range(10):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("❤ 💛 💚 💙 💜 ❤️")
        time.sleep(0.5)


# Function to create a random starfield
def starfield_effect(screen):
    # Set up the screen dimensions
    height, width = screen.height, screen.width

    # Create random positions for stars
    stars = []
    for _ in range(100):  # Create 100 stars
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        stars.append((x, y))

    # Print the stars at their random positions
    while True:
        screen.clear()

        # Simulate the star movement
        for i in range(len(stars)):
            x, y = stars[i]
            screen.print_at("*", x, y, color=random.randint(1, 7))

            # Move the stars down
            y += 1
            if y >= height:
                y = 0  # Reset star to top of the screen
                x = random.randint(0, width - 1)  # Randomize the x position

            stars[i] = (x, y)  # Update the position of the star

        screen.refresh()
        time.sleep(0.1)  # Control the speed of the animation


@click.command()
def starfield():
    """Start the starfield animation"""
    Screen.wrapper(starfield_effect)


@click.command()
def figlet_ascii():
    """Create ASCII art text using the Figlet font"""
    from asciimatics.renderers import FigletText

    def figlet_demo(screen):
        text5 = FigletText("I love you 💖", font='slant')
        screen.clear()
        screen.print_at(text5, 10, 10)
        screen.refresh()
        time.sleep(3)

    Screen.wrapper(figlet_demo)
