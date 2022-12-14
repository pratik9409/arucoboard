# Aruco-Board

https://user-images.githubusercontent.com/67755812/202192557-b8f40907-0153-4d75-906f-f2ce5e233556.mp4


An ArUco marker is a synthetic square marker composed by a wide black border and an inner binary matrix which determines its identifier (id). The black border facilitates its ast detection in the image and the binary codification allows its identification and the application of error detection and correction techniques. The marker size determines the size of the internal matrix. For instance a marker size of 4x4 is composed by 16 bits.

Some examples of ArUco markers:


![markers](https://user-images.githubusercontent.com/67755812/202192659-5551c742-3372-4f74-8415-0ad7f0cbd674.jpg)


A dictionary of markers is the set of markers that are considered in a specific application. It is simply the list of binary codifications of each of its markers.
The aruco module includes some predefined dictionaries covering a range of different dictionary sizes and marker sizes.

One may think that the marker id is the number obtained from converting the binary codification to a decimal base number. However, this is not possible since for high marker sizes the number of bits is too high and managing such huge numbers is not practical. Instead, a marker id is simply the marker index within the dictionary it belongs to. For instance, the first 5 markers in a dictionary have the ids: 0, 1, 2, 3 and 4.
