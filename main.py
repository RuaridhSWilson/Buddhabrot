from buddha import Buddha

if __name__ == '__main__':
    buddha = Buddha()
    buddha.build(iterations=100, n_points=3)
    print(buddha.paths)
