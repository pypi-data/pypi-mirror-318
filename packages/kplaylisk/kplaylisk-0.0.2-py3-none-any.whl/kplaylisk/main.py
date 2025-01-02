# coding: utf-8

from kplaylisk.parsing import get_args
from kplaylisk.process import build_playlist


def main():
    args = get_args()
    if args.command == "build":
        build_playlist(in_paths=args.paths[:-1], out_path=args.paths[-1],
                       if_abs_path=args.abs_path,
                       audio_only=args.audio_only, video_only=args.video_only,
                       if_shuffle=args.shuffle, if_sort=args.sort,
                       print_not_included=args.print_not_included)
    else:
        print(f"main: Failed successfully. ")
        exit(-1)


if __name__ == "__main__":
    main()
