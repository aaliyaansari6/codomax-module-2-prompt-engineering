# Codomax Internship - Module 2
# Prompt Engineering & AI Productivity
# Name: Aaliya Ansari

# --------------------------------------------------
# Experiment 1: Zero-Shot Prompting
# --------------------------------------------------

prompt = """
Classify the following customer feedback as Positive, Negative, or Neutral:

"The product arrived on time and works perfectly."
"""

print("ZERO-SHOT PROMPT:")
print(prompt)

# Expected classification: Positive


# --------------------------------------------------
# Experiment 2: Few-Shot Prompting
# --------------------------------------------------

prompt = """
Classify the customer feedback as Positive, Negative, or Neutral.

Example 1:
"The product is excellent and works perfectly."
Classification: Positive

Example 2:
"The product stopped working after two days."
Classification: Negative

Example 3:
"The product is okay, but delivery was average."
Classification: Neutral

New feedback:
"The product quality is very good and I am satisfied."
"""

print("\nFEW-SHOT PROMPT:")
print(prompt)

# Expected classification: Positive


# --------------------------------------------------
# Experiment 3: Roles, Context, Instructions & Constraints
# --------------------------------------------------

prompt = """
Role: You are a professional career advisor.

Context:
A third-year engineering student wants to prepare for corporate jobs.

Instruction:
Provide practical career preparation advice.

Constraints:
- Use simple language.
- Give actionable suggestions.
- Keep the response concise.
"""

print("\nROLE, CONTEXT, INSTRUCTIONS & CONSTRAINTS:")
print(prompt)


# --------------------------------------------------
# Experiment 4: Structured JSON Output
# --------------------------------------------------

prompt = """
Provide information about wireless headphones in JSON format.

Required fields:
- product_name
- brand
- price
- rating
"""

print("\nSTRUCTURED JSON PROMPT:")
print(prompt)


# --------------------------------------------------
# Experiment 5: Summarization
# --------------------------------------------------

prompt = """
Summarize the given text into three important points.
Use clear and concise language.
"""

print("\nSUMMARIZATION PROMPT:")
print(prompt)


# --------------------------------------------------
# Experiment 6: Classification
# --------------------------------------------------

feedback_examples = [
    "The product is excellent and works perfectly.",
    "The product stopped working after two days.",
    "The product is okay, but delivery was average."
]

print("\nCLASSIFICATION EXAMPLES:")

for feedback in feedback_examples:
    print("-", feedback)


# --------------------------------------------------
# Experiment 7: Content Generation
# --------------------------------------------------

prompt = """
Write a professional LinkedIn post about learning
Prompt Engineering and AI Productivity during an internship.

Requirements:
- Professional tone
- Simple language
- Mention practical learning
"""

print("\nCONTENT GENERATION PROMPT:")
print(prompt)


# --------------------------------------------------
# Experiment 8: AI-Assisted Coding
# --------------------------------------------------

number = 10

if number % 2 == 0:
    print("\nAI-ASSISTED CODING:")
    print("The number is even.")
else:
    print("The number is odd.")


# --------------------------------------------------
# Experiment 9: AI-Assisted Debugging
# --------------------------------------------------

numbers = [10, 20, 30, 40, 50]

total = 0

# Corrected loop
for i in range(len(numbers)):
    total = total + numbers[i]

print("\nAI-ASSISTED DEBUGGING:")
print("Total:", total)


# --------------------------------------------------
# Experiment 10: Prompt Evaluation
# --------------------------------------------------

basic_prompt = "Write about AI."

improved_prompt = """
Write a 150-word professional explanation of Generative AI
for a third-year engineering student.

Use simple language and include:
1. Definition
2. Applications
3. Benefits
4. One limitation
"""

print("\nPROMPT EVALUATION:")
print("Basic Prompt:", basic_prompt)
print("\nImproved Prompt:")
print(improved_prompt)


# --------------------------------------------------
# Overall Learning
# --------------------------------------------------

print("\nOVERALL LEARNING:")
print("Clear and specific prompts generally provide more useful and structured responses.")
