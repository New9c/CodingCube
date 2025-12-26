for i in range(5):
    for j in range(5):
        for k in range(5):
            ni = (i-2)/2
            nj = (j-2)/2
            nk = (k-2)/2
            if abs(ni)==1 and abs(nk)==1 and abs(nj)==1:
                pass
            elif abs(nk)==1 and abs(nj)==1:
                print([ni, nj, nk])
            elif abs(ni)==1 and abs(nk)==1:
                print([ni, nj, nk])
            elif abs(ni)==1 and abs(nj)==1:
                print([ni, nj, nk])
            """
            elif abs(nk)==0 and abs(nj)==0:
                print([ni, nj, nk])
            elif abs(ni)==0 and abs(nk)==0:
                print([ni, nj, nk])
            elif abs(ni)==0 and abs(nj)==0:
                print([ni, nj, nk])
        """
