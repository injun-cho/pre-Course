import fah_converter

if __name__ == '__main__' :
    print("Enter a celcius value :")
    celcius = float(input())
    
    fah = fah_converter.convert_c_to_f(celcius)
    print("that's {0} degrees Fahrenheit".format(fah))
    