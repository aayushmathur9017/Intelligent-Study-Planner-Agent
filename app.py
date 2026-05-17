import json

from flask import Flask, jsonify, render_template, request
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage

app = Flask(__name__)
_llm = None


def get_llm():
    global _llm
    if _llm is None:
        _llm = init_chat_model(model="llama3.2:latest", model_provider="ollama")
    return _llm


def create_study_plan(prompt: str, syllabus: str = "", weak_areas: str = "") -> str:
    llm = get_llm()
    system_message = (
        "You are an intelligent study planner, content creator, quiz author, and learning coach. "
        "You must build a study solution that includes:\n"
        "- A daily/weekly study schedule\n"
        "- Clear topic notes and summaries\n"
        "- MCQs and PYQs for practice\n"
        "- Performance tracking suggestions\n"
        "- Adaptive adjustments based on weak areas\n"
        "Respond clearly with headings and bullet lists."
    )
    user_message = (
        f"Study request: {prompt}\n"
        f"Syllabus details: {syllabus if syllabus else 'No additional syllabus provided.'}\n"
        f"Weak areas: {weak_areas if weak_areas else 'No specific weak areas provided.'}\n"
    )
    messages = [HumanMessage(content=system_message), HumanMessage(content=user_message)]
    response = llm.invoke(messages)
    if hasattr(response, "content"):
        return response.content
    if isinstance(response, dict):
        if "messages" in response:
            parts = []
            for item in response["messages"]:
                if isinstance(item, dict):
                    parts.append(item.get("content", ""))
                else:
                    parts.append(str(item))
            return "\n\n".join(parts).strip()
        return json.dumps(response, indent=2, default=str)
    return str(response)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/plan", methods=["POST"])
def api_plan():
    payload = request.get_json(force=True, silent=True) or {}
    prompt = payload.get("prompt", "").strip()
    syllabus = payload.get("syllabus", "").strip()
    weak_areas = payload.get("weak_areas", "").strip()

    if not prompt:
        return jsonify(error="Please enter a study request."), 400

    try:
        answer = create_study_plan(prompt, syllabus=syllabus, weak_areas=weak_areas)
        return jsonify(answer=answer, image_url="/static/study-output.svg")
    except Exception as exc:
        return jsonify(error=str(exc)), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
