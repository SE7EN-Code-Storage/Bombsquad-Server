import ba
from settings import configs


def texts(self):
    """Method to add left and write texts on map, Pythonic version cause this has to be more customisable"""

    if self.name not in self.adaptive:
        self.left = ba.NodeActor(
            ba.newnode(
                "text",
                attrs={
                    "v_attach": "bottom",
                    "v_align": "bottom",
                    "h_attach": "left",
                    "h_align": "left",
                    "flatness": 1.0,
                    "opacity": 1.0,
                    "shadow": 0.5,
                    "color": (1, 1, 1),
                    "scale": 0.55,
                    "position": (60, 5),
                    "text": configs.maptext.bottom_left,
                },
            ))

    self.right = ba.NodeActor(
        ba.newnode(
            "text",
            attrs={
                "v_attach": "bottom",
                "v_align": "bottom",
                "h_attach": "right",
                "h_align": "right",
                "flatness": 1.0,
                "opacity": 1.0,
                "shadow": 0.5,
                "color": (1, 1, 1),
                "scale": 0.55,
                "position": (-120, 5),
                "text": configs.maptext.bottom_right,
            },
        ))