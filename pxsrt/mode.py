def target_mode(target: str) -> str:
    """Returns a target mode to load image into based on user args.mode"""
    try:
        modes = {'H': 'HSV',
                 'S': 'HSV',
                 'V': 'HSV',
                 'R': 'RGB',
                 'G': 'RGB',
                 'B': 'RGB'}

    except KeyError as e:
        print(f"{type(e).__name__}: {e} is an invalid mode. "
              f"Mode must contain one of the following letters: H/S/V R/G/B")
        raise SystemExit
    except Exception as e:
        print(f"{type(e).__name__}: {e}")

    return modes[target]
