#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
网页转PDF工具
输入网址链接，读取该网页并在本地生成PDF文件
"""

import requests
import os
import sys
from urllib.parse import urlparse
from datetime import datetime
import weasyprint
from weasyprint import HTML, CSS
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class WebToPDF:
    def __init__(self):
        self.session = requests.Session()
        # 设置请求头，模拟浏览器访问
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
    
    def get_webpage_content(self, url):
        """
        获取网页内容
        """
        try:
            logger.info(f"正在获取网页内容: {url}")
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            # 检查内容类型
            content_type = response.headers.get('content-type', '').lower()
            if 'text/html' not in content_type:
                logger.warning(f"警告: 内容类型不是HTML ({content_type})")
            
            # 检测并设置正确的编码
            if response.encoding == 'ISO-8859-1':
                # 尝试检测真实编码
                response.encoding = response.apparent_encoding
            
            # 确保使用UTF-8编码
            if response.encoding.lower() not in ['utf-8', 'utf8']:
                logger.info(f"检测到编码: {response.encoding}，转换为UTF-8")
                content = response.content.decode(response.encoding, errors='replace')
                content = content.encode('utf-8').decode('utf-8')
            else:
                content = response.text
            
            return content, response.url
            
        except requests.exceptions.RequestException as e:
            logger.error(f"获取网页失败: {e}")
            raise
    
    def generate_filename(self, url, output_dir="pdfs"):
        """
        根据URL生成PDF文件名
        """
        # 创建输出目录
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            logger.info(f"创建输出目录: {output_dir}")
        
        # 解析URL生成文件名
        parsed_url = urlparse(url)
        domain = parsed_url.netloc.replace('.', '_')
        path = parsed_url.path.strip('/').replace('/', '_') or 'index'
        
        # 添加时间戳避免文件名冲突
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{domain}_{path}_{timestamp}.pdf"
        
        # 确保文件名合法
        filename = "".join(c for c in filename if c.isalnum() or c in ('_', '-', '.'))
        
        return os.path.join(output_dir, filename)
    
    def html_to_pdf(self, html_content, output_path, base_url=None):
        """
        将HTML内容转换为PDF
        """
        try:
            logger.info(f"正在生成PDF文件: {output_path}")
            
            # 创建HTML对象
            html_doc = HTML(string=html_content, base_url=base_url)
            
            # 添加一些基本的CSS样式来改善PDF输出
            css_content = """
            @page {
                margin: 1in;
                size: A4;
            }
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                color: #333;
            }
            img {
                max-width: 100%;
                height: auto;
            }
            a {
                color: #0066cc;
                text-decoration: none;
            }
            """
            
            css = CSS(string=css_content)
            
            # 生成PDF
            html_doc.write_pdf(output_path, stylesheets=[css])
            
            logger.info(f"PDF文件生成成功: {output_path}")
            return True
            
        except Exception as e:
            logger.error(f"生成PDF失败: {e}")
            raise
    
    def convert_url_to_pdf(self, url, output_dir="pdfs"):
        """
        主函数：将URL转换为PDF
        """
        try:
            # 获取网页内容
            html_content, final_url = self.get_webpage_content(url)
            
            # 生成输出文件名
            output_path = self.generate_filename(final_url, output_dir)
            
            # 转换为PDF
            self.html_to_pdf(html_content, output_path, base_url=final_url)
            
            return output_path
            
        except Exception as e:
            logger.error(f"转换失败: {e}")
            raise

def main():
    """
    主程序入口
    """
    print("=" * 50)
    print("网页转PDF工具")
    print("=" * 50)
    
    # 创建转换器实例
    converter = WebToPDF()
    
    while True:
        try:
            # 获取用户输入
            url = input("\n请输入网址链接 (输入 'quit' 退出): ").strip()
            
            if url.lower() in ['quit', 'exit', 'q']:
                print("程序退出")
                break
            
            if not url:
                print("请输入有效的网址链接")
                continue
            
            # 确保URL有协议
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url
            
            print(f"\n正在处理: {url}")
            
            # 转换URL为PDF
            output_path = converter.convert_url_to_pdf(url)
            
            print(f"\n✅ 转换成功!")
            print(f"📄 PDF文件保存位置: {output_path}")
            print(f"📁 文件大小: {os.path.getsize(output_path) / 1024:.2f} KB")
            
        except KeyboardInterrupt:
            print("\n\n程序被用户中断")
            break
        except Exception as e:
            print(f"\n❌ 转换失败: {e}")
            print("请检查网址是否正确，或稍后重试")

if __name__ == "__main__":
    main() 