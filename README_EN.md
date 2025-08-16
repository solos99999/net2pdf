# 🌐 Web to PDF Tool

A powerful Python tool for converting web pages to PDF files with complete Chinese support and batch processing capabilities.

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)]()

## ✨ Features

- 🚀 **Fast Conversion** - Support single and batch web page to PDF conversion
- 🔤 **Chinese Optimization** - Complete Chinese encoding support and font optimization
- 📄 **Smart Naming** - Automatically generate meaningful filenames
- 🎨 **Style Optimization** - Optimized PDF styles and layouts
- 🔄 **Batch Processing** - Extract links from web pages and batch convert
- 📝 **Detailed Logging** - Complete operation logs and error information
- 🛡️ **Error Handling** - Comprehensive exception capture and fallback mechanisms
- 🌍 **Cross-Platform** - Support Windows, Linux, macOS

## 📋 System Requirements

### Python Version
- Python 3.7 or higher

### System Dependencies

#### Windows
- Automatic wkhtmltopdf installation (handled by the program)
- Optional: GTK+ Runtime Environment (for weasyprint version)

#### Linux
```bash
# Ubuntu/Debian
sudo apt-get install build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info

# CentOS/RHEL
sudo yum install redhat-rpm-config python3-devel python3-pip python3-cffi libffi-devel cairo pango gdk-pixbuf2
```

#### macOS
```bash
brew install cairo pango gdk-pixbuf libffi
```

## 🚀 Quick Start

### 1. Clone the Project
```bash
git clone https://github.com/yourusername/web-to-pdf-tool.git
cd web-to-pdf-tool
```

### 2. Install Dependencies
```bash
# Auto-install all dependencies
python install_dependencies.py

# Or install manually
pip install -r requirements.txt
```

### 3. Run the Program

#### Single Web Page Conversion
```bash
python web_to_pdf_simple.py
```

#### Batch Web Page Conversion
```bash
python batch_web_to_pdf.py
```

#### Windows Users (Recommended)
```bash
run.bat
```

## 📖 Usage

### Single Web Page Conversion
1. Run `python web_to_pdf_simple.py`
2. Enter the URL of the web page to convert
3. The program automatically processes and generates a PDF file
4. Enter `quit` to exit the program

### Batch Web Page Conversion
1. Run `python batch_web_to_pdf.py`
2. Choose operation mode:
   - Enter web page URL, extract links and batch convert
   - Directly enter multiple URLs for batch conversion
3. Select links to convert
4. The program automatically processes in batch

### Example Output
```
Enter URL (type 'quit' to exit): https://www.example.com
Processing: https://www.example.com
✅ Conversion successful!
📄 File saved to: outputs/www_example_com_index_20231201_143022.pdf
📁 File type: PDF
📁 File size: 245.67 KB
```

## 📁 Project Structure

```
web-to-pdf-tool/
├── 📄 Core Program Files
│   ├── web_to_pdf_simple.py      # Simple version (recommended)
│   ├── web_to_pdf.py             # Full version (requires weasyprint)
│   ├── batch_web_to_pdf.py       # Batch processing version
│   └── web_to_pdf_enhanced.py    # Enhanced version
│
├── 🛠️ Tools and Scripts
│   ├── install_dependencies.py   # Dependency installation script
│   ├── install_wkhtmltopdf.py    # wkhtmltopdf installation script
│   ├── run.bat                   # Windows batch script
│   └── requirements.txt          # Python dependency list
│
├── 🧪 Test Files
│   ├── test_chinese.py           # Chinese support test
│   ├── test_pdf_generation.py    # PDF generation test
│   └── example.py                # Usage examples
│
└── 📚 Documentation
    ├── README.md                 # Chinese documentation
    ├── README_EN.md              # English documentation
    ├── PROJECT_STRUCTURE.md      # Project structure guide
    └── CHANGELOG.md              # Update log
```

## 🔧 Advanced Usage

### Using as a Module
```python
from web_to_pdf_simple import SimpleWebToPDF

# Single conversion
converter = SimpleWebToPDF()
output_path, file_type = converter.convert_url_to_pdf("https://www.example.com")
print(f"File saved to: {output_path}")

# Batch conversion
from batch_web_to_pdf import BatchWebToPDF
batch_converter = BatchWebToPDF()
results = batch_converter.batch_convert(["url1", "url2", "url3"])
```

### Custom Output Directory
```python
converter = SimpleWebToPDF()
output_path, file_type = converter.convert_url_to_pdf("https://www.example.com", "my_pdfs")
```

## 🧪 Testing Features

### Test Chinese Support
```bash
python test_chinese.py
```

### Test PDF Generation
```bash
python test_pdf_generation.py
```

### Run Examples
```bash
python example.py
```

## 📋 Version Description

| Version | Features | Recommended For |
|---------|----------|-----------------|
| **Simple Version** | Uses pdfkit, fewer dependencies, stable and reliable | Most users |
| **Full Version** | Uses weasyprint, most comprehensive features | Advanced users |
| **Batch Version** | Supports batch processing and link extraction | Users needing batch processing |
| **Enhanced Version** | Optimized for Chinese content | Users mainly processing Chinese content |

## ⚠️ Important Notes

1. **Network Connection** - Ensure stable network connection
2. **Website Access Rights** - Some websites may have anti-crawling mechanisms
3. **JavaScript Rendering** - This tool does not support JavaScript dynamic content
4. **File Size** - Large web pages may generate large PDF files
5. **Copyright Issues** - Please comply with website copyright and usage terms

## 🔍 Troubleshooting

### Common Issues

#### 1. Dependency Installation Failed
```bash
# Use auto-installation script
python install_dependencies.py

# Or install manually
pip install --upgrade pip
pip install -r requirements.txt
```

#### 2. PDF Generation Failed
- Check if wkhtmltopdf is properly installed
- Run `python test_pdf_generation.py` to test
- Check error logs for detailed information

#### 3. Chinese Display Issues
- Run `python test_chinese.py` to test Chinese support
- Ensure web page encoding is correct
- Check generated HTML file encoding

#### 4. Batch Processing Failed
- Check network connection
- Verify link validity
- Check detailed error information

### Getting Help
- View [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) to understand project structure
- View [CHANGELOG.md](CHANGELOG.md) to understand update history
- Submit [Issue](https://github.com/yourusername/web-to-pdf-tool/issues) to report problems

## 🤝 Contributing

Welcome to submit Issues and Pull Requests to improve this project!

### How to Contribute
1. Fork this project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

Thanks to the following open source projects:
- [pdfkit](https://github.com/JazzCore/python-pdfkit) - PDF generation
- [weasyprint](https://github.com/Kozea/WeasyPrint) - HTML to PDF
- [requests](https://github.com/psf/requests) - HTTP requests
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/) - HTML parsing

---

⭐ If this project helps you, please give it a star! 