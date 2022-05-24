from buddha import Buddha

if __name__ == '__main__':
    buddha = Buddha()
    buddha.build(iterations=100, n_points=1_000_000)
    buddha.render(resolution=(500, 500), zoom=1.2, offset=(0, 100))
    buddha.show()
