#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
中文网页支持测试脚本
测试程序对中文网页的处理能力
"""

import os
import sys
from datetime import datetime

def test_chinese_websites():
    """测试中文网站"""
    print("=" * 60)
    print("中文网页支持测试")
    print("=" * 60)
    
    # 测试用的中文网站列表
    chinese_sites = [
        "https://www.baidu.com",
        "https://www.sina.com.cn",
        "https://www.163.com",
        "https://www.qq.com"
    ]
    
    # 优先使用简化版本
    try:
        from web_to_pdf_simple import SimpleWebToPDF
        converter = SimpleWebToPDF()
        print("✅ 使用简化版本进行测试")
        
        for i, url in enumerate(chinese_sites, 1):
            print(f"\n[{i}/{len(chinese_sites)}] 测试中文网站: {url}")
            try:
                output_path, file_type = converter.convert_url_to_pdf(url, "chinese_test")
                print(f"✅ 转换成功: {output_path} ({file_type})")
                
                # 检查文件大小
                file_size = os.path.getsize(output_path) / 1024
                print(f"📁 文件大小: {file_size:.2f} KB")
                
                # 如果是HTML文件，检查中文内容
                if file_type == "html":
                    with open(output_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # 检查是否包含中文字符
                        chinese_chars = sum(1 for c in content if '\u4e00' <= c <= '\u9fff')
                        print(f"🔤 中文字符数量: {chinese_chars}")
                        
                        if chinese_chars > 0:
                            print("✅ 中文内容检测成功")
                        else:
                            print("⚠️  未检测到中文内容")
                
            except Exception as e:
                print(f"❌ 转换失败: {e}")
                
    except ImportError:
        print("❌ 简化版本不可用")
        return False
    
    return True

def test_encoding_detection():
    """测试编码检测功能"""
    print("\n" + "=" * 60)
    print("编码检测功能测试")
    print("=" * 60)
    
    import requests
    
    # 测试不同编码的网站
    test_urls = [
        ("https://httpbin.org/html", "UTF-8"),
        ("https://www.baidu.com", "UTF-8"),
        ("https://www.sina.com.cn", "UTF-8")
    ]
    
    for url, expected_encoding in test_urls:
        try:
            print(f"\n测试URL: {url}")
            response = requests.get(url, timeout=10)
            
            print(f"声明编码: {response.encoding}")
            print(f"检测编码: {response.apparent_encoding}")
            
            # 测试我们的编码处理逻辑
            if response.encoding == 'ISO-8859-1':
                response.encoding = response.apparent_encoding
            
            if response.encoding.lower() not in ['utf-8', 'utf8']:
                content = response.content.decode(response.encoding, errors='replace')
                content = content.encode('utf-8').decode('utf-8')
            else:
                content = response.text
            
            # 检查中文字符
            chinese_chars = sum(1 for c in content if '\u4e00' <= c <= '\u9fff')
            print(f"中文字符数量: {chinese_chars}")
            
            if chinese_chars > 0:
                print("✅ 编码处理成功，中文内容正常")
            else:
                print("⚠️  未检测到中文内容")
                
        except Exception as e:
            print(f"❌ 测试失败: {e}")

def main():
    """主函数"""
    print("中文网页支持测试工具")
    print("测试程序对中文网页的处理能力")
    print()
    
    # 创建测试输出目录
    if not os.path.exists("chinese_test"):
        os.makedirs("chinese_test")
        print("📁 创建测试输出目录: chinese_test")
    
    # 运行测试
    success = test_chinese_websites()
    test_encoding_detection()
    
    print("\n" + "=" * 60)
    print("测试完成!")
    print("=" * 60)
    
    if success:
        print("✅ 中文支持测试完成")
        print("📁 查看chinese_test目录中的输出文件")
    else:
        print("❌ 测试过程中遇到问题")
    
    print("💡 建议:")
    print("   1. 在浏览器中打开生成的HTML文件检查中文显示")
    print("   2. 检查文件编码是否为UTF-8")
    print("   3. 确认中文字符是否正确显示")

if __name__ == "__main__":
    main() 