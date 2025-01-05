import typer
from dektools.shell import associate_console_script, associate_console_script_remove

app = typer.Typer(add_completion=False)


@app.command()
def assoc(delete: bool = typer.Option(False, "--delete", "-d")):
    from ..image.design.const import image_ignore_file
    from ..image.svg.design.const import svg_ignore_file
    args_list = [
        (image_ignore_file, __name__, 'ImageDesign', 'image design'),
        (svg_ignore_file, __name__, 'SvgDesign', 'image svg design')
    ]
    for args in args_list:
        if delete:
            associate_console_script_remove(*args[:-1])
        else:
            associate_console_script(*args)
