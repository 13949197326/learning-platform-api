from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 示例数据
MODULES = [
    {
        "id": 1,
        "title": "字母学习",
        "icon": "A",
        "description": "学习英语字母的读写",
        "progress": 0.7
    },
    {
        "id": 2,
        "title": "基础词汇",
        "icon": "B",
        "description": "学习基本英语单词",
        "progress": 0.4
    }
]

@app.route('/api/modules', methods=['GET'])
def get_modules():
    """获取所有学习模块"""
    return jsonify(MODULES)

@app.route('/api/progress/<int:user_id>', methods=['GET'])
def get_progress(user_id):
    """获取用户学习进度"""
    return jsonify({"progress": 0.5})

if __name__ == '__main__':
    app.run(debug=True) 