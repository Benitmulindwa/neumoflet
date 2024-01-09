from flet import *


# Text - Slider
def text_slider_ui(
    event, txt: str, min: float, max: float, width: int, data, default_val: int = 0
) -> Container:
    return Container(
        Row(
            [
                Container(
                    Text(txt, size=15, weight=FontWeight.W_600, font_family="muli")
                ),
                Slider(
                    min=min,
                    max=max,
                    divisions=10,
                    value=default_val,
                    label="{value}",
                    width=width,
                    active_color="#164863",
                    inactive_color="#164863",
                    on_change=event,
                    data=data,
                ),
            ]
        ),
    )
