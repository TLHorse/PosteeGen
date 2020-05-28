from dataclasses import dataclass

@dataclass
class PosterArrangement:
    """This is a model-class that use to storage configuration of a poster.
    """

    posterTitle: str = "手抄报标题"
    part1text: str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam ut dapibus est. Vivamus accumsan volutpat vehicula."
    part2text: str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam ut dapibus est. Vivamus accumsan volutpat vehicula."
    part3text: str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam ut dapibus est. Vivamus accumsan volutpat vehicula."
    part4text: str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam ut dapibus est. Vivamus accumsan volutpat vehicula."

    posterTitleFont: str = "黑体"
    posterTextFont: str = "黑体"
    posterTitleSize: int = 16
    posterTextSize: int = 16

    template: int = 1
