import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import folium

# 全局变量
all_entries = []
current_index = [0]


def save_entry_data(entries):
    """
    将输入框中内容保存到 all_entries 列表中。
    如果样点编号已存在，则覆盖提醒。
    保存后会清空输入框。
    """
    global all_entries, current_index
    entry_id = entries["样点编号"].get()
    # 若已存在相同编号的记录，则覆盖
    for index, entry in enumerate(all_entries):
        if entry["样点编号"] == entry_id:
            messagebox.showwarning("警告", "覆盖相同编号的记录")
            all_entries[index] = {
                field: entries[field].get() for field in entries
            }
            return

    # 如果不存在相同编号，就追加
    data = {field: entries[field].get() for field in entries}
    all_entries.append(data)
    current_index[0] = len(all_entries) - 1  # 更新到最新一条
    # 清空所有输入框
    for field, widget in entries.items():
        if isinstance(widget, ttk.Combobox):
            widget.set('')
        else:
            widget.delete(0, tk.END)


def show_previous_entry(entries):
    """
    查看上一个样点信息。
    """
    global all_entries, current_index
    if current_index[0] > 0:
        current_index[0] -= 1
        data = all_entries[current_index[0]]
        for field, widget in entries.items():
            widget.delete(0, tk.END)
            widget.insert(0, data.get(field, ''))


def show_next_entry(entries):
    """
    查看下一个样点信息。
    """
    global all_entries, current_index
    if current_index[0] < len(all_entries) - 1:
        current_index[0] += 1
        data = all_entries[current_index[0]]
        for field, widget in entries.items():
            widget.delete(0, tk.END)
            widget.insert(0, data.get(field, ''))


def import_from_excel():
    """
    从 Excel 文件导入数据，扩展到 all_entries 列表中。
    """
    global all_entries
    file_path = filedialog.askopenfilename(
        filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
    )
    if file_path:
        df = pd.read_excel(file_path)
        imported_entries = df.to_dict(orient='records')
        all_entries.extend(imported_entries)
        messagebox.showinfo("导入成功", "Excel数据已成功导入")


def export_to_excel():
    """
    将 all_entries 列表中的内容导出到 Excel 文件。
    """
    global all_entries
    file_path = filedialog.asksaveasfilename(
        defaultextension='.xlsx',
        filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
    )
    if file_path:
        df = pd.DataFrame(all_entries)
        df.to_excel(file_path, index=False)
        messagebox.showinfo("成功", "数据已导出到Excel")


def show_on_map(entries):
    """
    使用 folium 在地图上显示所有样点信息。
    并根据用地类型改变标记颜色。
    """
    global all_entries
    try:
        # 初始地图中心点（以武汉市坐标为例）
        m = folium.Map(location=[30.5928, 114.3055], zoom_start=6)

        for entry in all_entries:
            lon = entry.get("点的经度", "")
            lat = entry.get("点的纬度", "")
            if lon and lat:
                longitude = float(lon)
                latitude = float(lat)
                popup_info = "<br>".join([f"{k}: {v}" for k, v in entry.items()])

                # 不同用地类型 -> 不同颜色
                land_type = entry.get("用地类型", "")
                color = "purple"  # 默认颜色
                if land_type == "耕地":
                    color = "lightgreen"
                elif land_type == "园地":
                    color = "orange"
                elif land_type == "林地":
                    color = "darkgreen"
                elif land_type == "草地":
                    color = "olive"
                elif land_type == "坑塘水面":
                    color = "blue"

                folium.Marker(
                    [latitude, longitude],
                    popup=popup_info,
                    icon=folium.Icon(color=color)
                ).add_to(m)

        file_path = filedialog.asksaveasfilename(
            defaultextension='.html',
            filetypes=[("HTML files", "*.html"), ("All files", "*.*")]
        )
        if file_path:
            m.save(file_path)
            messagebox.showinfo("成功", f"地图已保存为 {file_path}")
    except ValueError:
        messagebox.showerror("错误", "请输入有效的经纬度")


