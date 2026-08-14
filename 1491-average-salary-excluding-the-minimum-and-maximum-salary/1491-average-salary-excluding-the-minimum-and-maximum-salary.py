class Solution(object):
    def average(self, salary):
        return (sum(salary)-min(salary)-max(salary))/(len(salary)-2)