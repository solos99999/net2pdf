# 更新日志

## [1.0.0] - 2025-08-16

### 🎉 首次发布

#### ✨ 新增功能
- **基础网页转PDF功能**
  - 支持单个网页转换为PDF
  - 支持HTML文件保存
  - 自动编码检测和转换

- **中文支持优化**
  - 智能编码检测（UTF-8, GBK, GB2312等）
  - 中文字体优化显示
  - 自动添加meta标签

- **批量处理功能**
  - 从网页中提取链接
  - 用户选择链接
  - 批量转换为PDF

- **多种版本支持**
  - 简化版本（pdfkit）
  - 完整版本（weasyprint）
  - 增强版本（优化中文）
  - 批量版本（批量处理）

#### 🛠️ 工具和脚本
- 自动依赖安装脚本
- wkhtmltopdf自动下载安装
- Windows批处理脚本
- 中文支持测试脚本
- PDF生成测试脚本

#### 📚 文档
- 完整的中文说明文档
- 英文说明文档
- 项目结构说明
- 使用示例

#### 🔧 技术特性
- 跨平台支持（Windows, Linux, macOS）
- 完善的错误处理
- 详细的日志记录
- 用户友好的交互界面

#### 📦 依赖包
- requests>=2.25.1
- pdfkit>=1.0.0
- beautifulsoup4>=4.9.0
- lxml>=4.6.3
- weasyprint>=54.0
- cairocffi>=1.2.0

## 计划中的功能

### 🚀 未来版本计划

#### v1.1.0
- [ ] 支持更多输出格式（EPUB, MOBI）
- [ ] 添加GUI界面
- [ ] 支持自定义CSS样式
- [ ] 添加进度条显示

#### v1.2.0
- [ ] 支持JavaScript渲染
- [ ] 添加代理支持
- [ ] 支持登录认证
- [ ] 添加定时任务功能

#### v2.0.0
- [ ] Web界面版本
- [ ] API接口支持
- [ ] 云端转换服务
- [ ] 移动端支持

## 贡献指南

欢迎提交Issue和Pull Request来改进这个项目！

### 如何贡献
1. Fork 这个项目
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。 