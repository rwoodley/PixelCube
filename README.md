# PixelCube

Take a video with resolution NxN that has N frames. That is your pixel cube. This app will allow you to slice the cube along any plane.

Python package requirement is PIL. Build your virtual environment and install PIL with these instructions:
```
sudo pip install virtualenv
virtualenv env
source env/bin/activate
pip install Image
```

# How-To/Example

To build the cube, you have to work with ffmpeg and run the python program slice_cube.py.

In this example we're aiming for a 400x400x400 cube. We have a starting image with the wrong resolution and the wrong number of frames. Not a cube, in other words.

Crop it down to 400x400 resolution. :
```
ffmpeg -i extract.mp4 -filter:v "crop=400:400:530:300" out.mp4
```

Build stills, they must be named filenameNNN.jpg where NNN goes from 0 to number of frames:
```
ffmpeg -i out.mp4  frames/filename%03d.jpg
```

Run the python program. It outputs 400 frames labelled outNNN.jpg. If there are fewer than 400 frames, it loops. If there are more, it ignores.
```
python slice_cube.py
```
Combine the frames into a new video:
```
ffmpeg -framerate 30 -i frames/out%03d.jpg outputY.mp4
```

If the original was less than 400 frames long you can extend it so you can place it side by side with the others if you want. Ours was 3.75 seconds long which is 112 frames. Loop to get 400 frames which is 13.39 seconds approx.
```
ffmpeg -re -f lavfi -i "movie=filename=out.mp4:loop=4, setpts=N/(FRAME_RATE*TB)" loop.mp4
ffmpeg -i loop.mp4 -ss 00:00:00 -t 00:00:13.39 loopTruncated.mp4
```

Now stack them all side by side in a new video:
```
ffmpeg -i outputX.mp4 -i outputY.mp4 -i loopTruncated.mp4 -filter_complex hstack=3 stack.mp4
```

