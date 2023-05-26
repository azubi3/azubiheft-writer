from transformers import pipeline, set_seed
from random import randrange

model_path = "model"

generator = pipeline('text-generation', model=model_path, )

while True:
    set_seed(randrange(1000000))
    stichwort = input("Anfang des Satzes: ")
    a = generator(stichwort, max_length=30, num_return_sequences=1, pad_token_id=generator.tokenizer.eos_token_id)
    generated_seq = a[0]['generated_text']
    try:
        sentence = generated_seq[:generated_seq.index('.')+1].strip()
        print(sentence)
    except:
        sentence = generated_seq[:generated_seq.index('\n')+1].strip()+"."
        print(sentence)