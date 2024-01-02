from flet import *
from flet_contrib.color_picker import ColorPicker


def main(page: Page):
    def text_slider(txt: str, min: float, max: float):
        return Container(
            Row(
                [
                    Text(txt, size=20),
                    Slider(
                        min=min,
                        max=max,
                        divisions=10,
                        label="{value}",
                        active_color="#164863",
                        inactive_color="#164863",
                    ),
                ]
            ),
            margin=margin.only(left=30),
        )

    # ColorPicker
    # _________________________________________________________________________________________________________________________________
    def open_color_picker(e):
        d.open = True
        page.update()

    color_picker = ColorPicker(color="#ffffff", width=300)

    color_container = Container(
        width=20,
        height=20,
        bgcolor="white",
        border=border.all(1, "black"),
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
                    Container(
                        border_radius=50,
                        width=250,
                        height=250,
                        bgcolor="blue",
                        margin=margin.only(left=50, right=50),
                    ),
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
            Container(
                Column(
                    [
                        Container(
                            Row(
                                [
                                    Text("Pick a color", size=20),
                                    color_container,
                                ]
                            ),
                            margin=margin.only(top=20, left=30, right=10),
                        ),
                        text_slider("Size: ", 0, 370),
                        text_slider("Radius: ", 0, 370),
                        text_slider("Distance: ", 0, 370),
                        text_slider("Intensity: ", 0, 370),
                        text_slider("Blur: ", 0, 370),
                    ]
                ),
                border_radius=45,
                width=500,
                height=450,
                bgcolor="red",
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
                margin=margin.only(bottom=28),
            ),
        ],
        alignment=MainAxisAlignment.CENTER,
    )

    page.theme_mode = "light"
    page.add(title, main_content)


if __name__ == "__main__":
    app(target=main)
