

class TrieNode:
    def __init__(self, character=''):
        self.children = {}
        self.is_complete_word = False
        self.character = character

    def get_char(self):
        return self.character

    def add_word(self, word):
        if word is None or len(word) == 0:
            return

        first_char = word[0]

        child = self.get_child(first_char)

        if child is None:
            child = TrieNode(first_char)
            self.children[first_char] = child

        if len(word) > 1:
            child.add_word(word[1:])
        else:
            child.set_terminates(True)

    def get_child(self, c):
        if c in self.children:
            return self.children[c]
        else:
            return None

    def terminates(self):
        return self.is_complete_word

    def set_terminates(self, value):
        self.is_complete_word = value


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        self.root.add_word(word)
        print(word, 'is Done.')

    def contains(self, prefix, exact):
        last_node = self.root

        for i in range(len(prefix)):
            last_node = last_node.get_child(prefix[i])
            if last_node is None:
                return False

        return not exact or last_node.terminates()

    def get_root(self):
        return self.root








