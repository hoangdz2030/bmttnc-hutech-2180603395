from SinhVien import SinhVien
class QuanLySinhVien: 
    listSinhVien = []
    
    
    def generateID (self): 
        maxId = 1
        if (self.soLuongSinhVien() > 0):
            maxId = self.listSinhVien [0]._id
            for sv in self.listSinhVien:
                if (maxId < sv._id):
                    maxId = sv._id
            maxId = maxld + 1
        return maxId
def soLuongSinhVien (self):
    return self.listSinhVien. _len_()
def nhapSinhVien (self):
    svId = self.generateID()
    name = input ("Nhap ten sinh vien: ")
    sex = input ("Nhap gioi tinh sinh vien: ")
    major
    input ("Nhap chuyen nganh cua sinh vien: ")
    diemTB - float (input("Nhap diem cua sinh vien: "))
    sv = SinhVien (svId, name, sex, major, diemTB) 
    self.xepLoaiHocLuc (sv)
    self.listSinhVien.append (sv)
def updateSinhVien (self, ID):
    sv: SinhVien = self.findByID (ID)
    if (sv!= None):
        name = input ("Nhap ten sinh vien: ")
        sex = input ("Nhap gioi tinh sinh vien: ")
        major = int (input("Nhap chuyen6 nganh cua sinh vien: "))
        diemTB = float(input("Nhap diem cua sinh vien: "))
        sv. name = name
        sv. sex - sex
        sv._major = major
        sv. diemTB = diemTB
        self.xepLoaiHocLuc (sv)
    else:
        print ("Sinh vien co ID = {} khong ton tai.".format(ID))
        def sortByID(self):
            self.listSinhVien.sort(key=lambda x: x._id, reverse=False)
        def sortByName(self):
            self.listSinhVien.sort(key=lambda x: x._name, reverse=False)
        def sortByDiemTB (self):
            self.listSinhVien.sort(key=lambda x: x. diemTB, reverse=False)
        def findByID (self, ID):
            searchResult = None
        if (self.soLuongSinhVien () > 0):
            for sv in self.listSinhVien:
                if (sv. id == ID):
                    searchResult = sv
        return searchResult
    
    def findByName (self, keyword):
        listSV = []
        if (self.soLuongSinhVien () > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV
    def deleteById(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if (sv!= None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted
    def xepLoaiHocLuc (self, sv: SinhVien): 
        if (sv. diemTB >= 8): 
            sv. hocLuc = "Gioi"
        elif (sv._diemTB >= 6.5):
            sv. hocLuc = "Kha"
        elif (sv._diemTB >= 5):
            sv._hocLuc = "Trung binh"
        else:
            sv. hocLuc = "Yeu"
    def showSinhVien (self, listSV):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}"
            .format("ID", "Name", "Sex", "Major", "Diem TB", "Hoc Luc"))
        if (listSV._len_() > 0):
         for sv in listSV:
             print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}"
                .format(sv. id, sv._name, sv. sex, sv._major, sv. diemTB, sv. hocLuc))
        print("\n")
    def getListSinhVien(self):
        return self.listSinhVien