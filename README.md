# 个人博客系统

这是一个使用Django开发的个人博客系统，具有文章发布、评论、用户认证等功能。

## 功能特性

- 用户认证系统（登录/注册）
- 文章发布和编辑
- 图片上传功能
- 文章评论系统
- 响应式设计
- 分页功能

## 技术栈

- Python 3.x
- Django 4.2.19
- Bootstrap 5.1.3
- SQLite3数据库

## 项目结构

```
├── blog/                   # 项目主目录
│   ├── __init__.py
│   ├── settings.py        # 项目配置文件
│   ├── urls.py           # 主URL配置
│   ├── wsgi.py          # WSGI配置
│   └── asgi.py          # ASGI配置
├── blog_posts/           # 博客应用
│   ├── migrations/       # 数据库迁移文件
│   ├── templates/       # 模板文件
│   ├── admin.py        # 后台管理配置
│   ├── models.py       # 数据模型
│   ├── views.py        # 视图函数
│   └── urls.py         # 应用URL配置
├── static/              # 静态文件目录
├── media/              # 媒体文件目录
├── manage.py           # Django管理脚本
└── db.sqlite3          # SQLite数据库文件
```

## 安装步骤

1. 克隆项目到本地：
   ```bash
   git clone [项目地址]
   cd xinwen
   ```

2. 创建并激活虚拟环境（推荐）：
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. 安装依赖包：
   ```bash
   pip install django==4.2.19
   pip install Pillow  # 用于图片处理
   ```

4. 执行数据库迁移：
   ```bash
   python manage.py migrate
   ```

5. 创建超级用户（用于后台管理）：
   ```bash
   python manage.py createsuperuser
   ```
    //我创建的是test 1234
## 运行项目

1. 启动开发服务器：
   ```bash
   python manage.py runserver
   ```

2. 在浏览器中访问：
   - 博客首页：http://127.0.0.1:8000
   - 后台管理：http://127.0.0.1:8000/admin

## 使用说明

1. 后台管理
   - 使用创建的超级用户账号登录后台
   - 可以管理用户、文章和评论

2. 发布文章
   - 登录后可以点击首页的"写新文章"按钮
   - 填写标题、内容，可选择上传图片
   - 点击发布即可

3. 评论功能
   - 登录用户可以在文章详情页发表评论
   - 评论会显示发布时间和作者

## 项目配置

主要配置文件位于 `blog/settings.py`：

- `DEBUG`：调试模式开关
- `ALLOWED_HOSTS`：允许访问的主机
- `DATABASES`：数据库配置
- `STATIC_URL`/`MEDIA_URL`：静态文件和媒体文件的URL配置

## 注意事项

1. 开发环境下的DEBUG模式已开启，部署到生产环境时需要关闭
2. 项目使用SQLite数据库，适合小型应用，如需要可以切换到MySQL等数据库
3. 确保media目录具有写入权限，用于存储上传的图片