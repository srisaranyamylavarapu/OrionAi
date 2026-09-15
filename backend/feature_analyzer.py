def _get_details(chunk):
    """Extract useful file/function/class information from a code chunk."""
    file_path = chunk.get("file_path", "Unknown")
    content = chunk.get("content", "")

    function_name = chunk.get("function_name")
    class_name = chunk.get("class_name")

    return file_path, function_name, class_name, content


def implementation_finder(question, retrieved_chunks):
    if not retrieved_chunks:
        return {
            "status": "Not Found",
            "question": question,
            "results": []
        }

    results = []

    for chunk in retrieved_chunks:
        file_path, function_name, class_name, content = _get_details(chunk)

        results.append({
            "file": file_path,
            "function": function_name or "Not identified",
            "class": class_name or "Not identified",
            "code": content[:500]
        })

    return {
        "status": "Found",
        "question": question,
        "results": results
    }


def impact_analyzer(file_name, retrieved_chunks):
    affected_files = []

    for chunk in retrieved_chunks:
        path = chunk.get("file_path", "")

        if not path or path == file_name:
            continue

        if path not in affected_files:
            affected_files.append(path)

    if len(affected_files) == 0:
        risk = "LOW"
    elif len(affected_files) <= 2:
        risk = "MEDIUM"
    else:
        risk = "HIGH"

    return {
        "changed_file": file_name,
        "risk": risk,
        "affected_files": affected_files,
        "note": "Impact is estimated from retrieved related code."
    }


def beginner_explanation(feature_name, retrieved_chunks):
    if not retrieved_chunks:
        return {
            "feature": feature_name,
            "files": [],
            "summary": "No relevant code was found.",
            "steps": []
        }

    files = []

    for chunk in retrieved_chunks:
        path = chunk.get("file_path", "")

        if path and path not in files:
            files.append(path)

    steps = [
        "Start with the main file responsible for the feature.",
        "Find the main function or class.",
        "Follow related functions or modules.",
        "Understand how data moves through the code.",
        "Check the final output or response."
    ]

    return {
        "feature": feature_name,
        "files": files,
        "summary": (
            "This explanation is based on code retrieved "
            "from the repository."
        ),
        "steps": steps
    }