from typing import Dict
from emoji.unicode_codes.data_dict import *
from emoji.unicode_codes.data_dict import LanguagesT

__all__ = [
    'get_emoji_unicode_dict', 'get_aliases_unicode_dict',
    'EMOJI_DATA', 'STATUS', 'LANGUAGES'
]


_EMOJI_UNICODE: Dict[LanguagesT, Dict[str, str]] = {}  # Cache for the language dicts

_ALIASES_UNICODE: Dict[str, str] = {}  # Cache for the aliases dict


def get_emoji_unicode_dict(lang: LanguagesT) -> Dict[str, str]:
    """Generate dict containing all fully-qualified and component emoji name for a language
    The dict is only generated once per language and then cached in _EMOJI_UNICODE[lang]"""

    if lang not in _EMOJI_UNICODE:
        _EMOJI_UNICODE[lang] = {
            data[lang]: emj for emj, data in EMOJI_DATA.items()
            if lang in data and data['status'] <= STATUS['fully_qualified']
        }

    return _EMOJI_UNICODE[lang]


def get_aliases_unicode_dict() -> Dict[str, str]:
    """Generate dict containing all fully-qualified and component aliases
    The dict is only generated once and then cached in _ALIASES_UNICODE"""

    if not _ALIASES_UNICODE:
        _ALIASES_UNICODE.update(get_emoji_unicode_dict('en'))
        for emj, data in EMOJI_DATA.items():
            if 'alias' in data and data['status'] <= STATUS['fully_qualified']:
                for alias in data['alias']:
                    _ALIASES_UNICODE[alias] = emj

    return _ALIASES_UNICODE
