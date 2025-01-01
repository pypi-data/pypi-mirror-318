import click

from romanticCLI.auth import is_logged_in, login, logout, get_username
from romanticCLI.backend_service import get_romantic_message
from romanticCLI.cmd import mood_check, display_gradient_text, text
from romanticCLI.services import print_colored_message


@click.group()
def baby():
    """Your personalized love-filled CLI, just for you my love ❤️"""
    if not is_logged_in():
        click.echo(click.style("You are not logged in. Please log in to continue.", fg="red"))
        username = click.prompt("Username")
        password = click.prompt("Password", hide_input=True)
        login(username, password)
    else:
        click.echo(click.style(f"Welcome back! {get_username()}", fg="green"))


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
baby.add_command(text)
baby.add_command(compliments)
baby.add_command(display_gradient_text)

if __name__ == '__main__':
    baby()
