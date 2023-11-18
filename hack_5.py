"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    return result.replace("o", "0").replace("i", "1").replace("a", "@")
