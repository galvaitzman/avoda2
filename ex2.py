#test
##teattttt
#goniiiijjj
import os

class Heap:
    def __init__(self, file_name):
        """
        :param file_name: the name of the heap file to create. example: kiva_heap.txt
        """
        self.file = open(file_name, "w+")
        self.file.close()
        self.rowSize = -1
        self.headSize = -1

    def create(self, source_file):
        """
        The function create heap file from source file.
        :param source_file: the name of file to create from. example: kiva.txt
        """
        self.rowSize = self.getRowSize(source_file, 1)
        self.headSize = self.getRowSize(source_file, 0)
        with open(source_file, "r") as sf:
            for line in sf:
                self.insert(line)
        sf.close()

    def insert(self, line):
        """
        The function insert new line to heap file
        :param line: string reprsent new row, separated by comma. example: '653207,1500.0,USD,Agriculture'
        """
        with open(self.file.name, "a+") as file1:
            file1.write(line)
        file1.close()

    def delete(self, col_name, value):
        """
        The function delete records from the heap file where their value in col_name is value.
        Deletion done by mark # in the head of line.
        :param col_name: the name of the column. example: 'currency'
        :param value: example: 'PKR'
        """
        currentFieldIndex = self.fieldIndex(col_name)
        file = open(self.file.name, "r+")
        file.seek(0,0)
        line = file.readline()
        counter = 0
        line = file.readline()
        while line and len(line)>2:
            lineSplit = line.split(',')
            if currentFieldIndex == (len(lineSplit) - 1):
                if value in lineSplit[currentFieldIndex]:
                    file.seek(self.headSize + self.rowSize * counter, 0)
                    file.write('#')
            else:
                if lineSplit[currentFieldIndex] == value:
                    file.seek(self.headSize + self.rowSize * counter, 0)
                    file.write('#')
            counter += 1
            file.seek(self.headSize + self.rowSize * counter, 0)
            line = file.readline()
        file.close()

        """""
        currentFieldIndex = self.fieldIndex(col_name)
        file = open(self.file.name, "r")
        tempFile = open('tempFile', 'w')
        line = file.readline()
        tempFile.write(line)
        line = file.readline()
        while(line):
            lineSplit = line.split(',')
            if(currentFieldIndex == (len(lineSplit)-1)):
                if(value in lineSplit[currentFieldIndex]):
                    tempFile.write('#' + line)
                else:
                    tempFile.write(line)
            else:
                if(lineSplit[currentFieldIndex] == value):
                    tempFile.write('#'+line)
                else:
                    tempFile.write(line)
            line = file.readline()
        file.close()
        tempFile.close()
        self.copyFromFileToFile(tempFile)
        os.remove(tempFile.name)
        """""
    def copyFromFileToFile(self, source):
        """
        function to copy source file to our field file
        """
        with open(self.file.name, "w") as file1, open(source.name, "r") as temp:
            for line in temp:
                file1.write(line)
        file1.close()
        temp.close()

    def fieldIndex(self, col_name):
        """
        function to find the index of the col name
        """
        file = open(self.file.name, "r")
        line = file.readline()
        lineSplit = line.split(',')
        currentFieldIndex = 0
        while (currentFieldIndex < len(lineSplit)):
            if col_name in lineSplit[currentFieldIndex]:
                break;
            currentFieldIndex += 1
        file.close()
        return currentFieldIndex

    def update(self, col_name, old_value, new_value):
        """
        The function update records from the heap file where their value in col_name is old_value to new_value.
        :param col_name: the name of the column. example: 'currency'
        :param old_value: example: 'TZS'
        :param new_value: example: 'NIS'
        """
        currentFieldIndex = self.fieldIndex(col_name)
        file = open(self.file.name, "r+")
        file.seek(0, 0)
        line = file.readline()
        counter = 0
        line = file.readline()
        while line and len(line) > 2:
            lineSplit = line.split(',')
            newLine = ""
            fieldcounter = 0
            while fieldcounter < len(lineSplit):
                if currentFieldIndex == fieldcounter and fieldcounter != len(lineSplit) - 1:
                    newLine = newLine + new_value + ","
                if currentFieldIndex == fieldcounter and fieldcounter == len(lineSplit) - 1:
                    newLine = newLine + new_value
                if currentFieldIndex != fieldcounter and fieldcounter != len(lineSplit) - 1:
                    newLine = newLine + lineSplit[fieldcounter] + ","
                if currentFieldIndex != fieldcounter and fieldcounter == len(lineSplit) - 1:
                    newLine = newLine + lineSplit[fieldcounter]
                fieldcounter += 1
            if currentFieldIndex == (len(lineSplit) - 1):
                if old_value in lineSplit[currentFieldIndex] and '#' not in line:
                    file.seek(self.headSize + self.rowSize * counter, 0)
                    file.write(newLine)
            else:
                if lineSplit[currentFieldIndex] == old_value and '#' not in line:
                    file.seek(self.headSize + self.rowSize * counter, 0)
                    file.write(newLine)
            counter += 1
            file.seek(self.headSize + self.rowSize * counter, 0)
            line = file.readline()

        """
        currentFieldIndex = self.fieldIndex(col_name)
        file = open(self.file.name, "r")
        tempFile = open('tempFile', 'w')
        line = file.readline()
        tempFile.write(line)
        line = file.readline()
        while (line):
            lineSplit = line.split(',')
            if (currentFieldIndex == (len(lineSplit) - 1)):
                if (old_value in lineSplit[currentFieldIndex]):
                    lineSplit[currentFieldIndex] = new_value+'\n'
                    tempFile.write(','.join(lineSplit))
                else:
                    tempFile.write(line)
            else:
                if (lineSplit[currentFieldIndex] == old_value):
                    lineSplit[currentFieldIndex] = new_value
                    tempFile.write(','.join(lineSplit))
                else:
                    tempFile.write(line)
            line = file.readline()
        file.close()
        tempFile.close()
        self.copyFromFileToFile(tempFile)
        os.remove(tempFile.name)
        """

    def getRowSize(self, source_file, index):
        file = open(source_file, "r")
        line0 = file.readline()
        line1 = file.readline()
        file.close()
        if index == 0:
            return len(line0)
        if index == 1:
            return len(line1)
        return




