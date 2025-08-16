#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
网页转PDF工具使用示例
演示如何使用程序进行批量转换
"""

import os
import sys
from datetime import datetime

# 添加当前目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def example_single_conversion():
    """示例：单个网页转换"""
    print("=" * 50)
    print("示例1: 单个网页转换")
    print("=" * 50)
    
    # 优先尝试简化版本，因为它更稳定
    try:
        from web_to_pdf_simple import SimpleWebToPDF
        converter = SimpleWebToPDF()
        
        # 转换一个示例网页
        url = "https://httpbin.org/html"
        print(f"正在转换: {url}")
        
        output_path, file_type = converter.convert_url_to_pdf(url, "examples")
        print(f"✅ 转换成功: {output_path} ({file_type})")
        
    except ImportError:
        print("⚠️  简化版本不可用，尝试完整版本...")
        try:
            from web_to_pdf import WebToPDF
            converter = WebToPDF()
            
            url = "https://httpbin.org/html"
            print(f"正在转换: {url}")
            
            output_path = converter.convert_url_to_pdf(url, "examples")
            print(f"✅ 转换成功: {output_path}")
            
        except (ImportError, OSError) as e:
            print(f"❌ 完整版本也不可用: {e}")
            print("💡 建议安装GTK+运行时环境或使用简化版本")

def example_batch_conversion():
    """示例：批量网页转换"""
    print("\n" + "=" * 50)
    print("示例2: 批量网页转换")
    print("=" * 50)
    
    # 示例网址列表
    urls = [
        "https://httpbin.org/html",
        "https://httpbin.org/json",
        "https://httpbin.org/xml"
    ]
    
    # 优先尝试简化版本
    try:
        from web_to_pdf_simple import SimpleWebToPDF
        converter = SimpleWebToPDF()
        
        for i, url in enumerate(urls, 1):
            print(f"\n[{i}/{len(urls)}] 正在转换: {url}")
            try:
                output_path, file_type = converter.convert_url_to_pdf(url, "examples")
                print(f"✅ 成功: {output_path} ({file_type})")
            except Exception as e:
                print(f"❌ 失败: {e}")
                
    except ImportError:
        print("⚠️  简化版本不可用，尝试完整版本...")
        try:
            from web_to_pdf import WebToPDF
            converter = WebToPDF()
            
            for i, url in enumerate(urls, 1):
                print(f"\n[{i}/{len(urls)}] 正在转换: {url}")
                try:
                    output_path = converter.convert_url_to_pdf(url, "examples")
                    print(f"✅ 成功: {output_path}")
                except Exception as e:
                    print(f"❌ 失败: {e}")
                    
        except (ImportError, OSError) as e:
            print(f"❌ 完整版本也不可用: {e}")
            print("💡 建议安装GTK+运行时环境或使用简化版本")

def example_custom_settings():
    """示例：自定义设置"""
    print("\n" + "=" * 50)
    print("示例3: 自定义设置")
    print("=" * 50)
    
    # 优先尝试简化版本
    try:
        from web_to_pdf_simple import SimpleWebToPDF
        converter = SimpleWebToPDF()
        
        # 自定义输出目录
        custom_dir = f"custom_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        url = "https://httpbin.org/html"
        print(f"正在转换: {url}")
        print(f"输出目录: {custom_dir}")
        
        output_path, file_type = converter.convert_url_to_pdf(url, custom_dir)
        print(f"✅ 转换成功: {output_path} ({file_type})")
        
    except ImportError:
        print("⚠️  简化版本不可用，尝试完整版本...")
        try:
            from web_to_pdf import WebToPDF
            converter = WebToPDF()
            
            custom_dir = f"custom_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            
            url = "https://httpbin.org/html"
            print(f"正在转换: {url}")
            print(f"输出目录: {custom_dir}")
            
            output_path = converter.convert_url_to_pdf(url, custom_dir)
            print(f"✅ 转换成功: {output_path}")
            
        except (ImportError, OSError) as e:
            print(f"❌ 完整版本也不可用: {e}")
            print("💡 建议安装GTK+运行时环境或使用简化版本")

def main():
    """主函数"""
    print("网页转PDF工具 - 使用示例")
    print("这些示例将演示如何使用网页转PDF工具")
    print()
    
    # 创建示例输出目录
    if not os.path.exists("examples"):
        os.makedirs("examples")
        print("📁 创建示例输出目录: examples")
    
    # 运行示例
    example_single_conversion()
    example_batch_conversion()
    example_custom_settings()
    
    print("\n" + "=" * 50)
    print("示例运行完成!")
    print("=" * 50)
    print("📁 查看examples目录中的输出文件")
    print("💡 更多用法请查看README.md文件")

if __name__ == "__main__":
    main() 