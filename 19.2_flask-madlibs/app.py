from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def gen_questions():
    """Generate questions"""
    
    # To generate text from a story, pass in a dictionary-like thing
    #of {prompt: answer, promp:answer):
    
    prompts = story.prompts
    return render_template('questions.html', prompts=prompts)

@app.route('/story')
def gen_story():
    """Generates story and shows html"""
    text = story.generate(request.args)
    
    return render_template('story.html', text=text)