#if __name__ == '__main__':
  #f=open('fixed_kiva_loans.txt',"r").readlines()
  #x=1
  #heap = Heap('heap.txt')
  #heap.create('fixed_kiva_loans.txt')
  #heap.insert('653207,150.0,USD,Agri')

  #print(heap.headSize)
  #print(heap.rowSize)
  #heap.delete('sector', 'Trns')
  #heap.update('currency', 'PKR', 'gal')





class SortedFile:

    def __init__(self, file_name, col_name):
        """
        :param file_name: the name of the sorted file to create. example: kiva_sorted.txt
        :param col_name: the name of the column to sort by. example: 'lid'
        """
        self.file = open(file_name, "w+")
        self.file.close()
        self.col_name = col_name
        self.col_index = -1
        self.rowSize = -1
        self.headSize = -1
        self.numberOfRowsInFile = 0
        self.numberOfColumnsInFile = 0

    def create(self, source_file):
        """
        The function create sorted file from source file.
        :param source_file: the name of file to create from. example: kiva.txt
        """
        self.rowSize = self.getRowSize(source_file, 1)
        self.headSize = self.getRowSize(source_file, 0)
        with open(source_file, "r+") as sf:
            self.numberOfColumnsInFile = len(sf.readline().split(','))
            sf.seek(0,0)
            with open(self.file.name , "a+") as sorted:
                sorted.write(sf.readline())
            self.col_index = self.fieldIndex(self.col_name)
        sf.close()
        self.fillSortedArray(source_file)

    def fillSortedArray(self, source_file):
        firstTime = True
        finish = False
        min = "a"
        max = "b"
        with open(source_file, "r") as sf:
            while finish is False:
                if min == max:
                    finish = True
                sf.seek(0,0)
                sf.readline()
                if firstTime:
                    firstTime = False
                    lineSplit = sf.readline().split(',')
                    min = lineSplit[self.col_index]
                    max = min
                    line = sf.readline()
                    while line and len(line) > 2:
                        lineSplit = line.split(',')
                        if lineSplit[self.col_index] < min:
                            min = lineSplit[self.col_index]
                        if lineSplit[self.col_index] > max:
                            max = lineSplit[self.col_index]
                        line = sf.readline()
                else:
                    oldMin = min
                    min = max
                    line = sf.readline()
                    while line and len(line) > 3:
                        lineSplit = line.split(',')
                        if lineSplit[self.col_index] == oldMin:
                            self.insertFirst(line)
                        if lineSplit[self.col_index] < min and lineSplit[self.col_index] > oldMin :
                            min = lineSplit[self.col_index]
                        line = sf.readline()
                        if len(line)<self.rowSize:
                            line = line[0: self.rowSize-2]
                            line = line + "\r\n"

        sf.close()

    #inserting line to last row in file
    def insertFirst(self, line):
        """
        The function insert new line to heap file
        :param line: string reprsent new row, separated by comma. example: '653207,1500.0,USD,Agriculture'
        """
        with open(self.file.name, "a+") as file1:
            file1.write(line)
            self.numberOfRowsInFile += 1
        file1.close()

    def getRowSize(self, source_file, index):
        file = open(source_file, "r")
        line0 = file.readline()
        line1 = file.readline()
        file.close()
        if index == 0:
            return len(line0)
        if index == 1:
            return len(line1)
        return

    def fieldIndex(self, col_name):
        """
        function to find the index of the col name
        """
        file = open(self.file.name, "r")
        line = file.readline()
        lineSplit = line.split(',')
        currentFieldIndex = 0
        while (currentFieldIndex < len(lineSplit)):
            if col_name in lineSplit[currentFieldIndex]:
                break;
            currentFieldIndex += 1
        file.close()
        return currentFieldIndex


    def insert(self, line):
        value = line.split(',')[self.col_index]
        wantedRow =  self.binarySearch(value)
        """
        The function insert new line to sorted file according to the value of col_name.
        :param line: string of row separated by comma. example: '653207,1500.0,USD,Agriculture'
        """
        if wantedRow == self.numberOfRowsInFile:
            file = open(self.file.name, "a+")
            line = line + "\r\n"
            file.write(line)
            self.numberOfRowsInFile += 1
            return
        file = open(self.file.name, "r+")
        file.seek(self.headSize + self.rowSize * wantedRow)
        lineInFile = file.readline()
        counter=0
        while lineInFile and counter<self.numberOfRowsInFile:
            file.seek(self.headSize + self.rowSize * (wantedRow+counter), 0)
            file.write(line)
            line = lineInFile
            counter += 1
            file.seek(self.headSize + self.rowSize * (wantedRow+counter), 0)
            if counter < self.numberOfRowsInFile:
                lineInFile = file.readline()
        file.close()
        file = open(self.file.name, "a+")
        file.write(line)
        file.close()
        self.numberOfRowsInFile+=1



    def binarySearch(self,value):
        return self.recursiveBinarySearch(value, 0, self.numberOfRowsInFile - 1)

    def recursiveBinarySearch(self, value, left, right):
        if left > right:
            return -1
        middle = (left + right) / 2
        file = open(self.file.name, "r")
        file.seek(self.headSize + self.rowSize * middle)
        currentValue = file.readline().split(',')[self.col_index]
        if currentValue in value:
            return middle
        elif currentValue > value:
            if middle == 0:
                return middle
            file.seek(self.headSize + self.rowSize * (middle-1))
            previousValue = file.readline().split(',')[self.col_index]
            if previousValue <= value:
                return middle
                file.close()
            else:
                file.close()
                return self.recursiveBinarySearch(value, left, middle-1)
        else:
            file.close()
            if (left == right):
                return self.numberOfRowsInFile
            return self.recursiveBinarySearch(value, middle+1,right)


    def recursiveBinarySearchForUpdateOrDelete(self, value, left, right):
        if left > right:
            return -1
        middle = (left + right) / 2
        file = open(self.file.name, "r")
        file.seek(self.headSize + self.rowSize * middle)
        currentValue = file.readline().split(',')[self.col_index]
        if currentValue in value:
            file.close()
            return middle
        elif currentValue > value:
            file.close()
            return self.recursiveBinarySearchForUpdateOrDelete(value, left, middle-1)
        else:
            file.close()
            return self.recursiveBinarySearchForUpdateOrDelete(value, middle+1,right)


    # searching for first record with wanted value: upOrDown = -1, returnValue=1
    # searching for first record after wanted value: upOrDown = 1, returnValue=0
    # searching for last record with wanted value: upOrDown = 1, returnValue = -1
    def findIndexForDeleteOrUpdate(self,wantedValue, upOrDown, returnValue):
        x = self.recursiveBinarySearchForUpdateOrDelete(wantedValue, 0, self.numberOfRowsInFile - 1)
        if x == -1 or x == self.numberOfRowsInFile:
            return -1
        if x == 0 and returnValue == 1:
            return 0
        x = x + upOrDown
        file = open(self.file.name, "r")
        file.seek(self.headSize + self.rowSize * x)
        currentValue = file.readline().split(',')[self.col_index]
        while x >= 0 and wantedValue in currentValue and x < self.numberOfRowsInFile:
            x+=upOrDown
            file.seek(self.headSize + self.rowSize * x)
            if (x<self.numberOfRowsInFile):
                currentValue = file.readline().split(',')[self.col_index]
        return (x + returnValue)


    def delete(self, value):
        """
        The function delete records from sorted file where their value in col_name is value.
        Deletion done by mark # in the head of line.
        :param value: example: 'PKR'
        """

        startingIndexToDelete = self.findIndexForDeleteOrUpdate(value, -1, 1)
        startingReplacementIndex = self.findIndexForDeleteOrUpdate(value, 1, 0)
        if startingIndexToDelete == -1:
            return
        tempFile = open("tempFile", "w+")
        file = open(self.file.name, "r+")
        tempFile.write(file.readline())
        line = file.readline()
        counter = 0
        while line and len(line) > 2:
            if counter < startingIndexToDelete or counter >= startingReplacementIndex:
                file.seek(self.headSize + self.rowSize * counter, 0)
                tempFile.write(line)
            else:
                self.numberOfRowsInFile -= 1
            counter += 1
            file.seek(self.headSize + self.rowSize * counter, 0)
            line = file.readline()
        file.close()
        file = open(self.file.name, "w+")
        tempFile.seek(0, 0)
        for line in tempFile:
            file.write(line)
        file.close()
        tempFile.close()
        os.remove(tempFile.name)


    def update(self, old_value, new_value):
        """
        The function update records from the sorted file where their value in col_name is old_value to new_value.
        :param old_value: example: 'TZS'
        :param new_value: example: 'NIS'
        """
        startingIndexToDelete = self.findIndexForDeleteOrUpdate(old_value, -1, 1)
        lastIndexToUpdate = self.findIndexForDeleteOrUpdate(old_value, 1, -1)
        if startingIndexToDelete == -1:
            return
        tempFile = open("tempFile2", "w+")
        file = open(self.file.name, "r+")
        counter = startingIndexToDelete
        while counter <= lastIndexToUpdate:
            file.seek(self.headSize + self.rowSize * counter)
            line = file.readline()
            line = line.replace(old_value, new_value)
            tempFile.write(line)
            counter += 1
        self.delete(old_value)
        tempFile.seek(0, 0)
        for line in tempFile:
            self.insert(line)
        file.close()
        tempFile.close()
        os.remove(tempFile.name)

