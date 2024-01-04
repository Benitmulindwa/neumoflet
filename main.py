from flet import *
from flet_contrib.color_picker import ColorPicker


def is_color_dark(hex_color):
    # Convert hex color to RGB components
    r = int(hex_color[1:3], 16) / 255.0
    g = int(hex_color[3:5], 16) / 255.0
    b = int(hex_color[5:], 16) / 255.0

    # Calculate relative luminance
    luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b

    # Check if color is dark (adjust the threshold as needed)
    return luminance < 0.5


def main(page: Page):
    color_picker = ColorPicker(color="#ffffff", width=300)

    # Source of light
    def light_source(data, **radius):
        return Container(
            border=border.all(2, "black"),
            border_radius=border_radius.only(**radius),
            width=30,
            height=30,
            bgcolor="transparent",
            on_click=_exposure,
            data=data,
        )

    # when the light source is clicked
    def _exposure(e):
        e.control.bgcolor = "yellow"
        # print(e.control.data)
        e.control.update()

    TOP_LEFT = light_source("top_left", bottom_right=30)
    BOTTOM_RIGHT = light_source("bottom_left", top_right=30)
    TOP_RIGHT = light_source("top_right", bottom_left=30)
    BOTTOM_LEFT = light_source("bottom_left", top_left=30)

    # L=0.2126*R+0.7152*G+0.0722*B
    def get_slider_value(e):
        if e.control.data == "radius":
            _element.border_radius = e.control.value
            _element.update()
        elif e.control.data == "size":
            _element.width = e.control.value
            _element.height = e.control.value
            _element.update()

    def open_color_picker(e):
        d.open = True
        page.update()

    def text_slider(
        txt: str, min: float, max: float, width: int, data, default_val: int = 0
    ) -> Container:
        return Container(
            Row(
                [
                    Container(Text(txt, size=15, weight=FontWeight.W_600)),
                    Slider(
                        min=min,
                        max=max,
                        divisions=10,
                        value=default_val,
                        label="{value}",
                        width=width,
                        active_color="#164863",
                        inactive_color="#164863",
                        on_change=get_slider_value,
                        data=data,
                    ),
                ]
            ),
        )

    SIZE = text_slider("Size: ", 10, 350, width=270, data="size", default_val=250)
    RADIUS = text_slider("Radius: ", 0, 175, width=250, data="radius", default_val=50)
    DISTANCE = text_slider("Distance: ", 0, 370, width=240, data="distance")
    INTENSITY = text_slider("Intensity: ", 0, 370, width=240, data="intensity")
    BLUR = text_slider("Blur: ", 0, 370, width=270, data="blur")

    _element = Container(
        border_radius=50,
        width=250,
        height=250,
        bgcolor=color_picker.color,
        margin=margin.only(left=50, right=50),
        shadow=BoxShadow(
            blur_radius=60,
            color=colors.BLUE_GREY_300,
            offset=Offset(-2, -2),
            blur_style=ShadowBlurStyle.OUTER,
        ),
    )
    color_picker_container = Container(
        width=32,
        height=32,
        bgcolor="white",
        border=border.all(2, "black"),
        on_click=open_color_picker,
    )

    setting_container = Container(
        Column(
            [
                Container(
                    Row(
                        [
                            Text(
                                "Pick a color: ",
                                size=15,
                                weight=FontWeight.W_600,
                            ),
                            color_picker_container,
                        ]
                    ),
                    margin=margin.only(right=10),
                ),
                SIZE,
                RADIUS,
                DISTANCE,
                INTENSITY,
                BLUR,
                Text("Code: ", size=15, weight=FontWeight.W_600),
                Container(
                    bgcolor="yellow",
                    width=380,
                    height=100,
                ),
            ],
            spacing=0,
        ),
        border_radius=35,
        width=350,
        height=450,
        bgcolor=color_picker.color,
        padding=padding.only(30, 20, 30, 20),
        shadow=BoxShadow(
            blur_radius=15,
            color=colors.BLUE_GREY_300,
            offset=Offset(0, 0),
            blur_style=ShadowBlurStyle.OUTER,
        ),
    )

    # Change Color
    # _________________________________________________________________________________________________________________________________

    def change_color(e):
        # Check if the picked color is dark
        if is_color_dark(color_picker.color):
            TEXT_SLIDERS_COLOR = "white"

        else:
            TEXT_SLIDERS_COLOR = "#001f3f"

        # Text - Slider color
        for txt_slider in [SIZE, RADIUS, DISTANCE, INTENSITY, BLUR]:
            txt_slider.content.controls[0].content.color = TEXT_SLIDERS_COLOR
            txt_slider.content.controls[1].inactive_color = TEXT_SLIDERS_COLOR
            txt_slider.content.controls[1].active_color = TEXT_SLIDERS_COLOR

        for bubble in [TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT]:
            bubble.border.top.color = TEXT_SLIDERS_COLOR

        title.controls[0].content.controls[0].color = TEXT_SLIDERS_COLOR
        title.controls[0].content.controls[1].color = TEXT_SLIDERS_COLOR
        color_picker_container.border.top.color = TEXT_SLIDERS_COLOR
        color_picker_container.bgcolor = color_picker.color
        page.bgcolor = color_picker.color
        _element.bgcolor = color_picker.color
        setting_container.bgcolor = color_picker.color

        setting_container.content.controls[0].content.controls[
            0
        ].color = TEXT_SLIDERS_COLOR  # pick_a_color(text)
        setting_container.content.controls[
            6
        ].color = TEXT_SLIDERS_COLOR  # code_text color
        d.open = False
        page.update()

    def close_dialog(e):
        d.open = False
        d.update()

    d = AlertDialog(
        content=color_picker,
        actions=[
            TextButton("OK", on_click=change_color),
            TextButton("Cancel", on_click=close_dialog),
        ],
        actions_alignment=MainAxisAlignment.START,
        on_dismiss=change_color,
    )
    page.dialog = d

    # _____________________________________________________________________________________________________________________________________
    def star_github(e):
        page.launch_url("https://github.com/Benitmulindwa/neumorphic")
        page.update()

    main_content = Row(
        [
            Container(
                Row(
                    [
                        Column(
                            [
                                TOP_LEFT,
                                BOTTOM_RIGHT,
                            ],
                            spacing=370,
                        ),
                        _element,
                        Column(
                            [
                                TOP_RIGHT,
                                BOTTOM_LEFT,
                            ],
                            spacing=370,
                        ),
                    ]
                ),
                margin=margin.only(right=30),
            ),
            setting_container,
        ],
        alignment=MainAxisAlignment.CENTER,
        spacing=10,
    )
    title = Row(
        [
            Container(
                Column(
                    [
                        Text("Neumoflet.io", size=50, weight=FontWeight.BOLD),
                        Text("Generate Soft-UI Flet code"),
                    ],
                    spacing=0,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                ),
                expand=True,
                margin=margin.only(bottom=25),
            ),
            Container(
                Chip(
                    label=Text("Star on GitHub"),
                    bgcolor="white",
                    leading=Icon(icons.STAR_BORDER),
                    on_click=star_github,
                ),
                margin=margin.only(bottom=40),
            ),
        ],
        alignment=MainAxisAlignment.CENTER,
    )

    page.bgcolor = color_picker.color

    page.theme_mode = "light"
    page.add(title, main_content)


if __name__ == "__main__":
    app(target=main)
