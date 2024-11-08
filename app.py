from flask import Flask, render_template, request, flash
import sys
import os

# Asegura que Python pueda encontrar la carpeta 'src'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
from src.functionalities.rle_compression import rle_encode, rle_decode, RLECompressionError, RLECompressionZeroCountError, RLECompressionNoneError, RLECompressionDictError, RLECompressionIntegerError, RLECompressionListError, RLECompressionNegativeValueError
import sys
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'


@app.route('/')
def index():
    return render_template('index.html', result_text=None)

@app.route('/compress', methods=['POST'])
def compress_text():
    text_to_compress = request.form.get('text_to_compress')
    
    if not text_to_compress:
        flash('Por favor, ingrese el texto para comprimir')
        return render_template('index.html', result_text=None)

    try:
        compressed_text = rle_encode(text_to_compress)
        flash('Texto comprimido exitosamente.')
        return render_template('index.html', result_text=compressed_text)
    except (RLECompressionNoneError, RLECompressionIntegerError, RLECompressionListError,
            RLECompressionDictError, RLECompressionNegativeValueError, RLECompressionZeroCountError) as e:
        flash(str(e))
        return render_template('index.html', result_text=None)

@app.route('/decompress', methods=['POST'])
def decompress_text():
    text_to_decompress = request.form.get('text_to_decompress')

    if not text_to_decompress:
        flash('Por favor, ingrese el texto para descomprimir')
        return render_template('index.html', result_text=None)

    try:
        decompressed_text = rle_decode(text_to_decompress)
        flash('Texto descomprimido exitosamente.')
        return render_template('index.html', result_text=decompressed_text)
    except (RLECompressionNoneError, RLECompressionIntegerError, RLECompressionNegativeValueError,
            RLECompressionZeroCountError) as e:
        flash(str(e))
        return render_template('index.html', result_text=None)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
