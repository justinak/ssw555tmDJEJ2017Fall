# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 13:47:05 2017


Create a data repository for Stevens Institute of Technology containing information about students, instrustors and grades.

For Student:
    -track required courses
    -track courses completed
    -track grades
    -calculate GPA
    
    METHODS: study, register
    
For Intructor:
    
    METHODS: teach
    
For Faculty Advisor:
    -create student study plans

Homework 9:
    -Build framework to summarize student and instructor data
    -Read data from each of 3 files
    -Store in data structure that is easy to process
    
    PHASE 1:
        CLASS REPOSITORY
        -Initialize repository
        -Read Students data file
        -Store students (Student Collaborator)
        -Read Instructor data file
        -Store instructors (Instructor Collaborator)
        -Read Grades data file
        -Assign course/grade to student (Student Collaborator)
        -Assign course to instructor (Instructor Collaborator)
        -Create Student Summary (Student, PrettyTable)
        -Create Instructor Summary (Instructor, PrettyTable)
        
        CLASS STUDENT
        -Initialize Student
        -Store student CWID (Repository Collaborator)
        -Store student name (Repository Collaborator)
        -Store student major (Repository Collaborator)
        -Note courses taken (Grade Collaborator)
        -Provide set of courses taken
        
        CLASS INSTRUCTOR 
        -Initialize instructor
        -Store instructor CWID
        -Store instructor name
        -Store instructor department
        -Store courses taught (Grade Collaborator)
        -Store # students in each course (Grade Collaborator)
        -Return courses taught
        -Return number students in each course
        
        CLASS GRADE
        -Initialize Grade
        -Store student CWID
        -Store course
        -Store grade
        -Store instructor CWID
        
