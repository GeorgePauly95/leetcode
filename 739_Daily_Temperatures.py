from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n, result = len(temperatures), []
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                result.append(0)
            else:
                if temperatures[i] < temperatures[i + 1]:
                    result.append(1)
                else:
                    next_index = i + 1
                    while (
                        next_index < n and temperatures[i] >= temperatures[next_index]
                    ):
                        step = result[(n - 1) - next_index]
                        if step == 0:
                            result.append(0)
                            break
                        next_index += step
                    else:
                        if temperatures[i] < temperatures[next_index]:
                            result.append(next_index - i)
                        elif next_index >= n:
                            result.append(0)
        result.reverse()
        return result
