def hello(name, lang):
    greetings = {
        "English": "Hello",
        "spanish": "Hola",
        "Japanese": "kunichiwa",
    }

    msg = f"{greetings[lang]} {name}"
    print(msg)

if __name__ == '__main__':
    import argparse 

    parser = argparse.ArgumentParser(
    description = "provides a personal greeting."
    )

    parser.add_argument(
        "-n", '--name', metavar="name",
        required=True, help="The name of the perosn to greet."
    )


    parser.add_argument(
        "-l", "--lang", metavar="language",
        required=True, choices=["English", "spanish", "German"],
        help="The language of the greeting."
    )

    args = parser.parse_args()

    hello(args.name, args.lang)

    msg = f"Hello {args.name}!"
    print(msg)
