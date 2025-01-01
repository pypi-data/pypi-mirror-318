#!/usr/bin/env python3

"""gen-alt-text

Usage:
    gen-alt-text [-m MODEL] <path_to_image>
    gen-alt-text -h

Options:
    -h          show this help message and exit
    -m MODEL    Use MODEL as the model. If MODEL is not provided, it defaults
                to llama3.2-vision:11b.

Supported vision models:
    - llama3.2-vision:11b
    - llama3.2-vision:90b
    - llava:7b
    - llava:13b
    - llava:34b
    - llava-llama3:8b
    - bakllava:7b
    - moondream:1.8b
    - llava-phi3:3.8b
    - minicpm-v:8b

Examples:
    gen-alt-text -m llama3.2-vision:90b ~/pictures/rubber_duck.jpg
    gen-alt-text ~/pictures/coffee.jpg
"""

import os

from docopt import docopt
from ollama import Client, ResponseError
from rich.console import Console
from rich.markdown import Markdown


def main():
    args = docopt(__doc__)
    vision_models = [
        "llama3.2-vision:11b",
        "llama3.2-vision:90b",
        "llava:7b",
        "llava:13b",
        "llava:34b",
        "llava-llama3:8b",
        "bakllava:7b",
        "moondream:1.8b",
        "llava-phi3:3.8b",
        "minicpm-v:8b",
    ]

    print()
    console = Console()

    if args["-m"]:
        if args["-m"] not in vision_models:
            console.print(
                "You must use a vision model to generate alt-text from images."
            )
            print()
            console.print("[bold magenta]Available vision models:[/bold magenta]")
            for model in vision_models:
                print(f"- {model}")
            print()
            exit("Select a model above and run the command again.")
        else:
            model = args["-m"]
    else:
        model = "llama3.2-vision:11b"

    if os.getenv("OLLAMA_HOST"):
        client = Client(host=os.getenv("OLLAMA_HOST"))
    else:
        client = Client(host="http://localhost:11434")

    try:
        with console.status(
            f"[bold magenta] {model}[/bold magenta] is generating alt-text for "
            + args["<path_to_image>"]
            + "...",
            spinner="aesthetic",
        ):
            response = client.chat(
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": "Describe this image concisely",
                        "images": [args["<path_to_image>"]],
                    }
                ],
                stream=False,
            )
    except ResponseError as e:
        if e.status_code == 404:
            with console.status(
                f"[bold magenta] {model}[/bold magenta] was not found on the ollama server. Pulling it now...",
                spinner="aesthetic",
            ):
                client.pull(model=model)
            console.print(
                f"Successfully pulled [bold magenta]{model}[/bold magenta]. You may try running the command again."
            )
            exit(0)
        else:
            print("Error: ", e.error)
            exit(1)

    console.print(Markdown(response["message"]["content"]))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit("Keyboard interrupt detected. Exiting.")
