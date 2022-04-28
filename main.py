import json

def translate(files_src):
    try:
        with open(files_src, "r") as read_file:
            data = json.load(read_file)
            for key in data['playlists']:
                for song in key['items']:
                    print(song["track"]["artistName"] +" - "+ song["track"]["trackName"])
    except:
        with open(files_src, "r") as read_file:
            data = json.load(read_file)
           
            for song in data['tracks']:  
                #print(song)
                print(song["artist"] +" - "+ song["track"])
        
translate('1_Playlist1.json')
translate('2_YourLibrary.json')