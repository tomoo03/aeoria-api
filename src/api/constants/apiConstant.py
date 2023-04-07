class API_CONSTANT:
    AUTHORIZATION = 'Authorization'
    CONTENT_TYPE = 'Content-Type'
    DEEPL: dict[str, dict[str, str] | str] = {
        'SCHEME': {
            'AUTHORIZATION': 'DeepL-Auth-Key'
        },
        'TRANSLATE_CONTENT_TYPE': 'application/x-www-form-urlencoded',
        'TRANSLATE_PATH': 'v2/translate',
        'URL_BASE': 'https://api.deepl.com'
    }
    OPENAI = {
        'COMPLETION_URL': 'https://api.openai.com/v1/chat/completions'
    }
