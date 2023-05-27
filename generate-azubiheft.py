import gradio as gr
from transformers import pipeline, set_seed
from random import randrange

model_path = "model"

generator = pipeline('text-generation', model=model_path)

def generate_sequence(stichwort):
    set_seed(randrange(1000000))
    a = generator(stichwort, max_length=30, num_return_sequences=5, pad_token_id=generator.tokenizer.eos_token_id)
    sentence = None
    iterator=0
    while sentence is None:
        try:
            generated_seq = a[iterator]['generated_text']
            sentence = generated_seq[:generated_seq.index('.')+1].strip()
        except:
            iterator+=1
            if iterator > 5:
                sentence = "Error, try again."
    return sentence

def my_function(stichwort):
    return generate_sequence(stichwort)

ui = gr.Interface(fn=my_function, inputs=[gr.Textbox(label="Anfang des Satzes")],
                  outputs=[gr.Textbox(label="Generierter Bericht")], allow_flagging="never")

ui.launch()