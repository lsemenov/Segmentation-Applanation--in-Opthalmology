from flask import Flask, url_for, request, redirect, render_template
from werkzeug.utils import secure_filename
from main.Model import ApplanationSegmentation
import matplotlib.image as mpimage
import numpy as np
from main import preprocess
import torch
from PIL import Image
import os

# определили экземпляр класса flask
app = Flask(__name__)

# ограничение объема файла в байтах
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
UPLOAD_FOLDER = "static/images/"
RELATIVE_FILE_PATH = "static/images"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
device = torch.device("cpu")
# загрузка модели
model = ApplanationSegmentation.load_from_checkpoint("epoch_15_step_18847.ckpt")

# главная страница
@app.route("/index")
@app.route('/')
def main_page():
    # возвращает шаблон из папки templates
    return render_template("base.html")


# загрузка изображения и отображение
@app.route('/upload', methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        # это поле ассоциировано загруженным на сервер изображением
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('show',
                                    filename=filename))
    return ''


@app.route('/<filename>')
def show(filename):
    path = RELATIVE_FILE_PATH + '/' + str(filename)
    return render_template('show.html', name=path)


@app.route('/<path:path>', methods=["POST", "GET"])
def segmentation(path):
    path_mask = os.path.join(app.config['UPLOAD_FOLDER'], "segmentation" + ".bmp")
    path_overlay = os.path.join(app.config['UPLOAD_FOLDER'], "overlay" + ".bmp")

    def overlay_builder(path_mask, path_overlay, img_test):
        data = Image.open(path).convert("RGB")
        width = data.size[0]
        height = data.size[1]
        mask = Image.open(path_mask).convert("RGB")
        mask = mask.resize((width, height))
        mask = np.array(mask)

        for i in range(height):
            for j in range(width):
                if mask[i, j].sum() == 0:
                    mask[i, j] = [127, 255, 0]

        mask = Image.fromarray(np.uint8(mask)).convert('RGB')
        overlay = Image.blend(data, mask, 0.2)
        overlay.save(path_overlay, quality=100)

    # оригинальное изображение
    data = Image.open(path).convert("L")

    data = data.resize((256, 256))
    data = np.array(data)
    standardized_scan = preprocess.standardize(preprocess.normalize(data))

    # Got 3D input, but bilinear mode needs 4D input
    data = torch.tensor(standardized_scan).to(device).unsqueeze(0).unsqueeze(0).float()

    # сегментированное изображение
    with torch.no_grad():
        pred = model(data)
    pred = pred.cpu().numpy()

    img_test = np.array(pred)
    img_test = np.squeeze(img_test)

    mpimage.imsave(path_mask, img_test, cmap="Greys")
    overlay_builder(path_mask, path_overlay, img_test)
    del img_test

    path = path.replace("static/images/", "")

    return render_template('segmentation.html', path=path, path_overlay=path_overlay)


# запуск flask приложения
if __name__ == '__main__':
    # app.run(host, port, debug, options)
    # запуск локального веб-сервера 127.0.0.1:5000
    # доступ только с локальной машины
    # host='0.0.0.0' - позволит принимать запросы с интерфейса, поделюченного к обшедоступной сети
    # port=8080
    app.run(debug=True, host='0.0.0.0', port=os.environ['PORT'])
