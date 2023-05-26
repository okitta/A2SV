graph=defaultdict(set)
        count=defaultdict(int)
        
        for i in range(1,len(alien_dict)):
            prev=alien_dict[i-1]
            curr=alien_dict[i]
     
            for j in range(min(len(prev),len(curr))):
                if prev[j]!=curr[j] :
                    if curr[j] not in graph[prev[j]]:
                        graph[prev[j]].add(curr[j])
                        count[curr[j]]+=1
                    break
        
        queue=deque()
        for i in range(K):
            letter=chr(97+i)
            if count[letter]==0:
                queue.append(letter)
         
        result=[]
        while queue:
            curr=queue.popleft()
            result.append(curr)
            
            for neigh in graph[curr]:
                count[neigh]-=1
                if count[neigh]==0:
                    queue.append(neigh)
                    
        return result