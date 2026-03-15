from flask import Flask, request, jsonify, render_template_string
from rag_pipeline import get_answer

app = Flask(__name__)

# Simple HTML UI
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>RAG Project</title>
</head>
<body>
    <h2>RAG Question Answering</h2>
    <form method="post">
        <input type="text" name="question" placeholder="Enter your question" size="60" required>
        <br><br>
        <button type="submit">Ask</button>
    </form>

    {% if answer %}
        <h3>Answer:</h3>
        <p>{{ answer }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    answer = None
    if request.method == "POST":
        question = request.form.get("question")
        answer = get_answer(question)
    return render_template_string(HTML_PAGE, answer=answer)

if __name__ == "__main__":
    app.run(debug=True)