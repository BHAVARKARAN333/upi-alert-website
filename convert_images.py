
import base64
import os

files = [
    r"C:\Users\AKSHAY BHAWAR\.gemini\antigravity\brain\c200eeb1-5eb2-4df8-a23c-4225cec1b3ae\media__1773310644442.jpg",
    r"C:\Users\AKSHAY BHAWAR\.gemini\antigravity\brain\c200eeb1-5eb2-4df8-a23c-4225cec1b3ae\media__1773310650794.jpg"
]

with open("base64_images.txt", "w") as out:
    for f in files:
        if os.path.exists(f):
            with open(f, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
                out.write(f"--- START {os.path.basename(f)} ---\n")
                out.write(encoded_string + "\n")
                out.write(f"--- END {os.path.basename(f)} ---\n\n")
        else:
            out.write(f"File not found: {f}\n")
