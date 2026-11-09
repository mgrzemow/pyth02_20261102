"""Brudnopis: TaskGroup i except* - błąd jednego zadania anuluje pozostałe."""

import asyncio


async def zadanie(nazwa, czas, blad=False):
    """Czeka podany czas; opcjonalnie kończy się wyjątkiem ValueError."""
    await asyncio.sleep(czas)
    if blad:
        raise ValueError(f"błąd w {nazwa}")
    print("koniec", nazwa)


async def main():
    """Uruchamia zadania w TaskGroup i łapie wyjątki z grupy przez except*."""
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(zadanie("A", 0.1))
            tg.create_task(zadanie("A", 0.1))
            tg.create_task(zadanie("A", 0.1))
            tg.create_task(zadanie("A", 0.1))
            tg.create_task(zadanie("A", 0.1))
            tg.create_task(zadanie("B", 0.2, blad=True))
            tg.create_task(zadanie("C", 0.3))  # anulowane po błędzie B
    except* ValueError as grupa:
        print("złapane", grupa.exceptions)
    except* ZeroDivisionError as grupa:
        print("złapane", grupa.exceptions)


if __name__ == "__main__":
    asyncio.run(main())
