import requests
import json


def get_href(word: str) -> dict:
    href: str = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word
    resp: requests.Response = requests.get(href)
    if resp.status_code == 404:
        print("Word not found")
        return {}
    elif resp.status_code == 200:
        return json.loads(resp.text)[0]
    else:
        print(f"Error {resp.status_code}")
        return {}


def print_result(resp: dict) -> None:
    phonetics: dict = resp.get('phonetics')
    if len(phonetics) > 1:
        phonetic_text: str = phonetics[1].get('text') if phonetics[1].get('text') else 'Can\'t find phonetic'
        phonetic_audio: str = phonetics[1].get('audio') if phonetics[1].get('audio') else 'Can\'t find audio phonetic'
    else:
        phonetic_text: str = phonetics[0].get('text') if phonetics[0].get('text') else 'Can\'t find phonetic'
        phonetic_audio: str = phonetics[0].get('audio') if phonetics[0].get('audio') else 'Can\'t find audio phonetic'
    meanings: dict = resp.get('meanings')[0]
    part_of_speech: str = meanings.get('partOfSpeech')
    definitions: list = meanings.get('definitions')
    print(f"{phonetic_text}\n{phonetic_audio}")
    print(f"{part_of_speech}")
    for definition in definitions:
        print(definition.get('definition'))


if __name__ == '__main__':
    inp = input()
    if inp:
        print('Getting response...')
        json_response = get_href(inp)
        if json_response:
            print_result(json_response)
    else:
        print('Request is empty')