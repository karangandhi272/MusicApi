from ast import excepthandler
from flask import Flask, send_file
import sys
from selenium import webdriver 
import os 
from  pytube import YouTube
from moviepy.editor import * 
app = Flask(__name__)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_argument("disable-gpu")

@app.route("/<songname>",  methods=["GET", "POST"])
def home(songname):
        if songname != "favicon.ico" and not os.path.exists(f'{songname}.mp3'):
                driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)
                driver.get(f"https://www.youtube.com/results?search_query={songname}+lyrics")
                s = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a').get_attribute('href')
                print(s)
                video = YouTube(s)
                video = video.streams.filter(only_audio = True).first()
                file = video.download()
                new_file =  f'{songname}.mp3'
                os.rename(file, new_file)
                return send_file(f'{songname}.mp3', as_attachment=True)
                
        
                        



