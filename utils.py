def is_color_dark(hex_color):
    # Convert hex color to RGB components
    r = int(hex_color[1:3], 16) / 255.0
    g = int(hex_color[3:5], 16) / 255.0
    b = int(hex_color[5:], 16) / 255.0

    # Calculate relative luminance
    luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b

    # Check if color is dark (adjust the threshold as needed)
    return luminance < 0.5


def calculate_shadow_colors(background_color):
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
    highlight_brightness = 1.2

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

    return shadow_color, highlight_color
