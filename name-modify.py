import argparse
import os
import glob
import io


# Set default paths
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
DEFAULT_TEXT_DIR = os.path.join(SCRIPT_PATH, 'naver-nanum-handwriting-fonts.txt')
DEFAULT_FONTS_DIR = os.path.join(SCRIPT_PATH, 'fonts')


# Filename modify function
def name_modify(txt_dir, fonts_dir, output_dir):

    fonts = sorted(glob.glob(os.path.join(fonts_dir, '*.ttf')))

    if not os.path.exists(output_dir):
        os.makedirs(os.path.join(output_dir))

    # Generate list from .txt
    with io.open(txt_dir, 'r', encoding='utf-8') as f:
        labels = f.read().splitlines()

    # Rename
    idx = 0

    for f in fonts:
        fontname = fonts[idx][6:-4]
        new_f = f.replace(fontname, labels[idx])
        os.rename(f, new_f)
        print('{} --> {}'.format(f,new_f))
        idx = idx + 1


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    
    parser.add_argument('--txt-dir', type=str, dest='txt_dir', default=DEFAULT_TEXT_DIR, help='File containing newline delimited labels.')
    parser.add_argument('--fonts-dir', type=str, dest='fonts_dir', default=DEFAULT_FONTS_DIR, help='Directory of ttf fonts to use.')
    parser.add_argument('--output-dir', type=str, dest='output_dir', default=DEFAULT_OUTPUT_DIR, help='Output directory to store modified name')
   
    args = parser.parse_args()

    name_modify(args.txt_dir, args.fonts_dir, args.output_dir)