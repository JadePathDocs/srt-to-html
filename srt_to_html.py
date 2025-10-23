import re
import sys
import os

def srt_to_html(input_file):
    """
    Converts an SRT subtitle file to an HTML file for use with furigana browser addons.
    """
    # Generate output filename automatically
    base_name = os.path.splitext(input_file)[0]
    output_file = f"{base_name}.html"
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # More robust: remove digit lines only if followed by timecode
    lines = content.split('\n')
    filtered = []
    for i, line in enumerate(lines):
        # Check if this is a line number (digits only) followed by a timecode
        if re.match(r'^\d+\s*$', line) and i+1 < len(lines) and '-->' in lines[i+1]:
            continue  # Skip subtitle numbers
        filtered.append(line)
    content = '\n'.join(filtered)
    
    # Remove timecodes (format: 00:00:00,000 --> 00:00:00,000)
    content = re.sub(r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}', '', content)
    
    # Remove extra blank lines, convert to <p> tags
    lines = content.strip().split('\n\n')
    paragraphs = ''.join([f'<p>{line.strip()}</p>\n' for line in lines if line.strip()])
    
    # Build simple HTML structure
    html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Japanese Transcript</title>
    <style>
        body {{
            font-family: 'Noto Sans JP', sans-serif;
            line-height: 1.8;
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            font-size: 18px;
        }}
        p {{
            margin-bottom: 1em;
        }}
    </style>
</head>
<body>
{paragraphs}
</body>
</html>"""
    
    # Write HTML to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"HTML conversion complete! Output saved to {output_file}")
    input("Press Enter to close...")  # Keeps window open so you can see the message

# Check if file was provided
if len(sys.argv) < 2:
    print("Usage: Drag and drop an SRT file onto this script, or run:")
    print("python srt_to_html.py yourfile.srt")
    input("Press Enter to close...")
    sys.exit(1)

input_srt = sys.argv[1]

if not os.path.exists(input_srt):
    print(f"Error: File '{input_srt}' not found!")
    input("Press Enter to close...")
    sys.exit(1)

srt_to_html(input_srt)