def layout_input_fields(window, entries):
    """
    在输入界面中布局所有输入字段。
    """
    fields = [
        "样点编号", "所在城区", "空间要素类型", "所在街道", "所在行政村",
        "用地类型", "作物类型", "物化投入（元/每亩）", "劳动投入（元/人/天）",
        "每亩总投入（元）", "每亩总产出（元）", "每亩总收益（元）",
        "点的经度", "点的纬度"
    ]

    city_options = ["东西湖区", "蔡甸区", "汉南区", "黄陂区", "新洲区", "江夏区"]
    element_options = ["点", "线", "面"]
    land_options = ["耕地", "园地", "林地", "草地", "坑塘水面", "其他"]

    row = 0
    for field in fields:
        label = tk.Label(window, text=field, bg='lightgrey')
        label.grid(row=row, column=0, padx=5, pady=5, sticky="e")

        if field == "所在城区":
            entry = ttk.Combobox(window, values=city_options)
        elif field == "空间要素类型":
            entry = ttk.Combobox(window, values=element_options)
        elif field == "用地类型":
            entry = ttk.Combobox(window, values=land_options)
        else:
            entry = tk.Entry(window)

        entry.grid(row=row, column=1, padx=5, pady=5, sticky="w")
        entries[field] = entry
        row += 1

    # 自动计算“每亩总收益（元）”的逻辑
    def calculate_profit():
        try:
            total_input = float(entries["每亩总投入（元）"].get())
            total_output = float(entries["每亩总产出（元）"].get())
            profit = total_output - total_input
            entries["每亩总收益（元）"].delete(0, tk.END)
            entries["每亩总收益（元）"].insert(0, str(profit))
        except ValueError:
            pass

    # 失去焦点后计算收益
    entries["每亩总投入（元）"].bind("<FocusOut>", lambda e: calculate_profit())
    entries["每亩总产出（元）"].bind("<FocusOut>", lambda e: calculate_profit())


def show_input_interface():
    """
    弹出输入界面，用于录入和管理样点信息。
    """
    input_window = tk.Toplevel()
    input_window.geometry("600x700")
    input_window.configure(bg='lightgrey')
    input_window.title("样点信息输入")

    entries = {}
    layout_input_fields(input_window, entries)

    # 按钮：保存
    save_btn = tk.Button(input_window, text="输入保存",
                         command=lambda: save_entry_data(entries), bg='grey')
    save_btn.grid(row=0, column=2, padx=15, pady=10)

    # 按钮：查看上一个样点
    prev_btn = tk.Button(input_window, text="查看上一个样点",
                         command=lambda: show_previous_entry(entries), bg='grey')
    prev_btn.grid(row=1, column=2, padx=15, pady=10)

    # 按钮：查看下一个样点
    next_btn = tk.Button(input_window, text="查看下一个样点",
                         command=lambda: show_next_entry(entries), bg='grey')
    next_btn.grid(row=2, column=2, padx=15, pady=10)

    # 按钮：导入Excel
    import_btn = tk.Button(input_window, text="导入Excel",
                           command=import_from_excel, bg='lightgreen')
    import_btn.grid(row=3, column=2, padx=15, pady=10)

    # 按钮：导出为Excel
    export_btn = tk.Button(input_window, text="导出为Excel",
                           command=export_to_excel, bg='lightgreen')
    export_btn.grid(row=4, column=2, padx=15, pady=10)

    # 按钮：地图显示
    map_btn = tk.Button(input_window, text="在地图上显示",
                        command=lambda: show_on_map(entries),
                        bg='lightblue')
    map_btn.grid(row=5, column=2, padx=15, pady=10)


def main_interface():
    """
    主界面，显示初始窗口 + “点击输入”按钮。
    """
    root = tk.Tk()
    root.geometry("800x600")
    root.configure(bg='blue')
    root.title("农用地调查系统")

    welcome_label = tk.Label(
        root,
        text="武汉市农用地基准地价实地调查样点\n信息输入系统（2023版）",
        bg='blue', fg='white', font=("宋体", 25, 'bold')
    )
    welcome_label.pack(pady=50)

    def on_click_enter():
        show_input_interface()

    enter_button = tk.Button(root, text="点击输入",
                             font=("宋体", 20),
                             command=on_click_enter,
                             height=2, width=20)
    enter_button.pack(pady=20)

    developer_label = tk.Label(
        root, text="开发者：华中师范大学 张祚",
        bg='blue', fg='white', font=("宋体", 20)
    )
    developer_label.pack(pady=60)

    root.mainloop()


# 仅当直接运行 gui.py 时，执行主界面
if __name__ == "__main__":
    main_interface()
