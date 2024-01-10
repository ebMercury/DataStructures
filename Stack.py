class Stack():
    def __init__(self,limit=10):
        self.stack=[]
        self.limit=limit

    def peek(self):
        if len(self.stack)<=0:
            return -1
        
        else:
            return self.stack[len(self.stack)-1]
        
    def display(self):
        if len(self.stack)<=0:
            return -1
        else:
            for i in self.stack:
                print(i)

#تمرین : با استفاده از ساختمان داده پشته تابع ای را بنویسید که عددی را از مبنای 10 به 2 ببرد
    def dec2bin(number):
        s=Stack()
        while number>0:
            r=number%2
            s.push(r)
            number=number//2

        b=""
        while not s.is_empty():
            b=b+str(s.pop())
            return b

    def is_empty(self):
        if len(self.stack)<=0:
            return True
        else:
            return False
        

#تمرین :با اسفاده از پشته تابع ای بنویسید که محتوای یک لیست را معکوس کند
    
    def reverse(lst):
        s=Stack()
        for e in lst:
            s.push(e)
        for i in range(len(lst)):
            lst[i]=s.pop()

    def revers_Stack(s):
        s1=Stack()
        s2=Stack()
        while not s.is_empty():
            s1.push(s.pop())
        while not s1.is_empty():
            s2.push(s1.pop())
        while not s2.is_empty():
            s.push(s2.pop())

    def respost(self, lst):
        for e in lst:
            if e == '*':
                t2 = self.pop()
                t1 = self.pop()
                if t1 is not None and t2 is not None:
                    t = t1 * t2
                    self.push(t)

            elif e == '+':
                t2 = self.pop()
                t1 = self.pop()
                if t1 is not None and t2 is not None:
                    t = t1 + t2
                    self.push(t)

            elif e == '-':
                t2 = self.pop()
                t1 = self.pop()
                if t1 is not None and t2 is not None:
                    t = t1 - t2
                    self.push(t)

            elif e == '/':
                t2 = self.pop()
                t1 = self.pop()
                if t1 is not None and t2 is not None and t2 != 0:
                    t = t1 / t2
                    self.push(t)
            else:
                self.push(e)
        return self.pop()

    def match_s(self, str):
        pairs = {')': '(', ']': '[', '}': '{'}
        for i in str:
            if i in '({[':
                self.push(i)
            elif i in ')]}':
                if self.is_empty() or self.peek() != pairs[i]:
                    return False
                else:
                    self.pop()
        return self.is_empty()
