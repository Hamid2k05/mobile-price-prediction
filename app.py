
from flask import Flask, request, render_template_string
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open('mobile_price_model.pkl', 'rb'))

html = '''

<!DOCTYPE html>
<html>

<head>
    <title>Mobile Price Prediction</title>
</head>

<body style="font-family: Arial; text-align:center; margin-top:40px;">

    <h1>Mobile Price Prediction System</h1>

    <form method="POST">

        <input type="number" name="battery_power" placeholder="Battery Power" required><br><br>

        <input type="number" name="ram" placeholder="RAM" required><br><br>

        <input type="number" name="px_width" placeholder="Pixel Width" required><br><br>

        <button type="submit"
        style="padding:10px 20px; font-size:18px;">
            Predict
        </button>

    </form>

    <h2>{{prediction_text}}</h2>

</body>

</html>

'''

@app.route('/', methods=['GET', 'POST'])

def home():

    prediction_text = ""

    if request.method == 'POST':

        battery_power = int(request.form['battery_power'])
        ram = int(request.form['ram'])
        px_width = int(request.form['px_width'])

        # Sample complete data
        data = [[battery_power,1,2.2,0,1,0,7,0.6,188,2,2,20,756,
                 px_width,ram,9,7,19,0,0,1]]

        prediction = model.predict(data)

        prediction_text = "Predicted Price Range: " + str(prediction[0])

    return render_template_string(html,
                                  prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
