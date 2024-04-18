from pytube import YouTube
 
def download_video(videourl, outputpath="."): 
     try:

         yt = YouTube(videourl) # creates a YouTube object by passing the video_url to its constructor.
 
         # filter_stream = yt.streams.filter(resolution="480p")
         video_stream = yt.streams.get_highest_resolution()
 
         # Download the video
         print(f"Downloading: {yt.title}")
         video_stream.download(output_path)
         print("Download complete!")
 
     except Exception as e:
         print(f"An error occurred: {e}")
 
if __name__ == "__main__":
 
     video_url = "https://youtu.be/isKgnM7CQ00?si=_8-_lD_eS4-AXerB" #insert video url
     output_path = "./downloads"
 
     download_video(video_url, output_path)