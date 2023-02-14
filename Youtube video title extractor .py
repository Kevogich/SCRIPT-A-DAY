from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set DEVELOPER_KEY to the API key value from the Google Developers Console.
# Replace with your own key.
DEVELOPER_KEY = "YOUR_API_KEY"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def get_channel_videos(channel_id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Retrieve the contentDetails of the channel.
    channels_response = youtube.channels().list(
        part='contentDetails',
        id=channel_id
    ).execute()

    for channel in channels_response['items']:
        # Retrieve the playlist id that corresponds to the channel's uploaded videos.
        uploads_playlist_id = channel['contentDetails']['relatedPlaylists']['uploads']

        # Retrieve the videos in the uploads playlist.
        playlistitems_list_request = youtube.playlistItems().list(
            playlistId=uploads_playlist_id,
            part='snippet',
            maxResults=50
        )

        while playlistitems_list_request:
            playlistitems_list_response = playlistitems_list_request.execute()

            # Print the title of each video.
            for video in playlistitems_list_response['items']:
                print(video['snippet']['title'])

            playlistitems_list_request = youtube.playlistItems().list_next(
                playlistitems_list_request, playlistitems_list_response)
                
# Replace CHANNEL_ID with the ID of the channel you want to extract video titles from.
get_channel_videos('CHANNEL_ID')
