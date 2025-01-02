#!/usr/bin/python3

"""Run '%mscene -h' to view commands."""

from IPython.display import display, HTML, clear_output
from pathlib import Path
import subprocess
import requests
import sys


def progress(value, max, st=None):
    p = int(100 * value / max)
    html = f"<progress value='{value}' max='{max}' style='width: 25%; accent-color: #41FDFE;'></progress> &emsp;[{p}%]"
    return HTML(html)


latex_pkg = (
    "texlive",
    "texlive-latex-extra",
    "texlive-science",
    "texlive-fonts-extra",
)


def install_manim(lite=False):

    cmd = [("apt-get", "update")]

    cmd.append(("apt-get", "install", "-y", "libpango1.0-dev"))

    if lite:
        # [optional font] STIX Two Text (stixfonts.org)
        font_url = "https://raw.githubusercontent.com/stipub/stixfonts/master/fonts/static_ttf/STIXTwoText-Regular.ttf"
        font_path = "/usr/share/fonts/truetype/stixfonts"
        font_cmd = ("wget", "-P", font_path, font_url)
        cmd.append(font_cmd)
    else:
        for pkg in latex_pkg:
            cmd.append(("apt-get", "install", "-y", pkg))

    cmd.append(("uv", "pip", "install", "--system", "manim"))

    # cmd.append(("uv", "pip", "install", "--system", "IPython==8.21.0"))

    n = len(cmd)
    print("Manim Installation")
    output = display(progress(0, n), display_id=True)

    for i, c in enumerate(cmd, 1):
        subprocess.run(c)
        output.update(progress(i, n))


def config_manim():

    config.disable_caching = True
    config.verbosity = "WARNING"
    config.media_width = "50%"
    config.media_embed = True

    Text.set_default(font="STIX Two Text")

    info = f"Manim – Mathematical Animation Framework (Version {version('manim')})"

    clear_output()
    print(info)


def install_latex():

    cmd = [("apt-get", "install", "-y", pkg) for pkg in latex_pkg]

    n = len(cmd)
    print("LaTeX Installation")
    output = display(progress(0, n), display_id=True)

    for i, c in enumerate(cmd, 1):
        subprocess.run(c)
        output.update(progress(i, n))


def add_plugins(*args):

    mscene_path = Path(__file__).parent

    plugin_url = "https://raw.githubusercontent.com/curiouswalk/mscene/refs/heads/main/source/plugins"

    plugin_csv = f"{plugin_url}/plugins.csv"

    plugins = requests.get(plugin_csv).text.strip().split(",")

    plugin_txt = ", ".join(f"'{i}'" for i in plugins)

    def get_plugin(m):
        filename = f"{m}.py"
        path = f"{mscene_path}/{filename}"
        url = f"{plugin_url}/{filename}"
        cmd = ("wget", "-O", path, url)
        subprocess.run(cmd)

    if "info" in args:
        cmd_info = (
            "- Run '%mscene -p <plugin>' to add plugin.",
            "- Run '%mscene -p all' to add all plugins.",
            "- Run 'from mscene.<plugin> import *' to import plugin.",
            "[source] https://mscene.curiouswalk.com/plugins",
        )

        print("Plugins", "-" * 8, plugin_txt, "-" * 6, *cmd_info, sep="\n")

    elif "all" in args:

        for p in plugins:
            get_plugin(p)
        msg1 = f"[Info] Plugin added to mscene: {plugin_txt}."
        msg2 = "[Note] Run 'from mscene.<plugin> import *' to import plugin."
        print(msg1, msg2, sep="\n")

    else:

        found, not_found = ([], [])

        for i in args:
            if i in plugins:
                get_plugin(i)
                found.append(f"'{i}'")
            else:
                not_found.append(f"'{i}'")

        if not_found:
            p = ", ".join(not_found)
            msg1 = f"[Error] Plugin not found: {p}."
            msg2 = "[Info] Run '%mscene -p info' to view plugins."
            print(msg1, msg2, sep="\n")

        if found and not_found:
            print("-" * 8)

        if found:
            p = ", ".join(found)
            msg1 = f"[Info] Plugin added to mscene: {p}."
            msg2 = f"[Note] Run 'from mscene.<plugin> import *' to import plugin."
            print(msg1, msg2, sep="\n")


if __name__ == "__main__":

    args = sys.argv[1:]

    if "manim" in args and len(args) == 1:

        if "manim" not in sys.modules:
            install_manim()

        from manim import *

        config_manim()

    elif all(i in args for i in ("-l", "manim")) and len(args) == 2:

        if "manim" not in sys.modules:
            install_manim(lite=True)

        from manim import *

        config_manim()

    elif "-p" in args and len(args) > 1:

        args.remove("-p")

        add_plugins(*args)

    elif "latex" in args and len(args) == 1:

        install_latex()

        clear_output()

        print("LaTeX Installation Complete")

    elif "-h" in args and len(args) == 1:

        cmd_info = (
            "— Run '%mscene -l manim' to install Manim without LaTeX.",
            "— Run '%mscene manim' to install Manim with LaTeX.",
            "— Run '%mscene latex' to install only LaTeX.",
            "— Run '%mscene -p <plugin>' to add plugin.",
            "— Run '%mscene -p info' to view plugins.",
            "— Run '%mscene -h' to view commands.",
        )

        print("Commands", "-" * 8, *cmd_info, sep="\n")

    else:

        err = "[Error] Invalid Command"
        msg = "[Info] Run '%mscene -h' to view commands."
        print(err, msg, sep="\n")
