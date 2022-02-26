"""
Promises:
    - ExecuteAS and ExecuteIterAS will block any other execution on the database by threads using the same lock

Not promised:
    - ExecuteAS and ExecuteIterAS will block all other execution on the database
"""
"""
class AtomSafeDB:
    def __init__(self, database: Connection) -> None:
        self.db = database
        self.cursor: Cursor = self.db.cursor()
        
    def generateLock(self) -> Lock:
        return Lock()
    
    def Execute(self, command: str) -> Any:
        return self.cursor.execute(command)
    
    def ExecuteAS(self, commands: List[str], lock: Lock) -> List[Any]:
        lock.acquire()
        results = []
        
        for command in commands:
            results.append(self.cursor.execute(command))
            
        lock.release()
        return results
    
    def ExecuteIterAS(self, function: Callable[[int, List[Any]], Union[Tuple[None, Any], str]], lock: Lock) -> Any:
        lock.acquire()
        step, results = 0, []
        
        while (x := function(step, results))[0] is not None:
            results.append(self.cursor.execute(x))
            step += 1
            
        lock.release()
        return x[1]
"""