Homework 10:   
-Courses required remaining for the student
     
        
"""

import unittest
from prettytable import PrettyTable
from collections import defaultdict


class Repository:
    """Create a repository to hold data structures """
    def __init__(self): # initialize repository
        self.students = dict() # key: student CWID, value: instance of class Student
        self.instructors = dict() # key: instructor CWID, value: instance of class Instructor
        self.grades = list()
        self.majors = defaultdict(set) #key: major, value: the required courses for that major

    def read_students(self, students_file):
        try:
            fp = open(students_file, 'r')
        except FileNotFoundError:
            print("File", students_file, "cannot be read, not a .txt file" )
        else:
            for line in fp:
                CWID, name, major = line.strip().split("\t")
                self.students[CWID]=Student(CWID, name, major)
            
    def read_instructors(self, instructors_file):
        try:
            fp = open(instructors_file, 'r')
        except FileNotFoundError:
            print("File", instructors_file, "cannot be read, not a .txt file" )
        else:
            for line in fp: 
                CWID, name, dept = line.strip().split("\t")
                self.instructors[CWID]=Instructor(CWID, name, dept) 

    def read_grades(self, grades_file): 
        try:
            fp = open(grades_file, 'r')
        except FileNotFoundError:
            print("File", grades_file, "cannot be read, not a .txt file" )
        else:
            for line in fp:
                student_CWID, course, grade, instructor_CWID = line.strip().split("\t")
                self.grades.append(Grade(student_CWID, course, grade, instructor_CWID))
                
    def read_majors(self, majors_file):
        try:
            fp = open(majors_file, 'r')
        except FileNotFoundError:
            print("File", majors_file, "cannot be read, not a .txt file")
        else:
            for line in fp:
                major, course = line.strip().split("\t")
                self.majors[major].add(course)
                
    def assign_course(self):
        """ Tell student to take another course, tell instructor about the student """
        for grade in self.grades: # loop through all grades using Student collaborator
            s = self.students[grade.CWID_st] # finds instance of class Student for this grade to look up by CWID
            i = self.instructors[grade.CWID_in] # finds instance of class Instructor for this grade to look up by CWID
            s.st_add_course(grade) # updates dict in s that tracks the class Student for this grade
            i.in_add_course(grade.course) # updates dict in i that tracks the class Instructor for this grade
    
    def student_summary(self):
        """ Create a table summarizing all the info about students from students.txt and grades.txt """
        student_table = PrettyTable(['CWID', 'Name', 'Major', 'Completed Courses', 'Remaining Courses'])
        for student in self.students.values():
            student_table.add_row([student.CWID, student.name, student.major, sorted(student.courses_taken.keys()), (self.majors[student.major]-student.courses_taken.keys())])
        print(student_table)
        
    def instructor_summary(self):
        """ Create a table summarizing all the info about instructors from instructors.txt and grades.txt """
        instructor_table = PrettyTable(['CWID', 'Name', 'Dept', 'Course', 'Students'])
        for instructor in self.instructors.values():
            for course in instructor.courses_taught:
                instructor_table.add_row([instructor.CWID, instructor.name, instructor.dept, course, instructor.courses_taught[course]])
        print(instructor_table)
        
        
class Student:
    def __init__(self, CWID, name, major): # initialize student class
        self.CWID = CWID
        self.name = name
        self.major = major
        self.courses_taken = defaultdict(str) #key: course, value: grade
        
    def st_add_course(self, grade): # counting how many grades there are for a given course which determines number of student who have taken the course
        self.courses_taken[grade.course]=grade.grade 
        return sorted(self.courses_taken)
        
    def courses_completed(self, course):
        """Create a defaultdict(str) where key==CWID, value=={dict w/ key==course, value==grade} showing which 
           courses a student has completed"""
        grades = 0 # instanciating that there are 0 grades for the first course
        for grade in Student.st_add_course(): # for every student that has a grade for a course
            grades +=1 # count how many grades the course has
            add_course = self.courses_taken.append[course][grades] # add the course and how many grades were counted for it      
            return add_course  
           
    
class Instructor:
    def __init__(self, CWID, name, dept): # initialize instructor class
        self.CWID = CWID
        self.name = name
        self.dept = dept
        self.courses_taught = defaultdict(int)
        
    def in_add_course(self, course):
        self.courses_taught[course] +=1
        
    def courses_taught(self, course):
        """Create a defaultdict(int) where key==course, value==num_students"""
        taught_course = self.courses_taught.append[course]
        return taught_course
    
        
class Grade:
    def __init__(self, CWID_st, course, grade, CWID_in): # initialize grade class
        self.CWID_st = CWID_st
        self.course = course
        self.grade = grade
        self.CWID_in = CWID_in 
        
        
def main():  
    sitdata_rep = Repository()
    sitdata_rep.read_students("C:\Python27\students.txt")
    sitdata_rep.read_instructors("C:\Python27\instructors.txt")
    sitdata_rep.read_grades("C:\Python27\grades.txt")
    sitdata_rep.read_majors("C:\Python27\majors.txt")
    sitdata_rep.assign_course()
    sitdata_rep.student_summary()
    sitdata_rep.instructor_summary()
    
        
  
class StevensDataRepositoryTest(unittest.TestCase):
    
    def read_students(self, students_file):
        try:
            fp = open(students_file, 'r')
        except FileNotFoundError:
            print("File", students_file, "cannot be read, not a .txt file" )
        else:
            for line in fp:
                CWID, name, major = line.strip().split("\t")
                self.students[CWID]=Student(CWID, name, major)
    
    def test_stsummary(self):
        """ Test Student summary table """
        StevensDataRepositoryTest.read_sudents
        CWID, name, courses_taken = repository.student_summary
        self.assertEqual(CWID, '10103')
        self.assertEqual(name, 'Baldwin, C')
        self.assertEqual(courses_taken, ['SSW 567', 'SSW 564', 'SSW 687'])  

    def test_insummary(self):
        """ Test Instructor summary table """
        sitdata_rep = Repository()
        sitdata_rep.read_instructors("C:\Python27\instructors.txt")
        CWID, name, dept, course, students = repository.instructor_summary
        self.assertEqual(CWID, '98764')
        self.assertEqual(name, 'Feynman, R')
        self.assertEqual(dept, 'SFEN')
        self.assertEqual(course, 'SSW 687')
        self.assertEqual(students, '3')
        

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=3)
    main()
    
    # ERROR: test_insummary (__main__.StevensDataRepositoryTest)