if __name__ == '__main__':
    N = int(raw_input())
    listt=[]
    for i in xrange(N):
        st=raw_input()
        command=str(st.split(" ")[0])
        if command=="insert":
            i,j=map(int,st.split(" ")[1:])
            listt.insert(i,j)
        elif command=="print":
            print listt
        elif command=="remove":
            i=int(st.split(" ")[1])
            listt.remove(i)
        elif command=="append":
            i=int(st.split(" ")[1])
            listt.append(i)
        elif command=="sort":
            listt.sort()
        elif command=="pop":
            listt.pop()
        elif command=="reverse":
            listt.reverse()
           
        
