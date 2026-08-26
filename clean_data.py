"""
Quy Trình Làm Sạch Dữ Liệu Netflix (Data Cleaning Pipeline)
Tệp đầu vào: netflix_titles.csv
Tệp đầu ra: netflix_titles_cleaned.csv
Nhóm 8 - KADA
"""

import os
import sys
import pandas as pd
import numpy as np

# Cấu hình UTF-8 cho Windows console
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Đường dẫn file
base_dir = os.path.dirname(__file__)
input_file = os.path.join(base_dir, "netflix_titles.csv")
output_file = os.path.join(base_dir, "netflix_titles_cleaned.csv")

print("=" * 65)
print("BẮT ĐẦU QUY TRÌNH LÀM SẠCH DỮ LIỆU NETFLIX (DATA CLEANING)")
print("=" * 65)

# 1. Đọc dữ liệu thô
df = pd.read_csv(input_file)
initial_rows = len(df)
print(f"\n1. Dữ liệu gốc: {initial_rows:,} dòng, {df.shape[1]} cột")

# 2. Xử lý trùng lặp (Duplicates)
duplicates = df.duplicated().sum()
print(f"2. Số dòng trùng lặp hoàn toàn: {duplicates}")
if duplicates > 0:
    df = df.drop_duplicates()

# 3. Sửa lỗi lệch cột (Data Misalignment)
# Một số phim của Louis C.K. bị ghi nhầm thời lượng vào cột rating (ví dụ: '74 min')
misaligned_mask = df['rating'].astype(str).str.contains('min', na=False)
num_misaligned = misaligned_mask.sum()
print(f"3. Sửa lỗi lệch cột duration nằm trong rating ({num_misaligned} dòng)...")

df.loc[misaligned_mask & df['duration'].isnull(), 'duration'] = df.loc[misaligned_mask, 'rating']
df.loc[misaligned_mask, 'rating'] = 'NR'  # Gán lại rating thành Not Rated

# 4. Xử lý giá trị bị thiếu (Missing Values / Imputation)
print("\n4. Xử lý các giá trị bị thiếu:")
print(" - Cột 'director': Điền 'Unknown' cho giá trị thiếu")
df['director'] = df['director'].fillna('Unknown').str.strip()

print(" - Cột 'cast': Điền 'Unknown' cho giá trị thiếu")
df['cast'] = df['cast'].fillna('Unknown').str.strip()

print(" - Cột 'country': Điền 'Unknown' cho giá trị thiếu")
df['country'] = df['country'].fillna('Unknown').str.strip()

print(" - Cột 'rating': Điền giá trị phổ biến nhất (Mode) cho các dòng còn trống")
df['rating'] = df['rating'].fillna(df['rating'].mode()[0]).str.strip()

# 5. Chuẩn hóa và làm sạch ngày tháng (date_added)
print("\n5. Chuẩn hóa cột thời gian 'date_added' sang định dạng chuẩn YYYY-MM-DD:")
df['date_added'] = df['date_added'].astype(str).str.strip()
df['date_added_dt'] = pd.to_datetime(df['date_added'], format='%B %d, %Y', errors='coerce')

# Điền ngày thêm vào nếu thiếu dựa theo release_year (ngày 01/01 của năm phát hành)
missing_date_mask = df['date_added_dt'].isnull()
df.loc[missing_date_mask, 'date_added_dt'] = pd.to_datetime(
    df.loc[missing_date_mask, 'release_year'].astype(str) + '-01-01'
)

df['date_added_clean'] = df['date_added_dt'].dt.strftime('%Y-%m-%d')
df['year_added'] = df['date_added_dt'].dt.year.astype(int)
df['month_added'] = df['date_added_dt'].dt.month.astype(int)

# 6. Chuẩn hóa thời lượng (duration) thành số và đơn vị
print("\n6. Trích xuất thời lượng thành trường số (duration_int) và đơn vị (duration_unit):")
df['duration_int'] = df['duration'].astype(str).str.extract('(\\d+)').astype(float).fillna(0).astype(int)
df['duration_unit'] = df['duration'].astype(str).str.extract('([a-zA-Z]+)').fillna('min')

# 7. Trích xuất đặc trưng bổ sung (Feature Engineering)
print("\n7. Tạo các cột đặc trưng mới:")
# Quốc gia chính (quốc gia đầu tiên xuất hiện trong danh sách)
df['primary_country'] = df['country'].apply(lambda x: x.split(',')[0].strip() if x != 'Unknown' else 'Unknown')

# Thể loại chính (thể loại đầu tiên)
df['primary_genre'] = df['listed_in'].apply(lambda x: x.split(',')[0].strip())

# Số lượng diễn viên tham gia
df['cast_count'] = df['cast'].apply(lambda x: len(x.split(',')) if x != 'Unknown' else 0)

# Chuẩn hóa chuỗi text (loại bỏ khoảng trắng thừa)
for text_col in ['title', 'type', 'listed_in', 'description']:
    df[text_col] = df[text_col].astype(str).str.strip()

# 8. Sắp xếp lại thứ tự cột cho gọn gàng và dễ theo dõi
columns_order = [
    'show_id',
    'type',
    'title',
    'director',
    'cast',
    'cast_count',
    'country',
    'primary_country',
    'date_added_clean',
    'year_added',
    'month_added',
    'release_year',
    'rating',
    'duration_int',
    'duration_unit',
    'listed_in',
    'primary_genre',
    'description'
]

df_cleaned = df[columns_order].copy()
df_cleaned.rename(columns={'date_added_clean': 'date_added'}, inplace=True)

# 9. Xuất file CSV đã làm sạch
df_cleaned.to_csv(output_file, index=False, encoding='utf-8-sig')

print("\n" + "=" * 65)
print(f"XUẤT THÀNH CÔNG FILE DỮ LIỆU ĐÃ LÀM SẠCH:")
print(f"📁 Đường dẫn: {output_file}")
print(f"📊 Kích thước: {len(df_cleaned):,} dòng x {df_cleaned.shape[1]} cột")
print("=" * 65)

# In thử 5 dòng đầu tiên
print("\n[Xem trước 5 dòng đầu tiên của dữ liệu đã làm sạch]:")
print(df_cleaned[['show_id', 'type', 'title', 'primary_country', 'date_added', 'rating', 'duration_int', 'duration_unit']].head())
