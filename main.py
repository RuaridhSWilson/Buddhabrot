from buddha import Buddha

if __name__ == '__main__':
    buddha = Buddha()
    buddha.build(iterations=100, n_points=1_000_000, spawn_limit=2)
    buddha.render(resolution=(1000, 1000), zoom=1, offset=(0, 0))
    buddha.show()
