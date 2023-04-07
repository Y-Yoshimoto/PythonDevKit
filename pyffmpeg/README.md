#

## ffmpegでm3u8ファイルを生成する

ffmpeg -i input.mp4 -codec copy -hls_time 10 -hls_list_size 0 -hls_segment_filename "output%d.ts" output.m3u8

## オプション

-i: インプットファイル
-hls_time: tsファイルの長さ
-hls_segment_filename: tsファイルのファイル名
-hls_list_size: プレイリストに含まれるtsファイル数
