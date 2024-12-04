num = int(input())

def all_sublists(lst):
    # Create an empty list to store the sublists
    sublists = []
    # Use two loops to generate all possible sublists
    for i in range(len(lst) + 1):
        for j in range(i + 1, len(lst) + 1):
            sublists.append(lst[i:j])
    return sublists


def get_prefixes_suffixes(words):
    prefixes = set()
    suffixes = set()

    # Iterate through each word in the list
    for word in words:
        # Get all prefixes of the word
        for i in range(1, len(word) + 1):
            prefixes.add(word[:i])

        # Get all suffixes of the word
        for i in range(len(word)):
            suffixes.add(word[i:])

    return sorted(prefixes), sorted(suffixes)

for i in range(num):
    lst = list(str(input()))
    prefixes = []
    suffixes = []
    sublist = all_sublists(lst)
    for j in range(len(lst)):
        pref = lst[:j+1]
        if pref in sublist:
            prefixes.append(pref)
        suffix = lst[j:]
        if suffix in sublist:
            suffixes.append(suffix)
    print(len(prefixes))
    print(prefixes)
    print(len(suffixes))
    print(suffixes)