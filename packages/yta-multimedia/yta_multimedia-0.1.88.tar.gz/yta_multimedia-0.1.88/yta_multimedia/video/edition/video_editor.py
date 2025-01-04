"""
When we need to use videos generated with manim
we have many different types of videos, and we
need to ensure that the provided wrapper class
is one of the types the method we are using is
expecting.

If we are trying to overlaying a text which is
generated with a text manim wrapper class, we
need to raise an exception if the provided class
is not a text manim wrapper class, because the
process will fail as the video generated will be
different as the expected.

All the classes we have that belong to manim video
creation have the same structure, having a wrapper
class that internally uses a generator class to
actually build the video animation, so we need
those wrapper class names. But also, the wrapper
class name is the same as the file name but in
camel case and ending in 'Wrapper'.
"""
from yta_multimedia.video.parser import VideoParser
from yta_multimedia.video.generation.manim.classes.base_manim_animation_wrapper import BaseManimAnimationWrapper
from yta_multimedia.video.edition.resize import resize_video
from yta_multimedia.video.edition.duration import set_video_duration, ExtendVideoMode
from yta_multimedia.video.combine import VideoCombinatorAudioMode, VideoAudioCombinator
from yta_general_utils.programming.parameter_validator import PythonValidator
from yta_general_utils.file.handler import FileSearchOption, FileHandler
from yta_general_utils.programming.var import snake_case_to_upper_camel_case
from yta_general_utils.programming.path import get_project_abspath
from moviepy.Clip import Clip
from moviepy import CompositeVideoClip


# TODO: Check yta_multimedia\video\combine.py because
# its functionality could end being part of this 
# VideoEditor


# TODO: Please, rename this class as this name is
# not a proper name
class VideoClassifier:
    @staticmethod
    def get_manim_wrapper_class_names_from_files(abspath: str, files_to_ignore: list[str] = []):
        """
        Obtain a list with the manim wrapper class names of
        all the available files that are in the provided
        'abspath', excluding the ones in the also given
        'files_to_ignore'. The file name is turned into the
        wrapper class name and returned.
        """
        files_to_ignore = [files_to_ignore] if PythonValidator.is_string(files_to_ignore) else files_to_ignore

        if not PythonValidator.is_list_of_string(files_to_ignore):
            raise Exception('The "files_to_ignore" parameter provided is not a valid list of strings.')

        # Transform the file name in the wrapper class that is inside
        transform_function = lambda file: snake_case_to_upper_camel_case(file.split("/")[-1].replace(".py", ""))

        return [
            f'{transform_function(file)}Wrapper'
            for file in FileHandler.get_list(abspath, FileSearchOption.FILES_ONLY, '*.py')
            if not any(file.endswith(file_to_ignore) for file_to_ignore in files_to_ignore)
        ]

    @staticmethod
    def text_manim_premades():
        """
        Get a list containing the manim text animation wrapper
        class names that can be used when text manim videos
        are needed.
        """
        #from yta_multimedia.video.generation.manim.classes.text import magazine_text_is_written_manim_animation

        return [
            'MagazineTextIsWrittenManimAnimationWrapper',
            'MagazineTextStaticManimAnimationWrapper',
            'RainOfWordsManimAnimationWrapper',
            'SimpleTextManimAnimationWrapper',
            'TestTextManimAnimationWrapper',
            'TextTripletsManimAnimationWrapper',
            'TextWordByWordManimAnimationWrapper'
        ]

        # TODO: Maybe try another way of getting all the classes
        # within a module, not a file, and identify like I tried
        # with this 'get_manim_wrapper_class_names_from_files'
        # method that is not working because files change when
        # imported as library
        return VideoClassifier.get_manim_wrapper_class_names_from_files(
            f'{get_project_abspath()}/video/generation/manim/classes/text/',
            ['__init__.py']
        )


