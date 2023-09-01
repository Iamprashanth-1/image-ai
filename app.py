from fastapi import *
from fastapi.responses import RedirectResponse
import gradio as gr

from main import demo

app = FastAPI()

app = gr.mount_gradio_app(app, demo, path='/ai')
@app.get('/')
async def root():
    return RedirectResponse('/ai')

