# coding: utf-8

import os
import re
import random
import m3u8
from tqdm import tqdm
from ksupk import get_files_list, get_audio_extensions, get_video_extensions, write_to_file_str


def is_url(path: str) -> bool:
    # url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    # Регулярное выражение для проверки HTTP/HTTPS URL, включая IP-адреса
    url_pattern = re.compile(
        # r'^(https?|sftp)://'  # Допускаем протоколы http, https или sftp
        r'^(https?://)' # Протокол (http или https)
        r'('
        r'(([A-Za-z0-9-]+\.)+[A-Za-z]{2,})'  # Доменное имя (e.g. example.com)
        r'|'  # Или
        r'((\d{1,3}\.){3}\d{1,3})'  # IPv4 адрес (e.g. 192.168.0.1)
        r')'
        r'(:\d+)?'  # Опциональный порт (e.g. :8080)
        r'(/.*)?$',  # Опциональный путь/ресурс (e.g. /path/to/resource)
        re.IGNORECASE  # Игнорировать регистр
    )
    return bool(url_pattern.match(path))


def build_playlist(in_paths: list[str, ...], out_path: str,
                   if_abs_path: bool,
                   audio_only: bool, video_only: bool,
                   if_shuffle: bool, if_sort: bool,
                   print_not_included: bool):
    files = []
    if is_url(out_path):
        print(f"Output file \"{out_path}\" cannot be url. ")
        exit(-1)

    exit_needed = False
    for in_path_i in in_paths:
        if not is_url(in_path_i) and not os.path.exists(in_path_i):
            print(f"* \"{in_path_i}\" is not exists. ")
            exit_needed = True
            continue
    if exit_needed:
        exit(-1)

    for in_path_i in in_paths:
        if not is_url(in_path_i):
            if os.path.isdir(in_path_i):
                files += get_files_list(in_path_i)
            elif os.path.isfile(in_path_i):
                files += [in_path_i]
            else:
                print(f"build_playlist 1: Failed successfully. ")
                exit(-1)
        else:
            files += [in_path_i]

    if audio_only:
        needed_ext = get_audio_extensions()
    elif video_only:
        needed_ext = get_video_extensions()
    else:
        needed_ext = set(list(get_video_extensions()) + list(get_audio_extensions()))

    if if_abs_path:
        files = [os.path.abspath(file_i) if not is_url(file_i) else file_i for file_i in files]

    if if_shuffle:
        random.shuffle(files)
    elif if_sort:
        files = sorted(files)

    playlist = m3u8.M3U8()

    for file_i in tqdm(files):
        if is_url(file_i):
            playlist.add_segment(m3u8.Segment(uri=file_i, duration=None))
        else:
            if os.path.splitext(file_i)[1].lower() in needed_ext:
                playlist.add_segment(m3u8.Segment(uri=file_i, duration=None))
            else:
                if print_not_included:
                    print(f"*\t File \"{file_i}\" will not included in playlist. ")

    write_to_file_str(out_path, playlist.dumps())
    print(f"Done! m3u8 file saved to \"{out_path}\". ")
