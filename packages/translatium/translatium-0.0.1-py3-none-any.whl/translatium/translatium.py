import yaml
import os


class TranslationError(Exception):
    def __init__(self, message, value=""):
        self.message = message
        self.value = value
        super().__init__(self.message)
    def __str__(self):
        return f'{self.message} -> {self.value}'


# Global variables to store translations and fallback language
_translations = {}
_fallback_language = None
_language = None

def init_translatium(path, fallback):
    global _translations, _fallback_language, _language
    _translations = load_translations(path)
    _fallback_language = fallback
    checks()

def checks():
    global _translations, _fallback_language
    # Check if fallback language is available
    if _fallback_language not in _translations:
        raise TranslationError("Fallback Language not found", _fallback_language)
    # Check if all keys in the languages (except the fallback language) are present in the fallback language
    fallback_keys = set(_translations[_fallback_language].keys())
    for lang, translations in _translations.items():
        if lang == _fallback_language:
            continue
        language_keys = set(translations.keys())
        for key in language_keys:
            if key not in fallback_keys:
                raise TranslationError(f"Translation key '{key}' in language '{lang}' not found in fallback language", key)

def set_language(language):
    global _language
    _language = language

def translation(translation_key):
    global _translations, _language, _fallback_language
    if _translations[_language].get(translation_key):
        return _translations[_language].get(translation_key)
    elif _translations[_fallback_language].get(translation_key):
        return _translations[_fallback_language].get(translation_key)
    else:
        raise TranslationError(f"Translation key not found in selected Language({_language}). Also not found in fallback Language({_fallback_language})", translation_key)

def load_translations(path):
    translations = {}
    for filename in os.listdir(path):
        if filename.endswith('.yaml') or filename.endswith('.yml'):
            lang_code = filename.split('.')[0]  # Extract the language code from the filename
            with open(os.path.join(path, filename), 'r') as file:
                translations[lang_code] = yaml.safe_load(file)
    return translations
