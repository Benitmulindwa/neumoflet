from flet import *

title = Row(
    [
        Column(
            [
                Text("NEUMORPHIC", size=50, weight=FontWeight.BOLD),
                Text("Generate Soft-UI Flet code"),
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
        )
    ],
    alignment=MainAxisAlignment.CENTER,
)

main_content = Row(
    [
        Row(
            [
                Column(
                    [
                        Container(width=20, height=20, bgcolor="yellow"),
                        Container(width=20, height=20, bgcolor="yellow"),
                    ],
                    spacing=370,
                ),
                Container(width=250, height=250, bgcolor="blue"),
                Column(
                    [
                        Container(width=20, height=20, bgcolor="yellow"),
                        Container(width=20, height=20, bgcolor="yellow"),
                    ],
                    spacing=370,
                ),
            ]
        ),
        Container(Column([]), width=500, height=500, bgcolor="red"),
    ],
    alignment=MainAxisAlignment.CENTER,
    spacing=10,
)


def main(page: Page):
    page.theme_mode = "light"
    page.add(title, main_content)


if __name__ == "__main__":
    app(target=main)
