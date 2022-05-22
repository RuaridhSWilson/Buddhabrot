from buddha import Buddha

if __name__ == '__main__':
    buddha = Buddha()
    buddha.build(iterations=100, n_points=1000)
    buddha.render(resolution=(10, 10))
    print(buddha.image)
