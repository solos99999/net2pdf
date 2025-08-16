# 🌐 网页转PDF工具

一个功能强大的Python工具，支持将网页转换为PDF文件，具有完整的中文支持和批量处理功能。

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)]()

## ✨ 功能特点

- 🚀 **快速转换** - 支持单个和批量网页转PDF
- 🔤 **中文优化** - 完整的中文编码支持和字体优化
- 📄 **智能命名** - 自动生成有意义的文件名
- 🎨 **样式优化** - 优化的PDF样式和布局
- 🔄 **批量处理** - 从网页中提取链接并批量转换
- 📝 **详细日志** - 完整的操作日志和错误信息
- 🛡️ **错误处理** - 完善的异常捕获和降级机制
- 🌍 **跨平台** - 支持Windows、Linux、macOS

## 📋 系统要求

### Python版本
- Python 3.7 或更高版本

### 系统依赖

#### Windows
- 自动安装wkhtmltopdf（程序会自动处理）
- 可选：GTK+运行时环境（用于weasyprint版本）

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

## 🚀 快速开始

### ⚡ 推荐使用简化版本

为了避免复杂的依赖问题，我们强烈推荐使用**简化版本**，它功能完整且稳定可靠。

### 1. 克隆项目
```bash
git clone https://github.com/yourusername/web-to-pdf-tool.git
cd web-to-pdf-tool
```

### 2. 安装依赖
```bash
# 自动安装所有依赖
python install_dependencies.py

# 或手动安装
pip install -r requirements.txt
```

### 3. 运行程序

#### 🎯 简化版本（推荐）
```bash
python web_to_pdf_simple.py
```

#### 批量网页转换
```bash
python batch_web_to_pdf.py
```

#### Windows用户（推荐）
```bash
run.bat
```

### 📋 版本对比

| 功能 | 简化版本 | 完整版本 |
|------|----------|----------|
| 单个网页转换 | ✅ | ✅ |
| 批量网页转换 | ✅ | ✅ |
| 中文支持 | ✅ | ✅ |
| PDF生成 | ✅ | ✅ |
| 依赖复杂度 | 低 | 高 |
| 安装难度 | 简单 | 复杂 |
| 稳定性 | 高 | 中等 |

**💡 建议：首次使用请选择简化版本！**

## 📖 使用方法

### 单个网页转换
1. 运行 `python web_to_pdf_simple.py`
2. 输入要转换的网址链接
3. 程序自动处理并生成PDF文件
4. 输入 `quit` 退出程序

### 批量网页转换
1. 运行 `python batch_web_to_pdf.py`
2. 选择操作模式：
   - 输入网页URL，提取链接并批量转换
   - 直接输入多个URL进行批量转换
3. 选择要转换的链接
4. 程序自动批量处理

### 示例输出
```
请输入网址链接 (输入 'quit' 退出): https://www.example.com
正在处理: https://www.example.com
✅ 转换成功!
📄 文件保存位置: outputs/www_example_com_index_20231201_143022.pdf
📁 文件类型: PDF
📁 文件大小: 245.67 KB
```

## 📁 项目结构

```
web-to-pdf-tool/
├── 📄 核心程序文件
│   ├── web_to_pdf_simple.py      # 简化版本（推荐使用）
│   ├── web_to_pdf.py             # 完整版本（需要weasyprint）
│   ├── batch_web_to_pdf.py       # 批量处理版本
│   └── web_to_pdf_enhanced.py    # 增强版本
│
├── 🛠️ 工具和脚本
│   ├── install_dependencies.py   # 依赖安装脚本
│   ├── install_wkhtmltopdf.py    # wkhtmltopdf安装脚本
│   ├── run.bat                   # Windows批处理脚本
│   └── requirements.txt          # Python依赖列表
│
├── 🧪 测试文件
│   ├── test_chinese.py           # 中文支持测试
│   ├── test_pdf_generation.py    # PDF生成测试
│   └── example.py                # 使用示例
│
└── 📚 文档
    ├── README.md                 # 中文说明文档
    ├── README_EN.md              # 英文说明文档
    ├── PROJECT_STRUCTURE.md      # 项目结构说明
    └── CHANGELOG.md              # 更新日志
```

## 🔧 高级用法

### 作为模块使用
```python
from web_to_pdf_simple import SimpleWebToPDF

# 单个转换
converter = SimpleWebToPDF()
output_path, file_type = converter.convert_url_to_pdf("https://www.example.com")
print(f"文件已保存到: {output_path}")

# 批量转换
from batch_web_to_pdf import BatchWebToPDF
batch_converter = BatchWebToPDF()
results = batch_converter.batch_convert(["url1", "url2", "url3"])
```

### 自定义输出目录
```python
converter = SimpleWebToPDF()
output_path, file_type = converter.convert_url_to_pdf("https://www.example.com", "my_pdfs")
```

## 🧪 测试功能

### 测试中文支持
```bash
python test_chinese.py
```

### 测试PDF生成
```bash
python test_pdf_generation.py
```

### 运行示例
```bash
python example.py
```

## 📋 版本说明

| 版本 | 特点 | 推荐用户 |
|------|------|----------|
| **简化版本** | 使用pdfkit，依赖少，稳定可靠 | 大多数用户 |
| **完整版本** | 使用weasyprint，功能最全面 | 高级用户 |
| **批量版本** | 支持批量处理和链接提取 | 需要批量处理的用户 |
| **增强版本** | 针对中文内容优化 | 主要处理中文内容的用户 |

## ⚠️ 注意事项

1. **网络连接** - 确保有稳定的网络连接
2. **网站访问权限** - 某些网站可能有反爬虫机制
3. **JavaScript渲染** - 此工具不支持JavaScript动态内容
4. **文件大小** - 大型网页可能生成较大的PDF文件
5. **版权问题** - 请遵守网站的版权和使用条款

## 🔍 故障排除

### 常见问题

#### 1. 安装依赖失败
```bash
# 使用自动安装脚本
python install_dependencies.py

# 或手动安装
pip install --upgrade pip
pip install -r requirements.txt
```

#### 2. WeasyPrint问题（完整版本）
如果遇到WeasyPrint导入错误，运行修复脚本：
```bash
python fix_weasyprint_issues.py
```

或者使用简化版本（推荐）：
```bash
python web_to_pdf_simple.py
```

#### 3. PDF生成失败
- 检查wkhtmltopdf是否正确安装
- 运行 `python test_pdf_generation.py` 测试
- 查看错误日志获取详细信息

#### 4. 中文显示问题
- 运行 `python test_chinese.py` 测试中文支持
- 确保网页编码正确
- 检查生成的HTML文件编码

#### 5. 批量处理失败
- 检查网络连接
- 确认链接有效性
- 查看详细错误信息

### 获取帮助
- 查看 [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) 了解项目结构
- 查看 [CHANGELOG.md](CHANGELOG.md) 了解更新历史
- 提交 [Issue](https://github.com/yourusername/web-to-pdf-tool/issues) 报告问题

## 🤝 贡献

欢迎提交Issue和Pull Request来改进这个项目！

### 如何贡献
1. Fork 这个项目
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

感谢以下开源项目的支持：
- [pdfkit](https://github.com/JazzCore/python-pdfkit) - PDF生成
- [weasyprint](https://github.com/Kozea/WeasyPrint) - HTML转PDF
- [requests](https://github.com/psf/requests) - HTTP请求
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/) - HTML解析

---

⭐ 如果这个项目对你有帮助，请给它一个星标！ 