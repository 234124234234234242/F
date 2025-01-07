from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 用于flash消息

# 确保 responses.json 文件存在
if not os.path.exists('responses.json'):
    with open('responses.json', 'w', encoding='utf-8') as f:
        f.write('')

# 问卷问题
survey_questions = [
    {"id": 1, "question": "曾涛的手机号码是什么?", "type": "text"},
    {"id": 2, "question": "曾涛的性别是什么？", "type": "radio", "options": ["男", "女"]},
    {"id": 3, "question": "曾涛是Gay吗？", "type": "radio", "options": ["是", "否", "不确定"]},
    {"id": 4, "question": "曾涛的年龄是多少？", "type": "number"},
    {"id": 5, "question": "曾涛的职业是什么？", "type": "text"},
]

@app.route('/', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        try:
            answers = {}
            # 检查所有问题是否都已回答
            all_answered = True
            for question in survey_questions:
                answer = request.form.get(str(question['id']))
                if not answer:
                    all_answered = False
                    break
                answers[question['id']] = answer
            
            if not all_answered:
                flash('请回答所有问题后再提交！')
                return redirect(url_for('survey'))
            
            # 保存答案
            with open('responses.json', 'a', encoding='utf-8') as f:
                json.dump(answers, f, ensure_ascii=False)
                f.write('\n')
            return render_template('thank_you.html')
        except Exception as e:
            print(f"Error: {str(e)}")  # 添加错误日志
            flash('提交失败，请重试！')
            return redirect(url_for('survey'))
    
    return render_template('survey.html', questions=survey_questions)

if __name__ == '__main__':
    try:
        app.run(host='127.0.0.1', port=5001, debug=True)
    except Exception as e:
        print(f"启动服务器时出错: {str(e)}") 