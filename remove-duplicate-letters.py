#
#


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = defaultdict(int)
        for idx in range(len(s)):
            last_index[s[idx]] = idx
        mono_stack = []
        mono_stack_set = set()
        for idx in range(len(s)):
            if s[idx] not in mono_stack_set:
                while mono_stack and s[idx] < mono_stack[-1] and idx < last_index[mono_stack[-1]]:
                    mono_stack_set.remove(mono_stack.pop())
                mono_stack.append(s[idx])
                mono_stack_set.add(s[idx])
        return "".join(mono_stack)