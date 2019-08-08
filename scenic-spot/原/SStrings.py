def gen_pnext(p):
    """ Generate a list for the next checking index,
    a little revised version.
    """
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m - 1:  # generate pnext[i+1]
        while k >= 0 and p[i] != p[k]:
            k = pnext[k]
        i, k = i + 1, k + 1
        if p[i] == p[k]:
            pnext[i] = pnext[k]
        else:
            pnext[i] = k
    return pnext


def KMPmatching(t, p, pnext):
    """ KMP string matching, a little revised version."""
    j, i = 0, 0
    n, m = len(t), len(p)
    while j < n and i < m:  # i==m means a matching
        while i >= 0 and t[j] != p[i]:
            i = pnext[i]
        j, i = j + 1, i + 1
    if i == m:  # find a matching, return its index
        return j - i
    return -1  # no matching, return special value


def matching(t, p):
    return KMPmatching(t, p, gen_pnext(p))
