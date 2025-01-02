<div align="center">
<img src="https://github.com/painebenjamin/taproot/assets/57536852/1ccacf0c-9609-40cc-a136-7ae83d411805" /><br />
A massively parallel task-based AI inference engine
</div>

TAPROOT enables developers to write Python scripts that invoke task-based methods efficiently and effectively in a deployment-agnostic manner.
Generally these are AI models (but not always.)

# Tap

Your primary interface into Taproot when performing inference.

```py
from PIL import Image
from taproot import Tap

async def main() -> None:
    # Perform edge detection on an image and save it.
    tap = Tap() # Expects a local cluster running on the default port
    image = Image.open("./base.png")
    edge = await tap("edge-detection", image)
    edge.save("./edge.png")

if __name__ == "__main__":
    main()
```

# Root

Your interface into taproot when registering a task able to completed by a Taproot cluster.

```py
from __future__ import annotations
from typing import TYPE_CHECKING
from taproot import Root

if TYPE_CHECKING: # Type checking is strictly enforced
    from PIL import Image

__all__ = ["CannyEdgeDetection"] # Must be defined in exposed modules

class CannyEdgeDetection(Root):
    """
    Document the capabilities of the root. Task and model combinations must be unique.
    """
    task = "edge-detection"
    model = "canny"

    def __call__(self, image: Image.Image, lower: int=100, upper: int=200) -> Image.Image:
        """
        The __call__ method will be introspected to enable parameter-passing.
        import cv2
        import numpy as np
        from PIL import Image
        canny = cv2.Canny(np.array(image), lower, upper)[:, :, None]
        return Image.fromarray(np.concatenate([canny, canny, canny], axis=2))
```

# Taproot

Your interface to run a taproot cluster.

```py
from taproot import Taproot

async def main():
    taproot = Taproot()
    await taproot.run() # Local cluster, default port

if __name__ == "__main__":
    main()
```
