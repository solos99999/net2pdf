#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量网页转PDF工具
从网页中获取链接，选择需要的链接，批量转换为PDF文件
"""

import requests
import os
import sys
import re
from urllib.parse import urlparse, urljoin
from datetime import datetime
import logging
from bs4 import BeautifulSoup
import time

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

try:
    import pdfkit
    PDFKIT_AVAILABLE = True
except ImportError:
    PDFKIT_AVAILABLE = False
    logger.warning("pdfkit未安装，将使用HTML文件保存方式")

class BatchWebToPDF:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        })
        
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
                'disable-smart-shrinking': None,
                'no-stop-slow-scripts': None,
                'load-error-handling': 'ignore',
                'load-media-error-handling': 'ignore',
                'javascript-delay': '1000',
                'no-images': None,
                'disable-javascript': None
            }
    
    def get_webpage_content(self, url):
        """获取网页内容"""
        try:
            logger.info(f"正在获取网页内容: {url}")
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            if response.encoding == 'ISO-8859-1':
                response.encoding = response.apparent_encoding
            
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
    
    def extract_links_from_page(self, url, html_content):
        """从网页中提取链接"""
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            links = []
            
            for link in soup.find_all('a', href=True):
                href = link.get('href')
                text = link.get_text(strip=True)
                
                absolute_url = urljoin(url, href)
                
                if self.is_valid_link(absolute_url, text):
                    links.append({
                        'url': absolute_url,
                        'text': text[:50] + '...' if len(text) > 50 else text,
                        'title': link.get('title', '')
                    })
            
            # 去重
            unique_links = []
            seen_urls = set()
            for link in links:
                if link['url'] not in seen_urls:
                    unique_links.append(link)
                    seen_urls.add(link['url'])
            
            logger.info(f"从页面中提取到 {len(unique_links)} 个有效链接")
            return unique_links
            
        except Exception as e:
            logger.error(f"提取链接失败: {e}")
            return []
    
    def is_valid_link(self, url, text):
        """判断链接是否有效"""
        invalid_patterns = [
            r'javascript:',
            r'mailto:',
            r'tel:',
            r'#',
            r'\.(css|js|png|jpg|jpeg|gif|ico|pdf|zip|rar)$',
            r'logout',
            r'login',
            r'admin',
            r'\.(com|cn|org|net)/$'
        ]
        
        for pattern in invalid_patterns:
            if re.search(pattern, url, re.IGNORECASE):
                return False
        
        if not text.strip():
            return False
        
        return True
    
    def display_links(self, links):
        """显示链接列表供用户选择"""
        print(f"\n发现 {len(links)} 个链接:")
        print("-" * 80)
        
        for i, link in enumerate(links, 1):
            print(f"{i:2d}. {link['text']}")
            print(f"    URL: {link['url']}")
            if link['title']:
                print(f"    标题: {link['title']}")
            print()
        
        return self.get_user_selection(links)
    
    def get_user_selection(self, links):
        """获取用户选择的链接"""
        while True:
            try:
                print("请选择要转换的链接 (输入数字，多个用逗号分隔，输入 'all' 选择全部，输入 'quit' 退出):")
                choice = input("您的选择: ").strip()
                
                if choice.lower() == 'quit':
                    return []
                elif choice.lower() == 'all':
                    return [link['url'] for link in links]
                else:
                    indices = [int(x.strip()) - 1 for x in choice.split(',')]
                    selected_links = []
                    
                    for idx in indices:
                        if 0 <= idx < len(links):
                            selected_links.append(links[idx]['url'])
                        else:
                            print(f"无效的选择: {idx + 1}")
                    
                    if selected_links:
                        return selected_links
                    else:
                        print("请选择有效的链接")
                        
            except ValueError:
                print("请输入有效的数字")
            except KeyboardInterrupt:
                print("\n操作被取消")
                return []
    
    def convert_url_to_pdf(self, url, output_dir="batch_outputs"):
        """转换单个URL为PDF"""
        try:
            html_content, final_url = self.get_webpage_content(url)
            
            if PDFKIT_AVAILABLE:
                try:
                    output_path = self.generate_filename(final_url, output_dir, "pdf")
                    self.convert_html_to_pdf(html_content, output_path)
                    return output_path, "pdf"
                except Exception as e:
                    logger.warning(f"HTML转PDF失败，将保存为HTML: {e}")
            
            output_path = self.generate_filename(final_url, output_dir, "html")
            self.save_as_html(html_content, output_path)
            return output_path, "html"
            
        except Exception as e:
            logger.error(f"转换失败: {e}")
            raise
    
    def generate_filename(self, url, output_dir="batch_outputs", extension="pdf"):
        """根据URL生成文件名"""
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
        """保存为HTML文件"""
        try:
            enhanced_content = self.enhance_html_for_chinese(html_content)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(enhanced_content)
            logger.info(f"HTML文件保存成功: {output_path}")
            return True
        except Exception as e:
            logger.error(f"保存HTML文件失败: {e}")
            raise
    
    def enhance_html_for_chinese(self, html_content):
        """增强HTML内容的中文支持"""
        if '<meta charset=' not in html_content and '<meta http-equiv="Content-Type"' not in html_content:
            if '<head>' in html_content:
                html_content = html_content.replace('<head>', '<head>\n    <meta charset="UTF-8">')
            elif '<head ' in html_content:
                html_content = re.sub(r'(<head[^>]*>)', r'\1\n    <meta charset="UTF-8">', html_content)
            else:
                html_content = html_content.replace('<html>', '<html>\n<head>\n    <meta charset="UTF-8">\n</head>')
        
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
    
    def convert_html_to_pdf(self, html_content, output_path):
        """将HTML内容转换为PDF"""
        try:
            logger.info(f"正在将HTML内容转换为PDF: {output_path}")
            
            temp_html = "temp_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".html"
            with open(temp_html, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            try:
                config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
                pdfkit.from_file(temp_html, output_path, options=self.pdfkit_options, configuration=config)
                logger.info(f"PDF文件生成成功: {output_path}")
                return True
            finally:
                if os.path.exists(temp_html):
                    os.remove(temp_html)
                    
        except Exception as e:
            logger.error(f"HTML转PDF失败: {e}")
            raise
    
    def batch_convert(self, urls, output_dir="batch_outputs"):
        """批量转换URL列表"""
        results = []
        total = len(urls)
        
        print(f"\n开始批量转换 {total} 个链接...")
        print("=" * 60)
        
        for i, url in enumerate(urls, 1):
            try:
                print(f"\n[{i}/{total}] 正在转换: {url}")
                
                output_path, file_type = self.convert_url_to_pdf(url, output_dir)
                
                file_size = os.path.getsize(output_path) / 1024
                print(f"✅ 成功: {output_path} ({file_type.upper()}, {file_size:.2f} KB)")
                
                results.append({
                    'url': url,
                    'output_path': output_path,
                    'file_type': file_type,
                    'file_size': file_size,
                    'status': 'success'
                })
                
                if i < total:
                    time.sleep(1)
                    
            except Exception as e:
                print(f"❌ 失败: {e}")
                results.append({
                    'url': url,
                    'error': str(e),
                    'status': 'failed'
                })
        
        return results
    
    def process_main_page(self, url):
        """处理主页面，提取链接并批量转换"""
        try:
            print(f"正在分析主页面: {url}")
            
            html_content, final_url = self.get_webpage_content(url)
            links = self.extract_links_from_page(final_url, html_content)
            
            if not links:
                print("未找到有效链接")
                return
            
            selected_urls = self.display_links(links)
            
            if not selected_urls:
                print("未选择任何链接")
                return
            
            results = self.batch_convert(selected_urls)
            self.show_batch_results(results)
            
        except Exception as e:
            logger.error(f"处理主页面失败: {e}")
            print(f"❌ 处理失败: {e}")

    def show_batch_results(self, results):
        """显示批量转换结果"""
        print("\n" + "=" * 60)
        print("批量转换结果统计")
        print("=" * 60)
        
        success_count = sum(1 for r in results if r['status'] == 'success')
        failed_count = len(results) - success_count
        
        print(f"总链接数: {len(results)}")
        print(f"成功转换: {success_count}")
        print(f"转换失败: {failed_count}")
        
        if success_count > 0:
            total_size = sum(r['file_size'] for r in results if r['status'] == 'success')
            print(f"总文件大小: {total_size:.2f} KB")
            
            pdf_count = sum(1 for r in results if r['status'] == 'success' and r['file_type'] == 'pdf')
            html_count = success_count - pdf_count
            
            print(f"PDF文件: {pdf_count}")
            print(f"HTML文件: {html_count}")
        
        print("\n详细结果:")
        for i, result in enumerate(results, 1):
            if result['status'] == 'success':
                print(f"{i}. ✅ {result['url']} -> {result['output_path']}")
            else:
                print(f"{i}. ❌ {result['url']} -> {result['error']}")

def main():
    """主程序入口"""
    print("=" * 60)
    print("批量网页转PDF工具")
    print("=" * 60)
    
    if not PDFKIT_AVAILABLE:
        print("⚠️  注意: pdfkit未安装，将保存为HTML文件")
        print("   要生成PDF，请安装: pip install pdfkit")
        print("   并下载wkhtmltopdf: https://wkhtmltopdf.org/downloads.html")
        print()
    else:
        print("✅ PDF生成功能已启用")
        print("🔤 中文支持已优化")
        print()
    
    converter = BatchWebToPDF()
    
    while True:
        try:
            print("\n请选择操作:")
            print("1. 输入网页URL，提取链接并批量转换")
            print("2. 直接输入多个URL进行批量转换")
            print("3. 退出")
            
            choice = input("\n请输入选择 (1-3): ").strip()
            
            if choice == '1':
                url = input("\n请输入网页URL: ").strip()
                if not url:
                    print("请输入有效的URL")
                    continue
                
                if not url.startswith(('http://', 'https://')):
                    url = 'https://' + url
                
                converter.process_main_page(url)
                
            elif choice == '2':
                print("\n请输入多个URL (每行一个，输入空行结束):")
                urls = []
                while True:
                    url = input().strip()
                    if not url:
                        break
                    if not url.startswith(('http://', 'https://')):
                        url = 'https://' + url
                    urls.append(url)
                
                if urls:
                    results = converter.batch_convert(urls)
                    converter.show_batch_results(results)
                else:
                    print("未输入任何URL")
                    
            elif choice == '3':
                print("程序退出")
                break
            else:
                print("无效选择，请重新输入")
                
        except KeyboardInterrupt:
            print("\n\n程序被用户中断")
            break
        except Exception as e:
            print(f"\n❌ 操作失败: {e}")
            print("请稍后重试")

if __name__ == "__main__":
    main() 