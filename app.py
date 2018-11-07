from flask import Flask
from challengeSet3.random_sentence import *

app = Flask(__name__)

@app.route('/')

def hello_world():
    text_list = text_to_list('blog-text')
    return generate_sentence(text_list)


# app.run(debug=True, port=33507)

# def text_to_list(file_name):
#     return read_txt_file(file_name)
#
#
# def display_sentence(text_list):
#     return generate_sentence(text_list)

#
# if __name__ == "__main__":
#     text_list = text_to_list('blog-text')
#
#     generate_sentence(text_list)
