## gguf node for comfyui [![Static Badge](https://img.shields.io/badge/ver-0.0.3-black?logo=github)](https://github.com/calcuis/gguf/releases)

### for general user(s)
download the compressed comfy pack (7z), decompress it, and run the .bat file striaght
```
py -m gguf_node
```

### for technical user/developer(s)
clone this repo to custom_nodes folder (./ComfyUI/custom_nodes)
```
git clone https://github.com/calcuis/gguf
```
check the dropdown menu for `gguf`

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
- design your prompt; or
- generate a random prompt/descriptor by the [simulator](https://prompt.calcuis.us) (though it might not be applicable for all)