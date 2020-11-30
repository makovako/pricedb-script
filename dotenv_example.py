#!/usr/bin/env python3

import os
from dotenv import load_dotenv, find_dotenv

def main(message):
    print(message)

if __name__ == "__main__":
    load_dotenv(find_dotenv())
    main(os.environ.get("HELLO_WORLD"))
