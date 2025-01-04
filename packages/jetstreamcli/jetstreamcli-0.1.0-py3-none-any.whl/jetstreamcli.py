import os
import click
import cmds
import robloxcmds
import projectscmds
import inquirer
from showinfm import show_in_file_manager

from pathlib import Path
from config import load_config, save_config, PROJECTS_DIR
from colorama import Fore, Back, Style
from robloxFuncs import keyTest, generate_script, get_image_ids, upload_images
from files import read_file, write_file

@click.group()
@click.version_option()
@click.pass_context
def cli(ctx: click.Context) -> None:
    """🚀 Jetstream - Roblox utility tool for converting videos/gifs into frames for importing into Roblox"""

    config = load_config()

    if not os.path.exists(PROJECTS_DIR):
        os.makedirs(PROJECTS_DIR)

    ctx.obj = {"projects_dir": PROJECTS_DIR, "config": config}

cli.add_command(cmds.create)
cli.add_command(cmds.builds)

@cli.group()
def roblox():
    """manage your Roblox configurations"""
    
roblox.add_command(robloxcmds.set)
roblox.add_command(robloxcmds.uploader)
roblox.add_command(robloxcmds.test)

@cli.group()
def projects():
    """manage your Jetstream projects"""

projects.add_command(projectscmds.view)
projects.add_command(projectscmds.open)
projects.add_command(projectscmds.generate)
projects.add_command(projectscmds.download)
