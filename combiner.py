from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx

clip1 = VideoFileClip("video1.mp4").subclip(10, 20)
clip2 = VideoFileClip("video2.mp4").subclip(10,20)
clip3 = VideoFileClip("video1.mp4").subclip(20,30)
clip4 = VideoFileClip("video2.mp4").subclip(10,20).fx(vfx.colorx, 1.5)\
                                                  .fx(vfx.lum_contrast, 0, 50, 128)

combined = concatenate_videoclips([clip1, clip2, clip3, clip4])
combined.write_videofile("combined.mp4")