# importing packages 
from pytube import YouTube 
import os 
import pandas as pd


def youtubeToMP3(video_url,output_filename):
    # url input
    yt = YouTube(video_url) 
    
    # extract only audio 
    video = yt.streams.filter(only_audio=True).first() 
    
    # check for destination to save file 
    output_folder = r"C:/Users/gia21/Downloads/Quenella/Songs"  #Specify the output folder path
    
    # download the file 
    out_file = video.download(output_path=output_folder) 
    
    # save the file 
    new_file = f"{output_folder}/{output_filename}.mp3"
    os.rename(out_file, new_file) 
    
    # result of success 
    print(yt.title + " has been successfully downloaded.")



# Using Excel file
# df = pd.read_excel('song_list.xlsx')

# for index, row in df.iterrows():
#    # Access each element of the row using column headings
#    title = row['title']
#    artist = row['name']
#    url = row['url']
   
#    file_name = artist+' '+title
    
#    youtubeToMP3(url,file_name)

# Manual Download
url = 'https://youtu.be/Pz3Okj_rdyg'
file_name = 'King Paluta Aseda'
youtubeToMP3(url,file_name)
