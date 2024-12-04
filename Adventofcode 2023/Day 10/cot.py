    for y in Tile.Map:
        y = list(filter(lambda x: x.distance != -1 and x.type != Types.CROSS, y))
        containing = False
        for n, x in enumerate(y):
            if (x.type in Types.P[1]):
                if (y[n-1].type != Types.P[0][Types.P[1].index(x.type)]):
                    containing = not containing

            elif (x.type == Types.STRAIGHT):
                containing = not containing

            if (containing and n < len(y)-1):
                c += y[n+1].x - x.x - 1