class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        size = len(skill)
        left_pointer =1 
        right_pointer = size-2
        check_num = skill[0] + skill[right_pointer+1]
        pro = skill[0] * skill[right_pointer+1]
        while left_pointer <= right_pointer:
            num = skill[left_pointer] + skill[right_pointer]
            if num == check_num:
                pro = pro + (skill[left_pointer] * skill[right_pointer])
                right_pointer -= 1
                left_pointer += 1
            else:
                return -1
        return pro