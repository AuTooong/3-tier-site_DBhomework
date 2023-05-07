import time

import mediapipe as mp
import pandas as pd
import pybase64
from flask import Flask, request, redirect, render_template, jsonify, send_file, make_response
from werkzeug.utils import secure_filename

from ball_speed_detect import blob2,calc_ball_speed
from calibration import undistortion
from cutBall import cutball
from function import *
from pred_RPM_pred_ip import pred
from cutBall import cutball
import gzip

UPLOAD_FOLDER = './file/uploded_video'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'asdsadasd'
# app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024
# path = 'C://Users//Ricky//PycharmProjects//server//file//uploded_video//t.txt'

DO_BODY_DETECT = False
DEBUG = 1


@app.route('/')
def index():
    return render_template('index.html')


MEDIA_PATH = './file/uploded_video'


@app.route('/download/<vid_name>')
def serve_video(vid_name):
    vid_path = os.path.join(MEDIA_PATH, vid_name)
    resp = make_response(send_file(vid_path, 'video/mp4'))
    resp.headers['Content-Disposition'] = 'inline'
    return resp


ALLOWED_EXTENSIONS = {'mp4', 'mov', 'avi'}
def pred_spinrate(video_path):
    ball_to_line_img = cutball(video_path)
    df = get_dataframe(ball_to_line_img)
    pred_spinrate = pred(df)
    return (pred_spinrate)
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    start_time = time.perf_counter()
    print("**")
    print("uploading data...")
    print("server accept mime: ", request.accept_mimetypes)  # /*
    print("client send mime: ", request.mimetype)  # video/quicktime
    print("data {} bytes".format(len(request.data)))
    print(type(request.data))

    if 'video' not in request.files:
        return redirect(request.url)

    file = request.files['video']

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        end_time = time.perf_counter()
        print('blob processing time', end_time - start_time, 's')
        spinrate = pred_spinrate(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # spinrate = 1832.6
        # ballspeed = 92.4
        data_return = {"RPM": int(spinrate)}

        time.sleep(5)
        return jsonify(data_return)

    else:
        return redirect(request.url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
