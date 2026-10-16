import math, json

def plural(n, one, many):
    return one if n == 1 else many

def tenths(x):
    return math.floor(x * 10 + 0.5) / 10

def fixed1(x):
    return f"{tenths(x):.1f}"

def roux_truth(fat):
    if not (fat > 0):
        raise ValueError("the fat must be above zero")
    asks = "asks" if fat == 1 else "ask"
    thickens = "thickens" if fat == 1 else "thicken"
    return f"{fat} {plural(fat, 'tablespoon', 'tablespoons')} of fat {asks} {fat} {plural(fat, 'tablespoon', 'tablespoons')} of flour and {thickens} {fat} {plural(fat, 'cup', 'cups')} of liquid honestly."

def crowd_truth(guests):
    if not (guests > 0):
        raise ValueError("the guests must be above zero")
    cups = tenths(guests / 3)
    asks = "asks" if guests == 1 else "ask"
    return f"{guests} {plural(guests, 'guest', 'guests')} at an honest third of a cup each {asks} {fixed1(cups)} cups of gravy - {fixed1(cups)} {plural(tenths(cups), 'tablespoon', 'tablespoons')} of fat and flour honestly."

def fix_truth(cups, mode):
    if not (cups > 0):
        raise ValueError("the cups must be above zero")
    if mode == "thin":
        asks = "asks" if tenths(cups) == 1 else "ask"
        return f"{fixed1(cups)} {plural(tenths(cups), 'cup', 'cups')} of thin gravy {asks} {fixed1(cups)} {plural(tenths(cups), 'teaspoon', 'teaspoons')} of cornstarch whisked into cold water honestly."
    if mode == "thick":
        loosens = "loosens" if tenths(cups) == 1 else "loosen"
        return f"{fixed1(cups)} {plural(tenths(cups), 'cup', 'cups')} of thick gravy {loosens} with {fixed1(cups * 2)} {plural(tenths(cups * 2), 'tablespoon', 'tablespoons')} of warm broth honestly."
    raise ValueError("the fix must be thin or thick")

FNS = {"rouxTruth": roux_truth, "crowdTruth": crowd_truth, "fixTruth": fix_truth}

CASES = [
    ("rouxTruth", [2]),
    ("rouxTruth", [1]),
    ("rouxTruth", [4]),
    ("rouxTruth", [6]),
    ("rouxTruth", [0]),
    ("rouxTruth", [-1]),
    ("crowdTruth", [8]),
    ("crowdTruth", [1]),
    ("crowdTruth", [3]),
    ("crowdTruth", [12]),
    ("crowdTruth", [5]),
    ("crowdTruth", [2]),
    ("crowdTruth", [0]),
    ("crowdTruth", [-4]),
    ("fixTruth", [4, "thin"]),
    ("fixTruth", [1, "thin"]),
    ("fixTruth", [2.5, "thin"]),
    ("fixTruth", [4, "thick"]),
    ("fixTruth", [1, "thick"]),
    ("fixTruth", [0.5, "thick"]),
    ("fixTruth", [3, "lumpy"]),
    ("fixTruth", [6, "thin"]),
    ("fixTruth", [2, "thick"]),
    ("rouxTruth", [3]),
    ("crowdTruth", [6]),
    ("fixTruth", [0, "thin"]),
]

out = []
for fn, args in CASES:
    rec = {"fn": fn, "args": args}
    try:
        rec["out"] = FNS[fn](*args)
    except ValueError as e:
        rec["err"] = str(e)
    out.append(rec)
    print(fn, args, "->", rec.get("out") or ("ERR: " + rec["err"]))

with open("expected.json", "w") as f:
    json.dump(out, f, indent=1)
    f.write("\n")
print(f"{len(out)} cases written")
