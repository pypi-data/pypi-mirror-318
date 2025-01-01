import random

import click
from rich.console import Console

from romanticCli.auth import is_logged_in
from romanticCli.backend_service import send_secret_note
from romanticCli.const import gradient_colors
from romanticCli.services import loading

console = Console()


@click.command()
@click.option('--mood', type=click.Choice(['happy', 'sad', 'romantic', 'playful'], case_sensitive=False),
              prompt="How are you feeling today?", help="Choose your mood and I'll respond!")
def mood_check(mood):
    """Respond based on her mood."""
    responses = {
        'happy': "I'm so glad you're happy! Let's make today even brighter 🌞",
        'sad': "Aww, don't worry, love. I'm sending virtual hugs your way 💖",
        'romantic': "Oh my love, I adore you more than words can express 💕",
        'playful': "Oh, feeling playful? Let's have some fun! 😋"
    }
    click.echo(
        click.style(responses[mood], fg=f'{random.choice(["green", "yellow", "blue", "magenta", "cyan"])}'))


@click.command()
def love_quiz():
    """A fun little love quiz for you!"""
    questions = [
        ("Which year you proposed me?", "2024"),
        ("Where did we first meet?", "college"),
        ("How much I love you?", "infinity"),
        ("Where we first time go out as a couple?", "pagoda"),
        ("Which temple we visited together as a couple?", "iscon"),
    ]

    score = 0
    console.print("**********************************************************************************",
                  style=f"bold {random.choice(gradient_colors)}")
    for question, answer in questions:
        user_answer = click.prompt(click.style(question, fg=f'{random.choice(gradient_colors)}'))
        if user_answer.lower() == answer:
            score += 1
    console.print("**********************************************************************************",
                  style=f"bold {random.choice(gradient_colors)}")
    click.echo(click.style(f"You scored {score}/{len(questions)}! Love you even more 💖",
                           fg=f'{random.choice(gradient_colors)}', bold=True))
    console.print("**********************************************************************************",
                  style=f"bold {random.choice(gradient_colors)}")


@click.command()
@click.option('--note', prompt="Write your secret note for me", help="Leave a secret love note")
def leave_secret_note(note):
    """Leave a secret note for me."""
    if is_logged_in():
        data = {"secret_message": note}
        res = send_secret_note(data)
        if res != 401:
            loading("Sending your note...",
                    after_text="Aapka note send ho gya hai mere bachchhe, main baad me check kar lunga 💌")
        else:
            click.echo(click.style("Wrong password, please logout and login with valid credentials", fg="red"))
    else:
        click.echo(click.style("You are not logged in. Please log in to continue.", fg="red"))
