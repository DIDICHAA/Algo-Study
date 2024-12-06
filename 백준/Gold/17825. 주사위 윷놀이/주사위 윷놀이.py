def solve(cnt, acc):
    global ans
    if acc + 40 * (10 - cnt) <= ans:
        return
    if cnt == 10:
        ans = max(ans, acc)
        return
    for pidx in range(4):
        if arrival[pidx]: continue

        dice_value = moves[cnt]
        cur_route_idx = piece_routes[pidx]
        cur_route = routes[cur_route_idx]
        cur_idx = piece_indices[pidx]
        nxt_idx = cur_idx + dice_value
        cur_position = cur_route[cur_idx]

        # arrive
        if nxt_idx >= len(cur_route):
            arrival[pidx] = 1
            piece_positions[pidx] = ARRIVAL
            nxt_position = ARRIVAL
            nxt = acc
        # if piece not available
        elif cur_route[nxt_idx] in piece_positions:
            continue
        # can move and not arrived
        else:
            nxt_position = cur_route[nxt_idx]
            nxt = acc + scores[nxt_position]

        # change route if needed
        if nxt_position > 20:
            pass
        elif nxt_position == FIRST_BLUE:
            piece_routes[pidx] = 1
        elif nxt_position == SECOND_BLUE:
            piece_routes[pidx] = 2
        elif nxt_position == THIRD_BLUE:
            piece_routes[pidx] = 3

        # next recursion
        piece_indices[pidx] = nxt_idx
        piece_positions[pidx] = nxt_position
        solve(cnt + 1, nxt)
        piece_positions[pidx] = cur_position
        piece_indices[pidx] = cur_idx
        piece_routes[pidx] = cur_route_idx
        if arrival[pidx]:
            arrival[pidx] = 0


FIRST_BLUE = 5
SECOND_BLUE = 10
THIRD_BLUE = 15
ARRIVAL = 32
piece_positions = [0] * 4
piece_indices = [0] * 4
blue_none = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 31, 32]
blue_first = [0, 1, 2, 3, 4, 5, 20, 21, 22, 28, 29, 30, 31, 32]
blue_second = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 23, 24, 28, 29, 30, 31, 32]
blue_third = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 25, 26, 27, 28, 29, 30, 31, 32]
scores = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32,
          34, 36, 38, 13, 16, 19, 22, 24, 28, 27, 26, 25, 30, 35, 40, 0]
piece_routes = [0] * 4
routes = [blue_none, blue_first, blue_second, blue_third]
route = [0] * 4
arrival = [0] * 4
moves = list(map(int, input().split()))

ans = 0
solve(0, 0)
print(ans)
