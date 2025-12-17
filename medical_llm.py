from transformers import pipeline

# FLAN-T5 is a text-to-text (seq2seq) model, NOT text-generation
medical_pipeline = pipeline(
    task="text2text-generation",
    model="google/flan-t5-base",
    max_length=256
)

def generate_medical_response(question: str) -> str:
    """
    Generates a safe, non-diagnostic medical response
    for general health-related questions.
    """

    prompt = (
        "You are a medical assistant. "
        "Provide general medical information only. "
        "Do not give diagnoses or prescriptions.\n\n"
        f"Question: {question}\n\nAnswer:"
    )

    response = medical_pipeline(prompt)
    return response[0]["generated_text"]
