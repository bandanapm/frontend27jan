# Programming Exercise 11-1

import emp

def main():
    # Local variables
    worker_name= ''
    worker_id = ''
    worker_shift = 0
    worker_pay = 0.0
    
    # Get data attributes
    worker_name = input('Enter the name: ')
    worker_id = input('Enter the ID number: ')
    worker_shift = int(input('Enter the shift number: '))
    worker_pay = float(input('Enter the hourly pay rate: '))

    # Create an instance of ProductionWorker
    worker = emp.ProductionWorker(worker_name, worker_id, \
                                  worker_shift, worker_pay)

    # Display information
    print ('Production worker information:')
    print ('Name:', worker.get_name())
    print ('ID number:', worker.get_id_number())
    print ('Shift:', worker.get_shift_number())
    print ('Hourly Pay Rate: $', \
           format(worker.get_pay_rate(), ',.2f'), sep='')

# Call the main function.
main()

