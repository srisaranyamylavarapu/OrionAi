from backend.feature_analyzer import (
    implementation_finder,
    impact_analyzer,
    beginner_explanation
)

retrieved_chunks = [
    {
        "file_path": "auth/login.py",
        "function_name": "login_user",
        "class_name": None,
        "content": """
def login_user(username, password):
    return authenticate(username, password)
"""
    },
    {
        "file_path": "auth/service.py",
        "function_name": "authenticate",
        "class_name": "AuthService",
        "content": """
def authenticate(username, password):
    # authentication logic
    pass
"""
    },
    {
        "file_path": "middleware/auth.py",
        "function_name": "check_authentication",
        "class_name": None,
        "content": """
def check_authentication(request):
    pass
"""
    }
]


print("\n==============================")
print("IMPLEMENTATION FINDER")
print("==============================")

result1 = implementation_finder(
    "Where is authentication implemented?",
    retrieved_chunks
)

print(result1)


print("\n==============================")
print("CHANGE IMPACT ANALYZER")
print("==============================")

result2 = impact_analyzer(
    "auth/login.py",
    retrieved_chunks
)

print(result2)


print("\n==============================")
print("NEW DEVELOPER MODE")
print("==============================")

result3 = beginner_explanation(
    "Authentication",
    retrieved_chunks
)

print(result3)