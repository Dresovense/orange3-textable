from PIL import Image, ImageDraw, ImageFont

# Define the texts and styles
text1 = "a simple example"
text2 = "what's the plan?"
group1_black = [(0, 0), (2, 7)]  # Group "a simple" (black with dotted lines)
group1_gray = [(8, 16)]  # Group "example" (gray)
group2 = [(11, 14)]  # Group "plan" (black with dotted lines)
group2_gray = [(0, 10)]  # Group "what's the" (gray)

# Font and size
font = ImageFont.truetype("arial.ttf", 40)  # Change font and size as needed

# Calculate image size (slightly larger for the outer border)
cell_size = 50
padding = 10  # Additional space around the dashed borders

# Increase width to ensure the second line fits completely
text1_width = len(text1) * cell_size
text2_width = (len(text2) - 1) * cell_size  # Adjust for the extra character
additional_space = 70  # Additional space for safety

width = max(text1_width, text2_width + additional_space) + 2 * padding
height = 2 * cell_size + 3 * padding  # Two rows of text

# Create image with white background
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Function to draw a dashed line
def draw_dashed_line(draw, start_pos, end_pos, dash_length=5):
    x_start, y_start = start_pos
    x_end, y_end = end_pos
    total_length = ((x_end - x_start) ** 2 + (y_end - y_start) ** 2) ** 0.5
    num_dashes = int(total_length // (2 * dash_length))
    for i in range(num_dashes):
        start_dash = (
            x_start + (x_end - x_start) * (2 * i) / (2 * num_dashes),
            y_start + (y_end - y_start) * (2 * i) / (2 * num_dashes),
        )
        end_dash = (
            x_start + (x_end - x_start) * (2 * i + 1) / (2 * num_dashes),
            y_start + (y_end - y_start) * (2 * i + 1) / (2 * num_dashes),
        )
        draw.line([start_dash, end_dash], fill="red", width=3)

# Draw first text ("a simple example")
offset_x = 6
for i, char in enumerate(text1):
    x = i * cell_size + padding + offset_x
    draw.rectangle([x, padding, x + cell_size, padding + cell_size], outline="black")
    if i >= group1_gray[0][0] and i <= group1_gray[0][1]:
        draw.text((x + cell_size // 4, padding), char, fill="gray", font=font)
    else:
        draw.text((x + cell_size // 4, padding), char, fill="black", font=font)

# Draw second text ("what's the plan?") slightly lower and skewed to the left
offset_x = -6  # Skew to the left
offset_y = cell_size + padding + 10  # Lower than the first line
for i, char in enumerate(text2):
    x = i * cell_size + padding + offset_x
    draw.rectangle([x, offset_y, x + cell_size, offset_y + cell_size], outline="black")
    if i >= group2[0][0] and i <= group2[0][1]:
        draw.text((x + cell_size // 4, offset_y), char, fill="black", font=font)
    elif i >= group2_gray[0][0] and i <= group2_gray[0][1]:
        draw.text((x + cell_size // 4, offset_y), char, fill="gray", font=font)

# Draw dotted red lines around "a simple" in the first text
for group in group1_black:
    start, end = group
    x_start = start * cell_size + padding + 6 - 5
    x_end = (end + 1) * cell_size + padding + 6 + 5
    y_top = padding - 5
    y_bottom = padding + cell_size + 5

    # Top border
    draw_dashed_line(draw, (x_start, y_top), (x_end, y_top))
    # Bottom border
    draw_dashed_line(draw, (x_start, y_bottom), (x_end, y_bottom))
    # Left border
    draw_dashed_line(draw, (x_start, y_top), (x_start, y_bottom))
    # Right border
    draw_dashed_line(draw, (x_end, y_top), (x_end, y_bottom))

# Draw dotted red lines around "plan" in the second text
start, end = group2[0]
x_start = start * cell_size + padding + offset_x - 5
x_end = (end + 1) * cell_size + padding + offset_x + 5
y_top = offset_y - 5
y_bottom = offset_y + cell_size + 5

# Top border
draw_dashed_line(draw, (x_start, y_top), (x_end, y_top))
# Bottom border
draw_dashed_line(draw, (x_start, y_bottom), (x_end, y_bottom))
# Left border
draw_dashed_line(draw, (x_start, y_top), (x_start, y_bottom))
# Right border
draw_dashed_line(draw, (x_end, y_top), (x_end, y_bottom))

# Draw the "?" at the end of the second line in gray
question_mark_index = len(text2) - 1  # Index of the "?" character
x = question_mark_index * cell_size + padding + offset_x
draw.rectangle([x, offset_y, x + cell_size, offset_y + cell_size], outline="black")
draw.text((x + cell_size // 4, offset_y), text2[question_mark_index], fill="gray", font=font)

# Display image
image.show()
