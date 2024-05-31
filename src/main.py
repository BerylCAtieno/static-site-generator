from textnode import TextNode


def main():
    textnode_obj = TextNode("This is a text node", "bold", "https://www.boot.dev")

    textnode_obj.__repr__()


if __name__ == "__main__":
    main()