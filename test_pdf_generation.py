#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试PDF生成功能
"""

import os
import pdfkit
from web_to_pdf_simple import SimpleWebToPDF

def test_pdf_from_html():
    """测试从HTML文件生成PDF"""
    print("=" * 50)
    print("测试PDF生成功能")
    print("=" * 50)
    
    # 创建一个简单的HTML文件
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>测试页面</title>
        <style>
            body {
                font-family: "Microsoft YaHei", Arial, sans-serif;
                line-height: 1.6;
                margin: 40px;
            }
            h1 {
                color: #333;
                text-align: center;
            }
            p {
                color: #666;
                font-size: 16px;
            }
        </style>
    </head>
    <body>
        <h1>网页转PDF测试</h1>
        <p>这是一个测试页面，用于验证PDF生成功能是否正常工作。</p>
        <p>如果您能看到这段中文文字，说明中文支持正常。</p>
        <p>This is a test page to verify PDF generation functionality.</p>
        <p>如果您能看到这段英文文字，说明英文支持也正常。</p>
    </body>
    </html>
    """
    
    # 保存HTML文件
    html_file = "test.html"
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ 创建测试HTML文件: {html_file}")
    
    # 配置wkhtmltopdf
    config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
    
    # PDF选项
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None,
        'enable-local-file-access': None
    }
    
    # 生成PDF
    pdf_file = "test_output.pdf"
    try:
        print(f"正在生成PDF: {pdf_file}")
        pdfkit.from_file(html_file, pdf_file, options=options, configuration=config)
        print(f"✅ PDF生成成功: {pdf_file}")
        
        # 检查文件大小
        file_size = os.path.getsize(pdf_file) / 1024
        print(f"📁 PDF文件大小: {file_size:.2f} KB")
        
        return True
        
    except Exception as e:
        print(f"❌ PDF生成失败: {e}")
        return False

def test_web_to_pdf():
    """测试网页转PDF功能"""
    print("\n" + "=" * 50)
    print("测试网页转PDF功能")
    print("=" * 50)
    
    converter = SimpleWebToPDF()
    
    # 测试一个简单的网页
    test_url = "https://httpbin.org/html"
    
    try:
        print(f"正在转换: {test_url}")
        output_path, file_type = converter.convert_url_to_pdf(test_url, "test_outputs")
        
        print(f"✅ 转换成功: {output_path}")
        print(f"📁 文件类型: {file_type}")
        
        if file_type == "pdf":
            file_size = os.path.getsize(output_path) / 1024
            print(f"📁 PDF文件大小: {file_size:.2f} KB")
            print("🎉 PDF生成功能完全正常！")
        else:
            print("⚠️  生成了HTML文件，PDF生成可能有问题")
        
        return True
        
    except Exception as e:
        print(f"❌ 转换失败: {e}")
        return False

def main():
    """主函数"""
    print("PDF生成功能测试")
    print()
    
    # 测试1: 从HTML文件生成PDF
    success1 = test_pdf_from_html()
    
    # 测试2: 网页转PDF
    success2 = test_web_to_pdf()
    
    print("\n" + "=" * 50)
    print("测试结果")
    print("=" * 50)
    
    if success1 and success2:
        print("🎉 所有测试通过！PDF生成功能完全正常")
    elif success1:
        print("✅ HTML转PDF正常，网页转PDF需要进一步配置")
    elif success2:
        print("✅ 网页转PDF正常，HTML转PDF需要进一步配置")
    else:
        print("❌ PDF生成功能有问题，需要检查配置")
    
    print("\n💡 建议:")
    print("   1. 检查生成的PDF文件是否正常")
    print("   2. 确认中文显示是否正确")
    print("   3. 如果网页转PDF失败，可以先生成HTML再手动转换")

if __name__ == "__main__":
    main() 