from transformers import pipeline
from langdetect import detect

# Load the multilingual translation model once (efficient & stable)
translator = pipeline(
    task="translation",
    model="facebook/nllb-200-distilled-600M"
)

# Mapping ISO language codes to NLLB language codes
LANGUAGE_MAP = {
    "en": "eng_Latn",
    "hi": "hin_Deva",
    "ta": "tam_Taml",
    "te": "tel_Telu",
    "ml": "mal_Mlym",
    "kn": "kan_Knda",
    "fr": "fra_Latn",
    "de": "deu_Latn",
    "es": "spa_Latn",
    "ru": "rus_Cyrl",
    "zh-cn": "zho_Hans",
    "ja": "jpn_Jpan"
}

def detect_language(text: str) -> str:
    """
    Detects the language of the input text.
    Returns ISO 639-1 language code.
    """
    return detect(text)


def translate_text(text: str, src: str, tgt: str) -> str:
    """
    Translates text from source language to target language
    using NLLB-200 multilingual model.
    """

    # If source and target are same, no translation needed
    if src == tgt:
        return text

    # Default to English if language not supported
    src_lang = LANGUAGE_MAP.get(src, "eng_Latn")
    tgt_lang = LANGUAGE_MAP.get(tgt, "eng_Latn")

    translated = translator(
        text,
        src_lang=src_lang,
        tgt_lang=tgt_lang,
        max_length=512
    )

    return translated[0]["translation_text"]
