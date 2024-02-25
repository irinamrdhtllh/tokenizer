def get_stats(ids):
    counts = {}
    for pair in zip(ids, ids[1:]):
        counts[pair] = counts.get(pair, 0) + 1
    return counts


if __name__ == "__main__":
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. In tellus integer feugiat scelerisque varius morbi enim. Faucibus vitae aliquet nec ullamcorper sit amet risus nullam. In arcu cursus euismod quis viverra. Luctus accumsan tortor posuere ac ut consequat semper. Adipiscing at in tellus integer feugiat scelerisque varius morbi. Consectetur libero id faucibus nisl tincidunt eget nullam non. Sed ullamcorper morbi tincidunt ornare. Amet massa vitae tortor condimentum lacinia quis vel eros donec. Quis ipsum suspendisse ultrices gravida dictum. In nibh mauris cursus mattis. Eu facilisis sed odio morbi quis commodo odio aenean sed. Cras tincidunt lobortis feugiat vivamus at. Quam lacus suspendisse faucibus interdum. Dictum sit amet justo donec enim diam vulputate ut. Euismod nisi porta lorem mollis aliquam ut. Lacus suspendisse faucibus interdum posuere lorem ipsum. Viverra suspendisse potenti nullam ac tortor vitae."

    tokens = text.encode("utf-8")  # Raw bytes
    tokens = list(map(int, tokens))  # Convert to a list of integers

    stats = get_stats(tokens)

    print(sorted(((value, key) for (key, value) in stats.items()), reverse=True))
