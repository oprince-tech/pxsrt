import args

def target_mode():
    try:
        target = args.mode.upper()
        modes = {'H': 'HSV', 'S': 'HSV', 'V': 'HSV', 'R': 'RGB', 'G': 'RGB', 'B': 'RGB'}

        return modes[target]
        
    except KeyError:
        print("Mode must contain one of the following letters: H/S/V R/G/B")
        exit()
