import google.generativeai as genai
import os



# Few-shot prompt
few_shot_prompt = """
You are an expert story writer. Write a story about a magic backpack that can grant wishes.

Here are some examples:

Story 1: The backpack could grant wishes for food, and the main character used it to feed the hungry in their town.
Story 2: The backpack could grant wishes for superpowers, and the main character used it to become a superhero.
"""
few_shot_response = model.generate_content(few_shot_prompt)

# Chain-of-thought prompt
cot_prompt = """
You are an expert story writer. Write a story about a magic backpack that can grant wishes.
Think step-by-step:
1. **Character:** Introduce a character who discovers the backpack.
2. **Wish 1:** The character makes their first wish, which has unexpected consequences.
3. **Lesson:** The character learns a lesson about the responsibility of having wishes granted.
4. **Wish 2:** The character makes a second wish, this time being more careful.
"""
cot_response = model.generate_content(cot_prompt)

# ReAct prompt (example of another prompt type)
react_prompt = """
You are an expert story writer. Write a story about a magic backpack that can grant wishes.
I want the story to focus on a character named Alex who is struggling in school.
Alex: I wish I could get better grades without having to study so hard.
Backpack: Your wish is granted! But be careful what you wish for...
"""
react_response = model.generate_content(react_prompt)

# Print and save responses
def print_and_save(prompt_type, prompt, response):
  print(f"## {prompt_type} Prompt:\n{prompt}\n\n## Response:\n{response.text}\n---")
  filename = f"{prompt_type}_prompt_response.txt"
  with open(filename, "w") as f:
    f.write(f"## {prompt_type} Prompt:\n{prompt}\n\n## Response:\n{response.text}\n---")
  print(f"Saved to {filename}")

print_and_save("Few-Shot", few_shot_prompt, few_shot_response)
print_and_save("Chain-of-Thought", cot_prompt, cot_response)
print_and_save("ReAct", react_prompt, react_response)
