from yta_multimedia.video.generation.manim.classes.base_manim_animation import BaseManimAnimation
from yta_multimedia.video.generation.manim.constants import MANDATORY_CONFIG_PARAMETER
from yta_general_utils.downloader.google_drive import GoogleDriveResource
from yta_general_utils.programming.parameter_validator import NumberValidator
from yta_general_utils.temp import create_temp_filename
from manim import *


__all__ = [
    'SimpleTextManimAnimationX'
]

class SimpleTextManimAnimationX:
    text: str = None
    duration: float = None
    _animation: callable = None

    def __init__(self, text: str, duration: float):
        exception_messages = []

        if not text:
            exception_messages.append('No "text" parameter provided.')
        
        if not NumberValidator.is_positive_number(duration):
            exception_messages.append('The "duration" parameter provided is not a positive number.')

        if len(exception_messages) > 0:
            raise Exception('\n'.join([exception_message for exception_message in exception_messages]))
        
        from yta_general_utils.programming.parameter_obtainer
        
        self.text = text
        self.duration = duration
        self._animation = SimpleTextManimAnimation

    @property
    def attributes(self):
        """
        Only the values that are actually set on the
        instance are obtained with 'vars'. If you set
        'var_name = None' but you don't do 
        'self.var_name = 33' in the '__init__' method,
        it won't be returned by the 'vars()' method.
        """
        # This has to be manually set if we make any
        # change to obtain only the expected ones
        UNWANTED_VARS = ['_animation', 'attributes']

        # Each attribute is a dict 'key: value'
        return [attribute for attribute in vars(self) if attribute not in UNWANTED_VARS]
    
    def generate(self):
        """
        Generate the manim animation if the parameters are
        valid and returns the filename of the generated
        video to be used in the app (you should handle it
        with a 'VideoFileClip(o, has_mask = True)' to load
        it with mask and to be able to handle it).
        """
        self._animation().generate(**self.attributes)

class SimpleTextManimAnimation(BaseManimAnimation):
    # TODO: Maybe make this more strict with 'type' also
    required_parameters = {
        'text': MANDATORY_CONFIG_PARAMETER,
        'duration': MANDATORY_CONFIG_PARAMETER,
    }

    def construct(self):
        """
        This method is called by manim when executed by shell and
        will call the scene animation render method to be processed
        and generated.
        """
        self.animate()

    def generate(self, text: str, duration: float, output_filename: str = 'output.mov'):
        """
        Checks and validates the provided parameters and generates
        the manim animation if those parameters are valid.
        """
        # Check and validate all parameters
        parameters = {}

        if super().parameter_is_mandatory('text', self.required_parameters) and not text:
            raise Exception('Field "text" is mandatory. Aborting manim creation...')
        
        parameters['text'] = text

        if super().parameter_is_mandatory('duration', self.required_parameters) and not duration:
            raise Exception('Field "duration" is mandatory. Aborting manim creation...')
        if duration < 0 or duration > 100:
            raise Exception('Field "duration" value is not valid. Must be between 0 and 100')
        
        parameters['duration'] = duration

        if not output_filename:
            output_filename = 'output.mov'

        # Generate the animation when parameters are valid
        super().generate(parameters, output_filename = output_filename)

        return output_filename
    
    def animate_one(self):
        """
        This code will generate the manim animation and belongs to the
        Scene manim object.
        """
        text = Text(self.parameters['text'], font_size = 140, stroke_width = 2.0, font = 'Haettenschweiler').shift(DOWN * 0).scale(0.001)
        self.wait(1 / 60)
        self.add(text)
        self.add_sound(GoogleDriveResource('https://drive.google.com/file/d/1WPS8uWB1LTuzPzxQ2Zcp1FpwvLM3fhM5/view?usp=sharing').download(create_temp_filename('tmp.mp3')))
        self.play(text.animate.scale(1000), run_time = 49 / 60)
        self.play(Rotate(text, 0.03), run_time = 3 / 60)
        self.play(Rotate(text, -0.04), run_time = 3 / 60)
        self.play(Rotate(text, -0.02), run_time = 3 / 60)
        self.play(Rotate(text, 0.04), run_time = 3 / 60)
        self.play(Rotate(text, -0.01), run_time = 3 / 60)
        self.play(Rotate(text, 0.03), run_time = 3 / 60)
        self.play(Rotate(text, -0.04), run_time = 3 / 60)
        self.play(Rotate(text, -0.02), run_time = 3 / 60)
        self.play(Rotate(text, 0.04), run_time = 3 / 60)
        self.play(Rotate(text, -0.01), run_time = 3 / 60)
        #self.add_sound(TOUSE_ABSOLUTE_PATH + 'sounds/xp_error.mp3')
        #self.play(AddTextLetterByLetter(text), run_time = self.parameters['duration'])
        
        #simple_play_animation(self, Write, text, self.parameters['duration'])

    def animate_two(self):
        """
        This code will generate the manim animation and belongs to the
        Scene manim object.
        """
        text = Text(self.parameters['text'], font_size = 140, stroke_width = 2.0, font = 'Haettenschweiler').shift(DOWN * 0).scale(7 / 10)
        self.wait(1 / 60)
        self.add(text)
        self.play(text.animate.scale(10 / 7), run_time = 6 / 60)
        self.play(ApplyWave(text), run_time = 30 / 60)

    def animate(self):
        text = Text(self.parameters['text'], font_size = 26, font = 'Minecraftia').shift(DOWN * 0).scale(1)
        self.add(text)
        # The sound duration will be set as video duration if
        # larger than the 'duration' parameter so I need to
        # look for a way to enshort the video
        #self.add_sound(GoogleDriveResource('https://drive.google.com/file/d/1Dzeb6Qae4UdpmuA6U9d6t3MXnvhzukzg/view?usp=sharing').download(create_temp_filename('tmp.mp3')))
        self.wait(self.parameters['duration'])