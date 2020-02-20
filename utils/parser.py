import re

def parse_error(err):
    print(str(err))
    items = re.findall("DETAIL:  Key \((.+)\)=\((.+)\) already exists.", str(err))
    return "the %s %s already exists" % (items[0][0], items[0][1])