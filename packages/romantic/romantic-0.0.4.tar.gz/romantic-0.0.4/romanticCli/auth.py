import json
import os

import click

# Get the app data directory, creating a hidden directory for the config file
APPDATA_PATH = os.getenv('APPDATA')
CONFIG_DIR = os.path.join(APPDATA_PATH, 'romanticCli')
CONFIG_FILE = os.path.join(CONFIG_DIR, 'config.json')


# Ensure the config directory exists and is hidden
def create_hidden_dir():
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)
        # Make the directory hidden on Windows
        if os.name == 'nt':
            os.system(f'attrib +h {CONFIG_DIR}')


def load_config():
    """Load the config file, if it exists."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    else:
        return {}


def save_config(config):
    """Save the config data to the config.json file."""
    create_hidden_dir()
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)


def is_logged_in():
    """Check if the user is already logged in by verifying the presence of credentials."""
    config = load_config()
    return 'username' in config and 'password' in config


def login(username, password):
    """Log in the user by saving their credentials in the config.json file."""
    config = load_config()
    config['username'] = username
    config['password'] = password
    save_config(config)
    click.echo(click.style("Login successful!", fg="green"))


def logout():
    """Log out the user by removing the config.json file."""
    if os.path.exists(CONFIG_FILE):
        os.remove(CONFIG_FILE)
        click.echo(click.style("Logged out successfully. Config files removed.", fg="yellow"))
    else:
        click.echo(click.style("You are not logged in.", fg="red"))


# Getter method for username
def get_username():
    """Retrieve the stored username from the config file."""
    config = load_config()
    return config.get('username', None)


# Getter method for password
def get_password():
    """Retrieve the stored password from the config file."""
    config = load_config()
    return config.get('password', None)
