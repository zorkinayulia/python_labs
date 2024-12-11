from task1 import Train, Student, Car

if __name__ == "__main__":
    train = Train(500, 350)
    student = Student(2, 4.5)
    car = Car(55, 40, 12)

    try:
        train.set_new_train_params('500', '500')
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        student.set_new_student_params([1], [2])
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        car.set_new_car_params('1', '1', '1', '1')
    except TypeError:
        print('Ошибка: неправильные данные')