import operator
urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "https://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png",
    "http://gliacloud.com/hh.png",

]

def main():
    result = {}
    filenames = map(lambda url: url.strip().split("/")[-1], urls)
    for filename in filenames:
        if filename in result.keys():
            result[filename] += 1
        else:
            result[filename] = 1 
    return sorted(result.items(), key=operator.itemgetter(1))


if __name__ == '__main__':
    filelist = main()[-3::]
    for filename in filelist[::-1]:
        print("{0} {1}".format(filename[0], filename[1])) 