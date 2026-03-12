import azure.functions as func
import json
from datetime import datetime

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="hello", methods=["GET", "POST"])
def hello(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get("name", "World")
    if not name:
        try:
            body = req.get_json()
            name = body.get("name") if body else "World"
        except:
            name = "World"
    
    response = {
        "message": f"Hello, {name}! This HTTP triggered function executed successfully.",
        "timestamp": datetime.utcnow().isoformat()
    }
    return func.HttpResponse(json.dumps(response), mimetype="application/json", status_code=200)
