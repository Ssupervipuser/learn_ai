import torch

data=torch.tensor([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]])

# print(data[:,0])
# print(data[:2,0:-1])



list1=[1,2,3,4]
# print(list1[2:])
# print(list1[-2:])

def f01():
    torch.manual_seed(40)
    d1=torch.randint(0,10,[2,2])
    d2=torch.randint(0,10,[2,2])
    print(d1)
    print(d2)

    new_d=torch.cat([d1,d2],dim=0)
    print(new_d)

    new_d=torch.cat([d1,d2],dim=1)
    print(new_d)
def f2():
    a=torch.tensor([[1,2],[3,4]])
    b=torch.tensor([[5,6],[7,8]])

    new_data=torch.stack([a,b],dim=0)
    print(new_data,new_data.shape)


    new_data = torch.stack([a, b], dim=1)
    print(new_data, new_data.shape)

    new_data = torch.stack([a, b], dim=2)
    print(new_data, new_data.shape)
if __name__ == '__main__':
    # f01()
    f2()