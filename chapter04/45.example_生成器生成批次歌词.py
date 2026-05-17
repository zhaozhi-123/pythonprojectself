"""
基于传入数据，创建生成器，生成批次歌词
"""
import math


def dataset_loader(batch_size):
    """
    自定义批量生成器
    :param batch_size:  #每批次的条数
    :return:            #生成器，每个元素都是一批次的数据
    """

    #读取文件数据
    with open('dataset.txt','r') as src_f:
        #一次读取所有行
        lines = src_f.readlines()

        #计算批次总数
        total_batch = math.ceil(len(lines)/batch_size)

        #获取每批次的数据，收到生成器中
        for idx in range(total_batch):  #idx的值：0，1，2，3，4
            #第一批歌词，批次索引（idx=0）,歌词为：第1条~第8条，索引为0~7
            #第二批歌词，批次索引（idx=1）,歌词为：第9条~第16条，索引为8~15
            #第三批歌词，批次索引（idx=2）,歌词为：第17条~第124条，索引为16~23
            yield lines[idx*batch_size:(idx+1)*batch_size]  #第一批

dl=dataset_loader(8)
print(next(dl))#第一批
print(next(dl))#第二批

for batch_data in dl:
    print(batch_data)

