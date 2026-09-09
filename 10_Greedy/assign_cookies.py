"""
Assign Cookies

Given:
    g[i] = minimum cookie size required by child i
    s[j] = size of cookie j

Each child can receive at most one cookie.

Goal:
    Maximize the number of satisfied children.

Greedy Strategy:
    Match each child with the smallest cookie that can satisfy them.

Time Complexity:
    O(n log n + m log m) - sorting
    O(n + m)             - two-pointer traversal

Space Complexity:
    O(1) auxiliary space
"""


def find_content_children(g, s):
    """
    Return the maximum number of children that can be satisfied.

    Args:
        g: List of children's greed factors.
        s: List of available cookie sizes.

    Returns:
        Maximum number of satisfied children.
    """

    # Sort both lists so we can make the smallest
    # possible valid assignment.
    g.sort()
    s.sort()

    child = 0
    cookie = 0

    while child < len(g) and cookie < len(s):

        # If this cookie can satisfy the current child,
        # assign it and move to the next child.
        if s[cookie] >= g[child]:
            child += 1

        # Whether assigned or not, this cookie is now used.
        cookie += 1

    return child


if __name__ == "__main__":
    greed = [1, 2, 3]
    cookies = [1, 1]

    result = find_content_children(greed, cookies)

    print("Maximum satisfied children:", result)
