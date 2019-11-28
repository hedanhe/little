import argparse
import math

parser = argparse.ArgumentParser(description='计算圆柱体积')
parser.add_argument('-r', '--radius', type=int, help='Radius ofcyLinder')
parser.add_argument('-H', '--height', type=int, help='Radius height')
group = parser.add_mutually_exclusive_group()       #互斥组
group.add_argument("-v", "--verbose", action="store_true")  #可选参数
group.add_argument("-q", "--quiet", action="store_true")
args = parser.parse_args()

def cyLinder_volume(radius, height):
    vol = (math.pi) * (radius ** 2) * height
    return vol

if __name__ == '__main__':
    vol = cyLinder_volume(args.radius, args.height)
    print("圆柱体积%s"%vol)
    if args.quiet:
        print("可选参数有-q %s" % args.quiet)
    elif args.verbose:
        print("可选参数有-v %s" % args.verbose)
    else:
        print("没有参数")
