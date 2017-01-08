# PixelCube

Take a video with resolution X*X that has X frames. That is your pixel cube. This app will allow you to slice the cube along any plane.

# Example

In this example we're aiming for a 400x400x400 cube.

ffmpeg -i ../dance148.mp4  -ss 00:00:46 -t 00:00:03.75  extract.mp4

Take starting image with the wrong resolution and the wrong number of frames. Not a cube, in other words.

Crop it down to 400x400:
    ffmpeg -i extract.mp4 -filter:v "crop=400:400:530:300" out.mp4

