def is_color_dark(hex_color):
    # Convert hex color to RGB components
    r = int(hex_color[1:3], 16) / 255.0
    g = int(hex_color[3:5], 16) / 255.0
    b = int(hex_color[5:], 16) / 255.0

    # Calculate relative luminance
    luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b

    # Check if color is dark (adjust the threshold as needed)
    return luminance < 0.5


def calculate_shadow_colors(background_color, intens: int = 0.15):
    # Validate and clean the background color string
    background_color = "".join(c for c in background_color if c.isalnum())

    # Convert hex to RGB
    r, g, b = (
        int(background_color[0:2], 16),
        int(background_color[2:4], 16),
        int(background_color[4:6], 16),
    )

    # Adjust brightness for shadow and highlight
    shadow_brightness = 0.8
    highlight_brightness = 1.1

    # Calculate shadow color
    shadow_color = "#{:02x}{:02x}{:02x}".format(
        min(int(r * shadow_brightness), 255),
        min(int(g * shadow_brightness), 255),
        min(int(b * shadow_brightness), 255),
    )

    # Calculate highlight color
    highlight_color = "#{:02x}{:02x}{:02x}".format(
        min(int(r * highlight_brightness), 255),
        min(int(g * highlight_brightness), 255),
        min(int(b * highlight_brightness), 255),
    )

    if intens:
        shadow_color = get_color_intensity(background_color, intens * -1)
        highlight_color = get_color_intensity(background_color, intens)

    return shadow_color, highlight_color


def get_color_intensity(hex, intensity):
    # Validate hex string
    hex = "".join(c for c in hex if c.isalnum())
    if len(hex) < 6:
        hex = hex[0] + hex[0] + hex[1] + hex[1] + hex[2] + hex[2]

    intensity = intensity or 0

    color = "#"
    for i in range(0, 3):
        c = int(hex[i * 2 : i * 2 + 2], 16)
        c = min(max(0, c + c * intensity), 255)
        color += format(int(c), "02x")

    return color


# To display the generated code
def display_code(
    shadow_color,
    highlight_color,
    size: int = 250,
    radius: int = 50,
    distance: tuple = (-20, -20),
    blur: int = 60,
    color="#c5b5b5",
):
    X, Y = distance
    code = f"""
```python
ft.Container(
            width = {int(size)},
            height = {int(size)},
            border_radius = {int(radius)},
            bgcolor = "{color}",
            shadow = [
                ft.BoxShadow(
                    offset = ft.Offset({-X if type(distance)==tuple else distance }, {-Y if type(distance)==tuple else distance}),
                    blur_radius = {int(blur)},
                    color = "{shadow_color}",
                    blur_style = ft.ShadowBlurStyle.NORMAL,
                ),
                ft.BoxShadow(
                    offset = ft.Offset({X if type(distance)==tuple else distance}, {Y if type(distance)==tuple else distance}),
                    blur_radius = {int(blur)},
                    color = "{highlight_color}",
                    blur_style = ft.ShadowBlurStyle.NORMAL,
                ),
            ],
        )

```

"""
    return code
