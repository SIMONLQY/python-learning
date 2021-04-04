# 输入：依次输入目标函数的c向量，之后一行一行输入方程组的系数矩阵，输出是最优解和最优值或无解或无界
import numpy as np


def pan_duan_dan_wei(A):
    """这个函数是判断A矩阵里有什么样的单位向量排布，好决定人工变量个数"""
    """返回形式是一个和A同列数的行向量，每个元素是k时表示A这一列为ek，为零时则表示这一列不是单位向量"""
    cows = len(A)
    cols = len(A[0])
    bools = [-1 for i in range(cols)]
    for i in range(cows):
        for j in range(cols):
            # 首先找到某个元素是1，这一列进入状态-2（备选是单位向量），如果发现其他都是零，则是单位向量，如果发现非零，则非单位
            if A[i][j] == 1:
                bools[j] = -2
                for k in range(cows):
                    if A[k][j] != 0 and k != i:
                        bools[j] = 0
                if bools[j] == -2:
                    bools[j] = i + 1
    for i in range(cols):
        if bools[i] == -1:
            bools[i] = 0
    return bools


def dan_chun_xing_fa(A_all, c, b_num):
    """有初始基本可行解之后的单纯形法"""
    A_all = np.array(A_all)
    b_num = np.array(b_num)
    c = np.array(c)  # 没有这一步，c无法根据下一步取元素

    cb = c[b_num]
    A = A_all[:, :-1]
    b = A_all[:, -1]
    b = np.array([b])
    x = np.zeros(len(A[0]))
    # 按照下标取出对应的列数据
    B = A_all[:, b_num]
    B = np.squeeze(B)

    judge_vector = np.squeeze(np.dot(np.dot(cb.T, np.linalg.inv(B)), A) - c.T)
    judge = max(judge_vector)
    A = np.dot(np.linalg.inv(B), A)
    b = np.squeeze(np.dot(np.linalg.inv(B), b.T))
    while judge > 0:
        k = np.where(judge_vector == max(judge_vector))
        k = np.array(np.squeeze(k))
        if np.size(k) != 1:
            k = k[0]
        A_k = np.squeeze(A[:, k])
        if max(A_k) <= 0:
            return "无界"
        else:
            u = min([b[i] / A_k[i] for i in range(len(b)) if A_k[i] > 0])
            r = np.where([(b[i] / A_k[i] if A_k[i] > 0 else u-1) for i in range(len(b))] == u)  # 返回是一个array
            b_num = np.squeeze(b_num)
            b_num[r[0]] = k
        B = np.squeeze(A[:, b_num])
        cb = c[b_num]
        judge_vector = np.dot(np.dot(cb.T, np.linalg.inv(B)), A) - c.T
        judge_vector = np.squeeze(judge_vector)
        judge = max(judge_vector)
        A = np.dot(np.linalg.inv(B), A)
        b = np.squeeze(np.dot(np.linalg.inv(B), b.T))
    x[b_num] = b
    return b_num, x, np.dot(c.T, x)


def di_yi_jie_duan(A, b, new_x, I):
    """两阶段法第一阶段，构造辅助问题并求解初始可行解"""
    # 将A矩阵扩充成辅助问题的A矩阵
    A = A.tolist()
    cows = len(A)
    ori_cols = len(A[0])
    for i in range(len(new_x)):
        for j in range(cows):
            A[j].append(1 if j == new_x[i] - 1 else 0)
    cols = len(A[0])  # 此时的cols为变量数目
    # 增广矩阵A_big
    A_big = np.array(A)
    A_big = A_big.tolist()
    for i in range(cows):
        A_big[i].append(b[i])
    # 辅助问题的目标函数
    g = [0 for i in range(cols)]
    for i in range(len(new_x)):
        g[-(1 + i)] = 1
    # 找到辅助问题的b_num
    bools = pan_duan_dan_wei(A)
    b_num = []
    for i in range(len(I)):
        bools = np.array(bools)
        l = np.where(bools == I[i])  # 返回一个array
        b_num.append(l[0])
    # 单纯形法求解辅助问题
    b_num, x, g_result = dan_chun_xing_fa(A_big, g, b_num)
    while 1:
        if g_result > 0:
            return [0 for i in range(len(ori_cols)+2)]  # 无解,返回一个比A列数还多的基矩阵
        elif max(b_num) < ori_cols:  # 如果g=0且基变量中没有人工变量
            return b_num
        else:  # 如果g=0且基变量中有人工变量，可以通过有限步将人工变量剔除
            br = np.where(b_num == max(b_num))  # where返回array
            r = np.squeeze(b_num[br[0]])
            A_big = np.array(A_big)
            B = np.squeeze(A_big[:, b_num])
            A_ = np.dot(np.linalg.inv(B), A)
            if max(np.squeeze(A_[br[0]])) != 0:
                j = np.where(np.squeeze(A_[br[0]]) == max(np.squeeze(A_[br[0]])))
                b_num[br] = j
            if min(np.squeeze(A_[br[0]])) != 0:
                j = np.where(np.squeeze(A_[br[0]]) == min(np.squeeze(A_[br[0]])))
                b_num[br[0]] = j
            # 将出基的人工变量删除
            A_big = A_big.tolist()
            for j in range(cows):
                A_big[j].pop(r)
            g.pop(r)
            A_big = np.array(A_big)
            b_num, x, g_result = dan_chun_xing_fa(A_big, g, b_num)
    return b_num


def liang_jie_duan(A_big, c):
    """两阶段法程序"""
    cows = len(A_big)
    cols = len(A_big[0]) - 1
    # 分离出A
    A_big = np.array(A_big)
    A = A_big[:, :-1]
    b = A_big[:, -1]

    # 第一阶段，找到初始基本可行解
    bools = pan_duan_dan_wei(A)
    I = list(range(1, cows + 1))
    new_x = [i for i in I if i not in bools]
    first_ji_num = []
    if len(new_x) != 0:
        # 不等于零说明单位向量数目不够，需要添加人工变量，并进行第一阶段找初始基本可行解
        first_ji_num = di_yi_jie_duan(A, b, new_x, I)
    else:
        # 等于0则代表原矩阵已经有了单位阵，容易找到初始基本可行解
        for i in range(len(I)):
            bools = np.array(bools)
            l = np.where(bools == I[i])  # 返回一个array
            first_ji_num.append(l[0])
    # 中间第一阶段如果出现辅助问题最优大于零，说明原问题无解
    if len(first_ji_num) > len(A):
        return "无解"

    # 第二阶段，用单纯形法找到最优解
    b_num, x, z_result = dan_chun_xing_fa(A_big, c, first_ji_num)
    return x, z_result


if __name__ == '__main__':
    A_big = [[1, 1, 1, 1, 1, 0, 0, 30],
             [3, 6, 1, -2, 0, 1, 0, 0],
             [0, 1, 0, 0, 0, 0, -1, 4]]
    c = [-3, -4, -2, 0, 0, 0, 0]
    # i = 1
    # while 1:
    #     print("本程序只适合标准形式的线性规划问题")
    #     msg = input("请输入第" + str(i) + "行方程组的系数：" + "（输入over结束输入）")
    #     if msg != "over":
    #         A_big.append([float(a) for a in msg.split()])
    #         i += 1
    #     else:
    #         c = [float(a) for a in input("请输入目标函数系数：").split()]
    #         break
    x, c = liang_jie_duan(A_big, c)
    print(x)
    print(c)
