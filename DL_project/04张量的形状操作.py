"""
reshape()
unsqueeze
squeeze
transpose
permute
view
contiguous
is_contiguous
"""
import torch
torch.manual_seed(24)

t1=torch.randint(1,10,(2,3))
def dm01():
    print(f't1:{t1},shape:{t1.shape},row:{t1.shape[0]},columns:{t1.shape[1],t1.shape[-1]}')

    #reshape
    t2=t1.reshape(3,2)
    print(f't2:{t2},shape:{t2.shape},row:{t2.shape[0]},columns:{t2.shape[1],t2.shape[-1]}')

def dm02():
    t2=t1.unsqueeze(0)
    print(t2,t2.shape)
    """
    [
    [[6, 9, 9],
     [2, 8, 7]
    ]
    ]
    """
    t3=t1.unsqueeze(1)
    print(t3,t3.shape)
    """
    [[[6, 9, 9]],

        [[2, 8, 7]]
    ]
    """

    t4=t1.unsqueeze(2)
    print(t4,t4.shape)

def dm03():
    t1=torch.randint(1,10,(2,3,4))
    t2=t1.transpose(0,1)
    print(t1,t1.shape)
    print(t2,t2.shape)
    t2=t1.transpose(0,2)
    print(t2,t2.shape)

    #2,3,4->4,2,3
    t2=t1.permute(2,0,1)
    print(t2,t2.shape)

if __name__ == '__main__':
    # dm01()
    # dm02()
    dm03()