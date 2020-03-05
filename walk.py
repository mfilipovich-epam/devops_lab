
import argparse
import os

parser = argparse.ArgumentParser(description="directiry list")
parser.add_argument("--version", action="version", version='version  \
    0.21 created by Maxim Filipovich', help="print version")
parser.add_argument("--dir", nargs='?', default='./', help="define dir")
parser.add_argument("--parent", "-p", action="store_true", help="output \
    files only from the parent directory")
parser.add_argument("--recur", "-r", action="store_true", help="list \
    files recursively")
parser.add_argument("--exten", "-e", nargs='?', default=None, help="filter \
    by file extension")
parser.add_argument("--filename", "-f", action="store_true", help="order \
    output by filename")
parser.add_argument("--date", "-d", action="store_true", help="order \
    output by date of creation")
args = parser.parse_args()

ext = args.exten
folder = args.dir
l1 = []


def list_files_rec(path):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                l1.append([entry.name, entry.stat().st_ctime])
            elif entry.is_dir():
                list_files_rec(entry.path)
    return l1


def list_files_par(path):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                l1.append([entry.name, entry.stat().st_ctime])
    return l1


def sort_files_ext(tmp, key):
    l2 = []
    for entry in tmp:
        if str(os.path.splitext(entry[0])[1][1:]) == key:
            l2.append(entry)
    return l2


if args.parent and not args.recur:
    lis = list_files_par(folder)
elif args.recur and not args.parent:
    lis = list_files_rec(folder)
else:
    print("only one type of searching could be define")
    exit(-2)

if args.filename and not args.date:
    lis.sort(key=lambda x: x[0])
elif args.date and not args.filename:
    lis.sort(key=lambda x: x[1])
else:
    print("only one sort could be define")
    exit(-2)

if args.exten:
    lis = sort_files_ext(lis, ext)

for files in lis:
    print(files[0])
