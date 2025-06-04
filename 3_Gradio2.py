import gradio as gr

def handle_input(text):
    return text

with gr.Blocks() as demo:
    text_input = gr.Textbox(label='문자입력', lines=1)
    text_output = gr.Textbox(label='출력')
    text_input.submit(handle_input, inputs=text_input, outputs=text_output)

demo.launch()