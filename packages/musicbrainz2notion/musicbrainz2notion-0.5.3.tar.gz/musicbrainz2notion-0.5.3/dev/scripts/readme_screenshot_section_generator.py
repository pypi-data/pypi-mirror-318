import os

# Directory containing screenshots
screenshot_dir = "media/screenshots/"

# Get list of image files
images = [f for f in os.listdir(screenshot_dir) if f.endswith((".png", ".jpg", ".jpeg", ".gif"))]

# Generate Markdown
markdown = "## 📸 Screenshots\n\n"
for img in images:
    alt_text = os.path.splitext(img)[0].replace("_", " ").title()
    markdown += f"### {alt_text}\n\n"
    markdown += f'<img src="{screenshot_dir}{img}" alt="{alt_text}" style="max-width: 100%; height: auto;">\n\n'

# Save to README.md or another file
with open("README_Screenshots.md", "w") as f:
    f.write(markdown)

print("Screenshots section generated successfully!")
