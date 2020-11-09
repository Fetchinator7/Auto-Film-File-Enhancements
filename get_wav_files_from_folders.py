# This script gets all the WAV files from folders for my zoom h6.

import pathlib as paths

parent_folder = paths.Path(paths.Path(__file__).parent)
parent_directory = paths.Path.joinpath(parent_folder, 'wav_files_in')
out_directory = paths.Path.joinpath(parent_folder, 'wav_files_out')

if parent_directory.exists() is False:
    parent_directory.mkdir()
if out_directory.exists() is False:
    out_directory.mkdir()

end_ext = '.WAV'

for path in parent_directory.glob(f"**/*{end_ext}"):
    moved_path = paths.Path.joinpath(out_directory, path.name)
    path.rename(moved_path)
    print(f'Renamed {path} to {moved_path}')
