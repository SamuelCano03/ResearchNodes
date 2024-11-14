from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Datos básicos de nodos y enlaces
    nodes = [
        {"id": "A", "group": 1},
        {"id": "B", "group": 2},
        {"id": "C", "group": 3},
        {"id": "D", "group": 1},
    ]
    links = [
        {"source": "A", "target": "B"},
        {"source": "A", "target": "C"},
        {"source": "B", "target": "D"},
        {"source": "C", "target": "D"},
    ]
    
    return render_template('index.html', nodes=nodes, links=links)

if __name__ == "__main__":
    app.run(debug=True)

