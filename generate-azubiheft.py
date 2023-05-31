import gradio as gr  # Importiere die Gradio-Bibliothek zur Erstellung der Benutzeroberfläche
from transformers import pipeline, set_seed  # Importiere die erforderlichen Funktionen aus der Transformers-Bibliothek
from random import randrange  # Importiere die Funktion randrange aus der random-Bibliothek

model_path = "model"  # Pfad zum Modell (hier sollte der Pfad zu einem vorab trainierten Modell angegeben werden)

generator = pipeline('text-generation', model=model_path)  # Erstelle ein Pipeline-Objekt für die Textgenerierung mit dem angegebenen Modell

prompt = "Nenne mir einen Ausbildungsbericht."  # Vorgabe-Prompt, um den Ausbildungsbericht zu generieren

def set_text():  # Definition der Funktion set_text
    error = True  # Initialisiere die Fehlervariable mit True
    while error == True:  # Solange ein Fehler auftritt...
        set_seed(randrange(1000000))  # Setze einen zufälligen Seed für die Textgenerierung
        a = generator(prompt, max_length=30, num_return_sequences=1, pad_token_id=generator.tokenizer.eos_token_id, temperature=1)  # Generiere einen Text basierend auf dem Prompt
        generated_seq = a[0]['generated_text']  # Extrahiere den generierten Text aus der Antwort des Generators
        try:  # Versuche den folgenden Code auszuführen
            l = generated_seq.replace(prompt,"").replace("\n","").replace(prompt,"")  # Entferne das Prompt und überflüssige Zeilenumbrüche aus dem generierten Text
            error = False  # Setze den Fehlervariable auf False, um die Schleife zu beenden
            substring = l.split('.')[0]+"."# Teile den generierten Text anhand des ersten Punktes auf und gib nur den ersten Satz zurück
            return(substring[1:])# Das leerzeichen am anfang entfernen
        except:  # Falls ein Fehler auftritt...
            pass  # ...überspringe den restlichen Code und starte die Schleife erneut

def get_week():# funktion get_week definiert
    week = [] # leere liste der woche definieren
    for i in range(6): # ein loop von 7 iterationen
        week.append(set_text()) # den generierten text die wochen liste anhängen
    return tuple(week) # die liste als Tupel ausgeben (geforderte format von gradio)

iface = gr.Interface(fn=get_week, inputs=None, 
                    outputs=[gr.Textbox(label="Montag"), # Tage definieren...
                             gr.Textbox(label="Dienstag"),
                             gr.Textbox(label="Mittwoch"),
                             gr.Textbox(label="Donnerstag"),
                             gr.Textbox(label="Freitag")],
                    title="Azubi Bericht Generator", allow_flagging="never")# Erstelle die Benutzeroberfläche mit der Funktion set_text als Funktion für die Textgenerierung

iface.launch()  # Starte die Benutzeroberfläche