import numpy as np

def markov():
    """
    马尔科夫链预测
    """
    initmat = np.array([1,0])
    transMat = np.array([[0,1],\
                        [1/6,5/6]])

    restmp = initmat
    for i in range(10):
        res = np.dot(restmp,transMat)
        print(res)
        restmp = res

#end markov

markov()