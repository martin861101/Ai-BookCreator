from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5", 
    torch_dtype=torch.float32
).to("cpu")

prompt = "Book cover with A4 dimentions for a AI educational book. text must say 'Intelligence with n8n'"
image = pipe(prompt).images[0]
image.save("cover2.png")
