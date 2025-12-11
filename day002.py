# The Basic Agent Loop
context = "Goal: Add travel expense..." # Initial Prompt

while True:
    # 1. & 2. Send to LLM
    response = llm.generate(context)
    
    # 3. Parse Response
    action = parse_action(response)
    
    # Check for termination
    if action == "DONE":
        break
        
    # 4. Execute Action (The "Computer" part)
    result = execute(action)
    
    # 5. Get Feedback (Success or Error)
    feedback = f"Action: {action}, Result: {result}"
    
    # 6. Update Context (The "Memory")
    context += feedback