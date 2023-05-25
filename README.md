# Azubiheft-Writer

Dieses Projekt enthält den Azubiheft-Writer, ein Tool zum Erstellen von Ausbildungsheften. Es enthält die Datei "generate-azubiheft.py", mit der Ausbildungshefte generiert werden können.

## Beschreibung

Der Azubiheft-Writer ist ein Python-Tool, das entwickelt wurde, um das Erstellen von Ausbildungsheften zu vereinfachen. Die Hauptdatei "generate-azubiheft.py" enthält die pipeline, die das vortrainierte Modell nutzt aus dem google drive Ordner.

## Installation

Um den Azubiheft-Writer zu verwenden, folgen Sie bitte den nachstehenden Schritten:

1. Dieses Repo klonen

2. Das model runterladen von google drive und den inhalt in den ordner model extrahieren.
    - dbmdz/german-gpt2 https://drive.google.com/file/d/1VB35eo4mfPD-xtZUMs4909mOJEx4sRZ3/view?usp=sharing
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
5. Starten mit ```python generate-azubiheft.py``` und den anfang des Satzes eingeben ca. 2 Wörter der rest wird Generiert.
```Verwalten von``` oder ```Mitarbeit an``` etc.

## Hinweis
Das Modell wurde mit sehr wenig daten von Anwedungsentwicklungs Berichte Trainiert. Es ist so, dass fehlerhafte Texte generiert werden die keinen Sinn ergeben.
Das Projekt dient nur zum Lernen von Machine Learning Projekten in Python.

