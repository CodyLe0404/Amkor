from ast import Try
import csv
import shutil
import glob
import os

# Convert a single digit string to its corresponding number
def convertDigitToNumber(digit):
    if "30" <= digit <= "39":
        return str(int(digit) - 30)
    else:
        return digit

def parsingData(sourcePath, inputFileCsv, outputDir):

    inputFileAsc = glob.glob(os.path.join(sourcePath, '*.asc'))

    for fileName in inputFileAsc:
        try:
            output_file_name = fileName.split('.')[0] + "_processed.asc"
            outputFileAsc = os.path.join(outputDir, output_file_name.split('\\')[-1])

            print(f"Processing {fileName} \nSaving to {outputFileAsc}")
            
            with open(fileName, 'r', newline='') as inputAsc, open(outputFileAsc, 'w', newline='') as outputAsc:
                reader = csv.reader(inputAsc)
                writer = csv.writer(outputAsc)

                letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
                        "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
                        "W", "X", "Y", "Z"]

                digit = ["41", "42", "43", "44", "45", "46", "47", "48", "49", 
                        "4A", "4B", "4C", "4D", "4E", "4F", "4G", "4H", "4I", 
                        "4J", "4K", "4L", "4M", "4N", "4O", "4P", "4Q"]
                
                for line in reader:
                    firstLine = []
                    allLine = []
                    temp = []

                    if "STN" in line:
                        firstLine.extend(line[:5])
                    else:
                        allLine.append(line[0])
                        allLine.append(line[1])
                        allLine.append(line[3]) 
                        allLine.append(line[4])
                        allLine.append(line[22])
                        #First character
                        for i in range(26):
                            if line[5] == digit[i]:
                                line[5] = letters[i]
                                temp.append(line[5])
                        #Second character
                        digit_value = int(line[6]) - 35
                        if 0 <= digit_value <= 26:
                            line[6] = letters[digit_value]
                            temp.append(line[6])
                        temp.extend(list(map(convertDigitToNumber, line[7:22])))

                        stringCompare = ""
                        stringCompare = ''.join(temp)
                        #print(stringCompare)
                        temp.clear()

                        with open(inputFileCsv, 'r', newline='') as inputTemp:
                            for line2 in inputTemp:
                                varFind = line2.strip().split('=')
                                if len(varFind) == 2:
                                    if stringCompare == varFind[1]:
                                        temp.append(varFind[0])
                        if temp:
                            allLine.append("".join(temp) + "000.00")
                        else: allLine.append("unknow      ")
                    if firstLine:
                        writer.writerow(firstLine)
                        
                    elif allLine:
                        allLine[3], allLine[5] = allLine[5], allLine[3]
                        allLine[4], allLine[5] = allLine[5], allLine[4]
                        writer.writerow(allLine)
                
            print(f"{output_file_name} -> Data update success!")

            try:
                filenamePath = fileName
                parsedPath = sourcePath + "parsed"
                file_name_original = os.path.basename(filenamePath)
                destination_file = os.path.join(parsedPath, file_name_original)
                shutil.move(filenamePath, destination_file)
                print(f"{filenamePath} -> Moving success!")
            except Exception as e:
                print(f"Cannot move {filenamePath}. Error: {e}")
                
        except FileExistsError:
            print(f"Error: File {fileName} not found.")

        except FileNotFoundError:
            print(f"Error: File {fileName} cannot open!")
    
def main():
    inputFileAsc = "C:/Workplace/Python/convertAsc/"
    inputFileCsv = "C:/Workplace/Python/convertAsc/C_KR0700.csv_temp"
    outputFileAsc = "C:/Workplace/Python/convertAsc/output/"

    parsingData(inputFileAsc, inputFileCsv, outputFileAsc)

if  __name__ == "__main__":
    main()
