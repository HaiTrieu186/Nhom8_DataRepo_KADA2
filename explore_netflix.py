"""
Khám phá và Phân tích Dữ liệu Netflix (Exploratory Data Analysis - EDA)
Sử dụng: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
Nhóm 8 - KADA
Hỗ trợ cả 2 tệp: netflix_titles_cleaned.csv và netflix_titles.csv
"""

import os
import sys

# Cấu hình encoding và tối ưu luồng OpenBLAS trên Windows
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Cấu hình giao diện biểu đồ
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
sns.set_palette("tab10")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.sans-serif'] = 'Arial'

# 1. ĐỌC DỮ LIỆU (Tự động ưu tiên file đã làm sạch)
base_dir = os.path.dirname(__file__)
cleaned_path = os.path.join(base_dir, "netflix_titles_cleaned.csv")
raw_path = os.path.join(base_dir, "netflix_titles.csv")
csv_path = cleaned_path if os.path.exists(cleaned_path) else raw_path

print("="*60)
print(f"ĐANG TẢI DỮ LIỆU TỪ: {csv_path}")
print("="*60)

df = pd.read_csv(csv_path)

# 2. KHẢO SÁT TỔNG QUAN
print("\n--- 1. TỔNG QUAN TẬP DỮ LIỆU ---")
print(f"Số dòng: {df.shape[0]:,}")
print(f"Số cột: {df.shape[1]}")
print("\nDanh sách các cột:")
for col in df.columns:
    print(f" - {col}: {df[col].dtype}")

print("\n--- 2. KIỂM TRA GIÁ TRỊ THIẾU (NULL VALUES) ---")
missing = df.isnull().sum()
if (missing > 0).any():
    missing_percent = (missing / len(df)) * 100
    missing_df = pd.DataFrame({'Missing Count': missing, 'Missing %': missing_percent})
    print(missing_df[missing_df['Missing Count'] > 0])
else:
    print("Dữ liệu hoàn toàn sạch, không có giá trị thiếu (0 missing values).")

# 3. CHUẨN HÓA CÁC TRƯỜNG DỮ LIỆU
df_clean = df.copy()
if 'duration_int' not in df_clean.columns:
    df_clean['duration_int'] = df_clean['duration'].astype(str).str.extract('(\\d+)').astype(float).fillna(0).astype(int)
if 'primary_country' not in df_clean.columns:
    df_clean['country'] = df_clean['country'].fillna('Unknown')
    df_clean['primary_country'] = df_clean['country'].apply(lambda x: x.split(',')[0].strip())
if 'year_added' not in df_clean.columns:
    df_clean['date_added'] = pd.to_datetime(df_clean['date_added'].astype(str).str.strip(), format='%B %d, %Y', errors='coerce')
    df_clean['year_added'] = df_clean['date_added'].dt.year.fillna(df_clean['release_year']).astype(int)

# 4. TRỰC QUAN HÓA & PHÂN TÍCH (VISUALIZATION)
output_dir = os.path.join(base_dir, "visualizations")
os.makedirs(output_dir, exist_ok=True)

# 4.1 Tỷ lệ Movies vs TV Shows
plt.figure(figsize=(7, 7))
type_counts = df_clean['type'].value_counts()
colors = ['#e50914', '#221f1f']
plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=140, colors=colors,
        explode=[0.05, 0], shadow=True, textprops={'fontsize': 12, 'weight': 'bold'})
plt.title('Tỷ lệ Phim lẻ (Movie) vs Phim bộ (TV Show) trên Netflix', fontsize=14, weight='bold')
plt.savefig(os.path.join(output_dir, '1_type_distribution.png'), bbox_inches='tight', dpi=300)
plt.close()

