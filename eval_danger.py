print(eval("2 + 3 * len('hello')") == 17)

s = """('eval'("__import__('os').system('clear')", {}))"""

# eval("__import__('os').system('clear')", {'__builtins__':{}})
