import math
import json

def busy_int(in_name, v):
   
    if isinstance(in_name, str):
        with open(in_name) as in_file:
            in_data = json.load(in_file)
        T = in_data['tasks']
        v = 1
    else:
        T = in_name
    
    
    ints = []
    for i in range(1, len(T)):
        t = 0
        for k in range(i+1):
            t += T[k]['c']
        try: 
            while True:
                t2 = 0
                for k in range(i + 1):
                    t2 += (math.ceil(t/T[k]['period'])*T[k]['c'])
                if t2 == t:
                    if v == 1:
                        print('Busy Interval for Task ' + str(i) + " is " + str(t))
                    ints.append(t)
                    break
                else:
                    t = t2
        except:
            print('Does not converge')
    return ints

if __name__ == '__main__':
    main()
