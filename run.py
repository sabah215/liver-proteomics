from flask import Flask, render_template, url_for
from bioinfokit import analys, visuz
import pandas as pd 

app = Flask(__name__)

df = pd.read_csv('~/Desktop/data/Liver_Homegenate_per_mg_protein_Log2FC_Normal_NAFLD.csv')



# posts = [
#     {
#         'author': 'Corey Schafer',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'April 20, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'April 21, 2018'
#     }
# ]

@app.route('/')
@app.route('/home')
def home():
       return render_template('home.html', df=df)

if __name__ == '__main__':
       app.run(debug=True)