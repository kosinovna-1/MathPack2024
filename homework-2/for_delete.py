def multiplicative_inverse(e: int, phi: int) -> int:
    A = [phi]
    B = [e]
    AmodB = [phi % e]
    celAB = [phi // e]
    while AmodB[-1] != 0:
        A.append(B[-1])
        B.append(AmodB[-1])
        AmodB.append(A[-1] % B[-1])
        celAB.append(A[-1] // B[-1])
    n = len(A)
    x = [0]
    y = [1]
    for i in range(n-1):
        x.append(y[-1])
        y.append(x[-2]-y[-1]*celAB[n-i-2])
    return y[-1]%phi

x = multiplicative_inverse(7,40)
print(x,sep='\n')
