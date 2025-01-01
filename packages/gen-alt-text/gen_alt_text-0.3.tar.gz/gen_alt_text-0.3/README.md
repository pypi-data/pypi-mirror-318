# gen-alt-text

* This program generates alt-text for images using a local or remote Ollama server. 
* The Ollama server must be running before using this program.
* See [Ollama](https://github.com/ollama/ollama) for installation and usage instructions.

## Installation

``` shell
pipx install gen-alt-text
```

## Usage

``` shell
gen-alt-text -m "llama3.2-vision:11b" ~/pictures/autumn-scenery.jpg
gen-alt-text ~/pictures/winter-scenery.jpg
gen-alt-text -m "llama3.2-vision:90b" ~/pictures/coffee.jpg
```

If the model supplied to the `-m` argument is not currently available on the Ollama server, `gen-alt-text` will pull it for you, and then you must re-run the program to use it.

### Remote Ollama server

For remote Ollama servers, the server must be configured to listen on `0.0.0.0:11434` and port `11434` must be open in the firewall. Edit the systemd service file as follows:

``` shell
sudo systemctl edit ollama.service
```

Add the following:

``` shell
[Service]
Environment="OLLAMA_HOST=0.0.0.0:11434"
```

Save the file and exit the editor.

I personally use a remote server that is not public-facing and is only accessible through my Tailscale network, or tailnet.

On the local machine that you're running this program on, set the `OLLAMA_HOST` environment variable to use a remote Ollama server.

``` shell
export OLLAMA_HOST="http://ollama.tailnet.ts.net:11434"
gen-alt-text ~/pictures/goth_hacker_girl.jpg
```

### Local Ollama server

The `ollama.service` systemd unit should already be configured to listen on `localhost:11434` by default, so no additional configuration is necessary.

## Example

I fed the image below to the llama3.2-vision:11b model.

![fall-leaves-cover-photo.jpg](https://files.hyperreal.coffee/images/fall-leaves-cover-photo.jpg)

This was the alt-text it generated:

> The image depicts a serene autumnal scene, with a cup of coffee placed on a stone surface amidst fallen leaves. In the foreground, a dark brown ceramic mug filled with black coffee sits atop a large, flat gray stone. The mug's handle is positioned towards the right side of the image. Surrounding the mug are vibrant red and orange fallen leaves, which have accumulated in a pile to the left of the stone. Some of these leaves appear to be scattered across the surface of the stone as well. The background of the image features more fallen leaves, creating a sense of depth and atmosphere. The overall mood of the scene is one of tranquility and coziness, evoking feelings of relaxation and comfort.
