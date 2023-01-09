class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dictionary = defaultdict(int)
        for cpdomain in cpdomains:
            count,cpdomain = cpdomain.split()
            count = int(count)
            dictionary[cpdomain] += count
            position = cpdomain.find('.')+1
            while position > 0:
                dictionary[cpdomain[position:]]+=count
                position = cpdomain.find('.',position)+1
        for key,value in dictionary.items():
            yield f'{value} {key}' 
        