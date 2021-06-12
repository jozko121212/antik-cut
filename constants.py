volumes_directory = '/run/user/1000/gvfs'
video_volume = 'afp-volume:host=JARVIS.local,user=mokusky,volume=video'
movies_volume = 'MOVIES'
uncut_movies = 'to_cut_backup'
videos_info = 'videos_info.txt'
cut_movies = 'to_cut_renamed_backup'

movie_info_suffix = 'pvr_meta'
movie_suffix = 'mp4'

uncut_movies_dir = f'{volumes_directory}/{video_volume}/{movies_volume}/{uncut_movies}'
cut_movies_dir = f'{volumes_directory}/{video_volume}/{movies_volume}/{cut_movies}'
videos_info_file = f'{volumes_directory}/{video_volume}/{movies_volume}/{uncut_movies}/{videos_info}'
