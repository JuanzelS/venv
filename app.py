from flask import Flask

app = Flask(__name__)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<dessert>')
def favorite_dessert(dessert):
    """Display a message about the user's favorite dessert."""
    return f'Yum! My favorite dessert is {dessert}!'

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    """Create a madlibs sentence using an adjective and noun."""
    return f'The {adjective} {noun} jumped over the lazy dog!'

@app.route('/multiply/<int:x>/<int:y>')
def multiply(x, y):
    """Multiply two numbers and display the result."""
    result = x * y
    return f'{x} times {y} is {result}'

@app.route('/sayntimes/<word>/<times>')
def say_n_times(word, times):
    """Repeat a word a specified number of times."""
    if times.isdigit():
        repeated_word = ' '.join([word] * int(times))
        return repeated_word
    else:
        return 'Invalid input. Please enter a number for times.'

if __name__ == '__main__':
    app.run(debug=True)
