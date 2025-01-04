import click


@click.group()
def cli():
    pass


@cli.command()
def diff():
    pass


if __name__ == "__main__":
    cli()
