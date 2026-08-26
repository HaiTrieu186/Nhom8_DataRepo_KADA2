# Nhóm 8 - KADA Data Repository

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HaiTrieu186/Nhom8_DataRepo_KADA2/blob/main/explore_netflix.ipynb)

## 👥 Danh Sách Thành Viên Nhóm 8

1. **Phạm Nguyễn Hải Triều**
2. **Lương Võ Khôi Quốc**
3. **Mô Ha Mách Bu Ba Ka**
4. **Trần Quốc Huy**
5. **Nguyễn Chí Thịnh**

---

## 📌 Giới Thiệu Dự Án

Repository lưu trữ tài liệu, mã nguồn và dữ liệu thực hành cho khóa học **KADA - Phân tích dữ liệu & Trí tuệ nhân tạo**.

### 🚀 Chạy Trực Tuyến Trên Google Colab
Bạn có thể mở và chạy trực tiếp file Notebook phân tích dữ liệu Netflix trên Google Colab mà không cần cài đặt môi trường trên máy:
👉 **[Mở Notebook trên Google Colab](https://colab.research.google.com/github/HaiTrieu186/Nhom8_DataRepo_KADA2/blob/main/explore_netflix.ipynb)**

---

## 🛠️ Hướng Dẫn Cài Đặt Môi Trường (Local)

### 1. Kích hoạt môi trường ảo (venv)

- **Windows (Command Prompt):**
  ```cmd
  cd Nhom8
  venv\Scripts\activate
  ```

- **Windows (PowerShell):**
  ```powershell
  Set-Location "Nhom8"
  .\venv\Scripts\Activate.ps1
  ```

- **macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```

### 2. Cài đặt các thư viện phụ thuộc

```bash
pip install jupyterlab pandas numpy matplotlib seaborn scikit-learn
```

### 3. Khởi chạy Jupyter Lab hoặc File Python

- **Khởi chạy Jupyter Lab:**
  ```bash
  jupyter lab
  ```
  *(Mở file `explore_netflix.ipynb` để tương tác trực quan)*

- **Chạy Script phân tích:**
  ```bash
  python explore_netflix.py
  ```
