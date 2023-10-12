def list_benefits():
    return "Code that is better structured and arranged", "Code that is easier to comprehend and understand", "Code that can be utilized again more effortlessly", "Facilitating the sharing and linking of code among programmers."

def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()