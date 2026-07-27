from openai_helper import llm
def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"

def generate_post(length, language, tag, tone, education, content_type):
    prompt =  get_prompt(
        length,
        language,
        tag,
        tone,
        education,
        content_type,
    )
    response = llm.invoke(prompt)
    return response.content

def get_prompt(length, language, tag, tone, education, content_type):
    length_str = get_length_str(length)

    prompt = f"""
    You are an expert academic content writer.

    Generate high-quality content.

    Topic:
    {tag}

    Content Type:
    {content_type}

    Language:
    {language}

    Length:
    {length_str}

    Tone:
    {tone}

    Education Level:
    {education}

    

    Rules:

    1. Follow the requested tone.

    2. Match the education level.

    3. Use proper headings.

    4. Include examples whenever appropriate.

    5. End with a conclusion.

    6. Do not write any introduction like
    "Sure" or
    "Here is your answer."

    Return only the content.
    """

    return prompt

print(generate_post(
    "Medium",
    "English",
    "Mental Health",
    "Academic",
    "College",
    "Assignment"
))