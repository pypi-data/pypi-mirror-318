import os
import gradio as gr
from summarizer.summarizer import process_text  # Adjust import path
from summarizer.utils import extract_from_url  # Adjust import path

# Set the Gradio temporary directory
os.environ['GRADIO_TEMP_DIR'] = os.path.expanduser('~/.gradio_tmp')

# Create the temporary directory if it does not exist
os.makedirs(os.environ['GRADIO_TEMP_DIR'], exist_ok=True)

def summarize_text(choice, url, file_path, text, model_name, max_length):
    input_text = ""
    if choice == "URL":
        try:
            input_text = extract_from_url(url)
        except Exception as e:
            return f"URL extraction failed: {str(e)}"
    elif choice == "File":
        if file_path is not None:
            try:
                with open(file_path.name, 'r', encoding='utf-8') as f:
                    input_text = f.read()
            except Exception as e:
                return f"File reading failed: {str(e)}"
        else:
            return "File reading failed: No file uploaded"
    elif choice == "Text":
        input_text = text

    if not input_text or len(input_text.strip()) < 50:
        return "Not enough text content to summarize"

    try:
        summary = process_text(input_text, model=model_name, max_length=max_length)
        return summary
    except Exception as e:
        return f"Summarization failed: {str(e)}"

def update_visibility(choice):
    return (
        gr.update(visible=(choice == "URL"), value=""),
        gr.update(visible=(choice == "File"), value=None),
        gr.update(visible=(choice == "Text"), value="")
    )

def main():
    choices = ["Text", "URL", "File"]
    with gr.Blocks() as demo:
        choice = gr.Dropdown(choices, label="Choose input text type", value="Text")
        url = gr.Textbox(label="URL to Summarize", visible=False)
        file = gr.File(label="Upload File", visible=False)
        text = gr.Textbox(label="Text to Summarize", lines=10, visible=True)  # Visible by default
        model = gr.Textbox(label="Model", value="t5-base")
        max_length = gr.Slider(label="Max Length", minimum=50, maximum=500, value=180, step=10)
        summary = gr.Textbox(label="Summary")

        choice.change(fn=update_visibility, inputs=choice, outputs=[url, file, text])

        gr.Button("Summarize").click(
            summarize_text,
            inputs=[choice, url, file, text, model, max_length],
            outputs=[summary]
        )

    demo.launch()  # Enable public link

if __name__ == "__main__":
    main()