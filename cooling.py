def cooling(reactor):

    while reactor.is_hot():
        reactor.add_water()

