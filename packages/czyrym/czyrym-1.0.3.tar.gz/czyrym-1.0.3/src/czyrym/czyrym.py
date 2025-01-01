from typing import Set, List, Optional, NamedTuple, Tuple, Dict, Union
from dataclasses import dataclass
import pyphen
import json
from datetime import datetime
import re
from math import inf
from abc import ABC, abstractmethod
import os
import unicodedata

# Initialize Polish dictionary
dic = pyphen.Pyphen(lang='pl_PL', left=1, right=1)

# Polish vowels
VOWELS: Set[str] = set('AEIOUYĄĘÓ')

NAME: str = "improved"

@dataclass(frozen=True)
class MutationResult:
    word: str
    cost: float

    def __hash__(self) -> int:
        return hash((self.word, self.cost))

@dataclass(frozen=True)
class MutationStep:
    before: str
    after: str
    mutator_name: str
    cost: float

    def __hash__(self) -> int:
        return hash((self.before, self.after, self.mutator_name, self.cost))

@dataclass(frozen=True)
class MutationPath:
    word: str
    cost: float
    steps: Tuple[MutationStep, ...]

    def __hash__(self) -> int:
        return hash((self.word, self.cost, self.steps))

@dataclass(frozen=True)
class RhymeMatch:
    common_form: str
    first_path: MutationPath
    second_path: MutationPath
    total_cost: float

class Mutator(ABC):
    def __init__(self, name: str) -> None:
        self.name: str = name

    @abstractmethod
    def mutate(self, before: str) -> Optional[MutationResult]:
        pass

class SimpleMutator(Mutator):
    def __init__(self, name: str, old: str, new: str, score: float = 1.0) -> None:
        super().__init__(name)
        self.old: str = old
        self.new: str = new
        self.score: float = score

    def mutate(self, before: str) -> Optional[MutationResult]:
        if self.old in before:
            return MutationResult(before.replace(self.old, self.new), self.score)
        return None

class RegexMutator(Mutator):
    def __init__(self, name: str, pattern: str, new: str, score: float = 1.0) -> None:
        super().__init__(name)
        self.pattern: str = pattern
        self.new: str = new
        self.score: float = score

    def mutate(self, before: str) -> Optional[MutationResult]:
        result = re.sub(self.pattern, self.new, before)
        if result != before:
            return MutationResult(result, self.score)
        return None

# could be rewritten as a regex_mutation - but let it stay here as an example
class FinalEjYMutator(Mutator):
    def __init__(self) -> None:
        super().__init__("final_ej_to_y")

    def mutate(self, before: str) -> Optional[MutationResult]:
        if before.endswith("EJ"):
            return MutationResult(before[:-2] + "Y", 1.0)
        return None

class DeleteFinalConsonantsMutator(Mutator):
    def __init__(self) -> None:
        super().__init__("delete_final_consonants")

    def mutate(self, before: str) -> Optional[MutationResult]:
        last_vowel_idx = -1
        for i, c in enumerate(before):
            if c in VOWELS:
                last_vowel_idx = i
        if last_vowel_idx == len(before) - 1:
            return None
        if last_vowel_idx == -1:
            return None
        discarded = len(before) - last_vowel_idx - 1
        return MutationResult(before[:last_vowel_idx + 1], 1 + discarded)

