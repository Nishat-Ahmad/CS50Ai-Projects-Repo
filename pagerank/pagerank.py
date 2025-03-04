import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    probability_distribution = {page_name : 0 for page_name in corpus}

    # return equal prob, if no link
    if len(corpus[page]) == 0:
        for page_name in probability_distribution:
            probability_distribution[page_name] = 1 / len(corpus)
        return probability_distribution

    random_prob_page = (1 - damping_factor) / len(corpus)
    picking_link_prob = damping_factor / len(corpus[page])

    for page_name in probability_distribution:
        probability_distribution[page_name] += random_prob_page

        if page_name in corpus[page]:
            probability_distribution[page_name] += picking_link_prob

    return probability_distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    visits = {page_name: 0 for page_name in corpus}
    current_page = random.choice(list(visits))
    visits[current_page] += 1

    for i in range(0, n-1):
        transition_model_dict = transition_model(corpus, current_page, damping_factor)
        rand_val = random.random()
        total_prob = 0

        for page_name, probability in transition_model_dict.items():
            total_prob += probability
            if rand_val <= total_prob:
                current_page = page_name
                break

        visits[current_page] += 1

    page_ranks = {page_name: (visit_num/n) for page_name, visit_num in visits.items()}

    print('Sum of sample page ranks: ', round(sum(page_ranks.values()), 4))

    return page_ranks


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    num_pages = len(corpus)
    initial_rank = 1 / num_pages
    random_choice_prob = (1 - damping_factor) / len(corpus)
    iterations = 0

    page_ranks = {page_name: initial_rank for page_name in corpus}
    new_ranks = {page_name: None for page_name in corpus}
    max_rank_change = initial_rank

    while max_rank_change > 0.001:
        iterations += 1
        max_rank_change = 0

        for page_name in corpus:
            surfer_choice_probability = 0
            for other_page in corpus:
                if len(corpus[other_page]) == 0:
                    surfer_choice_probability += page_ranks[other_page] * initial_rank
                elif page_name in corpus[other_page]:
                    surfer_choice_probability += page_ranks[other_page] / len(corpus[other_page])
            new_rank = random_choice_prob + (damping_factor * surfer_choice_probability)
            new_ranks[page_name] = new_rank

        norm_factor = sum(new_ranks.values())
        new_ranks = {page: (rank / norm_factor) for page, rank in new_ranks.items()}

        for page_name in corpus:
            rank_change = abs(page_ranks[page_name] - new_ranks[page_name])
            if rank_change > max_rank_change:
                max_rank_change = rank_change

        page_ranks = new_ranks.copy()

    print('Iteration took', iterations, 'iterations to converge')
    print('Sum of iteration page ranks: ', round(sum(page_ranks.values()), 4))

    return page_ranks

if __name__ == "__main__":
    main()