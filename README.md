# MusicStream - 在线音乐平台

MusicStream是一个基于Django开发的在线音乐播放平台，支持用户注册登录、音乐播放、搜索、评论、排行榜等完整功能。项目采用MTV架构，包含6个独立应用模块，提供完整的音乐流媒体服务。

## 功能特性

### 核心功能
- **用户系统**：自定义用户模型，支持QQ、微信、手机号、头像等扩展字段
- **音乐管理**：歌曲分类、歌曲信息管理、动态统计（播放次数、搜索次数、下载次数）
- **音乐播放**：在线播放、下载功能、播放列表管理
- **搜索功能**：多字段模糊搜索（歌曲名、歌手、专辑），搜索行为统计
- **评论系统**：歌曲评论、评论分页展示
- **排行榜**：按分类展示热门歌曲，基于播放次数排序
- **首页推荐**：新歌推荐、热门歌曲、热门专辑展示

### 技术特性
- 响应式前端设计，支持移动端访问
- 文件上传处理（音乐文件、图片、歌词文件）
- 会话管理，播放列表使用session存储
- 后台管理界面深度定制
- 数据统计与分析

## 技术栈

### 后端
- **框架**：Django 4.2+
- **语言**：Python 3.8+
- **数据库**：MySQL
- **架构**：MTV模式，6个独立应用模块

### 前端
- **模板引擎**：Django Templates
- **样式**：CSS3
- **脚本**：JavaScript
- **响应式设计**：Bootstrap兼容

### 开发工具
- 数据库迁移：Django Migrations
- 静态文件管理：Django Staticfiles
- 媒体文件管理：Django Media
- 用户认证：Django Auth（自定义扩展）

## 项目结构

```
music-main/
├── manage.py                    # Django项目管理脚本
├── requirements.txt             # Python依赖包
├── README.md                    # 项目说明文档
├── music/                       # 主应用配置
│   ├── settings.py              # 项目配置
│   ├── urls.py                  # 主路由配置
│   ├── wsgi.py                  # WSGI配置
│   └── asgi.py                  # ASGI配置
├── index/                       # 首页应用
│   ├── models.py                # 核心数据模型
│   ├── views.py                 # 首页视图
│   ├── urls.py                  # 首页路由
│   └── tests.py                 # 测试文件
├── ranking/                     # 排行榜应用
├── user/                        # 用户管理应用
│   ├── models.py                # 自定义用户模型
│   ├── views.py                 # 用户视图
│   └── urls.py                  # 用户路由
├── play/                        # 播放应用
│   ├── views.py                 # 播放视图
│   └── urls.py                  # 播放路由
├── search/                      # 搜索应用
├── comment/                     # 评论应用
├── templates/                   # HTML模板文件
│   ├── index.html               # 首页模板
│   ├── login.html               # 登录注册模板
│   ├── play.html                # 播放页面模板
│   ├── search.html              # 搜索页面模板
│   ├── comment.html             # 评论页面模板
│   ├── ranking.html             # 排行榜模板
│   ├── home.html                # 个人中心模板
│   └── 404.html                 # 错误页面模板
└── publicStatic/                # 静态文件目录
    └── image/                   # 图片资源
```

## 数据模型

### 核心模型 (index/models.py)
- **Label**: 歌曲分类标签
- **Song**: 歌曲信息（歌名、歌手、时长、专辑、语种、类型、发行时间、图片、歌词、文件）
- **Dynamic**: 歌曲动态数据（播放次数、搜索次数、下载次数）
- **Comment**: 歌曲评论

### 用户模型 (user/models.py)
- **MyUser**: 自定义用户模型，继承AbstractUser，扩展了QQ、微信、手机号、头像字段

## 安装与配置

### 环境要求
- Python 3.8+
- MySQL 5.7+
- pip (Python包管理工具)

### 安装步骤

1. **克隆项目**
   ```bash
   git clone <repository-url>
   cd music-main
   ```

2. **创建虚拟环境**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

