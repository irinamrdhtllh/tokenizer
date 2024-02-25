def get_stats(ids):
    counts = {}
    for pair in zip(ids, ids[1:]):
        counts[pair] = counts.get(pair, 0) + 1
    return counts


def merge_token(ids, pair, new_id):
    new_ids = []
    i = 0
    while i < len(ids):
        if i < len(ids) - 1 and ids[i] == pair[0] and ids[i + 1] == pair[1]:
            new_ids.append(new_id)
            i += 2
        else:
            new_ids.append(ids[i])
            i += 1
    return new_ids


if __name__ == "__main__":
    text = "In the modern era, technological advancements have become synonymous with progress and innovation, significantly influencing the trajectory of the global economy. Through a comprehensive statistical analysis, we can gain valuable insights into the profound impact of technology on various aspects of economic growth, productivity, and competitiveness. Economic Growth: Over the past decade, countries that have invested heavily in technological innovation have experienced robust economic growth rates averaging around 3.5% annually. The digital economy has emerged as a key driver of global GDP, contributing an estimated $11.5 trillion to the world economy in 2023, representing nearly 15% of total economic output. Productivity Enhancement: Automation technologies, including robotics and artificial intelligence, have revolutionized industrial production processes, leading to significant gains in productivity. For instance, manufacturing productivity has increased by an average of 2.9% per year due to automation adoption. Cloud computing has streamlined business operations, allowing companies to achieve cost savings of up to 30% on IT expenditures while enhancing workforce productivity by facilitating remote work and collaboration. Job Displacement and Creation: Despite concerns about job displacement, technological advancements have also created new employment opportunities in emerging sectors such as cybersecurity, data science, and renewable energy. According to recent data, the global tech industry employs over 65 million people, with job growth outpacing the overall economy at a rate of 2:1. Trade and Globalization: E-commerce has transformed the landscape of international trade, with online retail sales surpassing $4.2 trillion worldwide in 2023, accounting for over 20% of total global trade. Digital platforms and communication technologies have facilitated cross-border transactions, enabling small and medium-sized enterprises (SMEs) to access global markets and participate in international trade at unprecedented scales. Innovation and Entrepreneurship: Venture capital investment in technology startups reached a record high of $745 billion in 2023, fueling breakthrough innovations in areas such as biotechnology, renewable energy, and quantum computing. The proliferation of startup incubators and accelerators has created fertile ecosystems for entrepreneurship, with over 1.5 million new startups launched globally each year. Sustainable Development: Sustainable technologies, including renewable energy sources and green infrastructure, have emerged as key drivers of economic growth and environmental stewardship. Investments in renewable energy projects exceeded $400 billion in 2023, with solar and wind energy leading the way. The adoption of smart city technologies, such as IoT-enabled infrastructure and efficient transportation systems, has the potential to reduce greenhouse gas emissions by up to 15% and generate $2.5 trillion in economic benefits by 2025. In conclusion, the convergence of technology and economics has reshaped the global landscape, driving unprecedented levels of growth, innovation, and connectivity. By harnessing the power of technological advancements, policymakers, businesses, and individuals can navigate the challenges and opportunities of the digital age, fostering sustainable development and shared prosperity for future generations."

    tokens = text.encode("utf-8")  # Raw bytes
    tokens = list(map(int, tokens))  # Convert to a list of integers

    ids = list(tokens)

    vocab_size = 276  # The desired final vocab size
    num_merges = vocab_size - 256  # Num chars in UTF-8 is 256
    merges = {}
    for i in range(num_merges):
        stats = get_stats(ids)
        pair = max(stats, key=stats.get)
        new_id = 256 + i
        ids = merge_token(ids, pair, new_id)
        merges[pair] = new_id
        print(f"merging {pair} into a new token {new_id}")

    print(f"old tokens length: {len(tokens)}")
    print(f"merged tokens length: {len(ids)}")
    print(f"compression ratio: {len(tokens) / len(ids):.4f}")
