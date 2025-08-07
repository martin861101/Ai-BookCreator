from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5", 
    torch_dtype=torch.float32
).to("cpu")

prompt = "Book cover for a sci-fi novel titled 'Echoes of the Void'"
image = pipe(prompt).images[0]
image.save("cover.png")
