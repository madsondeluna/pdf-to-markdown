# MarkItDown on Google Colab

This repository demonstrates how to use Microsoft's [MarkItDown](https://github.com/microsoft/markitdown) library to convert PDF files into structured Markdown format, directly in Google Colab. This conversion facilitates document analysis and integration with natural language models.

## Features

- PDF to Markdown conversion
- Plugin support, including OCR for scanned PDFs
- File upload and download in the Google Colab environment
- Display of converted content directly in the notebook

## How to Use

1. **Install the MarkItDown library with all plugins:**

   ```python
   !pip install 'markitdown[all]' --quiet
   ```

2. **Import the necessary libraries:**

   ```python
   from markitdown import MarkItDown
   from google.colab import files
   import os
   ```

3. **Upload the PDF file you want to convert:**

   ```python
   print("Please select the PDF file to convert:")
   uploaded = files.upload()
   ```

4. **Initialize the converter with plugins enabled:**

   ```python
   md = MarkItDown(enable_plugins=True)
   ```

5. **Convert the PDF file to Markdown:**

   ```python
   for filename in uploaded.keys():
       print(f"\nConverting file: {filename}")
       result = md.convert(filename)

       # Display the converted content
       print("\nConverted Markdown content:")
       print(result.text_content)

       # Save the content to a .md file
       output_filename = os.path.splitext(filename)[0] + ".md"
       with open(output_filename, "w", encoding="utf-8") as f:
           f.write(result.text_content)

       # Make the file available for download
       print(f"\nDownloading the converted file: {output_filename}")
       files.download(output_filename)
   ```

## Notes

- **Integrated OCR:** If the PDF contains images with text (e.g., scanned documents), MarkItDown can extract this text automatically, as long as plugins are enabled.

- **Support for Multiple Formats:** In addition to PDFs, MarkItDown supports Word, PowerPoint, Excel, images, audio, and more.

- **Stream Conversion:** If working with in-memory files (e.g., using `io.BytesIO`), MarkItDown also supports stream-based conversion.

## Example Notebook

You can access an example notebook in Google Colab with all the steps above:

[Example Notebook on Google Colab](https://colab.research.google.com/drive/17o6GNKs4PFiCU4eTNCv-uvNtapm3_MSj?usp=sharing)

## License

This project is licensed under the [MIT License](LICENSE).

