# 项目结构说明

## 📁 目录结构

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
├── 📚 文档
│   ├── README.md                 # 中文说明文档
│   ├── README_EN.md              # 英文说明文档
│   ├── PROJECT_STRUCTURE.md      # 项目结构说明
│   └── CHANGELOG.md              # 更新日志
│
├── 📁 输出目录（自动创建）
│   ├── outputs/                  # 单个文件输出
│   ├── batch_outputs/            # 批量处理输出
│   ├── examples/                 # 示例输出
│   ├── chinese_test/             # 中文测试输出
│   └── test_outputs/             # 测试输出
│
└── 📁 其他
    ├── downloads/                # 下载文件目录
    └── __pycache__/              # Python缓存（可忽略）
```

## 🔧 文件功能说明

### 核心程序文件

| 文件名 | 功能 | 推荐度 |
|--------|------|--------|
| `web_to_pdf_simple.py` | 简化版本，使用pdfkit，稳定可靠 | ⭐⭐⭐⭐⭐ |
| `web_to_pdf.py` | 完整版本，使用weasyprint，功能强大 | ⭐⭐⭐⭐ |
| `batch_web_to_pdf.py` | 批量处理，可提取网页链接并批量转换 | ⭐⭐⭐⭐⭐ |
| `web_to_pdf_enhanced.py` | 增强版本，优化中文支持 | ⭐⭐⭐⭐ |

### 工具和脚本

| 文件名 | 功能 |
|--------|------|
| `install_dependencies.py` | 自动安装Python依赖包 |
| `install_wkhtmltopdf.py` | 自动下载安装wkhtmltopdf |
| `run.bat` | Windows用户友好的启动脚本 |
| `requirements.txt` | Python依赖包列表 |

### 测试文件

| 文件名 | 功能 |
|--------|------|
| `test_chinese.py` | 测试中文网页支持 |
| `test_pdf_generation.py` | 测试PDF生成功能 |
| `example.py` | 演示程序使用方法 |

## 🚀 快速开始

1. **安装依赖**：
   ```bash
   python install_dependencies.py
   ```

2. **运行程序**：
   ```bash
   # 单个网页转换
   python web_to_pdf_simple.py
   
   # 批量网页转换
   python batch_web_to_pdf.py
   
   # Windows用户
   run.bat
   ```

## 📋 版本说明

- **简化版本**：适合大多数用户，依赖少，稳定可靠
- **完整版本**：功能最全面，但需要更多系统依赖
- **批量版本**：适合需要处理多个网页的用户
- **增强版本**：针对中文内容优化

## 🔍 输出目录说明

- `outputs/`：单个网页转换的输出文件
- `batch_outputs/`：批量处理的输出文件
- `examples/`：示例程序的输出文件
- `chinese_test/`：中文测试的输出文件
- `test_outputs/`：功能测试的输出文件

所有输出目录会在首次使用时自动创建。 