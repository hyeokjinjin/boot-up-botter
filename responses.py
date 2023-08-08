

def handle_response(message) -> str:
    p_message = message.lower()
    
    if p_message == "$bootup":
        return "What time do you want to boot everyone up? (Respond with a time with starting with \"$$\")"
