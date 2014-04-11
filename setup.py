from distutils.core import setup
import py2exe

setup(
    version = "1.0.0",
    description = "Wikipedia-crawling trivia game",
    name = "Trivial Pysuit",

    # targets to build
    console = ["wiki_quiz.py"],
    )