from flask import Flask
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('./static/people.csv')

# class User(db.Model):
#     # 表名
#     __tablename__ = 'users'

#     # 字段
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(32), unique=True)
#     state = db.Column(db.String(32))
#     salary = db.Column(db.String(32))
#     grade = db.Column(db.String(32))
#     room = db.Column(db.String(32))
#     telnum = db.Column(db.String(32))
#     picture = db.Column(db.String(32))
#     keywords = db.Column(db.String(300))

#     def save(self):
#         db.session.add(self)
#         db.session.commit()

        
@app.route('/', methods=['GET', 'POST'])
def index():
    # 创建自定义的表单类
    # author_form = AuthorForm()

    '''
    验证逻辑:
    1. 调用WTF的函数实现验证
    2. 验证通过获取数据
    3. 判断作者是否存在
    4. 如果作者存在, 判断书籍是否存在, 没有重复书籍就添加数据, 如果重复就提示错误
    5. 如果作者不存在, 添加作者和书籍
    6. 验证不通过就提示错误
    '''
    # 查询所有的作者信息, 让信息传递给模板
#     people = User.query.all()
#     form = peopleForm()
#     form2 = UpForm()
#     print(form.data)
    return render_template('idx.html', df=df)


# @app.route("/")
# def hello():
#     return "I wanna shoot out this fkin world"
