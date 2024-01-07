from flet import *
from flet_contrib.color_picker import ColorPicker
from utils import is_color_dark, calculate_shadow_colors


def main(page: Page):
    color_picker = ColorPicker(color="#c5b5b5", width=300)
    shadow_color, highlight_color = calculate_shadow_colors(color_picker.color)

    # Source of light
    def light_source_ui(data, **radius):
        return Container(
            border=border.all(2, "black"),
            border_radius=border_radius.only(**radius),
            width=30,
            height=30,
            bgcolor="yellow" if data == "top_left" else "transparent",
            on_click=_exposure,
            data=data,
        )

    def handle_light(data, DIST):
        if data == "top_left":
            TOP_LEFT.bgcolor = "yellow"
            TOP_RIGHT.bgcolor = "transparent"
            BOTTOM_LEFT.bgcolor = "transparent"
            BOTTOM_RIGHT.bgcolor = "transparent"
            positionX = DIST * -1
            positionY = DIST * -1
        elif data == "top_right":
            TOP_RIGHT.bgcolor = "yellow"
            BOTTOM_RIGHT.bgcolor = "transparent"
            BOTTOM_LEFT.bgcolor = "transparent"
            TOP_LEFT.bgcolor = "transparent"
            positionX = DIST
            positionY = DIST * -1
        elif data == "bottom_left":
            BOTTOM_LEFT.bgcolor = "yellow"
            BOTTOM_RIGHT.bgcolor = "transparent"
            TOP_RIGHT.bgcolor = "transparent"
            TOP_LEFT.bgcolor = "transparent"
            positionX = DIST
            positionY = DIST
        elif data == "bottom_right":
            BOTTOM_RIGHT.bgcolor = "yellow"
            TOP_RIGHT.bgcolor = "transparent"
            TOP_LEFT.bgcolor = "transparent"
            BOTTOM_LEFT.bgcolor = "transparent"
            positionX = DIST * -1
            positionY = DIST

        page.update()
        return positionX, positionY

    # when the light source is clicked
    def _exposure(e):
        # light position based on positionX and positionY returned by the function handle_light()
        X, Y = handle_light(e.control.data, DISTANCE.content.controls[1].value)
        _element.shadow[1].offset = X, Y
        _element.shadow[0].offset = -X, -Y

        # light position for the setting_container
        setting_container.shadow[0].offset = -X, -Y
        setting_container.shadow[1].offset = X, Y

        # Update the involved controls
        setting_container.update()
        _element.update()
        e.control.update()

    TOP_LEFT = light_source_ui("top_left", bottom_right=30)
    BOTTOM_RIGHT = light_source_ui("bottom_right", top_right=30)
    TOP_RIGHT = light_source_ui("top_right", bottom_left=30)
    BOTTOM_LEFT = light_source_ui("bottom_left", top_left=30)

    def get_slider_value(e):
        if e.control.data == "size":
            size = e.control.value
            _element.width = size
            _element.height = size
            BLUR.content.controls[1].value = size // 5
            _element.shadow[0].blur_radius = size // 5
            _element.shadow[1].blur_radius = size // 5
            DISTANCE.content.controls[1].value = size // 10
            _element.shadow[0].blur_radius = size // 10
            _element.shadow[1].blur_radius = size // 10
            # print(code.value)

        elif e.control.data == "radius":
            _element.border_radius = e.control.value

        elif e.control.data == "distance":
            distance = e.control.value
            _element.shadow[0].blur_radius = distance
            _element.shadow[1].blur_radius = distance
            BLUR.content.controls[1].value = distance * 2  # Blur Ui
            _element.shadow[0].blur_radius = distance
            _element.shadow[1].blur_radius = distance * 2

        elif e.control.data == "blur":
            _element.shadow[0].blur_radius = e.control.value
            _element.shadow[1].blur_radius = e.control.value

        elif e.control.data == "intensity":
            intensity = e.control.value

            shadow_color, highlight_color = calculate_shadow_colors(
                color_picker.color, intensity
            )
            _element.shadow[0].color = shadow_color
            _element.shadow[1].color = highlight_color
        code.update()
        RADIUS.content.controls[1].update()
        DISTANCE.content.controls[1].update()
        BLUR.content.controls[1].update()
        _element.update()

    def open_color_picker(e):
        d.open = True
        page.update()

    # Text - Slider
    def text_slider_ui(
        txt: str, min: float, max: float, width: int, data, default_val: int = 0
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
                        on_change=get_slider_value,
                        data=data,
                    ),
                ]
            ),
        )

    # Each slider(& its text) is stored inside a variable
    SIZE = text_slider_ui("Size:", 10, 350, width=270, data="size", default_val=250)
    RADIUS = text_slider_ui("Radius:", 0, 175, width=250, data="radius", default_val=50)
    DISTANCE = text_slider_ui(
        "Distance:", 5, 50, width=240, data="distance", default_val=20
    )
    INTENSITY = text_slider_ui(
        "Intensity:", 0.01, 0.6, width=240, data="intensity", default_val=0.15
    )
    BLUR = text_slider_ui("Blur:", 0, 100, width=270, data="blur", default_val=60)

    _element = Container(
        border_radius=50,
        width=250,
        height=250,
        bgcolor=color_picker.color,
        margin=margin.only(left=10, right=10),
        shadow=[
            BoxShadow(
                blur_radius=DISTANCE.content.controls[1].value,
                color=shadow_color,
                offset=Offset(
                    DISTANCE.content.controls[1].value,
                    DISTANCE.content.controls[1].value,
                ),
                blur_style=ShadowBlurStyle.NORMAL,
            ),
            BoxShadow(
                blur_radius=DISTANCE.content.controls[1].value,
                color=highlight_color,
                offset=Offset(
                    -DISTANCE.content.controls[1].value,
                    -DISTANCE.content.controls[1].value,
                ),
                blur_style=ShadowBlurStyle.NORMAL,
            ),
        ],
    )
    color_picker_container = Container(
        width=32,
        height=32,
        bgcolor=color_picker.color,
        border=border.all(2, "black"),
        on_click=open_color_picker,
    )

    generated_code = f"""

``` python
ft.Container(
            width={SIZE.content.controls[1].value},
            height={SIZE.content.controls[1].value},
            border_radius={RADIUS.content.controls[1].value},
            bgcolor="{color_picker.color}",
            
            shadow=[
                ft.BoxShadow(
                    offset=ft.Offset({DISTANCE.content.controls[1].value}, {DISTANCE.content.controls[1].value}),
                    blur_radius={BLUR.content.controls[1].value},
                    color="{shadow_color}",
                    blur_style=ft.ShadowBlurStyle.NORMAL,
                ),
                ft.BoxShadow(
                    offset=ft.Offset(-{DISTANCE.content.controls[1].value}, -{DISTANCE.content.controls[1].value}),
                    blur_radius=60,
                    color="{highlight_color}",
                    blur_style=ft.ShadowBlurStyle.NORMAL,
                ),
            ],
        )


```

"""
    code = Markdown(
        generated_code,
        selectable=True,
        extension_set=MarkdownExtensionSet.GITHUB_WEB,
        code_theme="dark",
        code_style=TextStyle(font_family="mono", size=8),
    )

    setting_container = Container(
        Column(
            [
                Container(
                    Row(
                        [
                            Text(
                                "Pick a color:",
                                size=15,
                                weight=FontWeight.W_600,
                                font_family="muli",
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
                Text("Code:", size=15, weight=FontWeight.W_600, font_family="muli"),
                Container(
                    width=380,
                    height=110,
                    margin=margin.only(top=5),
                    content=Column(
                        [
                            code,
                        ],
                        scroll="always",
                        alignment=CrossAxisAlignment.CENTER,
                    ),
                ),
            ],
            spacing=0,
        ),
        border_radius=35,
        width=350,
        height=450,
        bgcolor=color_picker.color,
        padding=padding.only(30, 20, 30, 20),
        shadow=[
            BoxShadow(
                blur_radius=5,
                color=shadow_color,
                offset=Offset(5, 5),
                blur_style=ShadowBlurStyle.NORMAL,
            ),
            BoxShadow(
                blur_radius=5,
                color=highlight_color,
                offset=Offset(-5, -5),
                blur_style=ShadowBlurStyle.NORMAL,
            ),
        ],
    )

    # Change Color
    # _________________________________________________________________________________________________________________________________

    def change_color(e):
        # Check if the picked color is dark
        if is_color_dark(color_picker.color):
            TEXT_SLIDERS_COLOR = "white"
            code.code_theme = "lightfair"
            page.theme_mode = "light"

        else:
            code.code_theme = "atom-on-dark"
            page.theme_mode = "dark"

            TEXT_SLIDERS_COLOR = "#001f3f"
        shadow_color, highlight_color = calculate_shadow_colors(color_picker.color)
        # Text - Slider color
        for txt_slider in [SIZE, RADIUS, DISTANCE, INTENSITY, BLUR]:
            txt_slider.content.controls[0].content.color = TEXT_SLIDERS_COLOR
            txt_slider.content.controls[1].inactive_color = TEXT_SLIDERS_COLOR
            txt_slider.content.controls[1].active_color = TEXT_SLIDERS_COLOR

        for bubble in [TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT]:
            bubble.border.top.color = TEXT_SLIDERS_COLOR

        title_container.controls[1].content.controls[
            0
        ].content.color = TEXT_SLIDERS_COLOR
        title_container.controls[1].content.controls[1].color = TEXT_SLIDERS_COLOR
        color_picker_container.border.top.color = TEXT_SLIDERS_COLOR
        color_picker_container.bgcolor = color_picker.color
        page.bgcolor = color_picker.color
        _element.bgcolor = color_picker.color
        # Shadow colors for _element
        _element.shadow[0].color = shadow_color
        _element.shadow[1].color = highlight_color
        setting_container.bgcolor = color_picker.color

        setting_container.content.controls[0].content.controls[
            0
        ].color = TEXT_SLIDERS_COLOR  # pick_a_color(text)
        setting_container.content.controls[
            6
        ].color = TEXT_SLIDERS_COLOR  # code_text color

        # shadow colors for setting_container
        setting_container.shadow[0].color = shadow_color
        setting_container.shadow[1].color = highlight_color

        d.open = False
        code.update()
        page.update()

    # Handle the closing of the Alert Dialog for color picker
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
                        Column(
                            [Container(width=370), _element, Container(width=370)],
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                        ),
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
    title = Container(
        Text("Neumoflet.io", size=50, weight=FontWeight.BOLD, font_family="muli")
    )
    title.alignment = alignment.center
    title_container = Row(
        [
            Container(width=150),
            Container(
                Column(
                    [
                        title,
                        Text(
                            "Generate Soft-UI Flet code",
                            weight=FontWeight.W_500,
                            font_family="muli",
                        ),
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
    page.fonts = {
        "muli": "/fonts/Muli-Regular.ttf",
        "mono": "/fonts/RobotoMono-Thin.ttf",
    }

    page.theme_mode = "light"
    page.add(title_container, main_content)


if __name__ == "__main__":
    app(target=main, assets_dir="assets")
