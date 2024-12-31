import click
from pathlib import Path
from vizeer.core import Generator

@click.command()
@click.argument('video_path', type=click.Path(exists=True))
@click.option('-n', '--num-screenshots', default=6, show_default=True,
              help='Number of screenshots to take')
@click.option('-o', '--output', type=click.Path(), default='contact_sheet.jpg',
              show_default=True, help='Output file path')
@click.option('--min-scene-length', default=30, show_default=True,
              help='Minimum number of frames between scene changes')
@click.option('--bg-color', default='white', show_default=True,
              help='Background color (white/black/gray or rgb(r,g,b))')
def main(video_path: str, num_screenshots: int, output: str,
         min_scene_length: int, bg_color: str):
    """Create a contact sheet from video screenshots with smart scene detection.

    Examples:
        # Basic usage with white background
        $ vizeer video.mp4

        # Custom background color
        $ vizeer video.mp4 --bg-color rgb(50,50,50)

        # Black background with more screenshots
        $ vizeer video.mp4 --bg-color black -n 9
    """
    try:
        generator = Generator(video_path)
        output_path = generator.create_sheet(
            num_screenshots=num_screenshots,
            output_path=output,
            min_scene_length=min_scene_length,
            bg_color=bg_color
        )
        click.echo(click.style(
            f"Contact sheet created successfully: {output_path}",
            fg="green"
        ))
    except Exception as e:
        click.echo(click.style(f"Error: {str(e)}", fg="red"), err=True)
        raise click.Abort()

if __name__=="__main__":
    main()
