from dataclasses import dataclass

@dataclass
class PosterArrangement:
    """This is a model-class that use to storage configuration of a poster.
    """

    posterTitle: str = "手抄报标题"
    part1Text: str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam ut dapibus est. Vivamus accumsan volutpat vehicula."
    part2Text: str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam ut dapibus est. Vivamus accumsan volutpat vehicula."
    part3Text: str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam ut dapibus est. Vivamus accumsan volutpat vehicula."
    part4Text: str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam ut dapibus est. Vivamus accumsan volutpat vehicula."

    posterTitleFont: str = "黑体"
    posterTitleSize: int = 100
    posterTextFont: str = "黑体"
    posterTextSize: int = 20

    template: int = 1
