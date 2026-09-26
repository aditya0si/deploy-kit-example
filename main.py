"""Word-count service used as the deploy-kit CI example."""


def count_words(text: str) -> dict:
    words = [w for w in text.split() if w.strip()]
    return {"words": len(words), "unique": len({w.lower() for w in words})}


if __name__ == "__main__":
    print(count_words("deploy kit makes the live url a checked artifact"))
