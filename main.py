from buddha import Buddha

if __name__ == '__main__':
    buddha = Buddha()
    buddha.build(iterations=100, n_points=100_000)
    buddha.render(resolution=(1000, 1000))
    buddha.show()
