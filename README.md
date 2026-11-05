# PYTH02: kod ze szkolenia i pakiet `kursy-nbp`

- `zajecia/`: skrypty pisane na zajęciach, uruchamiane z katalogu głównego repo
- `src/kursy_nbp/`: pakiet z notowaniami NBP, wydzielony z kodu z zajęć
- `tests/`: testy pakietu
- `docs/`: źródła dokumentacji

## Uruchomienie

```text
uv sync
uv run kursy-nbp usd --limit 3
uv run --group zajecia python zajecia/c4.py
```

## Kontrola jakości

```text
uv run ruff format --check
uv run ruff check
uv run mypy
uv run pytest
```

## Dokumentacja i pakiet

```text
uv run --group docs zensical serve
uv build
```
