def target_mode(target: str) -> str:
    """Returns a target mode to load image into based on user args.mode"""
    modes = {
        'H': 'HSV',
        'S': 'HSV',
        'V': 'HSV',
        'R': 'RGB',
        'G': 'RGB',
        'B': 'RGB',
    }

    return modes[target]
