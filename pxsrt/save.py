import os
from pxsrt import args


def save(output):
    """Save pixel sorted image ('./images/export/')"""
    sub_path = './images/export/'
    base, file_extension = os.path.splitext(os.path.basename(args.input_image))
    if not os.path.exists(sub_path):
        os.makedirs(sub_path)

    save_choice = (input("Would you like to save? Y/N: ")).lower()
    if save_choice == "y":
        save_as_choice = (input("Save as (leave blank for auto renaming): "))
        print("Saving Image..")
        if save_as_choice == '':
            output_base = '{}_{}{}({}-{}){}{}{}'.format(base,
                                                        args.mode,
                                                        args.direction,
                                                        args.l_threshold,
                                                        args.u_threshold,
                                                        args.reverse,
                                                        args.outer,
                                                        file_extension)

        else:
            output_base = save_as_choice

        output_path = ('/').join(args.input_image.split('/')[:-1])
        output_file = output_path + sub_path + output_base
        output.save(output_file)
