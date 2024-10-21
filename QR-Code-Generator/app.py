from flask import Flask, request, render_template, url_for
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_code_img = None
    if request.method == 'POST':
        data = request.form['data']
        print(f"Form submitted with data: {data}")  # Debugging statement
        if not data:
            return "No data provided", 400

        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=70,
                border=2,
            )
            qr.add_data(data)
            qr.make(fit=True)

            img = qr.make_image(fill='black', back_color='white')

            buffer = BytesIO()
            img.save(buffer)
            buffer.seek(0)

            img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
            qr_code_img = f"data:image/png;base64,{img_str}"
            print(f"Generated QR code (first 30 chars): {qr_code_img[:30]}...")  # Debugging statement
        except Exception as e:
            print(f"Error generating QR code: {e}")

    return render_template('index.html', qr_code_img=qr_code_img)

if __name__ == '__main__':
    app.run(debug=True)
