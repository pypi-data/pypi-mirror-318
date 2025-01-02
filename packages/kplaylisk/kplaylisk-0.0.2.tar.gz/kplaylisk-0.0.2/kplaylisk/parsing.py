# coding: utf-8

import os
import argparse
from kplaylisk import __version__


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="kplaylisk is m3u8 playlist builder. ")

    parser.add_argument("--version", action="version", version=f"V{__version__}", help="Check version. ")

    subparsers = parser.add_subparsers(dest="command", required=True)

    build_parser = subparsers.add_parser("build", help='main')

    build_parser.add_argument("paths", type=str, nargs="+", help="Paths to the folders with media files. ")

    build_parser.add_argument("--abs_path", default=False, action="store_true",
                              help="In playlist will be written absolute paths. ")

    build_parser.add_argument("--shuffle", default=False, action="store_true",
                              help="Shuffle file order inside m3u8 file. ")
    build_parser.add_argument("--sort", default=False, action="store_true",
                              help="Sort by alphabet file order inside m3u8 file. ")

    build_parser.add_argument("--video_only", default=False, action="store_true",
                              help="Only video files will be added to the playlist.")
    build_parser.add_argument("--audio_only", default=False, action="store_true",
                              help="Only audio files will be added to the playlist.")

    build_parser.add_argument("--print_not_included", default=False, action="store_true",
                              help="All media files that are not included in the playlist, "
                                   "but are in the directories, will be output. ")

    args = parser.parse_args()

    if args.command == "build":
        if args.shuffle and args.sort:
            print("Only one of this options can be: \"--shuffle\" or \"--sort\". Not both. ")
            exit(-1)

        if args.video_only and args.audio_only:
            print("Only one of this options can be: \"--video_only\" or \"--audio_only\". Not both. ")
            exit(-1)

        if len(args.paths) < 2:
            print("Last file in sequence must be output m3u8-file. ")
            exit(-1)

        if os.path.splitext(args.paths[-1])[1].lower() != ".m3u8":
            print("Last file in sequence must be output m3u8-file. ")
            exit(-1)

    return args
