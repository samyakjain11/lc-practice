def longestCommonSubsequence(text1: str, text2: str) -> int:
    # def recursive_subproblem(text1_index, text2_index):
    #     if text1[text1_index] == text2[text2_index]:
    #         return 1 + recursive_subproblem(text1_index + 1, text2_index + 1)
    #     elif text2_index < len(text2) and text1_index < len(text1):
    #         return max(recursive_subproblem(text1_index + 1, text2_index), recursive_subproblem(text1_index, text2_index + 1))
    #     else:
    #         return 0
    text1_length, text2_length = len(text1), len(text2)
    memoized = [[0 for _ in range(text2_length + 1)] for _ in range(text1_length + 1)]

    for text1_index in reversed(range(text1_length)):
        for text2_index in reversed(range(text2_length)):
            if text1[text1_index] == text2[text2_index]:
                memoized[text1_index][text2_index] = 1 + memoized[text1_index + 1][text2_index + 1]
            elif text2_index < len(text2) and text1_index < len(text1):
                memoized[text1_index][text2_index] = max(memoized[text1_index + 1][text2_index], memoized[text1_index][text2_index + 1])
    
    return memoized[0][0]

text1 = "abcde"
text2 = "ace"

print(longestCommonSubsequence(text1, text2))