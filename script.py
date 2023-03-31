from duckduckgo_search import ddg

def main():
    response = ddg("crimea putin news")
    print(response[0])


if __name__ == "__main__":
    main()
