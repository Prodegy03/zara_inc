from generate import generate_code
from validator import validate_code
from dockerfile_writer import write_dockerfile

def handle_codegen(task):
    prompt = task.get("payload", {}).get("prompt", "")
    filename = task.get("payload", {}).get("filename", "output.py")

    code = generate_code(prompt)
    validation_result = validate_code(code)

    if validation_result["valid"]:
        with open(f"volumes/zara_project/{filename}", "w") as f:
            f.write(code)
        return f"Code written to {filename}"
    else:
        return f"Code failed validation: {validation_result['error']}"
