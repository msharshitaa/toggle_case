def toggle_case(A):
    N=len(A)
    A=list(A)
    for i in range(N):
        if 65<=ord(A[i])<=90:  
            A[i]=chr(ord(A[i])+32)  
        elif 97<=ord(A[i])<=122:  
            A[i]=chr(ord(A[i])-32)  
    return ''.join(A)
A=input()
print(toggle_case(A))
