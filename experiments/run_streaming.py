"""Experiment driver for the streaming drift bounds."""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    print(f"running streaming experiments with {args.config}")


if __name__ == "__main__":
    main()
