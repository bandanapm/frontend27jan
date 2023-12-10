# Programming Exercise 11-2

import emp

def main():
    # Local variables
    super_name= ''
    super_id = ''
    super_salary = 0.0
    super_bonus = 0.0
    
    # Get data attributes.
    super_name = input('Enter the name: ')
    super_id = input('Enter the ID number: ')
    super_salary = float(input('Enter the annual salary: '))
    super_bonus = float(input('Enter the bonus: '))

    # Create an instance of ShiftSupervisor.
    supervisor = emp.ShiftSupervisor(super_name, super_id, \
                                     super_salary, super_bonus)

    # Display information.
    print ('Shift supervisor worker information: ')
    print ('Name:', supervisor.get_name())
    print ('ID number:', supervisor.get_id_number())
    print ('Annual Salary: $', \
           format(supervisor.get_salary(), ',.2f'), \
           sep = '')
    print ('Annual Production Bonus: $', \
           format(supervisor.get_bonus(), ',.2f'), \
           sep = '')

# Call the main function.
main()

