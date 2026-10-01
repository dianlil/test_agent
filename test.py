import gradio

def reserve_text(text):
    reversed_text = text[::-1]
    len_text = len(text)
    return reversed_text,len_text

#功能
demo = gradio.Interface(
    fn = reserve_text,
    inputs= gradio.Textbox(label="输入字符"),
    outputs=[
        gradio.Textbox(label="反转字符"),
        gradio.Number(label="字符个数")],
    title = "文本处理工具",
    description="输入文字，输出反转文字和字符个数",
    examples=[["你好，世界"],["hello world"]]
)

demo.launch()