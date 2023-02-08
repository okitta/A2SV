class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        size = len(skill)
        left_pointer =1 
        right_pointer = size-2
        check_num = skill[0] + skill[right_pointer+1]
        check = []
        check.append(skill[0])
        check.append(skill[right_pointer+1])
        while left_pointer <= right_pointer:
            num = skill[left_pointer] + skill[right_pointer]
            if num == check_num:
                check.append(skill[left_pointer])
                check.append(skill[right_pointer])
                right_pointer -= 1
                left_pointer += 1
            else:
                return -1
        # print(check)
        pro = 0
        right = 1
        left = 0
        while right < len(check):
            pro = pro + (check[left]*check[right])
            # print(pro)
            left += 2
            right = left+1
        return pro