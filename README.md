# 🎬 Nhóm 8 - KADA Data Repository: Phân Tích & Trực Quan Hóa Dữ Liệu Netflix

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HaiTrieu186/Nhom8_DataRepo_KADA2/blob/main/explore_netflix.ipynb)
![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Jupyter](https://img.shields.io/badge/Jupyter-Lab%20%2F%20Notebook-orange.svg)
![Dataset](https://img.shields.io/badge/Dataset-8%2C807%20Titles-red.svg)

## Danh Sách Thành Viên Nhóm 8

1. **Phạm Nguyễn Hải Triều** - Nhóm trưởng
2. **Lương Võ Khôi Quốc**
3. **Mô Ha Mách Bu Ba Ka**
4. **Trần Quốc Huy**
5. **Võ Ngọc Ngà**
6. **Trần Thị Hồng Vân**

---

## Giới Thiệu Dự Án

Repository lưu trữ tài liệu, mã nguồn làm sạch và hệ thống trực quan hóa dữ liệu cho khóa học **KADA - Phân tích dữ liệu & Trí tuệ nhân tạo**.

Dự án tập trung khai thác tập dữ liệu **Netflix Movies & TV Shows (8.807 tác phẩm)** nhằm giải mã chiến lược nội dung, phân khúc khán giả, chu kỳ phát hành mùa vụ và các xu hướng điện ảnh toàn cầu.

### Chạy Trực Tuyến Trên Google Colab

Bạn có thể mở và chạy trực tiếp Notebook phân tích trên Google Colab mà không cần cài đặt môi trường trên máy:

- **[Mở Notebook EDA cơ bản trên Google Colab](https://colab.research.google.com/github/HaiTrieu186/Nhom8_DataRepo_KADA2/blob/main/explore_netflix.ipynb)**

---

## Cấu Trúc Dự Án (Project Structure)

```text
Nhom8/
├── netflix_titles_cleaned.csv            # Dữ liệu 8.807 titles đã làm sạch & chuẩn hóa
├── netflix_titles.csv                    # Tập dữ liệu gốc từ Netflix
├── clean_data.py                         # Kịch bản xử lý giá trị khuyết thiếu và kỹ thuật trích xuất đặc trưng
├── explore_netflix.ipynb                 # Notebook khám phá & EDA nền tảng
├── explore_netflix.py                    # Script tự động hóa phân tích EDA và xuất biểu đồ
├── netflix_visualizations_dashboard.ipynb# 🌟 Dashboard toàn diện với 18 biểu đồ thuộc 7 nhóm chủ đề
├── build_netflix_charts_notebook.py      # Kịch bản tự động xây dựng & tái tạo dashboard notebook
├── README.md                             # Tài liệu hướng dẫn dự án
├── visualizations/                       # Thư mục lưu trữ hình ảnh biểu đồ độ phân giải cao
└── venv/                                 # Môi trường ảo Python cục bộ
```

---

## Hệ Thống 18 Biểu Đồ Dashboard Chuyên Sâu (`netflix_visualizations_dashboard.ipynb`)

File Notebook **`netflix_visualizations_dashboard.ipynb`** được thiết kế theo phong cách giao diện hiện đại (**Netflix Brand Aesthetic: `#E50914`, `#141414`, `#221F1F`, `#0071EB`**), đã nhúng sẵn toàn bộ kết quả thực thi cho 18 biểu đồ thuộc 7 nhóm phân tích:

| Nhóm Phân Tích             |   #    | Tên Biểu Đồ                                  | Loại Biểu Đồ             | Phát Hiện & Ý Nghĩa Cốt Lõi                                                                    |
| :------------------------- | :----: | :------------------------------------------- | :----------------------- | :--------------------------------------------------------------------------------------------- |
| **1. Tổng Quan Nội Dung**  | **1**  | Cơ cấu Phim lẻ vs Phim bộ                    | **Donut Chart**          | Movie chiếm **69.6%** (6.131 titles), TV Show chiếm **30.4%** (2.676 titles).                  |
|                            | **2**  | Top 10 quốc gia sản xuất                     | **Horizontal Bar**       | Mỹ dẫn đầu (**3.211**), Ấn Độ đứng thứ 2 (**1.008**), tiếp đến là Anh (**628**).               |
| **2. Xu Hướng Thời Gian**  | **3**  | Tốc độ bổ sung nội dung mới                  | **Area Chart**           | Bùng nổ từ 2016 và đạt đỉnh năm 2019 (**2.016 titles**), chững lại trong đại dịch.             |
|                            | **4**  | So sánh Movie vs TV Show                     | **Grouped Bar**          | Phim lẻ dẫn đầu tăng trưởng; TV Show ổn định hơn trong giai đoạn 2020-2021.                    |
|                            | **5**  | Ma trận mùa vụ Tháng × Năm                   | **Heatmap (2D)**         | Tháng 7 (kỳ nghỉ hè) & Tháng 12 (lễ hội cuối năm) luôn là điểm rơi phát hành đậm đặc nhất.     |
|                            | **6**  | Phân phối theo 12 tháng                      | **Bar Chart**            | Tháng 7 cao nhất (**827**), Tháng 12 (**813**); Tháng 2 thấp nhất (**563**).                   |
| **3. Thể Loại & Rating**   | **7**  | Top 15 thể loại phổ biến                     | **Horizontal Bar**       | **Dramas (1.600)** và **Comedies (1.210)** áp đảo; Stand-Up Comedy đạt **334** show độc quyền. |
|                            | **8**  | Phân phối phân loại độ tuổi                  | **Bar Chart**            | Hơn 61% nội dung dành cho 14+ trở lên (**TV-MA 36.5%**, **TV-14 24.5%**).                      |
|                            | **9**  | Rating giữa Movie vs TV Show                 | **100% Stacked Bar**     | TV Show tập trung rất cao vào TV-MA (~43%); Movie phân bổ đều sang R, PG-13, PG.               |
| **4. Thời Lượng & Số Mùa** | **10** | Thời lượng phim lẻ (phút)                    | **Histogram & KDE**      | Trung bình **99.6 phút**, phân phối chuẩn hội tụ tại khoảng vàng **80–120 phút**.              |
|                            | **11** | Vòng đời số mùa TV Show                      | **Bar Chart**            | **67.0% TV Shows chỉ phát sóng 1 Mùa**; tỷ lệ giảm mạnh ở các mùa sau.                         |
| **5. Địa Lý & Năm SX**     | **12** | Bản đồ nội dung toàn cầu                     | **Choropleth Map**       | Bản đồ mật độ sản xuất toàn cầu (Bắc Mỹ, Nam Á, Tây Âu, Đông Á) qua Plotly.                    |
|                            | **13** | Phân phối năm sản xuất gốc                   | **Area Chart**           | Phim trải dài từ 1925 đến 2021; hơn 85% thư viện sản xuất từ sau năm 2010.                     |
| **6. Đạo Diễn & Dàn Cast** | **14** | Top 10 đạo diễn tiêu biểu                    | **Horizontal Bar**       | Rajiv Chilaka (**19**), Martin Scorsese (**12**), Steven Spielberg (**11**).                   |
|                            | **15** | Quy mô dàn diễn viên                         | **Box Plot (IQR)**       | Dramas/Action trung bình 8–12 diễn viên; Stand-Up & Docuseries chỉ 0–1 người.                  |
| **7. Nâng Cao & NLP**      | **16** | Năm SX vs Thời lượng phim                    | **Scatter Plot + Trend** | Phim cổ điển biến thiên rộng (>180p); phim hiện đại gom gọn quanh 90–110p.                     |
|                            | **17** | Hệ sinh thái Quốc gia $\rightarrow$ Thể loại | **Treemap Phân Tầng**    | Mỹ (Dramas/Stand-Up), Ấn Độ (Bollywood), Nhật (Anime), Hàn Quốc (K-Dramas).                    |
|                            | **18** | Khai phá từ khóa cốt truyện                  | **Word Cloud**           | Môtíp đối trọng: _love, life, family_ song hành cùng _murder, secret, crime_.                  |

---

## Hướng Dẫn Cài Đặt Môi Trường (Local Setup)

### 1. Kích hoạt môi trường ảo (Virtual Environment)

- **Windows (PowerShell):**

  ```powershell
  Set-Location "Nhom8"
  .\venv\Scripts\Activate.ps1
  ```

- **Windows (Command Prompt):**

  ```cmd
  cd Nhom8
  venv\Scripts\activate
  ```

- **macOS / Linux:**
  ```bash
  cd Nhom8
  source venv/bin/activate
  ```

### 2. Cài đặt các gói thư viện phụ thuộc

```bash
pip install jupyterlab pandas numpy matplotlib seaborn plotly wordcloud scikit-learn nbformat nbclient
```

### 3. Khởi chạy Dashboard và phân tích

- **Mở Dashboard 18 biểu đồ hoàn chỉnh:**

  ```bash
  jupyter lab netflix_visualizations_dashboard.ipynb
  ```

- **Mở Notebook phân tích khám phá (EDA cơ bản):**

  ```bash
  jupyter lab explore_netflix.ipynb
  ```

- **Chạy script phân tích tự động:**

  ```bash
  python explore_netflix.py
  ```

- **Tái tạo tự động file Notebook Dashboard:**
  ```bash
  python build_netflix_charts_notebook.py
  ```

---

## Tóm Tắt Nhận Định Chiến Lược (Key Insights)

1. **Chiến lược giữ chân (Retention):** Dù Phim lẻ chiếm gần 70% danh mục, TV Shows đóng vai trò cốt lõi duy trì lượng người đăng ký theo tháng.
2. **Khai thác thị trường:** Hoa Kỳ và Ấn Độ là hai động cơ sản xuất lớn nhất, tạo nền móng vững chắc cho danh mục phim quốc tế.
3. **Chu kỳ mùa vụ:** Tháng 7 và Tháng 12 là thời điểm vàng để tung ra các chiến dịch tiếp thị và phát hành bom tấn.
4. **Quy chuẩn thời lượng:** Phim lẻ 90–110 phút là định dạng tối ưu nhất cho trải nghiệm người dùng streaming.

---

**Nhóm 8 - KADA** | Cập nhật: Tháng 9/2026
