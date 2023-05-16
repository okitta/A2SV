class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.graph = defaultdict(list)
        self.dead = defaultdict(bool)
        

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)

        

    def death(self, name: str) -> None:
        self.dead[name] = True

        

    def getInheritanceOrder(self) -> List[str]:
        visited = set()
        cur = [self.kingName] if not self.dead[self.kingName] else []
        def successor(parent,cur_order):
            if parent not in visited:
                visited.add(parent)
                for suc in self.graph[parent]:
                    if not self.dead[suc]:
                        cur_order.append(suc)
                    successor(suc,cur_order)
                return cur_order
        return successor(self.kingName,cur)   

        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()