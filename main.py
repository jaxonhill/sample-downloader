from pytube import YouTube
import re
from datetime import date

# Create the regex needed to grab only letters and numbers from title
PATTERN = re.compile(r"[0-9A-Za-z]*")

# TODO TYPE THE FILE DIRECTORY IN BETWEEN THE QUOTES HERE WITH THE EXACT PATH YOU WANT THE FILES TO GO TO
FILE_PATH_TO_SAVE_TO = r""  # ex: "C:\Desktop\Samples"


def create_sanitized_title(original_title: str) -> str:
    # Get date to append to end of file name
    current_date = date.today()
    # Split the title on pattern to only match letters and numbers
    split_title = re.findall(pattern=PATTERN, string=original_title)
    # Filter out any empty strings and whitespace strings, lowercase all elements
    split_title = list(filter(lambda part: part and not part.isspace(), split_title))
    split_title = list(map(lambda part: part.lower(), split_title))
    # Return final title. Each word in title joined by an _ and date appended to end
    return ("_").join(split_title) + f"(DOWNLOADED_{current_date}).m4a"


def main():
    # Check that they have specified a file path
    if not FILE_PATH_TO_SAVE_TO:
        print(
            "You need to specify a file path in the .py file.\nFind the TODO comment at the top."
        )
        return

    # Create the YouTube video object based on user link
    link = input("\nEnter the YouTube link for the sample:\n")
    print("---")
    print("\nFetching and downloading from YouTube (this may take a few seconds)...")

    try:
        yt = YouTube(link)
    except Exception as e:
        print("Something went wrong. Ensure this is a valid YouTube link.")
        return

    # Get the raw title of the video and create sanitized file title from it
    raw_title = yt.title
    file_safe_title = create_sanitized_title(raw_title)

    # Get the highest quality audio stream (mp4 audio)
    highest_quality_audio_stream = yt.streams.get_audio_only()

    # Download the audio to path set above with sanitized file name made from video title
    try:
        path_audio_saved_to = highest_quality_audio_stream.download(
            output_path=FILE_PATH_TO_SAVE_TO, filename=file_safe_title
        )
    except Exception as e:
        print("Something went wrong when downloading.")
        return

    print(f'Sample downloaded successfully!\n\nSAVED TO\n"{path_audio_saved_to}"\n')


if __name__ == "__main__":
    main()
