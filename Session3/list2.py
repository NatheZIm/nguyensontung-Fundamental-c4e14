# ds = ["Vel'koz","Yasuo","Zed","Shen"]
# for i,p in enumerate(ds):
#     print(i+1,p)
# name = str(input("Any champion you want to master ? "))

# ds.append(name)                                            /// Thêm 1 phần tử
# print(*ds,sep = ' , ')                                     /// sep = dấu cách giữa các phần tử
# for i in range(len(ds)):
#     print(i+1,". ",ds[i])


# pos = int(input("vị trí cần sửa : "))
# value = input("Nội dung cần sửa : ")
# ds[pos-1]=value
# for i in range(len(ds)):
#     print(i+1,". ",ds[i])


# in cả chỉ số và nội dung
# for i , ds in enumerate(ds):
#     print(i+1,ds)


#                                                   /// Xóa vị trí
# wrong = True
# while wrong:
#     pos = int(input("vị trí cần xóa : "))
#     if pos > len(ds) or pos < 1:
#         print("Không có trong danh sách")
#     else:
#         ds.pop(pos-1)
#         for i,p in enumerate(ds):
#             print(i+1,p)
#             wrong = False


#                                                    /// Xóa giá trị
# value = input("Giá trị cần xóa ")
# if value not in ds:
#     print("Hông thấy")
# else:
#     ds.remove(value)
#     for i,p in enumerate(ds):
#         print(i+1,p)
