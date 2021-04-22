def quine(s):
    return s + "fun = quine(\"\"\"" + s + "\"\"\")\n"

def eniuq(s):
    return "fun += enuiq(\"\"\"" + s + "\"\"\")\n" + s

fun = quine("""def quine(s):
    return s + "fun = quine(\"\"\"" + s + "\"\"\")\n"

def eniuq(s):
    return "fun += enuiq(\"\"\"" + s + "\"\"\")\n" + s""")

fun += eniuq("""def pquine(s):
    return "print(\"" + s.replace("\n", "\\n").replace("\\", "\\\\").replace("\"", "\\\"") + "\")"

def powomega(args):
    if args == []:
        return pquine("0")
    if args[0] == 0:
        return powomega(args[1:])
    elif args[-1] > 0:
        return pquine(powomega(args[:-1] + [args[-1] - 1]))
    else:
        trail = 0
        while args[-1] == 0:
            trail += 1
            args.pop(-1)
        output = fun
        output += "shift = " + str(trail - 1) + "\n"
        output += "pre = " + str(args[:-1] + [args[-1] - 1]) + "\n"
        output += "i = 1\n"
        output += "while True:\n    print(powomega(pre + [i] + ([0] * shift)))\n    i += 1"
        return output
""")

def pquine(s):
    return "print(\"" + s.replace("\n", "\\n").replace("\\", "\\\\").replace("\"", "\\\"") + "\")"

def powomega(args):
    if args == []:
        return pquine("0")
    if args[0] == 0:
        return powomega(args[1:])
    elif args[-1] > 0:
        return pquine(powomega(args[:-1] + [args[-1] - 1]))
    else:
        trail = 0
        while args[-1] == 0:
            trail += 1
            args.pop(-1)
        output = fun
        output += "shift = " + str(trail - 1) + "\n"
        output += "pre = " + str(args[:-1] + [args[-1] - 1]) + "\n"
        output += "i = 1\n"
        output += "while True:\n    print(powomega(pre + [i] + ([0] * shift)))\n    i += 1"
        return output

i = 1
while True:
    print(powomega([1] + ([0] * i)))
    i += 1