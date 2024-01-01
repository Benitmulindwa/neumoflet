from flet import *


def main(page: Page):
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
                Column([]),
                border_radius=45,
                width=500,
                height=425,
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
