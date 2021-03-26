from flask import Flask


# server static files with folder
app =Flask(__name__,static_url_path='',static_folder='static')
