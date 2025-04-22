from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    decision = random.choice(['BUY', 'SELL', 'HOLD'])
    asset = random.choice(['BTC', 'ETH', 'ADA', 'XRP'])
    price = round(random.uniform(0.5, 100), 2)

    return render_template('index.html', decision=decision, asset=asset, price=price)

if __name__ == '__main__':
    app.run(debug=True)
