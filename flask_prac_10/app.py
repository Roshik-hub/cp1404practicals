from flask import Flask, render_template, request
import wikipedia

app = Flask(__name__)
app.secret_key = "any_random_secret_key"

@app.route('/')
def home():
    return render_template('search.html')  # The homepage with the form

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    try:
        summary = wikipedia.summary(query, sentences=3)
        title = wikipedia.page(query).title
        return render_template('results.html', title=title, summary=summary)
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation Error! Options: {e.options}"
    except wikipedia.exceptions.PageError:
        return "Page not found. Try another search."

if __name__ == '__main__':
    app.run(debug=True)
