#!/usr/bin/python3

"""'%run mscene -h' — view commands"""

from IPython.display import display, HTML, clear_output
from pathlib import Path
import subprocess
import requests
import sys


def progress(value, max, st=None):
    p = int(100 * value / max)
    html = f"<progress value='{value}' max='{max}' style='width: 25%; accent-color: #41FDFE;'></progress> &emsp;[{p}%]"
    return HTML(html)

base_pkg = ("libpango1.0-dev", "libcairo2-dev")
latex_pkg = ("texlive",
            "texlive-latex-extra",
            "texlive-science",
            "texlive-fonts-extra",
            )

def install_manim(lite=False):

    cmd = [("apt-get", "install", "-y", pkg) for pkg in base_pkg]

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

    plugin_url1 = "https://raw.githubusercontent.com/curiouswalk/mscene/refs/heads/main/docs/src"

    plugin_csv = f"{plugin_url}/plugins.csv"

    plugins = requests.get(plugin_csv).text.strip().split(',')

    def get_plugin(m):
        filename = f"{m}.py"
        path = f"{mscene_path}/{filename}"
        url = f"{plugin_url1}/{filename}"
        cmd = ("wget", "-O", path, url)
        subprocess.run(cmd)


    if "info" in args:

        p = ", ".join(f"'{i}'" for i in plugins)
        msg1 = "- Run '%mscene -m <plugin>' to add plugin."
        msg2 = "- Run '%mscene -m all' to add all plugins."
        msg3 = "- Run 'from mscene.<plugin> import *' to import plugin."
        print("Plugins", "-"*8, p, "-"*6, msg1, msg2, msg3, sep="\n")

    elif "all" in args:

        for i in plugins:
            get_plugin(i)
        p = ", ".join(f"'{i}'" for i in plugins)
        msg1 = f"[Info] Plugin added to mscene: {p}."
        msg2 = "[Note] Run 'from mscene.<plugin> import *' to import plugin."
        print(msg1, msg2, sep="\n")

    else:

        found, not_found = ([],[])
        for i in args:
            if i in plugins:
                get_plugin(i)
                found.append(f"'{i}'")
            else:
                not_found.append(f"'{i}'")

        if not_found:
            p = ", ".join(not_found)
            msg1 = f"[Error] Plugin not found: {p}."
            msg2 = "[Note] Run '%mscene -m info' to view plugin info."
            print(msg1, msg2, sep="\n")

        if found and not_found:
            print("-"*8)

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

    elif "-m" in args and len(args) > 1:
      
        args.remove("-m")

        add_plugins(*args)

    elif "latex" in args and len(args) == 1:

        install_latex()

        if "manim" not in sys.modules:
            install_manim(lite=True)

        from manim import *

        config_manim()

    elif "-h" in args and len(args) == 1:

        cmd_info = "Commands\n--------\n'%run mscene manim' — install Manim\n'%run mscene -l manim' — install Manim without LaTeX\n'%run mscene latex' — install LaTeX\n'%run mscene -h' — view commands"
        print(cmd_info)

    else:

        err_msg = "Invalid Command\n'%run mscene -h' — view commands"
        print(err_msg)
