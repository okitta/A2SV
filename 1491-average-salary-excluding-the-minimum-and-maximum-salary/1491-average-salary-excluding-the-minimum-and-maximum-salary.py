class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary_sum = sum(salary[1:-1])
        average_salary = salary_sum/(len(salary)-2)
        return average_salary
        