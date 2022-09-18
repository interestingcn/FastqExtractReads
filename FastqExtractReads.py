# coding: utf-8
'''

FastExtractReads
用于快速提取指定fastq文件格式中的全部reads信息为独立fq文件
Author：interestingcn01@gmail.com
Date：2022.9.12

'''

fastqFile_path = input('请输入待分离reads数据的fastq文件名称：')
with open(fastqFile_path,'r',encoding='utf8') as file:
    fastq_file = file.read().splitlines()

# 统计reads数量
reads_num = 0
# 存放全部reads信息
reads_list = []
# 存放单条reads信息
reads = []

for line in fastq_file:
    if line.startswith('@') and len(line) < 200:
        if len(reads) != 0:
            reads_list.append(reads)
        # 重置reads列表
        reads = []
        reads_num += 1
        reads.append(line)
        continue
    reads.append(line)
# 用于存储最后一次循环
reads_list.append(reads)


print('======================================')
print(f'在 {fastqFile_path} 中共计存在 {reads_num} 条reads信息')
print('======================================')

user_action = input('按回车键以继续将reads写入磁盘，或直接结束当前程序:')
for read in reads_list:
    file_name = read[0]+'.fastq'
    file_name = file_name.replace('/','-')
    with open('reads/'+file_name,'w',encoding='utf8') as file:
        print('正在写入reads文件：' + read[0])
        for line in read:
            file.write(line +'\n')
print('写入完成！')








