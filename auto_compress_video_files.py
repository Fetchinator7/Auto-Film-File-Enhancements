# This script automatically normalizes the audio for the input file(s) by increasing the max_volume and down mixes to stereo.
# It also sort the short files into a separeate folder since those probably aren't good takes.
# Dependencies: ffmpeg.py, system.py, ffmpeg (and ffprobe) and python3.
# NOTE: This only works with video/audio files, not sub folders as well.

from pathlib import Path
from pathlib import PosixPath
import sys
sys.path.append(str(Path.joinpath(
	Path(__file__).parent, 'FFmpeg-Commands')))
sys.path.append(str(Path.joinpath(
	Path(__file__).parent, 'System-Commands')))
import FileOperations as fo
import system as syst
import datetime as dates

delete_after_ren = False
create_month_date_dir = True
short_duration_sec_threshold = 30

# These are the names of the different output folders.
out_key = 'Out'
short_key = 'Short'

# Path to input and output folders.
parent_folder = Path(Path(__file__).parent)
input_directory = Path.joinpath(parent_folder, 'In')
output_directory = Path.joinpath(parent_folder, out_key)
output_short_directory = Path.joinpath(output_directory, short_key)

if input_directory.exists() is False:
	input_directory.mkdir()
if output_directory.exists() is False:
	output_directory.mkdir()

if type(input_directory) is PosixPath:
	# A mac may generate a .DS_Store file that isn't necessary and this script produces an error when the input is a
	#   .DS_Store so delete that file if it exists for the input and output directories.
	del_DS_file_list = [input_directory, output_directory]
	syst.Paths().del_ds_store(del_DS_file_list)


# Main function to run the loudnorm_stereo method from the ffmpeg_cmds module.
def main():
	files = []
	vid_ext = '.MP4'
	aud_ext = '.WAV'
	# Get all audio and video files.
	for vid in input_directory.glob(f"**/*{vid_ext}"):
		files.append(vid)
	for aud in input_directory.glob(f"**/*{aud_ext}"):
		files.append(aud)
	# Sort by date modified since sorting by date created gives inconsistent results.
	files.sort(key=lambda f: f.stat().st_mtime)

	for index, file in enumerate(files):
		# Get how long the input is.
		timecode_duration_str = fo.MetadataAcquisition(file, print_all_info=False, print_meta_value=False).return_metadata(duration=1)[0]
		sec_duration = fo.FileOperations(file, output_directory)._return_input_duration_in_sec(timecode_duration_str)
		# If the input is short put it in a "Short" folder but otherwise it goes in the base output folder.
		if sec_duration < short_duration_sec_threshold:
			print(f'{file.stem} is {sec_duration} seconds long which is less than the {short_duration_sec_threshold} second threshold so outputting to "Short" directory.', end='')
			file_out_dir = make_output_dir(short_key)
		else:
			file_out_dir = make_output_dir(out_key)
		# Normalize the audio.
		fo.FileOperations(file, file_out_dir).loudnorm_stereo()
		out_path = Path.joinpath(file_out_dir, file.name)
		out_path.rename(Path.joinpath(out_path.parent, f'{index + 1}-{out_path.name}'))
		if delete_after_ren is True:
			file.unlink()
			print(f'Deleted input file: "{file.name}"')


def make_output_dir(out_dir_name):
	if create_month_date_dir is True:
		# Create a folder for this month.
		out_dir_parent = Path.joinpath(output_directory, dates.datetime.now().strftime("%m-%d"))
		if out_dir_parent.exists() is False:
			out_dir_parent.mkdir()
	else:
		out_dir_parent = output_directory

	# Make a "Short" folder if necessary.
	if out_dir_name == short_key:
		out_dir = Path.joinpath(out_dir_parent, short_key)
		if out_dir.exists() is False:
			out_dir.mkdir()
	else:
		out_dir = out_dir_parent
	return out_dir


main()
