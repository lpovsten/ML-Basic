from models import AudioFile, VideoFile
from handlers import LocalStorageHandler, CloudStorageHandler

audio_file = AudioFile(file_path="/path/to/audio.mp3", metadata={"artist": "Prodigy", "album": "Experience"}, owner="User1")
video_file = VideoFile(file_path="/path/to/video.mp4", metadata={"resolution": "1080p", "length": "3 minutes"}, owner="User2")
image_file = ImageFile(file_path="/path/to/image.jpg", metadata={"width": "1920px", "height": "1080px"}, owner="User3")


local_storage = LocalStorageHandler()
local_storage.store_file(audio_file)

cloud_storage = CloudStorageHandler()
cloud_storage.store_file(video_file)