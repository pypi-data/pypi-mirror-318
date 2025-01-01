import random

import click

from romanticCli.auth import is_logged_in
from romanticCli.backend_service import send_secret_note
from romanticCli.services import loading


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
        click.echo(
            click.style(responses[mood], fg=f'{random.choice(["red", "green", "yellow", "blue", "magenta", "cyan"])}'))
    else:
        click.echo(click.style("You are not logged in. Please log in to continue.", fg="red"))


# @click.command()
# def surprise():

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
def leave_secret_note(note):
    """Leave a secret note for me."""
    loading("Sending your note...",
            after_text="Aapka note send ho gya hai mere bachchhe, main baad me check kar lunga 💌")
    send_secret_note(note)


@click.command()
def read_note():
    """Read the secret notes she's left for you"""
    try:
        with open('secret_note.txt', 'r') as f:
            notes = f.read()
            click.echo(click.style(f"Here are your secret notes:\n{notes}", fg='blue'))
    except FileNotFoundError:
        click.echo(click.style("No notes yet!", fg='red'))
