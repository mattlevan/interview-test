import sys


class stack(list):
    def push(self, k):
        """Push integer k onto the stack."""
        self.append(k)
    
    def empty(self):
        """Check if the stack is empty."""
        return not self
    
    def top(self):
        """Print the top element of the stack or EMPTY if it's empty."""
        if self.empty():
            return 'EMPTY'
        else:
            return self[len(self) - 1]
    
    def inc(self, e, k):
        """Add k to each of the bottom e elements of the stack."""
        if not self.empty() and e <= len(self):
            for i in range(0, e):
                self[i] = self[i] + k


def superStack(ops):
    """Create an empty stack and perform n operations to it in order, and 
    after performing each operation, print the value of stack's top element on 
    a new line; if the stack is empty, print EMPTY instead.

    Parameters:
    ops (list): A list of n strings
    """
    s = stack()

    for op in ops[1:]:
        print(op)
        op = op.split()
        if op[0] == 'push':
            s.push(int(op[1]))
        elif op[0] == 'pop':
            s.pop()
        elif op[0] == 'inc':
            e = int(op[1])
            k = int(op[2])
            s.inc(e, k)
        print(s.top())


if __name__ == '__main__':
    ops = []
    for line in sys.stdin:
        if line == '\n':
            break
        ops.append(line.rstrip())
    superStack(ops)