class VideoEditor:
    _video: Clip = None

    @property
    def video(self):
        return self._video

    def __init__(self, video: Clip):
        self._video = VideoParser.to_moviepy(video, do_include_mask = True, do_calculate_real_duration = True)

    def overlay_text(self, text_generator_wrapping_instance: BaseManimAnimationWrapper):
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
        if not PythonValidator.is_subclass(text_generator_wrapping_instance, BaseManimAnimationWrapper) or not PythonValidator.is_an_instance(text_generator_wrapping_instance):
            raise Exception('The "text_generator_wrapping_instance" is not a valid instance of a subclass of BaseManimAnimationWrapper class.')
        
        # We validate that the provided wrapper class is 
        # about text
        if not PythonValidator.is_instance(text_generator_wrapping_instance, VideoClassifier.text_manim_premades()):
            raise Exception('The provided "text_generator_wrapping_instance" is not an instance of a manim text generation class.')
        
        video = VideoParser.to_moviepy(text_generator_wrapping_instance.generate(), do_include_mask = True)
        video = _prepare_video(self.video, video, 1)
        video = _overlay_video(self.video, video, position = ('center', 'center'), audio_mode = VideoCombinatorAudioMode.ONLY_MAIN_CLIP_AUDIO)

        return video

        # TODO: Remove this below when the above is working
        return CompositeVideoClip([
            self.video,
            VideoParser.to_moviepy(text_generator_wrapping_instance.generate(), do_include_mask = True)
        ])
    
    def overlay_video_without_alpha_fullscreen(self, video: Clip, audio_mode: VideoCombinatorAudioMode = VideoCombinatorAudioMode.BOTH_CLIPS_AUDIO):
        """
        Useful to show a stock video while the main clip is
        still speaking, or to focus on the stock video.
        """
        video = VideoParser.to_moviepy(video)
        audio_mode = VideoCombinatorAudioMode.to_enum(audio_mode)

        video = _prepare_video(self.video, video, 1)
        video = _overlay_video(self.video, video, position = ('center', 'center'), audio_mode = audio_mode)

        return video

    def overlay_video_without_alpha_non_fullscreen(self, video: Clip, audio_mode: VideoCombinatorAudioMode = VideoCombinatorAudioMode.BOTH_CLIPS_AUDIO):
        """
        Useful to add a video like a reel or stock while the
        main clip is still visible.
        """
        video = VideoParser.to_moviepy(video)
        audio_mode = VideoCombinatorAudioMode.to_enum(audio_mode)

        video = _prepare_video(self.video, video, 8)
        video = _overlay_video(self.video, video, position = ('center', 'center'), audio_mode = audio_mode)

        return video
    
    def overlay_video_with_alpha_fullscreen(self, video: Clip, audio_mode: VideoCombinatorAudioMode = VideoCombinatorAudioMode.BOTH_CLIPS_AUDIO):
        """
        Useful to add an alphascreen, a transition or
        another kind of videos.
        """
        video = VideoParser.to_moviepy(video, do_include_mask = True)
        audio_mode = VideoCombinatorAudioMode.to_enum(audio_mode)

        video = _prepare_video(self.video, video, 1)
        video = _overlay_video(self.video, video, position = ('center', 'center'), audio_mode = audio_mode)

        return video
    
    def overlay_video_with_alpha_non_fullscreen(self, video: Clip, audio_mode: VideoCombinatorAudioMode = VideoCombinatorAudioMode.BOTH_CLIPS_AUDIO):
        """
        Useful for something that I don't know right now.

        TODO: Please, improve this doc... omg
        """
        video = VideoParser.to_moviepy(video, do_include_mask = True)
        audio_mode = VideoCombinatorAudioMode.to_enum(audio_mode)

        video = _prepare_video(self.video, video, 8)
        video = _overlay_video(self.video, video, position = ('center', 'center'), audio_mode = audio_mode)

        return video
    

def _prepare_video(main_video: Clip, video: Clip, size_factor: float = 1.0):
    """
    Resize the 'video' according to the 'main_video' dimensions
    and enshort the 'video' if larger than the 'main_video'.
    """
    # We resize the 'video' to fit expected size
    video = resize_video(video, main_video.size / size_factor)
    # We ensure the video is not larger than the main one
    video = set_video_duration(video, main_video.duration, extend_mode = ExtendVideoMode.DONT_ENLARGE)

    return video

def _overlay_video(main_video: Clip, video: Clip, position: tuple = ('center', 'center'), audio_mode: VideoCombinatorAudioMode = VideoCombinatorAudioMode.BOTH_CLIPS_AUDIO):
    return CompositeVideoClip([
        main_video,
        # TODO: Centered? I think this must be customizable
        video.with_position(position)
    ]).with_audio(VideoAudioCombinator(audio_mode).process_audio(main_video, video))



# 1. Videos must be 60fps both of them to simplify
# 2. The main video (background_video) must be 1920x1080 always,
#    and the other ones must be 1920x1080 or smaller
# 3. Duration of the video cannot be larger than the main video

# We should add a VideoModifications matrix in which we have
# layers that indicate the moment in which the modification has
# to be applied. Layer 1 will be prior, so once all layer 1
# modifications has been completed, layer 2 are applied. This
# is how editors work and also the better way to handle 
# priority. It is not the same applying a greenscreen and then
# an effect than applying the effect first to the clip and then
# the greenscreen that wraps the whole video.