from flask import Flask, Response, request

app = Flask(__name__)

video_frame = None  # Global variable to hold the latest video frame


@app.route('/upload', methods=['POST'])
def upload_frame():
    global video_frame
    video_frame = request.data  # Get the video frame sent by the sender
    return "Frame received", 200

@app.route('/stream')
def stream_video():
    def generate():
        try:
            while True:
                if video_frame:
                    yield (b'--frame\r\n'
                           b'Content-Type: image/jpeg\r\n\r\n' + video_frame + b'\r\n')
                else:
                    time.sleep(0.1)  # Introduce a small delay to avoid busy-waiting
        except GeneratorExit:
            print("Client disconnected from the stream")
        except Exception as e:
            print(f"Error in streaming: {e}")

    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')




if __name__ == "__main__":
    app.run(port=10000)
