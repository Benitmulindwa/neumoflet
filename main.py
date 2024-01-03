from flet import *
from flet_contrib.color_picker import ColorPicker


def main(page: Page):
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

    _element = Container(
        border_radius=50,
        width=250,
        height=250,
        bgcolor="blue",
        margin=margin.only(left=50, right=50),
        shadow=BoxShadow(
            blur_radius=60,
            color=colors.BLUE_GREY_300,
            offset=Offset(-2, -2),
            blur_style=ShadowBlurStyle.OUTER,
        ),
    )

    def get_slider_value(e):
        if e.control.data == "radius":
            _element.border_radius = e.control.value
            _element.update()
        elif e.control.data == "size":
            _element.width = e.control.value
            _element.height = e.control.value
            _element.update()

    # ColorPicker
    # _________________________________________________________________________________________________________________________________
    def open_color_picker(e):
        d.open = True
        page.update()

    color_picker = ColorPicker(color="#ffffff", width=300)

    color_container = Container(
        width=32,
        height=32,
        bgcolor="white",
        border=border.all(2, "black"),
        on_click=open_color_picker,
    )

    def change_color(e):
        color_container.bgcolor = color_picker.color
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

    def _exposure(e):
        e.control.bgcolor = "yellow"
        print(e.control.data)
        e.control.update()

    main_content = Row(
        [
            Container(
                Row(
                    [
                        Column(
                            [
                                Container(
                                    border=border.all(2, "black"),
                                    border_radius=border_radius.only(bottom_right=30),
                                    width=30,
                                    height=30,
                                    bgcolor="transparent",
                                    on_click=_exposure,
                                    data="top_left",
                                ),
                                Container(
                                    border=border.all(2, "black"),
                                    border_radius=border_radius.only(top_right=30),
                                    width=30,
                                    height=30,
                                    bgcolor="transparent",
                                    on_click=_exposure,
                                    data="bottom_left",
                                ),
                            ],
                            spacing=370,
                        ),
                        _element,
                        Column(
                            [
                                Container(
                                    border=border.all(2, "black"),
                                    border_radius=border_radius.only(bottom_left=30),
                                    width=30,
                                    height=30,
                                    bgcolor="transparent",
                                    on_click=_exposure,
                                    data="top_right",
                                ),
                                Container(
                                    border=border.all(2, "black"),
                                    border_radius=border_radius.only(top_left=30),
                                    width=30,
                                    height=30,
                                    bgcolor="transparent",
                                    on_click=_exposure,
                                    data="bottom_right",
                                ),
                            ],
                            spacing=370,
                        ),
                    ]
                ),
                margin=margin.only(right=30),
            ),
            Container(
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
                                    color_container,
                                ]
                            ),
                            margin=margin.only(right=10),
                        ),
                        text_slider(
                            "Size: ", 10, 350, width=270, data="size", default_val=250
                        ),
                        text_slider(
                            "Radius: ", 0, 132, width=250, data="radius", default_val=50
                        ),
                        text_slider("Distance: ", 0, 370, width=240, data="distance"),
                        text_slider("Intensity: ", 0, 370, width=240, data="intensity"),
                        text_slider("Blur: ", 0, 370, width=270, data="blur"),
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
                bgcolor="red",
                padding=padding.only(30, 20, 30, 20),
                shadow=BoxShadow(
                    blur_radius=15,
                    color=colors.BLUE_GREY_300,
                    offset=Offset(0, 0),
                    blur_style=ShadowBlurStyle.OUTER,
                ),
            ),
        ],
        alignment=MainAxisAlignment.CENTER,
        spacing=10,
    )
    title = Row(
        [
            Container(
                Column(
                    [
                        Text("NEUMORPHIC", size=50, weight=FontWeight.BOLD),
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

    page.bgcolor = "blue"

    page.theme_mode = "light"
    page.add(title, main_content)


if __name__ == "__main__":
    app(target=main)
