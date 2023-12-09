from flask import Flask, render_template_string, request, redirect, url_for
from googletrans import Translator, LANGUAGES

app = Flask(__name__)

def translate_text(language, text):
    translator = Translator()
    translation = translator.translate(text, dest=language)
    return translation.text

available_languages = [(lang, LANGUAGES[lang]) for lang in LANGUAGES]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_language = request.form.get('language')
        return redirect(url_for('custom_language', lang=selected_language))

    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                background-color: #1a1a1a; /* Dark background color */
                color: #ffffff; /* Text color */
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 50px;
            }

            select {
                padding: 10px;
                font-size: 16px;
            }

            button {
                padding: 10px;
                font-size: 16px;
                background-color: #333;
                color: #ffffff;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
        </style>
        <title>Translation App - Index</title>
    </head>
    <body>
        <h1>Select a Language</h1>
        <form action="/" method="post">
            <select name="language">
                {% for lang, lang_name in languages %}
                    <option value="{{ lang }}">{{ lang_name }}</option>
                {% endfor %}
            </select>
            <button type="submit">Go</button>
        </form>
    </body>
    </html>
    """, languages=available_languages)

@app.route('/language')
def default_language():
    default_text = translate_text('en', 'Strange women lying in ponds distributing swords is no basis for a system of government. Supreme executive power derives from a mandate from the masses, not from some farcical aquatic ceremony.')
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                background-color: #1a1a1a; /* Dark background color */
                color: #ffffff; /* Text color */
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 50px;
            }

            .card {
                background-color: #333; /* Card background color */
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                max-width: 600px;
                margin: auto;
                text-align: center;
            }

            p {
                font-weight: bold;
                text-align: center;
            }
        </style>
        <title>Translation App - Language Page</title>
    </head>
    <body>
        <div class="card">
            <p>{{ text }}</p>
        </div>
    </body>
    </html>
    """, text=default_text)

@app.route('/language/<lang>')
def custom_language(lang):
    custom_text = translate_text(lang, 'Strange women lying in ponds distributing swords is no basis for a system of government. Supreme executive power derives from a mandate from the masses, not from some farcical aquatic ceremony.')
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                background-color: #1a1a1a; /* Dark background color */
                color: #ffffff; /* Text color */
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 50px;
            }

            .card {
                background-color: #333; /* Card background color */
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                max-width: 600px;
                margin: auto;
                text-align: center;
            }

            p {
                font-weight: bold;
                text-align: center;
            }
        </style>
        <title>Translation App - Language Page</title>
    </head>
    <body>
        <div class="card">
            <p>{{ text }}</p>
        </div>
    </body>
    </html>
    """, text=custom_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)