def get_mutators() -> Set[Mutator]:
    simple_mutations: List[Union[Tuple[str, str], Tuple[str, str, float]]] = [
        ('Ó', 'U', 0.0), ('CH', 'H', 0.0),
        ('RZ', 'Ż', 0.0), ('B', 'P'), ('W', 'F'), ('B', 'G', 2),
        ('G', 'K'), ('DŹ', 'Ć'), ('DŻ', 'CZ'), ('Ś', 'SZ'),
        ('Ć', 'CZ'), ('WS', 'S'), ('TRZ', 'CZ'),
        ('II', 'I'), ('OŃ', 'ON'), ('UŁ', 'U'), ('IE', 'I'),
        ('M', 'N'), ('Y', 'E'), ('ĘŁ', 'Ę'), ('ĘN', 'Ę'), ('ĄŁ', 'Ą'), ('NK', 'K'), ('ĆCI', 'CI', 0.5),
        ('ŃJ', 'NI', 0.5), # STEFANIĄ - PAŃ JĄ
    ]

    mutators: Set[Mutator] = {
        SimpleMutator(f"simple_{old}_to_{new}", old, new, score[0] if score else 1.0)
        for old, new, *score in simple_mutations
    }

    mutators.add(RegexMutator("a_ogonek_to_ol", r'Ą(?=[FWSZŻŚŹH]|CH)', 'OŁ', 0.1))
    mutators.add(RegexMutator("a_ogonek_to_om", r'Ą(?=[PBM])', 'OM', 0.1))
    mutators.add(RegexMutator("a_ogonek_to_on", r'Ą(?=[TDCĆKGNŃLRJ])', 'ON', 0.1))
    mutators.add(RegexMutator("final_a_ogonek_to_ol", r'Ą$', 'OŁ', 0.1))
    mutators.add(RegexMutator("final_a_ogonek_to_o", r'Ą$', 'O'))

    mutators.add(RegexMutator("e_ogonek_to_el", r'Ę(?=[FWSZŻŚŹH]|CH)', 'EŁ', 0.1))
    mutators.add(RegexMutator("e_ogonek_to_em", r'Ę(?=[PBM])', 'EM', 0.1))
    mutators.add(RegexMutator("e_ogonek_to_en", r'Ę(?=[TDCĆKG])', 'EN', 0.1))
    mutators.add(RegexMutator("e_ogonek_to_e", r'Ę(?=L)', 'E', 0.1))
    mutators.add(RegexMutator("final_e_ogonek_to_e", r'Ę$', 'E'))

    mutators.add(RegexMutator("d_to_t", r'D(?![ZŻŹ])', 'T'))
    mutators.add(RegexMutator("dz_to_c", r'DZ(?!I)', 'C'))
    mutators.add(RegexMutator("dz_to_z", r'DZ(?!I)', 'Z', 1.5))
    # mutators.add(RegexMutator("i_to_j", r'(?<![CSNZ])I(?=[AEOUYĄĘÓ])', 'J')) # in theory it sounds like a good idea, in practice it dodn't catch any new rhymes
    mutators.add(RegexMutator("z_to_s", r'(?<![CDSR])Z', 'S'))
    mutators.add(RegexMutator("n_to_n", r'Ń(?![AEIOUYĄĘÓ])', 'N', 1.5))
    mutators.add(RegexMutator("i_to_y", r'(?<![SZC])I(?![AEIOUYĄĘÓ])', 'Y', 2.0))
    mutators.add(RegexMutator("i_to_zy", r'(?<=[SC])I(?![AEIOUYĄĘÓ])', 'ZY', 2.0))
    mutators.add(RegexMutator("zi_to_zy", r'ZI(?![AEIOUYĄĘÓ])', 'ŻY', 2.0))
    mutators.add(RegexMutator("double_consonant", r'([A-Z])\1', r'\1'))
    mutators.add(RegexMutator("z_acute_to_s_acute", r'(?<!D)Ź', 'Ś'))
    mutators.add(RegexMutator("z_dot_to_sz", r'(?<!D)Ż', 'SZ'))
    mutators.add(RegexMutator("si_to_sz", r'(?<=[SC])I(?=[AEIOUYĄĘÓ])', 'Z'))
    mutators.add(RegexMutator("final_u_to_o", r'U$', 'O', 1.5))
    mutators.add(RegexMutator("final_l", r'(?<![AEIOUYĄĘÓ])Ł$', ''))

    mutators.add(FinalEjYMutator())
    mutators.add(DeleteFinalConsonantsMutator())

    return mutators

MUTATORS: Set[Mutator] = get_mutators()

def apply_mutators(first: str, mutators: Set[Mutator]) -> Set[MutationPath]:
    initial_result: MutationPath = MutationPath(first, 0.0, ())
    result: Set[MutationPath] = {initial_result}
    new_strings_produced: bool = False
    first_pass: bool = True
    
    while new_strings_produced or first_pass:
        first_pass = False
        new_strings_produced = False
        current_words: Set[MutationPath] = result.copy()
        
        for word_path in current_words:
            for mutator in mutators:
                mutated: Optional[MutationResult] = mutator.mutate(word_path.word)
                if mutated is not None:
                    new_step: MutationStep = MutationStep(
                        word_path.word,
                        mutated.word,
                        mutator.name,
                        mutated.cost
                    )
                    new_path: MutationPath = MutationPath(
                        mutated.word,
                        word_path.cost + mutated.cost,
                        word_path.steps + (new_step,)
                    )
                    if not any(r.word == new_path.word and r.cost <= new_path.cost for r in result):
                        new_strings_produced = True
                        result.add(new_path)
                        result = {r for r in result if not (
                            r.word == new_path.word and r.cost > new_path.cost
                        )}
    
    return result

