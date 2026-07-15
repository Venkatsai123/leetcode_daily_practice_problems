class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beams_count = []
        for i in bank:
            beams_count.append(i.count('1'))
        beams_count = [i for i in beams_count if i>0]
        if(len(beams_count)<=1):
            return 0
        n=len(beams_count)
        laser_beams =0
        for i in range(1,n):
            laser_beams += beams_count[i]*beams_count[i-1]
        return laser_beams
