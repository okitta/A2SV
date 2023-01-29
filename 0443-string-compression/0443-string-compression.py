class Solution:
    def compress(self, chars: List[str]) -> int:
        string = ''
        counter = 1
        left = 0
        right = 1
        size = len(chars)
        arr = []
        for item in chars:
            string += item
        if size == 1:
            return 1
        while right < size and left < size:
                if len(arr) == 0:
                    arr.append(string[0])
                if string[left] == string[right]:
                    counter += 1
                    right += 1
                else:
                    if counter > 1:
                        counter = str(counter)
                        for item in counter:
                            arr.append(item)
                    arr.append(string[right])
                    left = right
                    right = left+1
                    counter = 1
        if counter > 1:
            counter = str(counter)
            for item in counter:
                arr.append(item)
        chars.clear()
        for item in arr:
            chars.append(item)
        return len(arr)
                    
        
                