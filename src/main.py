from textnode import TextType, TextNode

def main():
    print("Hello World.")

    testNode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(testNode)
if __name__ == "__main__":
    main()