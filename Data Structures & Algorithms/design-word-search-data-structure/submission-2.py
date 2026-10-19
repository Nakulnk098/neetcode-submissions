
class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr:
                curr[c] = {}

            curr = curr[c]

        curr["*"] = True

    def search(self, word: str) -> bool:

        def dfs(index, curr):

            for i in range(index, len(word)):
                c = word[i]

                if c == ".":
                    for key in curr:
                        if key != "*" and dfs(i + 1, curr[key]):
                            return True

                    return False

                if c not in curr:
                    return False

                curr = curr[c]

            return "*" in curr

        return dfs(0, self.root)
