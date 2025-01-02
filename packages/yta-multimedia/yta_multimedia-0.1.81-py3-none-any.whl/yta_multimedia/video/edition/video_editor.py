from yta_multimedia.video.parser import VideoParser
from moviepy.Clip import Clip
from moviepy import CompositeVideoClip


class VideoEditor:
    _video: Clip = None

    @property
    def video(self):
        return self._video

    def __init__(self, video: Clip):
        self._video = VideoParser.to_moviepy(video, do_include_mask = True, do_calculate_real_duration = True)

    def overlay_text(self, text_generator_wrapping_instance: any):
        # TODO: The instance must be an instance of an
        # specific class (we didn't create yet) to identify
        # it as a manim text animation video generator
        # wrapping class. Maybe identify it as a text that
        # is goin to be overlayed, that can be different
        # from a text that will be the whole scene (imagine
        # a title over a white background vs a text that
        # suddenly appears over what is being shown)
        # 
        # This class contains the needed parameters (with
        # their values actually set) and the animation
        # generator class that must be called with those
        # parameters to generate the animation video.
        
        # If we have the instance here, it is valid
        return CompositeVideoClip([
            self.video,
            VideoParser.to_moviepy(text_generator_wrapping_instance.generate(), do_include_mask = True)
        ])