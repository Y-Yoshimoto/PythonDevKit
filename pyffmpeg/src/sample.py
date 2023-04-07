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
    ## ffmpeg -i "http://hoge/hoge.m3u8" -c copy -bsf:a aac_adtstoasc "./files/sample_C.mp4"
    
    ## Python Sample
    ## import m3u8
    stream = ffmpeg.input(sample_url, headers='Authentication: token')
    ## Output sample.mp4
    stream = ffmpeg.output(stream, './files/move/sample.mp4', c='copy')
    ffmpeg.run(stream)
    print("end")


if __name__ == '__main__':
    main()
