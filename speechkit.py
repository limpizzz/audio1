import requests


def text_to_speech(text: str):
    # Токен, Folder_id для доступа к Yandex SpeechKit
    iam_token = "t1.9euelZrMxpKOnJ7Ij8uRjcvGkJuRku3rnpWajZmMmcqTisnKyJPOjYmVlpnl8_c4H39O-e8BOnxl_t3z93hNfE757wE6fGX-zef1656VmsnGnIqVlpmMy5iak8ablIyc7_zF656VmsnGnIqVlpmMy5iak8ablIycveuelZrOl4mKj4qRmpmNm8-anYuOnbXehpzRnJCSj4qLmtGLmdKckJKPioua0pKai56bnoue0oye.mnXoepp2N3S_DjcSUOCShG1FqMKX_X4ikN7-O0JZD6885AhCXghL1XVzllUXHd-XfE4QgQP1IL1q_XKo01pfCQ"
    folder_id = 'b1gb1o17aj4e22s1c3m4'

    # Аутентификация через IAM-токен
    headers = {
        'Authorization': f'Bearer {iam_token}',
    }
    data = {
        'text': text,  # текст, который нужно преобразовать в голосовое сообщение
        'lang': 'ru-RU',  # язык текста - русский
        'voice': 'filipp',  # голос Филлипа
        'folderId': folder_id,
    }
    # Выполняем запрос
    response = requests.post('https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize', headers=headers, data=data)

    if response.status_code == 200:
        return True, response.content  # Возвращаем голосовое сообщение
    else:
        return False, "При запросе в SpeechKit возникла ошибка"




