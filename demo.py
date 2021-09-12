import nltk
import sys, string, os,werkzeug,subprocess
import requests
from flask import Flask, render_template, flash,request,current_app
from nltk.tokenize import  word_tokenize
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField


# App config.
DEBUG = True
app = Flask(__name__,template_folder='template')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
	name = TextField('Name:', validators=[validators.required()])
	@app.route("/", methods=['GET', 'POST'])
	def hello():
		form = ReusableForm(request.form)
	
		
		if request.method == 'POST':
			name = request.form['text']
			tokenz=word_tokenize(name)
			out_str=[]
			f=open("test.txt","w")
			out_str = "\n".join(tokenz)
			out_str1=f.writelines(out_str)
			f.close()
			os.system("./tnt corpus_finalised test.txt > out")
                	#.0subprocess.Popen("crf_test -m model test.txt -o out1")
			with open("out","r") as f1:
				with open("outt","w+") as f2:
					text1=f1.read().split("\n")
					for i in range(len(text1)):
						if not text1[i].startswith("%"):
							f2.write(text1[i])
							f2.write('\n')
				f2.close()
				with open("outt","r") as f2:
					flash(f2.read())
                        

					
       		#flash(tokenz) 
		#flash(raw)
		return render_template('file.html', form=form)

if __name__ == "__main__":
    app.run()
   
