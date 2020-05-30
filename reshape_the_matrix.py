class Sol:
    def reshape_the_matrix(self,arrs,r,c):
        x=[]
        y=[]
        for arr in arrs:
            for num in arr:
                x.append(num)
        for i in range(r):
            y.append(list(x[i*c:i*c+c]))

        return y

if __name__ == '__main__':
    p1=Sol()
    print(p1.reshape_the_matrix([[1,2],[3,4],[5,6]],2,3))
