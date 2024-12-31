import typer

from .commands.color_shuffle import app as color_shuffle_app

app = typer.Typer()

app.add_typer(color_shuffle_app)
