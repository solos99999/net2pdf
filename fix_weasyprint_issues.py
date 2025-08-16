#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WeasyPrint 问题修复脚本
解决WeasyPrint在Windows上的依赖问题
"""

import os
import sys
import subprocess
import platform
import requests
import zipfile
import shutil
from pathlib import Path

def print_header():
    """打印标题"""
    print("=" * 60)
    print("WeasyPrint 问题修复工具")
    print("=" * 60)
    print()

def check_system():
    """检查系统信息"""
    system = platform.system()
    print(f"检测到系统: {system}")
    
    if system != "Windows":
        print("此脚本主要用于Windows系统")
        print("Linux/macOS用户请参考官方文档:")
        print("https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation")
        return False
    
    return True

def download_gtk_runtime():
    """下载GTK+运行时环境"""
    print("正在下载GTK+运行时环境...")
    
    # GTK+运行时环境下载链接（更新为最新版本）
    gtk_url = "https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases/download/2023-12-30/gtk3-runtime-3.24.37-win64.exe"
    
    try:
        # 创建下载目录
        download_dir = Path("downloads")
        download_dir.mkdir(exist_ok=True)
        
        installer_path = download_dir / "gtk3-runtime-installer.exe"
        
        print(f"下载地址: {gtk_url}")
        print(f"保存位置: {installer_path}")
        
        # 下载文件
        response = requests.get(gtk_url, stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        downloaded = 0
        
        with open(installer_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total_size > 0:
                        percent = (downloaded / total_size) * 100
                        print(f"\r下载进度: {percent:.1f}%", end='', flush=True)
        
        print(f"\n✅ 下载完成: {installer_path}")
        return installer_path
        
    except Exception as e:
        print(f"\n❌ 下载失败: {e}")
        return None

def install_gtk_runtime(installer_path):
    """安装GTK+运行时环境"""
    print(f"\n正在安装GTK+运行时环境...")
    print(f"安装程序: {installer_path}")
    
    try:
        # 静默安装GTK+运行时环境
        result = subprocess.run([
            str(installer_path), 
            '/S',  # 静默安装
            '/D=C:\\GTK3'  # 安装到C:\GTK3
        ], capture_output=True, text=True, timeout=300)
        
        if result.returncode == 0:
            print("✅ GTK+运行时环境安装成功")
            return True
        else:
            print(f"❌ 安装失败: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ 安装出错: {e}")
        return False

def test_weasyprint():
    """测试WeasyPrint是否正常工作"""
    print("\n正在测试WeasyPrint...")
    
    try:
        import weasyprint
        print("✅ WeasyPrint导入成功")
        
        # 创建测试HTML
        test_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>WeasyPrint Test</title>
        </head>
        <body>
            <h1>WeasyPrint 测试</h1>
            <p>如果您能看到这个PDF，说明WeasyPrint工作正常！</p>
            <p>If you can see this PDF, WeasyPrint is working correctly!</p>
        </body>
        </html>
        """
        
        # 生成测试PDF
        test_pdf = "weasyprint_test.pdf"
        html = weasyprint.HTML(string=test_html)
        html.write_pdf(test_pdf)
        
        if os.path.exists(test_pdf):
            file_size = os.path.getsize(test_pdf) / 1024
            print(f"✅ PDF生成成功: {test_pdf} ({file_size:.2f} KB)")
            
            # 清理测试文件
            os.remove(test_pdf)
            return True
        else:
            print("❌ PDF生成失败")
            return False
            
    except ImportError as e:
        print(f"❌ WeasyPrint导入失败: {e}")
        return False
    except Exception as e:
        print(f"❌ WeasyPrint测试失败: {e}")
        return False

def provide_alternative_solutions():
    """提供替代解决方案"""
    print("\n" + "=" * 60)
    print("替代解决方案")
    print("=" * 60)
    
    print("\n如果WeasyPrint仍然无法工作，您可以：")
    print()
    print("1. 🎯 使用简化版本（推荐）")
    print("   python web_to_pdf_simple.py")
    print("   这个版本使用pdfkit，依赖更少，更稳定")
    print()
    print("2. 🔧 手动安装GTK+运行时环境")
    print("   下载地址: https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases")
    print("   下载最新版本的gtk3-runtime-*.exe并安装")
    print()
    print("3. 🐍 使用conda环境")
    print("   conda create -n weasyprint python=3.9")
    print("   conda activate weasyprint")
    print("   conda install -c conda-forge weasyprint")
    print()
    print("4. 📦 使用Docker")
    print("   docker run --rm -v $(pwd):/app weasyprint weasyprint input.html output.pdf")
    print()
    print("5. 🌐 使用在线服务")
    print("   如果只是偶尔需要转换，可以使用在线PDF转换服务")

def main():
    """主函数"""
    print_header()
    
    if not check_system():
        return
    
    print("WeasyPrint在Windows上需要GTK+运行时环境才能正常工作。")
    print("此脚本将帮助您自动下载和安装所需的依赖。")
    print()
    
    # 首先测试WeasyPrint是否已经工作
    if test_weasyprint():
        print("\n🎉 WeasyPrint已经正常工作！")
        print("您可以直接使用完整版本：")
        print("python web_to_pdf.py")
        return
    
    print("WeasyPrint需要安装GTK+运行时环境...")
    print()
    
    # 下载GTK+运行时环境
    installer_path = download_gtk_runtime()
    if not installer_path:
        print("无法下载GTK+运行时环境")
        provide_alternative_solutions()
        return
    
    # 安装GTK+运行时环境
    if install_gtk_runtime(installer_path):
        print("\n正在重新测试WeasyPrint...")
        
        # 重新测试WeasyPrint
        if test_weasyprint():
            print("\n🎉 修复成功！WeasyPrint现在可以正常工作了")
            print("您可以使用完整版本：")
            print("python web_to_pdf.py")
        else:
            print("\n⚠️  WeasyPrint仍然无法工作")
            provide_alternative_solutions()
    else:
        print("\n❌ GTK+运行时环境安装失败")
        provide_alternative_solutions()

if __name__ == "__main__":
    main() 