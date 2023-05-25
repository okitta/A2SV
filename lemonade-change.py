class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        total = {5:0,10:0,20:0}
        for bill in bills:
            total[bill]+=1
            if bill==10:
                if total[5]>0:
                    total[5]-=1
                else:
                    return False
            elif bill==20:
                if total[10]>0 and total[5]>0:
                    total[10]-=1
                    total[5]-=1
                elif total[5]>2:
                    total[5]-=3
                else:
                    return False

        return True