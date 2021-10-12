import sys


class Trie:
    class __TrieNode:
        def __init__(self):
            self.children = {}
            self.final_node = False

    def __init__(self):
        self.__root = Trie.__TrieNode()

    def insert(self, word_):
        node = self.__root

        for symbol in word_:
            if symbol not in node.children:
                node.children[symbol] = Trie.__TrieNode()
            node = node.children[symbol]

        node.final_node = True

    def search_matches(self, word_):
        node = self.__root
        for symbol in word_:
            if symbol not in node.children:
                return False
            else:
                node = node.children[symbol]
        return node.final_node

    @staticmethod
    def __search_similar_recursive(node_, prefix_, symbol_, prev_symbol_, word_, previous_row_, pre_previous_row_,
                                   results_):
        if node_ is None:
            return
        columns = len(word_) + 1
        current_row = [previous_row_[0] + 1]

        for column in range(1, columns):

            insert_cost = previous_row_[column] + 1
            delete_cost = current_row[column - 1] + 1
            replace_cost = previous_row_[column - 1]

            if word_[column - 1] != symbol_:
                replace_cost += 1

            current_row.append(min(insert_cost, delete_cost, replace_cost))

            if prev_symbol_ is not None and column > 1 and symbol_ == word_[column - 2] and \
                    prev_symbol_ == word_[column - 1] and word_[column - 1] != symbol_:
                current_row[column] = min(current_row[column], pre_previous_row_[column - 2] + 1)

        if current_row[-1] == 1 and node_.final_node:
            results_.append(prefix_)

        if min(current_row) <= 1:
            prev_symbol_ = symbol_

            for symbol_, child_ in node_.children.items():
                Trie.__search_similar_recursive(child_, prefix_ + symbol_, symbol_, prev_symbol_, word_, current_row,
                                                previous_row_, results_)

    def search_similar(self, word_):
        current_row = range(len(word_) + 1)
        results = []
        for symbol, child in self.__root.children.items():
            Trie.__search_similar_recursive(child, symbol, symbol, None, word_, current_row, None, results)
        return sorted(results)


if __name__ == '__main__':
    my_trie = Trie()
    size_of_dict = int(input())
    for _ in range(size_of_dict):
        word = input().lower()
        my_trie.insert(word)

    for line in sys.stdin:
        if line == '\n':
            continue
        line = line[:-1]
        if my_trie.search_matches(line.lower()):
            print(f'{line} - ok')
        else:
            found_words = my_trie.search_similar(line.lower())
            if found_words:
                print(f'{line} ->', ', '.join(found_words))
            else:
                print(f'{line} -?')
