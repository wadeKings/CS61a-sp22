"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime

###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns True. If there are fewer than K such paragraphs, return
    the empty string.

    Arguments:
        paragraphs: a list of strings
        select: a function that returns True for paragraphs that can be selected
        k: an integer

    >>> ps = ['hi', 'how are you', 'fine']
    >>> s = lambda p: len(p) <= 4
    >>> choose(ps, s, 0)
    'hi'
    >>> choose(ps, s, 1)
    'fine'
    >>> choose(ps, s, 2)
    ''
    """
    # BEGIN PROBLEM 1
    i = 0
    n = -1
    while i < len(paragraphs):
        if (select(paragraphs[i])):
            n += 1
        if n == k:
            return paragraphs[i]

        i += 1
    if n < k:
        return ''


# END PROBLEM 1


def about(topic):
    """Return a select function that returns whether
    a paragraph contains one of the words in TOPIC.

    Arguments:
        topic: 与主题相关的单词列表

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'

    # BEGIN PROBLEM 2
    def judge(words, topic=topic):
        for word in words:
            if lower(word) in topic:
                return True

    def select(paragraphs):
        if paragraphs is not list:
            paragraphs = split(remove_punctuation(paragraphs))
            if judge(paragraphs):
                return True
        else:
            for p in paragraphs:
                p = split(remove_punctuation(p))
                if judge(p):
                    return True
        return False

    return select


