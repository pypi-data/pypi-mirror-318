from yta_multimedia.video.generation.manim.classes.base_manim_animation import BaseManimAnimation
from yta_multimedia.video.generation.manim.classes.base_three_d_manim_animation import BaseThreeDManimAnimation
from yta_general_utils.programming.parameter_validator import PythonValidator
from yta_general_utils.programming.attribute_obtainer import AttributeObtainer
from typing import Union


class BaseManimAnimationWrapper:
    """
    Base class for all the manim animation generator
    classes that we want to have in our system.

    This wrapper is to define the attributes that 
    are needed and the manim animation generator
    class that will be used to generate it.
    """
    animation_generator_instance: Union[BaseManimAnimation, BaseThreeDManimAnimation] = None

    def __init__(self, animation_generator_instance_or_class: Union[BaseManimAnimation, BaseThreeDManimAnimation]):
        if not PythonValidator.is_subclass(animation_generator_instance_or_class, BaseManimAnimation) and not PythonValidator.is_subclass(animation_generator_instance_or_class, BaseThreeDManimAnimation):
            raise Exception('The provided "animation_generator_instance_or_class" is not a subclass nor an instance of a subclass of BaseManimAnimation or BaseThreeDManimAnimation classes.')
        
        if PythonValidator.is_a_class(animation_generator_instance_or_class):
            animation_generator_instance_or_class = animation_generator_instance_or_class()

        self.animation_generator_instance = animation_generator_instance_or_class

    @property
    def attributes(self):
        """
        Only the values that are actually set on the
        instance are obtained with 'vars'. If you set
        'var_name = None' but you don't do 
        'self.var_name = 33' in the '__init__' method,
        it won't be returned by the 'vars()' method.
        """
        return AttributeObtainer.get_attributes_from_instance(self, ['animation_generator_instance', 'attributes'])

    def generate(self):
        """
        Generate the manim animation if the parameters are
        valid and returns the filename of the generated
        video to be used in the app (you should handle it
        with a 'VideoFileClip(o, has_mask = True)' to load
        it with mask and to be able to handle it).
        """
        return self.animation_generator_instance.generate(self.attributes, output_filename = 'output.mov')