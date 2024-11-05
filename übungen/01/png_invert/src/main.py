from src.invert import invert_png
import click

@click.command()
@click.argument(
    'png_file',
    type=click.Path(
        exists=True,
        resolve_path=True,
    ),
)
def cli(png_file: str):
    invert_png(
        input_path=png_file,
        output_path=png_file.replace('.png', '_inverted.png'),
    )
