## gguf node for comfyui [![Static Badge](https://img.shields.io/badge/ver-0.0.4-black?logo=github)](https://github.com/calcuis/gguf/releases)

[<img src="https://raw.githubusercontent.com/calcuis/comfy/master/gguf.gif" width="128" height="128">](https://github.com/calcuis/gguf)

#### install it via pip/pip3
```
pip install gguf-node
```

### for all/general user(s)
enter the user menu by:
```
py -m gguf_node
```
opt `1` to download the compressed comfy pack (7z), decompress it, and run the .bat file striaght

### for technical user/developer(s)
opt `2` to clone the gguf repo to the current directory (navigate to `./ComfyUI/custom_nodes` first)

>Please select:
>1. download the full pack
>2. clone the node only
>
>Enter your choice (1 to 2): _

alternatively, you could execute the git clone command to perform that task (see below):

navigate to `./ComfyUI/custom_nodes`, clone the gguf repo to that folder
```
git clone https://github.com/calcuis/gguf
```
check the dropdown menu for `gguf`

![screenshot](https://raw.githubusercontent.com/calcuis/comfy/master/gguf-node.png)

if you opt to clone the repo to custom_nodes (method 2); you need gguf-[connector](https://pypi.org/project/gguf-connector) as well

### setup (in general)
- drag gguf file(s) to diffusion_models folder (./ComfyUI/models/diffusion_models)
- drag clip or encoder(s) to text_encoders folder (./ComfyUI/models/text_encoders)
- drag controlnet adapter(s), if any, to controlnet folder (./ComfyUI/models/controlnet)
- drag lora adapter(s), if any, to loras folder (./ComfyUI/models/loras)
- drag vae decoder(s) to vae folder (./ComfyUI/models/vae)

### workflow
- drag the workflow json file to the activated browser; or
- drag any generated output file (i.e., picture, video, etc.; which contains the workflow metadata) to the activated browser

### simulator
- design your own prompt; or
- generate a random prompt/descriptor by the [simulator](https://prompt.calcuis.us) (though it might not be applicable for all)

### reference
[comfyui](https://github.com/comfyanonymous/ComfyUI)
[comfyui-gguf](https://github.com/city96/ComfyUI-GGUF)
[gguf-comfy](https://github.com/calcuis/gguf-comfy)
[testkit](https://huggingface.co/calcuis/gguf-node)