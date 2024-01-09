import json
import sys

header = [ "Firm", "URL", "tags"]

if len(sys.argv) != 2 :
    print(f"Usage: python {sys.argv[0]} <firms.json>")
    sys.exit(-1)

firms = [ [x['firm'], x['url']] + [x[k] for k in x.keys() if k not in ['url','firm']] for x in json.load(open(sys.argv[1]))]
firms.sort(key=lambda x: x[0])

print(
    "|" + "|".join([f" __{x}__ " for x in header]) + "|\n" +\
    (f":{'-'*3} |" * len(header))[:-1] + "\n" +\
    "\n".join([f"{x[0]} | [{x[1]}]({x[1]}){' | '.join(x[2:])}" for x in firms])
)
