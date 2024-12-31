from yta_multimedia.video.parser import VideoParser
from yta_multimedia.video.position import Position, DependantPosition, get_moviepy_upper_left_position
from yta_multimedia.video.edition.duration import set_video_duration
from yta_multimedia.audio.silences import AudioSilence
from yta_multimedia.video.dimensions import resize_video
from yta_general_utils.programming.parameter_validator import PythonValidator
from yta_general_utils.programming.enum import YTAEnum as Enum
from moviepy.Clip import Clip
from moviepy import CompositeVideoClip, CompositeAudioClip
from typing import Union


class VideoCombinatorAudioMode(Enum):
    """
    The mode in which the combined video audios
    will be handled.
    """
    BOTH_CLIPS_AUDIO = 'both_clips_audio'
    """
    Both, the main clip and the added clip audios 
    are preserved.
    """
    ONLY_MAIN_CLIP_AUDIO = 'only_main_clip_audio'
    """
    Only the main clip audio is preserved. The one
    from the added clip is not included.
    """
    ONLY_ADDED_CLIP_AUDIO = 'only_added_clip_audio'
    """
    Only the added clip audio is preserved. The one
    from the main clip is not included.
    """

class VideoCombinator:
    """
    A class to encapsulate and simplify the way we
    combine videos.
    """
    _audio_mode: VideoCombinatorAudioMode = None

    def __init__(self, audio_mode: VideoCombinatorAudioMode = VideoCombinatorAudioMode.BOTH_CLIPS_AUDIO):
        self._audio_mode = VideoCombinatorAudioMode.to_enum(audio_mode) if audio_mode is not None else VideoCombinatorAudioMode.default()

    def video_cover_video(self, video: Clip, background_video: Clip):
        """
        Place the provided 'video' covering the 'background_video'.

        The 'video' will be forced to last the same as the 
        'background_video' to be able to cover it.

        TODO: Explain more
        """
        background_video = VideoParser.to_moviepy(background_video)
        video = VideoParser.to_moviepy(video)

        # We adjust the 'video' size to cover the 
        # 'background_video'
        video = resize_video(video, background_video.size)

        return self.video_over_video(video, background_video, Position.CENTER)

    def video_over_video(self, video: Clip, background_video: Clip, position: Union[Position, DependantPosition, tuple, list]):
        """
        Place the provided 'video' over the 'background_video'
        in the given 'position' (adapted to the real background
        video size). The 'background_video' will be played 
        entirely, and the 'video' clip will be enlarged 
        according to our default enlarging videos strategy. So,
        you should call this method with the parts of the videos
        you want actually combine entirely and pre-processed.

        Pay attention to the size of the videos you provide as
        this method is not considering this part.

        This method returns a CompositeVideoClip with both 
        videos combined.
        """
        if not PythonValidator.is_instance(position, [Position, DependantPosition]) and not PythonValidator.is_tuple(position) and not PythonValidator.is_list(position):
            raise Exception('The provided "position" is not valid, it must be a Position, DependantPosition or a tuple or list with 2 values.')
        
        background_video = VideoParser.to_moviepy(background_video)
        video = VideoParser.to_moviepy(video)

        # TODO: What about sizes (?)

        # TODO: This length strategy is open to changes
        video = set_video_duration(video, background_video.duration)

        # We will place the 'video's center in the 'position'
        # but of the provided 'background_video'
        if PythonValidator.is_instance(position, Position):
            position = position.get_moviepy_upper_left_corner_tuple(video.size, background_video.size)
        elif PythonValidator.is_instance(position, DependantPosition):
            position = position.get_moviepy_position_upper_left_corner(video.size, background_video.size)
        else:
            position = get_moviepy_upper_left_position(background_video.size, video.size, position)

        video = video.with_position(position)

        return CompositeVideoClip([
            background_video,
            video
        ]).with_audio(self._process_audio(background_video, video))

    def _process_audio(self, main_video: Clip, added_video: Clip):
        """
        Process the 'video' and 'background_video' audios
        according to the instance audio mode defined when
        instantiated.

        This method must be called just before combining
        the videos and after video enlargment has been
        applied (if needed).
        """
        # TODO: What about silence 'frame_rate' (?)
        added_video_audio = added_video.audio if added_video.audio is not None else AudioSilence.create(added_video.duration)
        main_video_audio = main_video.audio if main_video.audio is not None else AudioSilence.create(main_video.duration)

        if self._audio_mode == VideoCombinatorAudioMode.BOTH_CLIPS_AUDIO:
            audio = CompositeAudioClip([
                added_video_audio, 
                main_video_audio
            ])
        elif self._audio_mode == VideoCombinatorAudioMode.ONLY_MAIN_CLIP_AUDIO:
            audio = main_video_audio
        elif self._audio_mode == VideoCombinatorAudioMode.ONLY_ADDED_CLIP_AUDIO:
            audio = added_video_audio

        return audio