def get_masculine_key(word: str) -> Set[MutationPath]:
    """
    For single-syllable words, find the last vowel and return mutations
    of the substring from that vowel to the end.
    """
    for i in range(len(word)-1, -1, -1):
        if word[i] in VOWELS:
            rhyme_part = word[i:]
            return apply_mutators(rhyme_part, MUTATORS)
    return set()

def get_feminine_key(syllables: List[str]) -> Set[MutationPath]:
    """
    For multi-syllable words, return a set containing the substring from the last vowel
    in the penultimate syllable to the end of the word, along with its mutations.
    """
    if len(syllables) < 2:
        return set()

    penultimate: str = syllables[-2]
    rest: str = ''.join(syllables[-1:])

    # Find last vowel in penultimate syllable
    last_vowel_idx: int = -1
    for i, char in enumerate(penultimate):
        if char in VOWELS:
            last_vowel_idx = i

    if last_vowel_idx == -1:
        return set()

    # Get substring from last vowel to end
    rhyme_part: str = penultimate[last_vowel_idx:] + rest
    return apply_mutators(rhyme_part, MUTATORS)

def get_rhyme_key(word: str) -> Set[MutationPath]:
    """
    Get the rhyme key for a word by analyzing its syllables.
    """
    # Get syllables using pyphen
    positions: List[int] = dic.positions(word)
    syllables: List[str] = [word[i:j] for i, j in zip([0] + positions, positions + [len(word)])] if positions else [word]
    
    # Choose key generator based on syllable count
    if len(syllables) == 1:
        return get_masculine_key(word)
    else:
        return get_feminine_key(syllables)

def normalize_word(text: str) -> str:
    text = text.upper()
    polish_letters = set("AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ'")
    result = []

    for char in text:
        if char in polish_letters:
            result.append(char)
        else:
            decomposed = unicodedata.normalize('NFKD', char)
            ascii_char = ''.join(c for c in decomposed if not unicodedata.combining(c))

            if ascii_char.upper() in polish_letters:
                result.append(ascii_char.upper())
            elif char in {"'", "′", "`", "'", "'"}:
                result.append("'")
            else:
                result.append(" ")

    text = ''.join(result)
    text = ' '.join(text.split())

    return text

def find_rhyme_match(first_word: str, second_word: str) -> Optional[RhymeMatch]:
    """
    Check if two Polish words rhyme and if they do, return details about how the rhyme was found.
    Returns None if the words don't rhyme.
    """

    first_word = normalize_word(first_word).replace(' ', '')
    second_word = normalize_word(second_word).replace(' ', '')

    first_keys: Set[MutationPath] = get_rhyme_key(first_word)
    second_keys: Set[MutationPath] = get_rhyme_key(second_word)

    min_cost: float = inf
    best_match: Optional[RhymeMatch] = None

    for first_key in first_keys:
        for second_key in second_keys:
            if first_key.word == second_key.word:
                total_cost: float = first_key.cost + second_key.cost
                if total_cost < min_cost:
                    min_cost = total_cost
                    best_match = RhymeMatch(
                        first_key.word,
                        first_key,
                        second_key,
                        total_cost
                    )

    if 'LOG_RHYME_RECOGNIZER' in os.environ:
        log_entry: Dict = {
            "timestamp": datetime.now().isoformat(),
            "name": NAME,
            "input": {
                "first_word": first_word,
                "second_word": second_word
            },
            "analysis": {
                "first_word_keys": [(k.word, k.cost, [
                    (s.before, s.after, s.mutator_name, s.cost) 
                    for s in k.steps
                ]) for k in first_keys],
                "second_word_keys": [(k.word, k.cost, [
                    (s.before, s.after, s.mutator_name, s.cost)
                    for s in k.steps
                ]) for k in second_keys],
                "best_match": {
                    "common_form": best_match.common_form,
                    "first_path": (best_match.first_path.word, best_match.first_path.cost, [
                        (s.before, s.after, s.mutator_name, s.cost)
                        for s in best_match.first_path.steps
                    ]),
                    "second_path": (best_match.second_path.word, best_match.second_path.cost, [
                        (s.before, s.after, s.mutator_name, s.cost)
                        for s in best_match.second_path.steps
                    ]),
                    "total_cost": best_match.total_cost
                } if best_match else None
            },
            "verdict": best_match is not None
        }

        with open('rhyme_recognizer_is_rhyme_log.json', 'a', encoding='utf-8') as f:
            json.dump(log_entry, f, ensure_ascii=False)
            f.write('\n')
    
    return best_match

def is_rhyme(first_word: str, second_word: str) -> bool:
    return find_rhyme_match(first_word, second_word) is not None
