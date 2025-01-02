import typer

from .about import __version__

app: typer.Typer = typer.Typer(help=f"D15 command line interface. (v{__version__})")


@app.command()
def render(text: str, to_file: str) -> str:
    """
    Render an image from a given text string. If the output file is null, the result is
    base64 encoded and printed.
    """
    from .render import d15_render

    image = d15_render(text)
    if to_file:
        image.save(to_file)
        return to_file
    import base64
    from io import BytesIO

    buffered = BytesIO()
    image.save(buffered, format="PNG")
    result = base64.b64encode(buffered.getvalue()).decode("utf-8")
    typer.echo(result)
    return result


if __name__ == "__main__":
    app()

__all__ = ()