# END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.
    
    Arguments:
        typed: a string that may contain typos
        reference: a string without errors

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    >>> accuracy('', '')
    100.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    if not typed_words and not reference_words:
        return 100.0
    if typed_words and reference_words:
        num = 0  #按顺序匹配相等的单词数
        number_min = min(len(typed_words), len(reference_words))
        number_max = max(len(typed_words), len(reference_words))
        for x in range(number_min):
            if (typed_words[x] == reference_words[x]):
                num += 1
        if (number_min == len(typed_words)):
            return (num / number_min) * 100
        return (num / number_max) * 100

    if typed_words or reference_words:
        return 0.0

    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string.

    Arguments:
        typed: an entered string
        elapsed: an amount of time in seconds

    >>> wpm('hello friend hello buddy hello', 15)
    24.0
    >>> wpm('0123456789',60)
    2.0
    """
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4

    return len(typed) / 5 * 60 / elapsed
    # END PROBLEM 4


###########
# Phase 2 #
###########


def autocorrect(typed_word, valid_words, diff_function, limit):
    """返回 VALID_WORDS 中与 TYPED_WORD 差异最小的元素。 
    如果差异大于 LIMIT，则返回 TYPED_WORD。

    Arguments:
        typed_word: 表示可能包含拼写错误的单词的一个字符串
        valid_words: 表示正确单词的字符串列表
        diff_function: 量化两个词之间差异的函数
        limit: a number

    >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
    >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
    'butter'
    >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
    >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
    'testing'
    """
    # BEGIN PROBLEM 5
    if typed_word in valid_words:
        return typed_word
    min1 = 10000
    string = ""
    for word in valid_words:
        lenght = diff_function(typed_word, word, limit)
        if limit >= lenght and lenght < min1:
            string = word
            min1 = lenght
    if not string:
        return typed_word

    return string
    # END PROBLEM 5


from cats import autocorrect, lines_from_file


def sphinx_switches(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths and returns the result.

    Arguments:
        start: a starting word
        goal: a string representing a desired goal word
        limit: a number representing an upper bound on the number of chars that must change

    >>> big_limit = 10
    >>> sphinx_switches("nice", "rice", big_limit)    # Substitute: n -> r
    1
    >>> sphinx_switches("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
    2
    >>> sphinx_switches("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
    3
    >>> sphinx_switches("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
    5
    >>> sphinx_switches("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
    5
    """

    # BEGIN PROBLEM 6

    max_lenght = max(len(start), len(goal))
    min_lenght = min(len(start), len(goal))
    revise_num = 0

    def compare_limit(start, goal, revise_num):
        if revise_num > limit:
            return limit + 1
        elif not goal or not start:
            revise_num += (max_lenght - min_lenght)
            if revise_num > limit:
                return limit + 1
            return revise_num
        elif start[0] != goal[0]:
            revise_num += 1
        return compare_limit(start[1:], goal[1:], revise_num)

    return compare_limit(start, goal, revise_num)
    # END PROBLEM 6


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL.
    This function takes in a string START, a string GOAL, and a number LIMIT.

    Arguments:
        start: a starting word
        goal: a goal word
        limit: a number representing an upper bound on the number of edits

    >>> big_limit = 10
    >>> pawssible_patches("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> pawssible_patches("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> pawssible_patches("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    if limit == -1:
        return 0
    elif not start or not goal:  # Fill in the condition
        # BEGIN
        return max(len(start), len(goal))
        # END

    elif start[0] == goal[0]:  # 随意删除或添加字母
        # BEGIN
        return pawssible_patches(start[1:], goal[1:], limit)
        # END

    else:
        # BEGIN
        add = 1 + pawssible_patches(start[0:], goal[1:], limit - 1)
        delete = 1 + pawssible_patches(start[1:], goal[0:], limit - 1)
        updata = 1 + pawssible_patches(start[1:], goal[1:], limit - 1)
        return min(add, delete, updata)
        # END


def final_diff(start, goal, limit):
    """A diff function that takes in a string START, a string GOAL, and a number LIMIT.
    If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function.'


FINAL_DIFF_LIMIT = 6  # REPLACE THIS WITH YOUR LIMIT

###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """将您的 id 和到目前为止的进度报告发送到多人服务器。
       返回到目前为止的进度.

    Arguments:
        typed: 到目前为止输入的单词列表
        prompt: 输入提示中的单词列表
        user_id: 一个数字，表示当前用户的 id
        send: 用于向多人服务器发送进度的函数

    >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
    >>> # The above function displays progress in the format ID: __, Progress: __
    >>> print_progress({'id': 1, 'progress': 0.6})
    ID: 1 Progress: 0.6
    >>> typed = ['how', 'are', 'you']
    >>> prompt = ['how', 'are', 'you', 'doing', 'today']
    >>> report_progress(typed, prompt, 2, print_progress)
    ID: 2 Progress: 0.6
    0.6
    >>> report_progress(['how', 'aree'], prompt, 3, print_progress)
    ID: 3 Progress: 0.2
    0.2
    """
    # BEGIN PROBLEM 8
    dic = {'id': user_id, 'progress': 0}
    i = 0
    a = -1
    while i < len(typed):
        if typed[i] != prompt[i]:
            a = i / len(prompt)
            dic['progress'] = a
            break
        i += 1
    if a != -1:
        dic['progress'] = a
    else:
        dic['progress'] = len(typed) / len(prompt)
    send(dic)
    return dic['progress']
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """给定时间数据，返回一个游戏数据抽象，其中包含单词列表和每个玩家输入每个单词所花费的时间。

    Arguments:
        times_per_player: 时间戳列表列表，包括玩家开始输入的时间，以及玩家完成输入每个单词的时间。
        words:单词列表，按输入顺序排列。
         

    >>> p = [[75, 81, 84, 90, 92], [19, 29, 35, 36, 38]]
    >>> game = time_per_word(p, ['collar', 'plush', 'blush', 'repute'])
    >>> all_words(game)
    ['collar', 'plush', 'blush', 'repute']
    >>> all_times(game)
    [[6, 3, 6, 2], [10, 6, 1, 2]]
    """
    # BEGIN PROBLEM 9

    lst = [[
        times_per_player[n][i] - times_per_player[n][i - 1]
        for i in range(1, len(times_per_player[n]))
    ] for n in range(len(times_per_player))]

    return game(words, lst)
    # END PROBLEM 9


def fastest_words(game):
    """返回每个玩家输入最快的单词列表。

    Arguments:
        game: time_per_word 返回的游戏数据抽象。

    >>> p0 = [5, 1, 3]
    >>> p1 = [4, 1, 6]
    >>> fastest_words(game(['Just', 'have', 'fun'], [p0, p1]))
    [['have', 'fun'], ['Just']]
    """
    player_indices = range(len(
        all_times(game)))  # contains an *index* for each player
    word_indices = range(len(
        all_words(game)))  # contains an *index* for each word
    # BEGIN PROBLEM 10
    times = all_times(game)
    words = all_words(game)
    if not words:
        return times
    lst = [[times[player][word] for player in player_indices]
           for word in word_indices]

    lst1 = [[
        words[word] for word in word_indices
        if lst[word][player] == min(lst[word])
    ] for player in player_indices]

    for word in words:
        bool = False
        for i in player_indices:
            if bool and word in lst1[i]:
                lst1[i].remove(word)
            if word in lst1[i]:
                bool = True

    return lst1
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str
                for w in words]), 'words should be a list of strings'
    assert all([type(t) == list
                for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times
                for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words)
                for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])


enable_multiplayer = True  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print(
            'If you only type part of it, you will be scored only on that part.\n'
        )
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
