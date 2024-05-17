


# Convert ply-files to txt-files
def plyfilesToTextFiles():
    print('path')
    directory_path = '/home/christian/Schreibtisch/PointNetData/PlyFiles'
    files = os.listdir(directory_path)
    header = ['X', 'Y', 'Z', 'red', 'green', 'blue']

    i = 0
    for file_name in files:
        # Counter for numberofFiles

        file_path = os.path.join(directory_path, file_name)
        plydata = PlyData.read(file_path)
        cntDP = len(plydata.elements[0])
        print(file_name[:-4])
        # Write new txt-file

        with open(os.path.join('/home/christian/Schreibtisch/PointNetData/txtCloudFiles', file_name[:-4] + '.txt' ), 'w') as file_txt:
            for dpIndex in range(cntDP):
                tupleValues = [str(value) for value in plydata.elements[0][dpIndex]]
                file_txt.write(", ".join(tupleValues))
                file_txt.write('\n')
        i += 1


    data = {}
    header = ['X', 'Y', 'Z', 'red', 'green', 'blue']
    for index, headerElement in enumerate(header):
        data[headerElement] = np.zeros(cntDP)
        tmpNPArray = np.zeros(len(plydata.elements[0]))
        for dpIndex in range(cntDP):
            data[headerElement][dpIndex] = plydata.elements[0][dpIndex][index]
