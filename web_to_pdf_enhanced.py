#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
网页转PDF工具 (增强版)
专门优化中文支持的版本
"""

import requests
import os
import sys
import re
from urllib.parse import urlparse
from datetime import datetime
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

try:
    import pdfkit
    PDFKIT_AVAILABLE = True
except ImportError:
    PDFKIT_AVAILABLE = False
    logger.warning("pdfkit未安装，将使用HTML文件保存方式")

class EnhancedWebToPDF:
    def __init__(self):
        self.session = requests.Session()
        # 设置请求头，模拟浏览器访问
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        })
        
        # 配置pdfkit选项，优化中文支持
        if PDFKIT_AVAILABLE:
            self.pdfkit_options = {
                'page-size': 'A4',
                'margin-top': '0.75in',
                'margin-right': '0.75in',
                'margin-bottom': '0.75in',
                'margin-left': '0.75in',
                'encoding': "UTF-8",
                'no-outline': None,
                'enable-local-file-access': None,
                'javascript-delay': '1000',
                'no-stop-slow-scripts': None,
                'load-error-handling': 'ignore',
                'load-media-error-handling': 'ignore'
            }
    
    def get_webpage_content(self, url):
        """
        获取网页内容，增强中文支持
        """
        try:
            logger.info(f"正在获取网页内容: {url}")
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            # 智能检测编码
            if response.encoding == 'ISO-8859-1':
                response.encoding = response.apparent_encoding
            
            # 确保使用UTF-8编码
            if response.encoding.lower() not in ['utf-8', 'utf8']:
                logger.info(f"检测到编码: {response.encoding}，转换为UTF-8")
                content = response.content.decode(response.encoding, errors='replace')
                content = content.encode('utf-8').decode('utf-8')
            else:
                content = response.text
            
            # 检查中文字符
            chinese_chars = sum(1 for c in content if '\u4e00' <= c <= '\u9fff')
            logger.info(f"检测到 {chinese_chars} 个中文字符")
            
            return content, response.url
            
        except requests.exceptions.RequestException as e:
            logger.error(f"获取网页失败: {e}")
            raise
    
    def enhance_html_for_chinese(self, html_content):
        """
        增强HTML内容的中文支持
        """
        # 确保有正确的meta标签
        if '<meta charset=' not in html_content and '<meta http-equiv="Content-Type"' not in html_content:
            if '<head>' in html_content:
                html_content = html_content.replace('<head>', '<head>\n    <meta charset="UTF-8">')
            elif '<head ' in html_content:
                html_content = re.sub(r'(<head[^>]*>)', r'\1\n    <meta charset="UTF-8">', html_content)
            else:
                html_content = html_content.replace('<html>', '<html>\n<head>\n    <meta charset="UTF-8">\n</head>')
        
        # 添加中文字体支持
        font_css = """
        <style>
        body {
            font-family: "Microsoft YaHei", "SimSun", "SimHei", "KaiTi", "FangSong", Arial, sans-serif;
            line-height: 1.6;
        }
        </style>
        """
        
        if '<head>' in html_content:
            html_content = html_content.replace('<head>', '<head>' + font_css)
        elif '<head ' in html_content:
            html_content = re.sub(r'(<head[^>]*>)', r'\1' + font_css, html_content)
        
        return html_content
    
    def generate_filename(self, url, output_dir="outputs", extension="pdf"):
        """
        根据URL生成文件名
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            logger.info(f"创建输出目录: {output_dir}")
        
        parsed_url = urlparse(url)
        domain = parsed_url.netloc.replace('.', '_')
        path = parsed_url.path.strip('/').replace('/', '_') or 'index'
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{domain}_{path}_{timestamp}.{extension}"
        
        filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
        
        return os.path.join(output_dir, filename)
    
    def save_as_html(self, html_content, output_path):
        """
        保存为HTML文件，增强中文支持
        """
        try:
            enhanced_content = self.enhance_html_for_chinese(html_content)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(enhanced_content)
            logger.info(f"HTML文件保存成功: {output_path}")
            return True
        except Exception as e:
            logger.error(f"保存HTML文件失败: {e}")
            raise
    
    def convert_to_pdf_with_pdfkit(self, url, output_path):
        """
        使用pdfkit转换为PDF
        """
        try:
            logger.info(f"正在使用pdfkit生成PDF: {output_path}")
            pdfkit.from_url(url, output_path, options=self.pdfkit_options)
            logger.info(f"PDF文件生成成功: {output_path}")
            return True
        except Exception as e:
            logger.error(f"pdfkit转换失败: {e}")
            raise
    
    def convert_url_to_pdf(self, url, output_dir="outputs"):
        """
        主函数：将URL转换为PDF或HTML
        """
        try:
            html_content, final_url = self.get_webpage_content(url)
            
            if PDFKIT_AVAILABLE:
                try:
                    output_path = self.generate_filename(final_url, output_dir, "pdf")
                    self.convert_to_pdf_with_pdfkit(final_url, output_path)
                    return output_path, "pdf"
                except Exception as e:
                    logger.warning(f"PDF转换失败，将保存为HTML: {e}")
            
            output_path = self.generate_filename(final_url, output_dir, "html")
            self.save_as_html(html_content, output_path)
            return output_path, "html"
            
        except Exception as e:
            logger.error(f"转换失败: {e}")
            raise

def main():
    """
    主程序入口
    """
    print("=" * 60)
    print("网页转PDF工具 (增强版 - 中文优化)")
    print("=" * 60)
    
    if not PDFKIT_AVAILABLE:
        print("⚠️  注意: pdfkit未安装，将保存为HTML文件")
        print("   要生成PDF，请安装: pip install pdfkit")
        print("   并下载wkhtmltopdf: https://wkhtmltopdf.org/downloads.html")
        print()
    
    converter = EnhancedWebToPDF()
    
    while True:
        try:
            url = input("\n请输入网址链接 (输入 'quit' 退出): ").strip()
            
            if url.lower() in ['quit', 'exit', 'q']:
                print("程序退出")
                break
            
            if not url:
                print("请输入有效的网址链接")
                continue
            
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url
            
            print(f"\n正在处理: {url}")
            
            output_path, file_type = converter.convert_url_to_pdf(url)
            
            print(f"\n✅ 转换成功!")
            print(f"📄 文件保存位置: {output_path}")
            print(f"📁 文件类型: {file_type.upper()}")
            print(f"📁 文件大小: {os.path.getsize(output_path) / 1024:.2f} KB")
            
            if file_type == "html":
                print("💡 提示: 您可以在浏览器中打开HTML文件，然后使用浏览器的打印功能保存为PDF")
                print("🔤 中文支持: 已优化中文字体显示")
            
        except KeyboardInterrupt:
            print("\n\n程序被用户中断")
            break
        except Exception as e:
            print(f"\n❌ 转换失败: {e}")
            print("请检查网址是否正确，或稍后重试")

if __name__ == "__main__":
    main() 