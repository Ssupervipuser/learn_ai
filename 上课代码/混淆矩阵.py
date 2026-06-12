from sklearn.metrics import confusion_matrix
import pandas as pd


def dmo1():


    # 真实标签(ground truth):
    # 共有 10 个样木:前 6 个是"恶性"(正例)，后 4 个是"良性"(反例)
    y_true =["恶性","恶性","恶性","恶性","恶性","恶性","良性","良性","良性","良性"]
    labels = ["恶性", "良性"]
    df_col = ["恶性(正例)","良性(反例)"]
    # 1.模型 A 的预测结果预测对了3个恶性肿瘤样本，4个良性肿瘤样本print("模型A:")
    # 模型 A 预测:
    # -前了个"恶性"预测正确(TP =3)
    # -后3 个"恶性"被错误预测为"良性"(FN = 3)
    # - 所有 4 个"良性"都预测正确 (TN = 4)
    y_pred1 =("恶性","恶性","恶性","良性","良性","良性","良性","良性","良性","良性")
    result = confusion_matrix(y_true, y_pred1, labels=labels)
    df = pd.DataFrame(result, columns=df_col, index=df_col)
    print(result)

    result=confusion_matrix(y_true,y_pred1,labels=labels)
    df=pd.DataFrame(result,columns=df_col,index=df_col)
    print(result)
    print(df)
if __name__ == '__main__':
    dmo1()