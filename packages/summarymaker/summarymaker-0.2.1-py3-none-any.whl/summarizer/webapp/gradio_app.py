import gradio as gr
from summarizer.summarizer import process_text  # Adjust import path
from summarizer.utils import extract_from_url  # Adjust import path

def summarize_text(choice, url, file_path, text, model, max_length):
    input_text = ""
    if choice == "URL":
        try:
            input_text = extract_from_url(url)
        except Exception as e:
            return f"URL extraction failed: {str(e)}"
    elif choice == "File":
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                input_text = f.read()
        except Exception as e:
            return f"File reading failed: {str(e)}"
    elif choice == "Text":
        input_text = text

    if not input_text or len(input_text.strip()) < 50:
        return "Not enough text content to summarize"

    try:
        summary = process_text(input_text, model=model, max_length=max_length)
        return summary
    except Exception as e:
        return f"Summarization failed: {str(e)}"

def update_visibility(choice):
    if choice == "URL":
        return gr.update(visible=True), gr.update(visible=False), gr.update(visible=False)
    elif choice == "File":
        return gr.update(visible=False), gr.update(visible=True), gr.update(visible=False)
    elif choice == "Text":
        return gr.update(visible=False), gr.update(visible=False), gr.update(visible=True)
    else:
        return gr.update(visible=False), gr.update(visible=False), gr.update(visible=False)

def main():
    choices = ["URL", "File", "Text"]
    with gr.Blocks() as demo:
        choice = gr.Dropdown(choices, label="Choose input text type")
        url = gr.Textbox(label="URL to Summarize", visible=False)
        file = gr.File(label="Upload File", visible=False)
        text = gr.Textbox(label="Text to Summarize", lines=10, visible=False)
        model = gr.Textbox(label="Model", value="t5-base")
        max_length = gr.Slider(label="Max Length", minimum=50, maximum=500, value=180, step=10)
        summary = gr.Textbox(label="Summary")

        choice.change(fn=update_visibility, inputs=choice, outputs=[url, file, text])

        gr.Button("Summarize").click(
            summarize_text,
            inputs=[choice, url, file, text, model, max_length],
            outputs=summary
        )

    demo.launch()

if __name__ == "__main__":
    main()