import sys
import difflib

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except IOError:
        print("ERROR: 没有找到文件:%s或读取文件失败！" % filename)
        sys.exit(1)

def compare_file(file1, file2, out_file):
    f1 = open(file1)
    f2 = open(file2)
    line1 = f1.readline()
    line2 = f2.readline()
    fout = open(out_file, "w")
    while line1 and line2:
        if line1 != line2:
            print("c :", line1.strip(), "\t\tpy:", line2.strip(), file=fout)
        line1 = f1.readline()
        line2 = f2.readline()
    fout.close()

if __name__ == '__main__':
    compare_file(r'result_c.txt', r'result_py.txt', r'compare_result.html')
