import json

# Input fuzzing for title lookup
def fuzz(some_text):
    return some_text # No longer using but keeping here due to many calls
    # some_text = str(some_text)
    # return_value = ''
    # for char in some_text:
    #     if char in 'abcdefghijklmnopqrstuvwxyz':
    #         return_value += char.lower()
    # return return_value


# Read songs into a python dict
def get_songs():
    with open('songs.json', 'r') as f:
        songs_dict = dict(json.load(f))
        return songs_dict
    
# Add a song
def add_song(title, youtube_url):
    songs = get_songs() # Load songs file into dict
    songs[title] = youtube_url # Add song name and url to dict
    with open('songs.json', 'w') as f:
        json.dump(songs, f, indent=4) # Write back to json in a pretty format

# Remove a song
def remove_song(user_title):
    songs = get_songs() # Load songs file into dict
    if user_title in list(songs):
        del songs[user_title] # Remove song name and url from dict
        with open('songs.json', 'w') as f:
            json.dump(songs, f, indent=4) # Put back
        return 'complete'
    else:
        return 'fail'