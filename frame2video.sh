ffmpeg -r 30 -i img_%04d.png -vcodec libx264 -pix_fmt yuv420p -r 30 output_video.mp4
