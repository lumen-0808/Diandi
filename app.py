
from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px

import csv, re, operator
# from textblob import TextBlob

app = Flask(__name__)

person = {
    'first_name': 'Tingyuan',
    'address' : 'Hubei Normal University',
    # 'job': 'Student',
    'tel': '15549864073',
    'email': 'ing0909@outlook.com',
    'capsname':'个人简历',
    'description' : 'I spend most of my time on study,i have passed CET4/6 . and ihave acquired basic knowledge of my major during my schooltime. ',
    'qq': '1373932',
    'wechat': 'huuubb',
    'github': 'https://github.com/lumen-0808',

	'languages' : ['HTNL','CSS (Stylus)', 'JavaScript & jQuery', 'Killer Taste'],
	'education' : ['湖北师范大学','XXXhigh school',  'XXXmiddle school'],

    'experiences' : [
        {
            'NO' : 'Job #1',
            'light': 'First Experience description',
            'justified' : 'Plaid gentrify put a bird on it, pickled XOXO farm-to-table irony raw denim messenger bag leggings. Hoodie PBR&B photo booth, vegan chillwave meh paleo freegan ramps. Letterpress shabby chic fixie semiotics. Meditation sriracha banjo pour-over. Gochujang pickled hashtag mixtape cred chambray. Freegan microdosing VHS, 90s bicycle rights aesthetic hella PBR&B.',
           
        },
        {
        	'NO' : ' Job #2',
        	'light': 'First Experience description',
        	'justified' : 'Beard before they sold out photo booth distillery health goth. Hammock franzen green juice meggings, ethical sriracha tattooed schlitz mixtape man bun stumptown swag whatever distillery blog. Affogato iPhone normcore, meggings actually direct trade lomo plaid franzen shoreditch. Photo booth pug paleo austin, pour-over banh mi scenester vice food truck slow-carb. Street art kogi normcore, vice everyday carry crucifix thundercats man bun raw denim echo park pork belly helvetica vinyl. ',
           
        }
    ]

}


@app.route('/')
def cv(person=person):
	return render_template('index2.html',person=person)



if __name__ == '__main__':
  app.run(debug= True,port=5000,threaded=True)
