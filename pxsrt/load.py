import numpy as np
from PIL import Image  # type: ignore


def load_image(
    image: str,
    target: str,
    mode: str,
    direction: str,
) -> np.ndarray:
    """Locate file and return image data as an np array."""
    try:
        with Image.open(image) as img:
            if mode != target:
                img = img.convert(target)
            if direction == 'v':
                img = img.rotate(90, expand=True)
            data = np.asarray(img)

    except Exception as e:
        print(f'{type(e).__name__}: {e}')
        raise SystemExit
    else:
        return data
