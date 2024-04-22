class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if "0000" in deadends: return -1 
        if target == "0000": return 0

        steps, visited_state, combinations = 0, set(["0000"]), set(["0000"])

        def get_pos_states(combs):
            result = set()
            for comb in combs:
                for i,c in enumerate(comb):
                    dig = int(c)
                    nxt_dig  = dig+1
                    prev_dig = dig -1

                    if nxt_dig == 10:
                        nxt_dig = 0
                    
                    if prev_dig == -1:
                        prev_dig = 9
                

                    result.add(comb[:i] + str(nxt_dig) + comb[i+1:])
                    result.add(comb[:i] + str(prev_dig) + comb[i+1:])

            return result


        
        while combinations:
            possible_states = get_pos_states(combinations)
            #print(f'possible states : {possible_states}')
            steps += 1
            next_states = set()
            for state in possible_states:
                if state not in deadends and state not in visited_state:
                    if state == target:
                        return steps
                    next_states.add(state)
                    visited_state.add(state)
            combinations = next_states

        return -1





        