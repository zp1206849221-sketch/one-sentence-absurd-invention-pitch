import os


def main():
    line = (
        "The WaveSaver is a wristband that violently yanks your arm down and coughs loudly "
        "whenever you wave back at someone who was waving at the person behind you, "
        "so you never have to pretend to check your phone for a week."
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
