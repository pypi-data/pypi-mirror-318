from yta_multimedia.video.generation.manim.classes.base_manim_animation import BaseManimAnimation
from yta_multimedia.video.generation.manim.constants import MANDATORY_CONFIG_PARAMETER
from yta_general_utils.downloader.google_drive import GoogleDriveResource
from yta_general_utils.programming.parameter_validator import NumberValidator
from yta_general_utils.temp import create_temp_filename
from manim import *


__all__ = [
    'SimpleTextManimAnimationX'
]


# TODO: This base class should be next to
# BaseManimAnimation class
class BaseManimAnimationWrapper:
    """
    Base class for all the mani animation generator
    classes that we want to have in our system.

    This wrapper is to define the attributes that 
    are needed and the manim animation generator
    class that will be used to generate it.

    TODO: maybe we can simplify this to a unique
    class that is not only the wrapper but also the
    generator, as the generator classes will be 
    refactored with this new format.
    """
    _animation: BaseManimAnimation = None

    @property
    def attributes(self):
        """
        Only the values that are actually set on the
        instance are obtained with 'vars'. If you set
        'var_name = None' but you don't do 
        'self.var_name = 33' in the '__init__' method,
        it won't be returned by the 'vars()' method.
        """
        # The variables we don't want have to be
        # manually set if we make any change
        # Each attribute is a dict 'key: value'
        return {k: v for k, v in vars(self).items() if k not in ['_animation', 'attributes']}

    def build(self):
        """
        Build the manim animation if the parameters are
        valid and returns the filename of the generated
        video to be used in the app (you should handle it
        with a 'VideoFileClip(o, has_mask = True)' to load
        it with mask and to be able to handle it).
        """
        return self._animation().generate(**self.attributes, output_filename = 'output.mov')
    
class ExampleManimAnimationWrapper(BaseManimAnimationWrapper):
    def __init__(self, text: str, duration: float):
        # TODO: This parameter validation could be done
        # by our specific parameter validator (under
        # construction yet)
        exception_messages = []

        if not text:
            exception_messages.append('No "text" parameter provided.')
        
        if not NumberValidator.is_positive_number(duration):
            exception_messages.append('The "duration" parameter provided is not a positive number.')

        if len(exception_messages) > 0:
            raise Exception('\n'.join([exception_message for exception_message in exception_messages]))
        
        self.text = text
        self.duration = duration
        self._animation = ExampleManimAnimationGenerator

class ExampleManimAnimationGenerator(BaseManimAnimation):
    def construct(self):
        """
        This method is called by manim when executed by shell and
        will call the scene animation render method to be processed
        and generated.
        """
        self.animate()

    def generate(self, parameters, output_filename: Union[str, None] = None):
        """
        Build the manim animation video and stores it
        locally as the provided 'output_filename', 
        returning the final output filename.

        This method will call the '.animate()' method
        to build the scene with the instructions that
        are written in that method.
        """
        # TODO: We know the attributes, so we validate
        # them specifically for this purpose, or maybe
        # we could validate them in the '__init__' (?)

        # TODO: Validate 'output_filename' better
        if output_filename is None:
            output_filename = 'output.mov'

        # Generate the animation when parameters are valid
        super().generate(parameters, output_filename = output_filename)

        return output_filename
    
    def animate(self):
        text = Text(self.parameters['text'], font_size = 26, font = 'Minecraftia').shift(DOWN * 0).scale(1)
        self.add(text)
        # The sound duration will be set as video duration if
        # larger than the 'duration' parameter so I need to
        # look for a way to enshort the video
        #self.add_sound(GoogleDriveResource('https://drive.google.com/file/d/1Dzeb6Qae4UdpmuA6U9d6t3MXnvhzukzg/view?usp=sharing').download(create_temp_filename('tmp.mp3')))
        self.wait(self.parameters['duration'])














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
        # The variables we don't want have to be
        # manually set if we make any change
        # Each attribute is a dict 'key: value'
        return {k: v for k, v in vars(self).items() if k not in ['_animation', 'attributes']}
    
    def generate(self):
        """
        Generate the manim animation if the parameters are
        valid and returns the filename of the generated
        video to be used in the app (you should handle it
        with a 'VideoFileClip(o, has_mask = True)' to load
        it with mask and to be able to handle it).
        """
        return self._animation().generate(**self.attributes)

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