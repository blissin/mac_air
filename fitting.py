import numpy as np

def hoc_ihoc_modeling(self,numraw_input,wpar_x=1023, wpar_y=1023, rpar_x=1023, rpar_y=511, order=3):
    N=0
    for i in range(order+1):
        N=N+i+1
    k_hosr_x_2N = np.zeros((2*N,1))
    k_hosr_y_2N = np.zeros((2*N,1))
    num_raw = numraw_input.copy()
    model_hosr = numraw_input.copy()
    resi_hosr = numraw_input.copy()

    #offset 제거
    rpar_x=rpar_x -1
    rpar_y=rpar_y -1

    intlist1 = np.array(list(map(int, reversed(list(np.binarry_repr(wpar_x,width=N))))))
    intlist2 = np.array(list(map(int, reversed(list(np.binarry_repr(wpar_y,width=N))))))
    intlist3 = np.array(list(map(int, reversed(list(np.binarry_repr(rpar_x,width=N))))))
    intlist4 = np.array(list(map(int, reversed(list(np.binarry_repr(rpar_y,width=N))))))

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

    k_hosr_x, res_x, rank_x, s_x = np.linalg.lstsq(M_x, np.asmatrix(num_raw.loc[:,'u'].T, rcond=None))
    k_hosr_y, res_y, rank_y, s_y = np.linalg.lstsq(M_y, np.asmatrix(num_raw.loc[:,'v'].T, rcond=None))

    k_hosr_x_2N[list(np.concatenate((index_w_x,index_r_x)))] = k_hosr_x
    k_hosr_y_2N[list(np.concatenate((index_w_y,index_r_y)))] = k_hosr_x

    model_hosr.loc[:,'u'] = M_x * k_hosr_x
    model_hosr.loc[:,'v'] = M_y * k_hosr_y
    
    resi_hosr.loc[:,['u','v']] = num_raw.loc[:,['u','v']] - model_hosr.loc[:,['u','v']]

    K = np.concatenate([k_hosr_x_2N,k_hosr_y_2N],axis=1)
    
    return model_hosr,resi_hosr,K