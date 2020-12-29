import args


def target_mode():
    """Returns a target mode to load image into based on user args.mode"""
    try:
        target = args.mode.upper()
        modes = {'H': 'HSV',
                 'S': 'HSV',
                 'V': 'HSV',
                 'R': 'RGB',
                 'G': 'RGB',
                 'B': 'RGB'}

        return modes[target]

    except:
        print("ERROR: Mode must contain one of the following letters: H/S/V R/G/B")
        raise
