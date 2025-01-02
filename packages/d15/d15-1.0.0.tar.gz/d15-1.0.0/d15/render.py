from PIL import Image


def d15_render(text: str) -> Image.Image:
    print(f"Rendering image from text: {text} [mocked]")
    return Image.new("RGB", (256, 256), (255, 0, 0))


__all__ = ["d15_render"]
