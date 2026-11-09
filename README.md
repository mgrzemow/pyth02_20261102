# PYTH02: Zaawansowane programowanie w języku Python

Kod, przykłady i prezentacje ze szkolenia PYTH02 (Altkom Akademia), edycja 2–6 listopada 2026.

**Autor i trener:** Michał Grzemowski · [LinkedIn](https://www.linkedin.com/in/michal-grzemowski-trainer/)

Materiały przygotował autor na potrzeby szkolenia. Repozytorium służy uczestnikom do nauki
i powtórki; przy dalszym wykorzystaniu proszę o podanie autora.

## Co jest w repozytorium

| Katalog | Zawartość |
|---|---|
| `zajecia/` | skrypty pisane na zajęciach: ćwiczenia, przykłady, brudnopisy (`tmp*.py`) |
| `src/kursy_nbp/` | pakiet `kursy-nbp`: notowania walut z API NBP, wydzielony z kodu z zajęć |
| `tests/` | testy pakietu (pytest) |
| `docs/` | źródła dokumentacji pakietu (Zensical + mkdocstrings) |
| `prezentacje/` | slajdy HTML: asyncio, pytest, narzędzia projektu |
| `.github/workflows/` | CI: formatowanie, lint, typy, testy, dokumentacja i budowa paczki |

## Prezentacje

Pliki HTML (reveal.js) otwiera się w przeglądarce po pobraniu repozytorium.
Potrzebny jest internet, bo biblioteka reveal.js ładuje się z CDN.

- [Nowoczesne asyncio](prezentacje/asyncio.html): pętla zdarzeń, `TaskGroup`, `timeout`, `to_thread`, httpx
- [pytest](prezentacje/pytest.html): testy, fikstury, `parametrize`, `monkeypatch`, z odniesieniami do xUnit w C#
- [Od skryptów do projektu](prezentacje/narzedzia_projektu.html): uv, ruff, mypy, pytest, dokumentacja, CLI, CI

Sterowanie: strzałki albo spacja; `Esc` pokazuje przegląd slajdów, `F` włącza pełny ekran.

## Przygotowanie środowiska

Potrzebny jest [uv](https://docs.astral.sh/uv/). Python 3.15 uv pobierze sam.

```text
git clone https://github.com/mgrzemow/pyth02_20261102.git
cd pyth02_20261102
uv sync
```

## Uruchamianie

Skrypty z zajęć uruchamiamy z katalogu głównego repozytorium. Grupa `zajecia` dokłada biblioteki
używane tylko w przykładach (faker, numpy, pdoc3):

```text
uv run --group zajecia python zajecia/c4.py
```

Pakiet ma polecenie `kursy-nbp`:

```text
uv run kursy-nbp usd --limit 3
uv run kursy-nbp --help
```

## Testy

```text
uv run pytest                          # testy pakietu z katalogu tests/
uv run pytest zajecia/c5_test.py -v    # testy pisane na zajęciach
```

## Kontrola jakości

Te same polecenia uruchamia CI przy każdym pushu na `main` i przy pull requeście:

```text
uv run ruff format --check
uv run ruff check
uv run mypy
uv run pytest
```

## Dokumentacja i paczka

```text
uv run --group docs zensical serve     # podgląd dokumentacji w przeglądarce
uv build                               # paczki .whl i .tar.gz w katalogu dist/
```

---

© 2026 Michał Grzemowski · [linkedin.com/in/michal-grzemowski-trainer](https://www.linkedin.com/in/michal-grzemowski-trainer/)
