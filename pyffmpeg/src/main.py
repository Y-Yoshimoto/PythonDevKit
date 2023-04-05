#!/usr/bin/env python
# coding:utf-8
# import requests
import requests
# https://kkroening.github.io/ffmpeg-python/
import ffmpeg

def main():
    print("start")
    
    # Get access token
    #
    # Sample URL for HLS
    sample_url = "http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8"
    
    # Download HLS
    ## ffmpeg Command Sample
    ## ffmpeg -i "http://hoge/hoge.m3u8" -c copy -bsf:a aac_adtstoasc "sample_O.mp4"
    
    ## Python Sample
    stream = ffmpeg.input(sample_url)
    
    stream = ffmpeg.output(stream, 'sample.mp4')

    print("end")


if __name__ == '__main__':
    main()
