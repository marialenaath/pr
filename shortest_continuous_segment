def shortest_continuous_segment(s):
    prev = s[0]
    count = 1
    prev_count = None
    prev_count_num = None

    for i in range(1,len(s)):

        if s[i]==prev:
            count += 1

        else:
            if prev_count is not None:
                if prev_count >= count and prev > prev_count_num:
                    prev_count = count
                    prev_count_num = prev

            else:
                prev_count = count
                prev_count_num = s[i-1]
                prev = s[i]
                count = 1

    return prev_count_num,prev_count
