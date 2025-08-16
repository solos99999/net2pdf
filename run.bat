@echo off
chcp 65001 >nul
title 网页转PDF工具

echo ================================================
echo 网页转PDF工具
echo ================================================
echo.

:menu
echo 请选择要运行的程序:
echo 1. 完整版本 (推荐)
echo 2. 简化版本
echo 3. 安装依赖
echo 4. 退出
echo.
set /p choice=请输入选择 (1-4): 

if "%choice%"=="1" goto full_version
if "%choice%"=="2" goto simple_version
if "%choice%"=="3" goto install_deps
if "%choice%"=="4" goto exit
echo 无效选择，请重新输入
goto menu

:full_version
echo.
echo 启动完整版本...
python batch_web_to_pdf.py
goto end

:simple_version
echo.
echo 启动简化版本...
python web_to_pdf_simple.py
goto end

:install_deps
echo.
echo 启动依赖安装脚本...
python install_dependencies.py
goto end

:exit
echo 程序退出
exit /b 0

:end
echo.
echo 程序已结束，按任意键返回菜单...
pause >nul
goto menu 