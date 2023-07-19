from flask import Flask, redirect, request, render_template, url_for


app = Flask(
    __name__,
    template_folder="templates",
    static_folder='static'  # Name of directory for static files
)

# Your code should be below

@app.route('/')
def funhome():
    return render_template('home.html')
@app.route('/product')
def funprdct():
    return render_template('product.html')
@app.route('/toy1')
def ty1():
    return render_template('toy1.html')
@app.route('/toy2')
def ty2():
    return render_template('toy2.html')
@app.route('/toy3')
def ty3():
    return render_template('toy3.html')
@app.route('/cart')
def crt():
    return render_template('cart.html')

# Your code should be above

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
