# Step 1: Install MarkItDown with all available plugins
!pip install 'markitdown[all]' --quiet

# Step 2: Import required libraries
from markitdown import MarkItDown
from google.colab import files
import os

# Step 3: Upload the PDF file to be converted
print("Please select the PDF file you want to convert:")
uploaded = files.upload()

# Step 4: Initialize the MarkItDown converter with plugins enabled (for features like OCR)
md = MarkItDown(enable_plugins=True)

# Step 5: Convert the uploaded PDF file(s) to Markdown
for filename in uploaded.keys():
    print(f"\nConverting file: {filename}")
    result = md.convert(filename)
    
    # Step 6: Display the converted Markdown content
    print("\nConverted Markdown content:")
    print(result.text_content)
    
    # Step 7: Save the Markdown content to a .md file
    output_filename = os.path.splitext(filename)[0] + ".md"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(result.text_content)
    
    # Step 8: Make the .md file available for download
    print(f"\nDownloading the converted file: {output_filename}")
    files.download(output_filename)
