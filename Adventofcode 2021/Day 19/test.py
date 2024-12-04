from collections import deque
from itertools import product, permutations


def compute_orientations(beacon, include_all=False):
    oriented_coords = []
    x, y, z = beacon
    for i in range(3):  # fixed axis
        base = [x, y, z]
        for _ in range(4):
            base[i], base[i - 1] = base[i - 1], -base[i]
            for _ in range(4):  # rotations
                base[i - 1], base[i - 2] = -base[i - 2], base[i - 1]
                if include_all or tuple(base[:]) not in oriented_coords:
                    oriented_coords.append(tuple(base[:]))

        base = [x, y, z]
        for _ in range(4):
            base[i], base[i - 2] = base[i - 2], -base[i]
            for _ in range(4):  # rotations
                base[i - 1], base[i - 2] = -base[i - 2], base[i - 1]
                if include_all or tuple(base[:]) not in oriented_coords:
                    oriented_coords.append(tuple(base[:]))

    return oriented_coords


def compute_vectors(beacons):
    starting_point_by_vector = {}
    for i, j in permutations(range(len(beacons)), 2):
        vector = (
            beacons[i][0] - beacons[j][0],
            beacons[i][1] - beacons[j][1],
            beacons[i][2] - beacons[j][2],
        )
        starting_point_by_vector[vector] = beacons[i]

    return starting_point_by_vector


class ThChSubmission():
    def run(self, s):
        """
        :param s: input in string format
        :return: solution flag
        """
        # Your code goes here
        beacons_by_scanner = {}

        for scanner in s.split("\n\n"):
            lines = scanner.splitlines()
            scanner_nb = int(lines[0].replace("--- scanner ",
                                              "").replace(" ---", ""))
            beacons = []
            for line in lines[1:]:
                coords = line.split(",")
                beacons.append(tuple(int(x) for x in coords))

            beacons_by_scanner[scanner_nb] = []
            for orientation in zip(*[
                    compute_orientations(beacon, include_all=False)
                    for beacon in beacons
            ]):
                beacons_by_scanner[scanner_nb].append(sorted(orientation))

        scanners_to_process = deque(beacons_by_scanner.keys())
        identified_scanners = set()
        position_by_scanner = {0: (0, 0, 0)}
        final_beacons = set()

        while scanners_to_process:
            s1 = scanners_to_process.popleft()
            has_identified = False
            for s2 in scanners_to_process:
                if s1 in identified_scanners and s2 in identified_scanners:
                    continue

                nb_orientations = max(len(beacons_by_scanner[s2]),
                                      len(beacons_by_scanner[s1]))
                for i, j in product(range(nb_orientations), repeat=2):
                    if i >= len(beacons_by_scanner[s2]) or j >= len(
                            beacons_by_scanner[s1]):
                        continue

                    starting_point_by_vector1 = compute_vectors(
                        beacons_by_scanner[s1][j])
                    starting_point_by_vector2 = compute_vectors(
                        beacons_by_scanner[s2][i])

                    inter = set(starting_point_by_vector2.keys()).intersection(
                        starting_point_by_vector1.keys())

                    if len(inter) >= 11:
                        # restrict orientations
                        beacons_by_scanner[s1] = [beacons_by_scanner[s1][j]]
                        beacons_by_scanner[s2] = [beacons_by_scanner[s2][i]]
                        # Mark scanner as identified
                        identified_scanners.add(s1)
                        identified_scanners.add(s2)
                        has_identified = True
                        break

                if has_identified:
                    # compute scanner position
                    vector = inter.pop()
                    point1 = starting_point_by_vector1[vector]
                    point2 = starting_point_by_vector2[vector]

                    if s1 in position_by_scanner:
                        position_by_scanner[s2] = tuple(
                            position_by_scanner[s1][k] + point1[k] - point2[k]
                            for k in range(3))
                    if s2 in position_by_scanner:
                        position_by_scanner[s1] = tuple(
                            position_by_scanner[s2][k] + point2[k] - point1[k]
                            for k in range(3))

                    break

            if has_identified:
                # Re-enqueue scanners to find more pairs
                scanners_to_process.appendleft(s2)
                scanners_to_process.appendleft(s1)
                for ss in [s1, s2]:
                    for beacon in beacons_by_scanner[ss][0]:
                        absolute_beacon = tuple(beacon[k] +
                                                position_by_scanner[ss][k]
                                                for k in range(3))
                        final_beacons.add(absolute_beacon)

        return final_beacons

print(ThChSubmission().run(open("./Day 19/data2").read()).__len__())