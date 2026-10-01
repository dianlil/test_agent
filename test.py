import gradio

def reserve_text(text):
    return  f"你好{text}"
#功能
demo = gradio.Interface(
    fn = reserve_text,
    inputs= "text",
    outputs="text"
)

demo.launch()