import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Thông tin nhân viên")
root.geometry("700x400")

# Frame chính
frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky="nsew")

# Tiêu đề và các checkbox
title_frame = ttk.Frame(frame)
title_frame.grid(row=0, column=0, columnspan=4, sticky="w")

ttk.Label(title_frame, text="Thông tin nhân viên", font=("Arial", 14, "bold")).grid(row=0, column=0, sticky="w", pady=5)

# Checkboxes bên cạnh tiêu đề
checkbox_frame = ttk.Frame(title_frame)
checkbox_frame.grid(row=0, column=1, padx=10, sticky="e")
ttk.Checkbutton(checkbox_frame, text="Là khách hàng").grid(row=0, column=0, padx=5)
ttk.Checkbutton(checkbox_frame, text="Là nhà cung cấp").grid(row=0, column=1, padx=5)

# Mã
ttk.Label(frame, text="Mã *").grid(row=1, column=0, sticky="w", pady=5)
ma_entry = ttk.Entry(frame, width=30)
ma_entry.grid(row=1, column=1, padx=10, pady=5)

# Tên
ttk.Label(frame, text="Tên *").grid(row=1, column=2, sticky="w", pady=5)
ten_entry = ttk.Entry(frame, width=30)
ten_entry.grid(row=1, column=3, padx=10, pady=5)

# Đơn vị
ttk.Label(frame, text="Đơn vị *").grid(row=2, column=0, sticky="w", pady=5)
donvi_combobox = ttk.Combobox(frame, values=["Phân xưởng que hàn", "Bộ phận khác"], width=28)
donvi_combobox.grid(row=2, column=1, padx=10, pady=5)

# Ngày sinh
ttk.Label(frame, text="Ngày sinh").grid(row=2, column=2, sticky="w", pady=5)
ngaysinh_entry = ttk.Entry(frame, width=30)
ngaysinh_entry.grid(row=2, column=3, padx=10, pady=5)

# Chức danh
ttk.Label(frame, text="Chức danh").grid(row=3, column=0, sticky="w", pady=5)
chucdanh_entry = ttk.Entry(frame, width=30)
chucdanh_entry.grid(row=3, column=1, padx=10, pady=5)

# Giới tính
ttk.Label(frame, text="Giới tính").grid(row=3, column=2, sticky="w", pady=5)
gioitinh_var = tk.StringVar(value="Nam")
ttk.Radiobutton(frame, text="Nam", variable=gioitinh_var, value="Nam").grid(row=3, column=3, sticky="w")
ttk.Radiobutton(frame, text="Nữ", variable=gioitinh_var, value="Nữ").grid(row=3, column=3, sticky="e")

# Số CMND
ttk.Label(frame, text="Số CMND").grid(row=4, column=0, sticky="w", pady=5)
socmnd_entry = ttk.Entry(frame, width=30)
socmnd_entry.grid(row=4, column=1, padx=10, pady=5)

# Nơi cấp
ttk.Label(frame, text="Nơi cấp").grid(row=4, column=2, sticky="w", pady=5)
noicap_entry = ttk.Entry(frame, width=30)
noicap_entry.grid(row=4, column=3, padx=10, pady=5)

# Ngày cấp
ttk.Label(frame, text="Ngày cấp").grid(row=5, column=0, sticky="w", pady=5)
ngaycap_entry = ttk.Entry(frame, width=30)
ngaycap_entry.grid(row=5, column=1, padx=10, pady=5)


root.mainloop()
