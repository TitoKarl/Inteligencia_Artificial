import json

config = {
    "modelo" : "llama3.2",
    "temperatura": 0.2
}

with open("fichero.json", "w", encoding="utf-8") as f: json.dump(config, f, ensure_ascii=False, indent=2)