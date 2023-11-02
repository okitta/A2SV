class Solution:
    def countOfAtoms(self, formula: str) -> str:
        idx,size = 0,len(formula)

        count = Counter()
        stack = [count]

        while idx < size:
            if formula[idx] == '(':
                idx += 1
                count = Counter()
                stack.append(count)
            elif formula[idx] == ')':
                idx += 1
                end = idx
                while idx < size and formula[idx].isdigit():
                    idx += 1
                mult = int(formula[end:idx] or 1)
                top = stack.pop()

                for name,value in top.items():
                    stack[-1][name] += value * mult
                
                count = stack[-1]

            else:
                start = idx
                idx += 1

                while idx < size and formula[idx].islower():
                    idx += 1
                
                name = formula[start:idx]
                start = idx

                while idx < size and formula[idx].isdigit():
                    idx += 1
                
                mult = int(formula[start:idx] or 1)

                stack[-1][name] += mult
        
        return "".join(name + (str(count[name]) if count[name] > 1 else '')for name in sorted(count))