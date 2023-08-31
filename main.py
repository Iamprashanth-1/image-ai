import gradio as gr
import random
import time
from utils import *
from promts import *
# Chatbot demo with multimodal input (text, markdown, LaTeX, code blocks, image, audio, & video). Plus shows support for streaming text.
import os

abs_path = os.path.dirname(os.path.abspath(__file__))

_IMAGE_ADDED = False
_IMAGE_PATH = ""
def add_text(history, text):
    print(text)
    history = history + [(text, None)]
    return history, gr.update(value="", interactive=True)


def add_file(history, file):
    history = history + [((file.name,), None)]
    return history





with gr.Blocks(title='Image AI Assistant') as demo:
    
    gr.HTML("<h1>Ask me anything about your image.</h1>")
    chatbot = gr.Chatbot([], elem_id="Image AI" ,label='Image AI').style(height=350)
    _IMAGE_ADDED = gr.State(value=False)
    _IMAGE_PATH = gr.State(value="")

    def bot(history):
        print(history)
        if history[-1][0][0].endswith(".jpg") or history[-1][0][0].endswith(".png") or history[-1][0][0].endswith(".jpeg"):
            _IMAGE_ADDED.value = True
            _IMAGE_PATH.value = history[-1][0][0]
            response = "**Ask Me Anything about Image**"
            history[-1][1] = ""
            for character in response:
                history[-1][1] += character
                time.sleep(0.05)
                yield history
        elif _IMAGE_ADDED:
            _promt = IMAGE_AI_PROMT.format(question=history[-1][0])
            llm = GPT4ALL()
            _code = llm.call(_promt)
            if not _code:
                _code = llm.call(_promt)
            if not _code:
                history[-1][1] = "Sorry, I don't know the answer to that question. Please try another question."
                yield history
            #print(_code ,'hi',_IMAGE_PATH)
            #gr.Image()
            img = run_python_code(str(_code) ,{'_in_img' : str(_IMAGE_PATH.value), '_out_img' : _IMAGE_PATH.value})
            # cv2.imwrite("temp.jpg", img)
        # _IMAGE_PATH = f'{abs_path}/temp.jpg'
            history[-1][1] = (img,None)
            yield history
            #response = "**Ask me Anything about your image**"
        else:
            response = "**Please Upload Image**"
            history[-1][1] = ""
            for character in response:
                history[-1][1] += character
                time.sleep(0.05)
                yield history
    with gr.Row():
        with gr.Column(scale=0.85):
           
            txt = gr.Textbox(
                show_label=False,
                placeholder="Enter text and press enter, or upload an image",
            ).style(container=False)
        with gr.Column(scale=0.15, min_width=0):
            btn = gr.UploadButton("📁", file_types=["image", "video", "audio"])
    def down(input):
        #print(input)
        
        return _IMAGE_PATH.value
    # with gr.Column():
    #     file_obj = gr.Gallery(
    #             label='Output',
    #             show_label=False,
    #             elem_id='gallery'
    #         ).style(
    #             grid=2,height='auto'
    #         )
    #     input= file_obj
    # tab2_submit_button = gr.Button("Submit")
    
    # tab2_submit_button.click(down, inputs=[input],
    #                         outputs=_IMAGE_PATH)
    
    txt_msg = txt.submit(add_text, [chatbot, txt], [chatbot, txt], queue=False).then(
        bot, chatbot, chatbot
    )
    txt_msg.then(lambda: gr.update(interactive=True), None, [txt], queue=False)
    file_msg = btn.upload(add_file, [chatbot, btn], [chatbot], queue=False).then(
        bot, chatbot, chatbot
    )

demo.queue()
demo.launch(debug=True)