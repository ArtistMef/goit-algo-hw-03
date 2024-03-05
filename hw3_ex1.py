import argparse
import shutil
from pathlib import Path

def parse_argv():
    parser = argparse.ArgumentParser("Сортування файлів по розширенню")
    parser.add_argument(
        "-S", "--source", type=Path, required=True, help="Папка з файлами"
    )
    parser.add_argument(
        "-O",
        "--output",
        type=Path,
        default=Path("dist"), 
        help="Папка для відсортованих файлів",
    )
    return parser.parse_args()

def recursive_copy(src: Path, dst: Path):
    for item in src.iterdir():
        if item.is_dir():
            recursive_copy(item, dst)
        else:
            
            file_extension = item.suffix[1:]
            if file_extension == "":
                file_extension = "no_extension"
            folder = dst / file_extension
            folder.mkdir(exist_ok=True, parents=True)
            shutil.copy2(item, folder)

def main():
    args = parse_argv()
    print(f"Вхідні аргументи: {args}")
    recursive_copy(args.source, args.output)

if __name__ == "__main__":
    main()
