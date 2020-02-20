"""Python allows negative integers to be used as indices into a sequence, such as a string. If string s has length n,
and expression s[k] is used for index −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references the
same element? """

a_string = 'hello'
# k has to be -2: 'l'
# j has to be k + len(a_string), which == 3: 'l'
