import numpy as np
class fitting():
    def __init__(self):
        pass

    def position_matrix_Cartesian(self, X, Y, order=3, par_x=-1, par_y=-1):
        N=0
        for ii in range(order+1):
            N=N+ii+1
        # print(N)
        if par_x==-1:
            par_x=2**N-1
        if par_y==-1:
            par_y=2**N-1
        # print(par_x,par_y)
        powerMat=self.get_powerMat(order=order)
        M_x = []
        M_y = []
        for m in range(len(powerMat)):
            M_x.append(X**powerMat[m,0]*Y**powerMat[m,1])
        for m in range(len(powerMat)):
            M_y.append(Y**powerMat[m,0]*X**powerMat[m,1])
        # print("M_x",M_x)       
        M_x = np.asarray(M_x).T
        M_y = np.asarray(M_y).T
        print("M_x",M_x,M_x.shape)

        intlist1 = np.array(list(map(int, reversed(list(np.binary_repr(par_x, width=N))))))
        print("intlist1",intlist1)
        print([bool(ii)for ii in intlist1])
        M_x=M_x[:,[bool(ii)for ii in intlist1]]
        intlist2 = np.array(list(map(int, reversed(list(np.binary_repr(par_y, width=N))))))
        M_y=M_y[:,[bool(ii)for ii in intlist2]]

        return M_x, M_y

    def get_powerMat(self,order=3):
        powerMat = []
        for i in range(order+1):
            for ii in range(i+1):
                xorder = i - ii
                yorder = ii
                powerMat.append([xorder,yorder])
        return np.asmatrix(powerMat)

    def hoc_ihoc_modeling(self,numraw_input,wpar_x=1023, wpar_y=1023, rpar_x=1023, rpar_y=511, order=3):
        N=0
        for i in range(order+1):
            N=N+i+1
        k_para_x_2N = np.zeros((2*N,1))
        k_para_y_2N = np.zeros((2*N,1))
        num_raw = numraw_input.copy()
        model_hosr = numraw_input.copy()
        resi_hosr = numraw_input.copy()

        #offset 제거
        rpar_x=rpar_x -1
        rpar_y=rpar_y -1

        intlist1 = np.array(list(map(int, reversed(list(np.binary_repr(wpar_x,width=N))))))
        intlist2 = np.array(list(map(int, reversed(list(np.binary_repr(wpar_y,width=N))))))
        intlist3 = np.array(list(map(int, reversed(list(np.binary_repr(rpar_x,width=N))))))
        intlist4 = np.array(list(map(int, reversed(list(np.binary_repr(rpar_y,width=N))))))

        index_w_x = np.where(intlist1==1)[0]
        index_w_y = np.where(intlist2==1)[0]
        index_r_x = np.where(intlist3==1)[0]
        index_r_y = np.where(intlist4==1)[0]
        
        gfX = num_raw.loc[:,'gfX'].values
        gfY = num_raw.loc[:,'gfY'].values
        fX = num_raw.loc[:,'fX'].values/10
        fY = num_raw.loc[:,'fY'].values/10

        Mw_x,Mw_y = self.position_matrix_Cartesian(gfX,gfY,order,par_x=wpar_x, par_y=wpar_y)
        Mf_x,Mf_y = self.position_matrix_Cartesian(fX,fY,order,par_x=rpar_x, par_y=rpar_y)
        # Mw_x,Mx_y = self.position_matrix_Cartesian(gfX,gfY,order,par_x=wpar_x, par_y=wpar_y)
        # Mf_x,Mf_y = self.position_matrix_Cartesian(fX,fY,order,par_x=rpar_x, par_y=rpar_y)

        if len(Mf_x) !=0:
            M_x = np.concatenate((Mw_x,Mf_x),axis=1)
        else:
            M_x = Mw_x

        if len(Mf_y) !=0:
            M_y = np.concatenate((Mw_y,Mf_y),axis=1)
        else:
            M_y = Mw_y

        k_para_x, res_x, rank_x, s_x = np.linalg.lstsq(M_x, np.asmatrix(num_raw.loc[:,'u'].T, rcond=None))
        k_para_y, res_y, rank_y, s_y = np.linalg.lstsq(M_y, np.asmatrix(num_raw.loc[:,'v'].T, rcond=None))

        k_para_x_2N[list(np.concatenate((index_w_x,index_r_x)))] = k_para_x
        k_para_y_2N[list(np.concatenate((index_w_y,index_r_y)))] = k_para_x

        model_hosr.loc[:,'u'] = M_x * k_para_x
        model_hosr.loc[:,'v'] = M_y * k_para_y
        
        resi_hosr.loc[:,['u','v']] = num_raw.loc[:,['u','v']] - model_hosr.loc[:,['u','v']]

        K = np.concatenate([k_para_x_2N,k_para_y_2N],axis=1)
        
        return model_hosr,resi_hosr,K

order=2

a=fitting()
# print(a.get_powerMat(3))
print(a.position_matrix_Cartesian((2,-1),(3,-1),3,-1,-1))