class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # win = defaultdict(int)
        loss = defaultdict(int)
        for match in matches:
            loss[match[1]] += 1
        no_loss = []
        one_loss = []
        visited = set()
        for match in matches:
            if loss[match[0]] == 0 and match[0] not in visited:
                no_loss.append(match[0])
                visited.add(match[0])
            elif loss[match[0]] == 1 and match[0] not in visited:
                one_loss.append(match[0])
                visited.add(match[0])
            if loss[match[1]] == 0 and match[1] not in visited:
                no_loss.append(match[1])
                visited.add(match[1])
            elif loss[match[1]] == 1 and match[1] not in visited:
                one_loss.append(match[1])
                visited.add(match[1])
        no_loss.sort()
        one_loss.sort()
        return [no_loss,one_loss]