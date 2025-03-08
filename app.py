from flask import Flask, render_template, request
from genai_manager import GenAIManager


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    try:
        query = request.args.get('msg')
        genai_manager = GenAIManager()
        # Use synchronous version instead of async
        response = genai_manager.generate_response_sync(query)
        return response
    except Exception as e:
        app.logger.error(f"Error in get_bot_response: {str(e)}")
        return "I apologize, but I encountered an error processing your request."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=54321, debug=True)