from flask import Flask, render_template, request
from genai_manager import GenAIManager


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
async def get_bot_response():
    query = request.args.get('msg')
    genai_manager = GenAIManager()
    response = await genai_manager.generate_response(query)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=54321)