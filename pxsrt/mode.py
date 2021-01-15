def target_mode(target: str) -> str:
    """Returns a target mode to load image into based on user args.mode"""
    try:
        modes = {'H': 'HSV',
                 'S': 'HSV',
                 'V': 'HSV',
                 'R': 'RGB',
                 'G': 'RGB',
                 'B': 'RGB'}

    except Exception as e:
        print(f"{type(e).__name__}: {e}")

    return modes[target]
