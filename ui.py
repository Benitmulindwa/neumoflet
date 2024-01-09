from flet import *


# Source of light
def light_source_ui(event, data, **radius):
    return Container(
        border=border.all(2, "black"),
        border_radius=border_radius.only(**radius),
        width=30,
        height=30,
        bgcolor="yellow" if data == "top_left" else "transparent",
        on_click=event,
        data=data,
    )


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