# 4.2 Lượng nội dung được thêm theo năm (Content Added Trend)
plt.figure(figsize=(12, 5))
yearly_trend = df_clean.groupby(['year_added', 'type']).size().unstack().fillna(0)
yearly_trend.plot(kind='line', marker='o', linewidth=2.5, color=['#e50914', '#0071eb'], ax=plt.gca())
plt.title('Xu hướng phát hành nội dung mới theo năm trên Netflix', fontsize=14, weight='bold')
plt.xlabel('Năm thêm vào Netflix', fontsize=12)
plt.ylabel('Số lượng phim', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig(os.path.join(output_dir, '2_content_growth_trend.png'), bbox_inches='tight', dpi=300)
plt.close()

# 4.3 Top 10 Quốc gia sản xuất nhiều nội dung nhất
plt.figure(figsize=(12, 6))
top_countries = df_clean[df_clean['primary_country'] != 'Unknown']['primary_country'].value_counts().head(10)
sns.barplot(x=top_countries.values, y=top_countries.index, palette='viridis', hue=top_countries.index, legend=False)
plt.title('Top 10 Quốc gia sản xuất nhiều nội dung nhất trên Netflix', fontsize=14, weight='bold')
plt.xlabel('Số lượng tác phẩm', fontsize=12)
plt.ylabel('Quốc gia', fontsize=12)
for i, v in enumerate(top_countries.values):
    plt.text(v + 15, i, str(v), color='black', va='center', fontweight='bold')
plt.savefig(os.path.join(output_dir, '3_top_10_countries.png'), bbox_inches='tight', dpi=300)
plt.close()

# 4.4 Phân bổ độ tuổi xem (Ratings)
plt.figure(figsize=(12, 6))
rating_order = df_clean['rating'].value_counts().index
sns.countplot(data=df_clean, x='rating', order=rating_order, hue='type', palette={'Movie': '#e50914', 'TV Show': '#221f1f'})
plt.title('Phân bố xếp hạng độ tuổi (Rating) theo loại nội dung', fontsize=14, weight='bold')
plt.xlabel('Độ tuổi / Phân loại', fontsize=12)
plt.ylabel('Số lượng', fontsize=12)
plt.xticks(rotation=45)
plt.savefig(os.path.join(output_dir, '4_ratings_distribution.png'), bbox_inches='tight', dpi=300)
plt.close()

# 4.5 Phân bố thời lượng phim lẻ (Movie Duration Distribution)
plt.figure(figsize=(10, 5))
movies_df = df_clean[df_clean['type'] == 'Movie']
sns.histplot(movies_df['duration_int'], kde=True, bins=35, color='#e50914')
mean_dur = movies_df['duration_int'].mean()
plt.title('Phân bố thời lượng phim lẻ (Phút)', fontsize=14, weight='bold')
plt.xlabel('Thời lượng (Phút)', fontsize=12)
plt.ylabel('Tần suất', fontsize=12)
plt.axvline(mean_dur, color='blue', linestyle='dashed', linewidth=2, label=f'Trung bình: {mean_dur:.1f} phút')
plt.legend()
plt.savefig(os.path.join(output_dir, '5_movie_duration_dist.png'), bbox_inches='tight', dpi=300)
plt.close()

# 4.6 Top 10 Thể loại phổ biến nhất
plt.figure(figsize=(12, 6))
genres = df_clean['listed_in'].str.split(', ').explode().value_counts().head(10)
sns.barplot(x=genres.values, y=genres.index, palette='mako', hue=genres.index, legend=False)
plt.title('Top 10 Thể loại phim phổ biến nhất trên Netflix', fontsize=14, weight='bold')
plt.xlabel('Số lượng tác phẩm', fontsize=12)
plt.ylabel('Thể loại', fontsize=12)
for i, v in enumerate(genres.values):
    plt.text(v + 10, i, str(v), color='black', va='center', fontweight='bold')
plt.savefig(os.path.join(output_dir, '6_top_genres.png'), bbox_inches='tight', dpi=300)
plt.close()

print(f"\n--- 4. ĐÃ LƯU 6 BIỂU ĐỒ VÀO THƯ MỤC: {output_dir} ---")

# 5. ỨNG DỤNG MACHINE LEARNING: GỢI Ý PHIM DỰA TRÊN NỘI DUNG (CONTENT-BASED RECOMMENDER)
print("\n--- 5. MACHINE LEARNING: XÂY DỰNG HỆ THỐNG GỢI Ý PHIM (TF-IDF & COSINE SIMILARITY) ---")

# Kết hợp text: listed_in + description
df_clean['features'] = df_clean['listed_in'].fillna('') + ' ' + df_clean['description'].fillna('')

# Tạo ma trận TF-IDF
tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
tfidf_matrix = tfidf.fit_transform(df_clean['features'])

# Tính ma trận độ tương đồng Cosine
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Hàm gợi ý phim
def recommend_movies(title, num_recommendations=5):
    matches = df_clean[df_clean['title'].str.lower() == title.lower()]
    if matches.empty:
        return f"Không tìm thấy phim '{title}' trong tập dữ liệu!"
    
    idx = matches.index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]
    
    movie_indices = [i[0] for i in sim_scores]
    results = df_clean.iloc[movie_indices][['title', 'type', 'listed_in', 'release_year', 'rating']]
    return results

# Thử nghiệm gợi ý cho phim "Squid Game" và "Dark Skies"
print("\n[Demo Gợi ý] 5 Phim tương tự 'Squid Game':")
print(recommend_movies("Squid Game"))

print("\n[Demo Gợi ý] 5 Phim tương tự 'Dark Skies':")
print(recommend_movies("Dark Skies"))

print("\n" + "="*60)
print("PHÂN TÍCH HOÀN TẤT THÀNH CÔNG!")
print("="*60)
