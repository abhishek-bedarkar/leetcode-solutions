class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        num_r,num_d= 0,0

        for mem in senate:
            if mem == "R":
                num_r += 1
            else:
                num_d += 1

        ban_r,ban_d = 0,0

        senate = list(senate)

        floating_d_bans,floating_r_bans = 0,0
   
        while ban_d!=num_d and ban_r!=num_r:
            for i,mem in enumerate(senate):
                if mem == 'R':
                    if floating_r_bans > 0:
                        floating_r_bans -= 1
                        senate[i] = 'X'
                        ban_r += 1
                    else:
                        floating_d_bans += 1
                if mem == 'D':
                    if floating_d_bans > 0:
                        floating_d_bans -= 1
                        senate[i] = 'X'
                        ban_d += 1
                    else:
                        floating_r_bans += 1
        if ban_r == num_r:
            return "Dire"
        return "Radiant"