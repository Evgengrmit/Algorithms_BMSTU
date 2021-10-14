import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')


class Trie:
    """
    Space complexity of trie:
    O(number) number - число узлов в префиксном дереве
    """

    class __TrieNode:
        def __init__(self):
            self.children = {}
            self.final_node = False

    def __init__(self):
        self.__root = Trie.__TrieNode()

    def insert(self, word_) -> None:
        """
        Вставка в префиксное дерево:
        сложность по времени O(length), где length - длина искомого слова.
        Быстрее осуществить нельзя, так как необходимо проверить,
        есть ли символ в нужной ветви и если нет, то надо добавить символ в префиксное дерево.
        сложность по памяти O(1) - проход по всем узлам для вставки нового
        узла не требует дополнительного выделения памяти. Для нового узла выделяется константный объем памяти
        :param word_:
        :return:
        """
        node = self.__root

        for symbol in word_:
            if symbol not in node.children:
                node.children[symbol] = Trie.__TrieNode()
            node = node.children[symbol]

        node.final_node = True
        # конец слова, нужен для того, чтобы избежать ситуации, когда, например,
        # в словаре solutions, а ищем solution

    def search_matches(self, word_) -> bool:
        """
        Поиск слова в префиксном дереве:
        сложность по времени O(length), где length - длина искомого слова. Быстрее осуществить нельзя, так как необходимо
        проверить, что каждый символ есть в префиксном дереве.

        сложность по  памяти O(1) - при проходе по ветви для определения наличия слова
        дополнительная память не выделяется.
        :param word_:
        :return bool:
        """
        node = self.__root
        for symbol in word_:
            if symbol not in node.children:
                return False
            else:
                node = node.children[symbol]
        return node.final_node  # проверяем является ли последний символ концом
        # для того, чтобы избежать ситуацию, когда, например, в словаре solutions, а ищем solution

    def search_similar(self, word_) -> []:
        """
        Для поиска расстояния Дамерау-Левенштейна создается таблица M*N, где M и N - длины сравниваемых слов
        В алгоритме для проверки расстояния нужно для каждого слова в словаре составить таблицу.
        Это O(size*max_length^2) по времени и O(max_length^2) по памяти,
        где size - размер словаря, max_length - максимальная длина слова

        Поиск похожих слов:
        Сложность по времени:
        Для слова, проверяется очередной символ из ветви дерева. То есть мы для каждого узла в Trie создаем по крайней
        мере одну строку в таблице, таким образом сложность по времени
        O(number*length),
        где number - число узлов в префиксном дереве, length - длина проверяемого слова.
        Что значительно лучше чем просто перебор.

        Сложность по памяти:
        Для обхода каждого узла требуется рекурсивный вызов, следовательно заполняется стек вызовов.
        Это O(number) вызовов функции, где number - число узлов. Для проверки каждого узла требуется
        3 строки матрицы длины length - длина проверяемого слова. Это
        O(length).
        Таким образом, сложность по памяти O(number*length)
        :param word_:
        :return list:
        """
        current_row = range(len(word_) + 1)
        results = []
        for symbol, child in self.__root.children.items():
            Trie.__search_similar_recursive(child, symbol, symbol, None, word_, current_row, None, results)
        return sorted(results)

    @staticmethod
    def __search_similar_recursive(node_, prefix_, symbol_, prev_symbol_, word_, previous_row_, pre_previous_row_,
                                   results_):
        """
        рекурсивный вызов
        """
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


def main():
    my_trie = Trie()
    size_of_dictionary = int(input())

    for _ in range(size_of_dictionary):
        word = input().lower()
        my_trie.insert(word)

    print_end = False

    for line in sys.stdin:
        if line == '\n':
            continue
        line = line[:-1]

        # чтобы в конце не было '\n'
        if print_end:
            print()
        else:
            print_end = True

        if my_trie.search_matches(line.lower()):
            print(f'{line} - ok', end='')
        else:
            found_words = my_trie.search_similar(line.lower())

            if found_words:
                print(f'{line} ->', ', '.join(found_words), end='')
            else:
                print(f'{line} -?', end='')


if __name__ == '__main__':
    main()
