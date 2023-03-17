from flask import Flask, Response, render_template
import cv2

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():    
    return render_template('index.html')
def get_frame():
    camera_port=0

    camera=cv2.VideoCapture(camera_port)
    
  


    while True:
        retval, im = camera.read()

        imgencode = cv2.imencode('.jpg', im)[1] 


        stringData=imgencode.tostring()
   
        yield (b'--frame\r\n'
               b'Content-Type: text/plain\r\n\r\n' + stringData+ b'\r\n')
    del(camera)
@app.route('/video_feed')
def video_feed():
    
    return Response(get_frame(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    app.run(host='192.168.1.2', debug=True, threaded=True)
    

