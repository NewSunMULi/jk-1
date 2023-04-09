from xml.etree import ElementTree as et


class Data_Update:
    def __init__(self):
        pass

    def plan(self, way="xml数据文件"):
        if way == "xml数据文件":
            xml_file = et.parse("./plan/data1.xml")
            data = xml_file.getroot()
            data_list = [[], [], []]
            for i in range(len(data)):
                for j in range(len(data[i])):
                    for k in range(len(data[i][j])):
                        data_list[i].append(data[i][j][k].text)
            return data_list
        else:
            pass


if __name__ == "__main__":
    print(Data_Update().plan())