__version__ = "0.1.0"

# cli.py
import click

@click.command()
@click.version_option(version=__version__)
def main():
    pass

if __name__ == "__main__":
    main()
