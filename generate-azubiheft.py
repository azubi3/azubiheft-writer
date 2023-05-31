import gradio as gr
from transformers import pipeline, set_seed
from random import randrange

model_path = "model"

generator = pipeline('text-generation', model=model_path)

prompt = "Nenne mir einen Ausbildungsbericht."

def set_text(input_text):
    error = True
    while error == True:
        set_seed(randrange(1000000))
        a = generator(prompt, max_length=30, num_return_sequences=1, pad_token_id=generator.tokenizer.eos_token_id, temperature=1)
        generated_seq = a[0]['generated_text']
        try:
            l = generated_seq.replace(prompt,"").replace("\n","").replace(prompt,"")
            error = False
            return(l.split('.')[0]+".")
        except:
            pass

iface = gr.Interface(fn=set_text, inputs=None, outputs=[gr.Textbox(label="Generierter Bericht")], title="Azubi Bericht Generator", allow_flagging="never")
iface.launch()