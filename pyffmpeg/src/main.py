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

    ## Download TSfile
    #tsfiles = get_tslist(sample_url)
    #for i in tsfiles:
    #    download_file(i, './files/')

    ## ffmpeg 
    download_hls_ffmpeg(sample_url, dryrun=False)

    print("end")

# HTTPでプレイリストを取得する
def get_tslist(url):
    # Get playlist
    print(url)
    playlist = requests.get(url)
    # URLからベースURLを生成する
    baseurl = url[:url.rfind('/') + 1]
    # m3u8ファイルを抽出する
    m3u8s = [baseurl + m3u8 for m3u8 in extract_lines(playlist.text, '.m3u8')]
    if len(m3u8s) > 0:
        # メディアプレイリストの場合は再帰的に処理する
        return sum([get_tslist(s) for s in m3u8s],[])  
    # tsファイルを抽出する
    return [baseurl + ts for ts in extract_lines(playlist.text, '.ts')]
    
# urlを指定して、ファイルをダウンロードする
def download_file(url, path):
    filename = url.split('/')[-1]
    print('Downloading: ' + filename)
    # with requests.get(url, stream=True) as r:
    #     with open(path + filename, 'wb') as f:
    #         for chunk in r.iter_content(chunk_size=8192):
    #             if chunk:
    #                 f.write(chunk)
    


# プレイリストからm3u8ファイルを抽出する
def extract_lines(file_content, ext: str='.ts'):
    for line in file_content.split('\n'):
        if ext in line:
            yield line.strip()
    
# ffmpegでm3u8ファイルからmp4ファイルを作成する
def download_hls_ffmpeg(url, dryrun=False):
    ## import m3u8
    stream = ffmpeg.input(url, headers='Authentication: token')
    ## Output sample.mp4
    stream = ffmpeg.output(stream, './files/sample.mp4', c='copy')
    if(not dryrun):
        ffmpeg.run(stream)

if __name__ == '__main__':
    main()
