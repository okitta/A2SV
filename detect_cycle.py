color=[0]*V
		def dfs(vertex,prev):
		    if color[vertex]==2:
		        return True
		    if color[vertex]==1:
		        return False
		        
		    color[vertex]=1
		    
		    for neigh in adj[vertex]:
		        if neigh != prev:
		            curr=dfs(neigh,vertex)
    		        if not curr:
    		            return curr
    		            
		    color[vertex]=2
		    return True
	    
	    for i in range(V):
	        if color[i]==0:
	            curr=dfs(i,-1)
	            if not curr:
	                return 1
	    return 0