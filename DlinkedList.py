class Dnode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    class dlinkedlist:
        def __init__(self):
            self.head = None

        def display(self):
            t = self.head
            while t != None:
                print(t.data, end="<-->")
                t = t.next
            print('None')

        def add_in_start(self, d):
            n = Dnode(d)
            if self.head != None:
                n.next = self.head
                self.head.prev = n
            self.head = n

        def add_in_end(self, d):
            n = Dnode(d)
            if self.head != None:
                t = self.head
                while t.next != None:
                    t = t.next
                t.next = n
                n.prev = t
            else:
                self.head = n
                n.next = self.head
                self.head.prev = n
                self.head = n

        def add_after(self, m, d):
            n = Dnode(d)
            t = self.head
            while t.data != m:
                t = t.next
            n.next = t.next
            n.prev = t
            t.next = n
            n.next.prev = n

        def del_first(self):
            if self.head == None:
                return -1
            self.head = self.head.next
            self.head.prev = None

        def del_lat(self):
            if self.head == None:
                return -1
            t = self.head
            while t.next != None:
                t = t.next
            t.prev.next = None
            t.prev = None

        def delete(self, d):
            t = self.head
            while t.data != d:
                t = t.next
            t.next.prev = t.prev
            t.prev.next = t.next
            t.next = None
            t.prev = None

        def del_mid(self):
            t = self.head
            count = 0
            while t != None:
                count += 1
            t = self.head
            if count % 2 == 0:
                for i in range(count // 2):
                    t = t.next
            else:
                for i in range(count // 2 + 1):
                    t = t.next
            t.next.prev = t.prev
            t.prev.next = t.next
            t.next = None
            t.prev = None