4. **配置数据库**
   - 创建MySQL数据库
   ```sql
   CREATE DATABASE music_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```
   - 修改数据库配置（可选）：编辑 `music/settings.py` 中的DATABASES配置

5. **应用数据库迁移**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **创建超级用户**
   ```bash
   python manage.py createsuperuser
   ```

7. **运行开发服务器**
   ```bash
   python manage.py runserver
   ```

8. **访问应用**
   - 网站首页: http://127.0.0.1:8000/
   - 后台管理: http://127.0.0.1:8000/admin/

## 使用指南

### 用户功能
1. **注册登录**：支持用户名、手机号登录
2. **个人中心**：查看和修改个人信息
3. **音乐播放**：点击歌曲播放，支持播放列表
4. **搜索音乐**：在搜索框输入关键词搜索
5. **发表评论**：在歌曲页面发表评论
6. **查看排行榜**：浏览热门歌曲排行榜

### 管理员功能
1. **歌曲管理**：添加、编辑、删除歌曲信息
2. **分类管理**：管理歌曲分类标签
3. **用户管理**：管理用户账户
4. **评论管理**：审核和管理歌曲评论
5. **数据统计**：查看歌曲播放、搜索、下载统计数据

## API接口

### 主要接口
- `GET /` - 首页
- `GET /play/<int:id>/` - 播放歌曲
- `GET /play/<int:id>/download/` - 下载歌曲
- `GET /search/` - 搜索歌曲
- `GET /comment/` - 歌曲评论
- `GET /ranking.html` - 排行榜
- `GET /user/` - 用户相关功能

## 开发说明

### 代码规范
- 遵循PEP 8 Python代码规范
- 使用Django最佳实践
- 重要功能添加单元测试

### 扩展开发
1. **添加新功能**：创建新的Django应用
2. **修改模型**：更新models.py后运行makemigrations和migrate
3. **添加模板**：在templates目录创建HTML文件
4. **添加静态资源**：在publicStatic目录添加CSS/JS/图片文件

## 测试

项目包含基本的测试框架，可使用以下命令运行测试：

```bash
# 运行所有测试
python manage.py test

# 运行特定应用测试
python manage.py test index
python manage.py test user
```

## 部署

### 生产环境部署建议
1. **使用环境变量**：将SECRET_KEY、数据库密码等敏感信息存储在环境变量中
2. **配置Web服务器**：使用Nginx + Gunicorn部署
3. **静态文件服务**：配置CDN或使用Nginx服务静态文件
4. **数据库优化**：配置数据库连接池，添加索引
5. **缓存配置**：添加Redis缓存提升性能
6. **安全配置**：配置HTTPS，添加安全头部

### Docker部署（建议）
```bash
# 构建Docker镜像
docker build -t musicstream .

# 运行容器
docker run -d -p 8000:8000 --name musicstream-app musicstream
```

## 项目亮点

### 技术亮点
1. **全栈开发**：完整的Django MTV架构实现
2. **自定义用户系统**：扩展Django原生用户模型，支持多种登录方式
3. **文件处理**：音乐文件、图片上传、存储管理
4. **搜索优化**：多字段模糊搜索，搜索行为统计
5. **数据统计**：实时统计播放次数、搜索次数、下载次数
6. **后台管理**：Django Admin深度定制，数据可视化

### 业务亮点
1. **完整功能**：涵盖音乐平台所有核心功能
2. **用户体验**：响应式设计，播放列表管理
3. **数据驱动**：基于用户行为的数据统计与分析
4. **可扩展性**：模块化设计，易于功能扩展

## 贡献指南

欢迎贡献代码！请遵循以下步骤：

1. Fork项目仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送分支 (`git push origin feature/AmazingFeature`)
5. 开启Pull Request

## 许可证

本项目仅供学习交流使用。

## 联系方式

如有问题或建议，请通过以下方式联系：
- 项目仓库：[GitHub Repository]
- 问题反馈：[Issues Page]

---

**最后更新**: 2026-03-10