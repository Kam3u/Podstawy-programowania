###
# Module 2: Types, Variables and Operators
# Section 3, Task 1: Analyzing variables
# Total number of variables: 7
#
company = "ABC Data"                  # name: company, value: "ABC Data", type: str
phone = "555-123-009"                 # name: phone, value: "555-123-009", type: str
employees = 25                        # name: employees, value: 25, type: int
remote_work = True                    # name: remote_work, value: True, type: bool
big_company = employees > 100         # name: big_company, value: False, type: bool
income = 4500000                      # name: income, value: 4500000, type: int
income_per_person = income / employees  # name: income_per_person, value: 180000.0, type: float

for var_name, val in [
    ("company", company),
    ("phone", phone),
    ("employees", employees),
    ("remote_work", remote_work),
    ("big_company", big_company),
    ("income", income),
    ("income_per_person", income_per_person),
]:
    print(f"{var_name}: value={val}, type={type(val)}")
