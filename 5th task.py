#Как известно, кортеж является неизменяемым типом. Напишите программу,
# которая позволяет в кортеж A добавить кортеж B таким образом, что кортеж B помещается на index[2].
#Пример: (1, 2, 3, 5, 8) (8,2,5) → (1, 2, 8, 2, 5, 3, 5, 8)
tupleA = (1, 2, 3, 5, 8)
tupleB = (8,2,5)
tupleAa = tupleA[0:2]
tupleAA = tupleA[2:5]
complete_tuple = tupleAa + tupleB + tupleAA
print(complete_tuple)
