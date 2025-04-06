# 小学英语学习平台 API

这是小学英语学习平台的后端API服务。

## 功能特点

- 用户进度管理
- 学习模块数据
- 题目管理
- 学习记录追踪

## 快速开始

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 运行服务：
```bash
python app/api.py
```

## API接口

### 获取学习模块
```
GET /api/modules
```

### 获取用户进度
```
GET /api/progress/<user_id>
```

## 开发说明

- Python 3.10+
- Flask框架
- RESTful API设计
