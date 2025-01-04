from flask import Flask, request, render_template
from summarizer.summarizer import process_text  # Adjust import path
from summarizer.utils import extract_from_url, read_file  # Adjust import path

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    if request.method == 'POST':
        choice = request.form.get('choice')
        url = request.form.get('url')
        file = request.files.get('file')
        text = request.form.get('text')
        model = request.form.get('model') or 't5-base'
        max_length = request.form.get('max_length')

        # Use default max_length if the field is empty
        if not max_length:
            max_length = 180
        else:
            # Convert max_length to integer if it's not empty
            try:
                max_length = int(max_length)
            except ValueError:
                return render_template('index.html', error="Invalid maximum length")

        # Ensure only one input is provided based on the choice
        if (choice == 'url' and not url) or (choice == 'file' and not file) or (choice == 'text' and not text):
            return render_template('index.html', error="Please provide the selected input type.")

        input_text = ""
        if choice == 'url':
            try:
                input_text = extract_from_url(url)
            except Exception as e:
                return render_template('index.html', error=f"URL extraction failed: {str(e)}")
        elif choice == 'file':
            try:
                input_text = file.read().decode('utf-8')
            except Exception as e:
                return render_template('index.html', error=f"File reading failed: {str(e)}")
        elif choice == 'text':
            input_text = text
        
        if not input_text or len(input_text.strip()) < 50:
            return render_template('index.html', error="Not enough text content to summarize")

        try:
            summary = process_text(input_text, model=model, max_length=max_length)
        except Exception as e:
            return render_template('index.html', error=f"Summarization failed: {str(e)}")

        return render_template('index.html', summary=summary, url=url, model=model, max_length=max_length, text=text)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)