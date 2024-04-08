class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stu, sand, check  = 0, 0, 0

        while stu < len(students) and sand < len(sandwiches):
            # if student and sandwich match
            # print(f'students : {students}, stu : {stu} , sand {sand}')
            if check <= len(students) - stu:

                if students[stu] == sandwiches[sand]:
                    stu += 1
                    sand += 1
                    check = 0

                    if stu == len(students) and sand == len(sandwiches):
                        return 0
                else:
                    check +=1 
                    students.append(students[stu])
                    del students[stu]
            else:
                return len(students) - stu
        
                

        