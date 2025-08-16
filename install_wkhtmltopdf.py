#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动下载和安装wkhtmltopdf
用于完成PDF生成功能
"""

import os
import sys
import platform
import subprocess
import zipfile
import requests
from pathlib import Path

def get_system_info():
    """获取系统信息"""
    system = platform.system().lower()
    machine = platform.machine().lower()
    
    if system == "windows":
        if "64" in machine or "x86_64" in machine:
            return "windows", "64"
        else:
            return "windows", "32"
    elif system == "linux":
        if "64" in machine or "x86_64" in machine:
            return "linux", "64"
        else:
            return "linux", "32"
    elif system == "darwin":
        return "macos", "64"
    else:
        return "unknown", "64"

def get_download_url():
    """获取下载URL"""
    system, arch = get_system_info()
    
    base_url = "https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1"
    
    if system == "windows":
        if arch == "64":
            return f"{base_url}/wkhtmltox-0.12.6-1.msvc2015-win64.exe"
        else:
            return f"{base_url}/wkhtmltox-0.12.6-1.msvc2015-win32.exe"
    elif system == "linux":
        if arch == "64":
            return f"{base_url}/wkhtmltox_0.12.6-1.bionic_amd64.deb"
        else:
            return f"{base_url}/wkhtmltox_0.12.6-1.bionic_i386.deb"
    elif system == "macos":
        return f"{base_url}/wkhtmltox-0.12.6-1.macos-cocoa.pkg"
    else:
        return None

def download_file(url, filename):
    """下载文件"""
    print(f"正在下载: {url}")
    print(f"保存到: {filename}")
    
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        downloaded = 0
        
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total_size > 0:
                        percent = (downloaded / total_size) * 100
                        print(f"\r下载进度: {percent:.1f}%", end='', flush=True)
        
        print(f"\n✅ 下载完成: {filename}")
        return True
        
    except Exception as e:
        print(f"\n❌ 下载失败: {e}")
        return False

def install_windows(installer_path):
    """Windows安装"""
    print("正在安装wkhtmltopdf...")
    try:
        # 静默安装
        result = subprocess.run([installer_path, '/S'], 
                              capture_output=True, text=True, timeout=300)
        if result.returncode == 0:
            print("✅ 安装成功")
            return True
        else:
            print(f"❌ 安装失败: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ 安装出错: {e}")
        return False

def install_linux(deb_path):
    """Linux安装"""
    print("正在安装wkhtmltopdf...")
    try:
        result = subprocess.run(['sudo', 'dpkg', '-i', deb_path], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ 安装成功")
            return True
        else:
            print(f"❌ 安装失败: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ 安装出错: {e}")
        return False

def install_macos(pkg_path):
    """macOS安装"""
    print("正在安装wkhtmltopdf...")
    try:
        result = subprocess.run(['sudo', 'installer', '-pkg', pkg_path, '-target', '/'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ 安装成功")
            return True
        else:
            print(f"❌ 安装失败: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ 安装出错: {e}")
        return False

def verify_installation():
    """验证安装"""
    print("验证安装...")
    try:
        result = subprocess.run(['wkhtmltopdf', '--version'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"✅ wkhtmltopdf安装成功")
            print(f"版本信息: {result.stdout.strip()}")
            return True
        else:
            print("❌ wkhtmltopdf未正确安装")
            return False
    except FileNotFoundError:
        print("❌ wkhtmltopdf未找到，请检查安装")
        return False
    except Exception as e:
        print(f"❌ 验证失败: {e}")
        return False

def main():
    """主函数"""
    print("=" * 60)
    print("wkhtmltopdf 自动安装工具")
    print("=" * 60)
    
    # 检查是否已安装
    if verify_installation():
        print("✅ wkhtmltopdf已经安装，无需重复安装")
        return
    
    # 获取系统信息
    system, arch = get_system_info()
    print(f"检测到系统: {system} {arch}位")
    
    # 获取下载URL
    download_url = get_download_url()
    if not download_url:
        print("❌ 不支持的操作系统")
        return
    
    # 创建下载目录
    download_dir = Path("downloads")
    download_dir.mkdir(exist_ok=True)
    
    # 下载文件名
    filename = download_url.split('/')[-1]
    filepath = download_dir / filename
    
    # 下载文件
    if not download_file(download_url, filepath):
        return
    
    # 安装
    print("\n开始安装...")
    success = False
    
    if system == "windows":
        success = install_windows(str(filepath))
    elif system == "linux":
        success = install_linux(str(filepath))
    elif system == "macos":
        success = install_macos(str(filepath))
    
    if success:
        # 验证安装
        if verify_installation():
            print("\n🎉 安装完成！现在可以使用PDF生成功能了")
            print("💡 运行 python web_to_pdf_simple.py 来测试PDF生成")
        else:
            print("\n⚠️  安装可能不完整，请手动验证")
    else:
        print("\n❌ 安装失败")
        print("💡 请手动下载安装: https://wkhtmltopdf.org/downloads.html")

if __name__ == "__main__":
    main() 