"""Example package configuration using bleeding edge toolset."""

from argparse import ArgumentParser, Namespace

from domainname import __version__


def parse_args() -> Namespace:
    """Parse CLI options and return them as Namespace (object instance)."""
    parser = ArgumentParser()
    parser.add_argument(
        '-v',
        '--version',
        help='Show package version.',
        action='store_true',
        default=False,
    )
    parser.add_argument('Domain name pattern')
    return parser.parse_args()


"""
Check domain availability.

These patterns are supported:
- S - any symobl
- L - any letter
- C - consonant
- V - vowel
- D - any diggit
- [] - set of letters

TODO:
Add argparse option to provide top level domain options to add to names.
Add pattern generation, which would accept sylable or vowel as part of pattern.
Add prefix suffix options, their combinations would be checked.
Add parallel execution option (whois server throtling is the limit, so we need to use multiple servers).
"""

import asyncio
import whois
from string import ascii_lowercase, digits
import sys


# AVAILABLE:   edukis.com, eduhis.com, edunaro.com, eduzas.com, edufas.com smartesto


top_level_domains = ['.com']
name_keywords = []
names = ['educcio']



consonants = 'bcdfghjklmnpqrstvwxz'
vowels = 'aeiouy'
letters = ascii_lowercase
digits = digits
symbols = letters + digits


def expand(keyword, escape_char: str, fillers: list[str] | None = None) -> list[str]:
    expanded_keywords = []
    for filler in fillers:
        expanded_keyword = keyword.replace(escape_char, filler, 1)
        expanded_keywords.append(expanded_keyword)
    return expanded_keywords


def expand_set(keyword) -> list[str]:
    expanded_keyword = []
    start = []
    fillers = []
    end = []

    put_to = start
    for letter in keyword:
        if letter == '[':
            put_to = fillers
            continue
        elif letter == ']':
            put_to = end
            continue

        put_to.append(letter)


    for filler in fillers:
        keyword = f'{"".join(start)}{filler}{"".join(end)}'
        expanded_keyword.append(keyword)
    return expanded_keyword


# TODO: make this function asynchronous and call it in parallel
async def is_domain_available(domain: str) -> bool:
    try:
        w = whois.whois(domain)
    except whois.parser.PywhoisError:
        return True
    if w.expiration_date:
        return False
    return True


async def print_domain_availability(domain: str) -> None:
    if await is_domain_available(domain):
        print(f"\033[1;32m{domain}\033[0m", end=" ", flush=True)
    else:
        print(f"\033[90m{domain}\033[0m", end=" ", flush=True)


def expand_patterns(keywords: list[str]) -> list[str]:
    expanded_keywords = []
    keywords = list(keywords)
    
    i = 0
    while i < len(keywords): 
        keyword = keywords[i]
        if 'C' in keyword:
            keywords.extend(expand(keyword, 'C', consonants))
        elif 'V' in keyword:
            keywords.extend(expand(keyword, 'V', vowels))
        elif 'S' in keyword:
            keywords.extend(expand(keyword, 'S', symbols))
        elif 'L' in keyword:
            keywords.extend(expand(keyword, 'L', letters))
        elif 'D' in keyword:
            keywords.extend(expand(keyword, 'D', digits))

        elif '[' in keyword:
            keywords.extend(expand_set(keyword))
        else:
           expanded_keywords.append(keyword)

        i += 1

    return expanded_keywords 


async def find_available_domains(keywords=[]):
    domains = []

    keywords = expand_patterns(keywords)

    for keyword in keywords:
        for top_level_domain in top_level_domains:
            domain = keyword if '.' in keyword else f'{keyword}{top_level_domain}'

            if domain not in domains:
                domains.append(domain)

    # TODO: make a decorator, which sync function parallelises using async context
    await asyncio.gather(*[print_domain_availability(domain) for domain in domains])
    print()


def check_domain() -> None:
    domain_keywords = sys.argv[1:]
    if '-h' in sys.argv or '--help' in sys.argv:
        print("""\
Check domain availability. Green is AVAILABLE.

These patterns are supported:
- S - symbol
- L - letter
- C - consonant
- V - vowel
- D - digit
- [] - set of letters
              """)
        return
    asyncio.run(find_available_domains(domain_keywords))


if __name__ == '__main__':
    check_domain()
