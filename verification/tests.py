"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [['p4', 'p5', 'p6', 'm1', 'm1', 'm1', 's2', 's3', 's4', 's9', 'we', 'we', 'dw', 'dw']],
            "answer": 1,
            "explanation": "tempay"
        },
        {
            "input": [['p4', 'p5', 'p6', 'm1', 'm1', 'm1', 's2', 's3', 's4', 's9', 'we', 'ws', 'dw', 'dw']],
            "answer": 2,
            "explanation": "ishanten"
        },
        {
            "input": [['p4', 'p5', 'p7', 'm1', 'm1', 'm1', 's2', 's3', 's4', 's9', 'we', 'ws', 'dw', 'dw']],
            "answer": 3,
            "explanation": "ryanshanten"
        },
        {
            "input": [['p4', 'p5', 'p7', 'm1', 'm1', 's2', 's3', 's4', 's9', 'we', 'ws', 'wn', 'dw', 'dw']],
            "answer": 4,
            "explanation": "sanshanten"
        },
    ],
    "Extra": [
        {
            "input": [],
            "answer": None,
            "explanation": "I speaked you about thoroughly check. And?"
        },
        {
            "input": ['incorrect string'],
            "answer": None,
            "explanation": "Sorry, your solution is incomplete yet."
        },
        {
            "input": [6, 66, 666],
            "answer": None,
            "explanation": "This is absolutely wrong input data. You should prevent errors."
        },
        {
            "input": ['s1', 's1', 's1', 's2', 's2', 's2', 's3', 's3', 's3', 's4', 's4', 's4', 's5', 'oh, no...'],
            "answer": None,
            "explanation": "Oh, no!"
        },
        {
            "input": [['s5', 's1', 's4', 's4', 's3', 's2', 's2', 's0', 's1', 's3', 's3', 's1', 's2', 's4']],
            "answer": None,
            "explanation": "Alas, there is no tile s0 in mahjong..."
        },
        {
            "input": ['s4', 's2', 's1', 's2', 's3', 's4', 's1', 's3', 's1', 's4', 's1', 's2', 's1', 's3'],
            "answer": None,
            "explanation": "There can't be FIVE same tiles..."
        },
        {
            "input": ['s4', 's2', 's4', 's5', 's5', 's2', 's4', 's6', 's2', 's3', 's3', 's3', 's6', 's6'],
            "answer": 0,
            "explanation": "Yes, this hand is ALREADY winning. And it cost very, very much..."
        },
        {
            "input": ['s3', 's3', 'dg', 's6', 's4', 's1', 's6', 's7', 's2', 's2', 's5', 's4', 's1', 's5'],
            "answer": 1,
            "explanation": "Chitoy. In tempay. What? You didn't think about it? ¯\_(ツ)_/¯"
        },
        {
            "input": ['p1', 'we', 'ws', 'wn', 'm1', 'm9', 's9', 'dg', 's1', 'p9', 'dw', 'dr', 'p5', 'ww'],
            "answer": 1,
            "explanation": "Kokushi muso. Also in tempay. I'm sorry that you forgot about it."
        },
        {
            "input": ['m1', 's7', 's5', 'm2', 'p7', 'p8', 's9', 's6', 's4', 'p3', 'm3', 'p2', 'dw', 's8'],
            "answer": 2,
            "explanation": "Ishanten. What did you say? I already checked it?"
        }
    ]
}
