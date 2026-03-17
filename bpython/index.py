# ordered, mutable, allow-dup array - []
# tuples ()
# ordered, immutable, allow-dup
# set {} unordered, mutable, not-dup
# frozenset{} unorderd, immutable, no-dup
# dict {key:value}

# array & dict are same
ls = ["airtel", "jio", 'VI', 'BSNL']
dc = {
    "bekar":"airtel",
    "bekar2":"jio",
    "bekar3":'VI',
    "valo":"BSNL"
}
print(ls[1])
print(dc["bekar2"])

print(dict.keys(dc))
print(dict.values(dc))
print(dict.items(dc))