#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
依赖安装脚本
自动安装网页转PDF工具所需的依赖包
"""

import subprocess
import sys
import os
import platform

def run_command(command, description):
    """运行命令并显示结果"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description}成功")
            if result.stdout:
                print(result.stdout)
        else:
            print(f"❌ {description}失败")
            if result.stderr:
                print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ {description}出错: {e}")
        return False
    return True

def check_python_version():
    """检查Python版本"""
    print("🐍 检查Python版本...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print(f"❌ Python版本过低: {version.major}.{version.minor}")
        print("   需要Python 3.7或更高版本")
        return False
    else:
        print(f"✅ Python版本: {version.major}.{version.minor}.{version.micro}")
        return True

def install_pip_packages():
    """安装pip包"""
    packages = [
        "requests>=2.25.1",
        "lxml>=4.6.3"
    ]
    
    print("\n📦 安装基础Python包...")
    for package in packages:
        if not run_command(f"pip install {package}", f"安装 {package}"):
            return False
    
    return True

def install_weasyprint():
    """安装weasyprint"""
    print("\n📄 尝试安装weasyprint...")
    
    # 先尝试直接安装
    if run_command("pip install weasyprint", "安装weasyprint"):
        return True
    
    # 如果失败，尝试使用conda
    print("\n🔄 尝试使用conda安装weasyprint...")
    if run_command("conda install -c conda-forge weasyprint -y", "使用conda安装weasyprint"):
        return True
    
    print("⚠️  weasyprint安装失败，将使用简化版本")
    return False

def install_pdfkit():
    """安装pdfkit"""
    print("\n📄 安装pdfkit...")
    if run_command("pip install pdfkit", "安装pdfkit"):
        return True
    else:
        print("⚠️  pdfkit安装失败")
        return False

def check_system_dependencies():
    """检查系统依赖"""
    system = platform.system().lower()
    
    if system == "windows":
        print("\n🖥️  检测到Windows系统")
        print("💡 提示: 如果weasyprint安装失败，请下载并安装GTK+运行时环境:")
        print("   https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases")
        
    elif system == "linux":
        print("\n🐧 检测到Linux系统")
        print("💡 提示: 如果weasyprint安装失败，请安装系统依赖:")
        print("   Ubuntu/Debian: sudo apt-get install build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info")
        print("   CentOS/RHEL: sudo yum install redhat-rpm-config python3-devel python3-pip python3-cffi libffi-devel cairo pango gdk-pixbuf2")
        
    elif system == "darwin":
        print("\n🍎 检测到macOS系统")
        print("💡 提示: 如果weasyprint安装失败，请使用Homebrew安装依赖:")
        print("   brew install cairo pango gdk-pixbuf libffi")

def main():
    """主函数"""
    print("=" * 60)
    print("网页转PDF工具 - 依赖安装脚本")
    print("=" * 60)
    
    # 检查Python版本
    if not check_python_version():
        return
    
    # 检查系统依赖
    check_system_dependencies()
    
    # 安装基础包
    if not install_pip_packages():
        print("\n❌ 基础包安装失败")
        return
    
    # 尝试安装weasyprint
    weasyprint_success = install_weasyprint()
    
    # 安装pdfkit作为备选
    pdfkit_success = install_pdfkit()
    
    print("\n" + "=" * 60)
    print("安装完成!")
    print("=" * 60)
    
    if weasyprint_success:
        print("✅ 完整版本可用: python web_to_pdf.py")
    else:
        print("⚠️  完整版本不可用，weasyprint安装失败")
    
    if pdfkit_success:
        print("✅ 简化版本可用: python web_to_pdf_simple.py")
        print("💡 注意: 简化版本需要安装wkhtmltopdf才能生成PDF")
        print("   下载地址: https://wkhtmltopdf.org/downloads.html")
    else:
        print("⚠️  简化版本不可用，pdfkit安装失败")
    
    if not weasyprint_success and not pdfkit_success:
        print("\n❌ 所有PDF生成工具都安装失败")
        print("💡 建议:")
        print("   1. 检查网络连接")
        print("   2. 安装系统依赖")
        print("   3. 使用管理员权限运行")
        print("   4. 尝试使用虚拟环境")
    
    print("\n📚 更多信息请查看README.md文件")

if __name__ == "__main__":
    main() 