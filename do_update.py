from urllib.request import urlopen

alias_dict = urlopen("https://raw.githubusercontent.com/cov-lineages/pango-designation/master/pango_designation/alias_key.json")

with open("alias_key.json", "w") as outfile:
	outfile.write("\n".join([x.decode("utf-8").strip() for x in alias_dict]))
