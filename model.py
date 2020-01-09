import numpy as np


def caculate(x1,x2,x3,x4,x5,x6):
    poly = np.array([[1.324, 44.535, 22.865, -1017.983, -1326.591, -2.854, -84.980]])
    params = np.array([[x1], [x2], [x3], [x4], [x5], [x6], [1]])
    # print("你的多项式参数为 : ===========>\n {}".format(poly))
    # print("你的输入参数为:============>\n {}".format(params))
    res_matrix =  np.dot(poly,params)
    print("你的结果为:" )
    print(round(res_matrix[0][0],2))

def getParams():
    """
    get params x1~x6
    """
    params = []
    params_string = ["反应时间 hour", "投氯量 mg/L", "pH值", "Na+离子强度 M", "Ca2+离子强度 M", "胶体浓度 mg/L"]
    for s in params_string:
        print("请输入你的{}: ".format(s))
        x = input()
        params.append(float(x))
    
    print("你的输入参数为: \n {}".format(params))
    return params

def main():
    params = getParams()
    res = caculate(*params)

if __name__ == "__main__":
    main()
    # x1 = 48
    # x2 = 0.5
    # x3 = 7
    # x4 = 0
    # x5 = 0
    # x6 = 0 
    # caculate(x1,x2,x3,x4,x5,x6)