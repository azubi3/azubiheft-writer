# Azubiheft-Writer

Dieses Projekt enthält den Azubiheft-Writer, ein Tool zum Erstellen von Ausbildungsheften. Es enthält die Datei "generate-azubiheft.py", mit der Ausbildungshefte generiert werden können.

## Beschreibung

Der Azubiheft-Writer ist ein Python-Tool, das entwickelt wurde, um das Erstellen von Ausbildungsheften zu vereinfachen. Die Hauptdatei "generate-azubiheft.py" enthält die pipeline, die das vortrainierte Modell nutzt aus dem google drive Ordner.

## Installation

Um den Azubiheft-Writer zu verwenden, folgen Sie bitte den nachstehenden Schritten:

1. Dieses Repo klonen

2. Das model runterladen von google drive und den inhalt in den ordner model extrahieren.
    - aktuelles modell (ohne input) https://drive.google.com/file/d/1--K17i0HhN2D4MQxPEOZfufAOVZMQh35/view?usp=drive_link
3. Ordner struktur sollte so aussehen:
```bash
└── azubiheft-writer
    ├── generate-azubiheft.py
    └── model/
        └── ... 

```

4. Installieren der requirements ```
pip install -r requirements.txt
```
5. Starten mit ```python generate-azubiheft.py```, die WebUI aufrufen unter ```http://127.0.0.1:7860/``` und der rest wird Generiert.

## Hinweis
Das Modell wurde mit sehr wenig daten von Anwedungsentwicklungs Berichte Trainiert. Es ist so, dass fehlerhafte Texte generiert werden die keinen Sinn ergeben.
Das Projekt dient nur zum Lernen von Machine Learning Projekten in Python.
