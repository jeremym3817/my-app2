import ratemyprofessor

#Uninstall RateMyProfessorAPI if need be
# python -m pip uninstall RateMyProfessorAPI

# To retrieve a list of professors, you have to first specify the school:

test = ratemyprofessor.get_school_by_name("Northeastern University")

# This will return None if no school is found corresponding with that name. Alternatively, to search for multiple schools, use

# ratemyprofessor.get_schools_by_name("School Name")
# This will return a list of Schools.


professor = ratemyprofessor.get_professor_by_school_and_name(
    ratemyprofessor.get_school_by_name("Northeastern University"), "John Park")
if professor is not None:
    print("%sworks in the %s Department of %s." % (professor.name, professor.department, professor.school.name))
    print("Rating: %s / 5.0" % professor.rating)
    print("Difficulty: %s / 5.0" % professor.difficulty)
    print("Total Ratings: %s" % professor.num_ratings)
    if professor.would_take_again is not None:
        print(("Would Take Again: %s" % round(professor.would_take_again, 1)) + '%')
    else:
        print("Would Take Again: N/A")