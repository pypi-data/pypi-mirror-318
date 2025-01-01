import random

import click

from romanticCli.auth import is_logged_in, login, logout
from romanticCli.backend_service import get_romantic_message
from romanticCli.cmd import love_quiz
from romanticCli.cmd import mood_check, leave_secret_note
from romanticCli.const import gradient_colors
from romanticCli.services import print_colored_message


@click.group()
def baby():
    """Your personalized love-filled CLI, just for you my love ❤️"""
    if not is_logged_in():
        click.echo(click.style("You are not logged in. Please log in to continue.", fg="red"))
        username = click.prompt("Username")
        password = click.prompt("Password", hide_input=True)
        login(username, password)
    else:
        print("----------------------------------------------")
        click.echo(click.style(f"Welcome back! mera bachchha", fg=f"{random.choice(gradient_colors)}"))
        print("----------------------------------------------")


@click.command()
def logout_cmd():
    """Command to log out."""
    logout()


@click.command()
@click.option('--today', '-t', is_flag=False, help="Get a random compliment of today")
def compliments(today):
    """Get compliments."""
    if is_logged_in():
        message = get_romantic_message(today=today)
        print_colored_message(message)
    else:
        click.echo(click.style("You are not logged in. Please log in to continue.", fg="red"))


baby.add_command(mood_check)
baby.add_command(logout_cmd)
baby.add_command(compliments)
baby.add_command(leave_secret_note)
baby.add_command(love_quiz)

if __name__ == '__main__':
    baby()
