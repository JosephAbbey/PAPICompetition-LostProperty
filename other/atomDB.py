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
"""
class AtomSafeDB (Database)
    Execute (command: str) -> Result:
        Returns the result of the command being executed in the database with NO ATOMIC SAFETY
    
    GenerateLock -> threading.lock:
        Returns a threading.lock()

    ExecuteAS (commands: List[str], obj: threading.lock) -> List
        Wait until lock can aquired
        Execute each command in turn and store result
        Release lock
        Return results

    ExecuteIterAS (function: F (int, List[str]) -> Union[Tuple[None, Any], str], obj: threading.lock) -> Any
        Wait until lock can aquired
        Initiate step to 0
        While F(step, results) is not (None, x),
            Run result of F(step, result)
            Store result
            Increment step
        Release lock
        Return F(step, results)[1]
"""