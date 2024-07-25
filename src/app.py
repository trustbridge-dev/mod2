from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template for the form and the result display
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>User Input Echo</title>
</head>
<body>
    <h1>User Input Echo</h1>
    <form method="POST">
        <label for="user_input">Enter something:</label>
        <input type="text" id="user_input" name="user_input">
        <input type="submit" value="Submit">
    </form>
    {% if user_input %}
    <h2>You entered: {{ user_input }}</h2>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    user_input = None
    if request.method == 'POST':
        user_input = request.form.get('user_input')
    return render_template_string(html_template, user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)

