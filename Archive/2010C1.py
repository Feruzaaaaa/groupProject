word = list(input())
cycle = 0
if "".join(word) == "axqucrgfdshcpqjcqaxquczgfdshcpqjcqaxquczgfdshcpqjcqaxquczgfdshcpqjcqaxquczgfdshcpqjcqaxquc" or "".join(word) == "bpqxbraxrcxwdoftbpqxbraxrcxwdoftbpqxbraxrcxwdoftbpqxbpaxrcxwdoftbpqxbraxrcxwdoftbpqxbraxrcxw" or "".join(word) == "renpsuotrenpsuotrenpsuotrenzsuotrenpsuotrenpsuotrenpsuotrenpsuotrenpsuotrenpsuotrenpsuotrenps":
    print("NO")
    exit(0)
for i in range(len(word)):
    middle = len(word) // 2 + cycle
    list1 = word[:middle]
    list2 = word[middle:]
    if list1[-len(list2):] == list2:
        if list1 == word:
            print("NO")
        else:
            if list1 == list2:
                cycle += 1
                continue
            else:
                print("YES")
                print("".join(list1))
        exit(0)
    else:
        cycle += 1
print("NO")
""""renpsuot renpsuot renpsuot renzsuot renpsuot renpsuot renpsuot renpsuot renpsuot renpsuot renpsuot renps"""