#if __name__ == '__main__':

 #sf = SortedFile('SortedFile.txt', 'loan_amount')
 #sf.create('fixed_kiva_loans.txt')
 #sf.insert('653207,628.0,USD,Agrs')
 #sf.insert('653208,628.0,USD,Agrs')
 #sf.insert('653208,628.0,USD,Agrs')
 #sf.insert('653208,628.0,USD,Agrs')
 #sf.insert('653208,628.0,USD,Agrs')
 #sf.delete('150.0')
 #sf.update('628.0','666.0')

class Hash:
    def __init__(self, file_name, N=5):
        """
        :param file_name: the name of the hash file to create. example: kiva_hash.txt
        :param N: number of buckets/slots.
        """

        self.file = open(file_name, "w+")
        self.file.close()
        self.numberOfBuckets = N
        self.col_name = ""
        self.col_index = -1
        self.rowSize = -1
        self.headSize = -1
        self.numberOfRowsInFile = 0
        self.numberOfColumnsInFile = 0
        self.sourceFile=""
    def create(self, source_file, col_name):
        """
        :param source_file: name of file to create from. example: kiva.txt
        :param col_name: the name of the column to index by example: 'lid'
        Every row will represent a bucket, every tuple <value|ptr> will separates by comma.
        Example for the first 20 instances in 'kiva.txt' and N=10:
        653060|11,
        653091|17,653051|1,
        653052|18,653062|14,653082|9,
        653063|4,653053|2,
        653054|16,653084|5,
        653075|15,
        653066|19,
        653067|7,
        653088|12,653048|10,653078|8,1080148|6,653068|3,
        653089|13,
        """

        self.rowSize = self.getRowSize(source_file, 1)
        self.headSize = self.getRowSize(source_file, 0)
        self.sourceFile = source_file
        sourceFile = open(source_file,"r")
        myFile = open(self.file.name,"r+")
        self.numberOfColumnsInFile = len(sourceFile.readline().split(','))
        self.col_index = self.fieldIndex(self.col_name, source_file)
        sourceFile.seek(self.headSize,0)
        line = sourceFile.readline()
        counter=1
        while counter <= self.numberOfBuckets:
            myFile.write(str(counter) + "\n")
            counter+=1
        counter=1
        myFile.close()
        while line and len(line)>2:
            value = line.split(',')[self.col_index]
            self.add(value,counter)
            counter += 1
            line = sourceFile.readline()

    def getRowSize(self, source_file, index):
        file = open(source_file, "r")
        line0 = file.readline()
        line1 = file.readline()
        file.close()
        if index == 0:
            return len(line0)
        if index == 1:
            return len(line1)
        return

    def fieldIndex(self, col_name, sourceFile):
        """
        function to find the index of the col name
        """
        file = open(sourceFile, "r")
        line = file.readline()
        lineSplit = line.split(',')
        currentFieldIndex = 0
        while (currentFieldIndex < len(lineSplit)):
            if col_name in lineSplit[currentFieldIndex]:
                break;
            currentFieldIndex += 1
        file.close()
        return currentFieldIndex

    def add(self, value, ptr):
        """
        The function insert <value|ptr> to hash table according to the result of the hash function on value.
        :param value: the value of col_name of the new instance.
        :param ptr: the row number of the new instance in the heap file.
        """
        hashIndex=0
        if self.col_index == 2 or self.col_index == 3:
            hashIndex = int(value[0]) % self.numberOfBuckets + 1
        else:
            hashIndex = int(value) % self.numberOfBuckets + 1
        file = open(self.file.name,"r+")
        addToLine = str(value) + "|" + str(ptr) + ","
        lineToWrite = ""
        counter = 1
        found = False
        counterForSeek = 0
        lineToOverride = ""
        while found is False:
            if counter == hashIndex:
                found = True
                lineToOverride = file.readline()
                if "|" not in lineToOverride:
                    lineToWrite = addToLine + "\n"
                else:
                    lineToWrite = addToLine + lineToOverride
            else:
                lineToOverride = file.readline()
                counter += 1
                counterForSeek += len(lineToOverride)
        file.seek(counterForSeek)
        file.readline()
        lengthToKeep = len(lineToWrite) - len(lineToOverride)
        counter=0
        firstTime = True
        lineToKeep = "a"
        while len (lineToKeep) > 0:
            counterForKeep=0
            lineToKeep = ""
            while counterForKeep < lengthToKeep:
                lineToKeep = lineToKeep + file.read(1)
                counterForKeep+=1
            file.seek(counterForSeek)
            file.write(lineToWrite)
            if firstTime:
                counterForSeek = counterForSeek + len(lineToWrite)
                firstTime = False
            else:
                counterForSeek = counterForSeek + counterForKeep
            lineToWrite = lineToKeep


    def remove(self, value, ptr):
        """
        The function delete <value|ptr> from hash table.
        :param value: the value of col_name.
        :param ptr: the row number of the instance in the heap file.
        """
        file = open(self.sourceFile,"r+")
        file.seek(self.headSize+self.rowSize*(ptr-1))
        file.write('#')
        file.close()
        hashIndex = 0
        file = open(self.file.name,"r+")
        if self.col_index == 2 or self.col_index == 3:
            hashIndex = int(value[0]) % self.numberOfBuckets + 1
        else:
            hashIndex = int(value) % self.numberOfBuckets + 1
        counter=0
        seekRow=0
        while counter<hashIndex-1:
            x = file.readline()
            counter+=1

        lineSplit = file.readline().split(',')
        for line in lineSplit:
            if ()



if __name__ == '__main__':

  # heap = Heap("heap_for_hash.txt")
  hash = Hash('hash_file.txt', 20)
  hash.create('fixed_kiva_loans.txt', 'lid')

  # heap.create('kiva.txt');

  # heap.insert('653207,1500.0,USD,Agriculture')
  hash.add('653207','11')


