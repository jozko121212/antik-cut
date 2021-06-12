from constants import *
import pathlib
import json
import os
import subprocess


def check_constants():
    file_list = file2list(videos_info_file)
    print("listing cut movie dir: {}".format(os.listdir(cut_movies_dir)))
    for line in file_list:
        movie_id, start_time = line.split(';')
        start_time = start_time.rstrip()

        movie_id_filename = f"{movie_id}.{movie_info_suffix}"
        movie_filename = f"{movie_id}_0.{movie_suffix}"

        movie_filename_fullpath = f"{uncut_movies_dir}/{movie_filename}"
        movie_info_fullpath = f"{uncut_movies_dir}/{movie_id_filename}"

        movie_file = pathlib.Path(movie_filename_fullpath)
        if movie_file.exists():
            movie_info = file2json(movie_info_fullpath)
            cut_movie_filename = f"{movie_info['name']}"
            cut_movie_description_list = movie_info['desc'].splitlines()
            cut_movie_description = cut_movie_description_list[0][0:25]
            cut_movie_filename = f"{cut_movie_filename}_{cut_movie_description}.{movie_suffix}"
            cut_movie_filename = cut_movie_filename.replace(' ','_')
            cut_movie_filename = cut_movie_filename.replace(':', '')
            cut_movie_filename = cut_movie_filename.replace('(', '')
            cut_movie_filename = cut_movie_filename.replace(')', '')
            cut_movie_filename = cut_movie_filename.replace('/', '-')
            cut_movie_filename_fullpath = f"{cut_movies_dir}/{cut_movie_filename}"
            print(f"cut movie filename: {cut_movie_filename}")

            print("going to cut movie file: {} as {}".format(movie_filename, cut_movie_filename))
            bash_command = f"ffmpeg -i {movie_filename_fullpath} -ss {start_time} -c:v copy -c:a copy {cut_movie_filename_fullpath}"
            cut_movie_file = pathlib.Path(cut_movie_filename_fullpath)
            print(f"cut movie file: {cut_movie_file}")
            if cut_movie_file.exists():
                print("file {} exists".format(cut_movie_file.name))
                continue
            print("running: {}".format(bash_command))
            # process = subprocess.run(bash_command.split(), stdout=subprocess.PIPE)
            # output, error = process.communicate()
            print("")
        else:
            print("movie not found: {}".format(movie_filename))
            print("")


def file2list(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    return lines


def file2json(file):
    with open(file, 'r') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    check_constants()
