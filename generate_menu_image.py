import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import font_manager as fm
import numpy as np

# 한글 폰트 설정
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# 데이터 정의
locations = ['장소', '다이소', '이마트', '편의점', '정육점', '집']
items = {
    '다이소': ['일회용접시', '물티슈', '소주잔', '꼬지'],
    '이마트': ['순두부', '햇반', '버섯', '볶음김치', '술', '소시지', '쌈장', '생수', '사과', '귤', '포도'],
    '편의점': ['보리차', '어묵탕', '대파', '방울토마토', '떡'],
    '정육점': ['삼겹200', '목살200', '소200'],
    '집': ['종이컵', '위생장갑', '수저(숟4/젓4)', '소금', '파우치']
}

# Figure 생성
fig, ax = plt.subplots(figsize=(20, 14), dpi=100)
ax.set_xlim(0, 10)
ax.set_ylim(0, 14)
ax.axis('off')

# 제목
title = ax.text(5, 13.5, 'Restaurant Menu & Shopping List', 
                fontsize=48, weight='bold', ha='center', va='top',
                bbox=dict(boxstyle='round,pad=0.8', facecolor='#667eea', edgecolor='black', linewidth=3, alpha=0.8),
                color='white')

# 각 장소별 섹션 생성
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
y_position = 12.5
x_positions = [1.5, 3.5, 5.5, 7.5, 9]

for idx, (location, color) in enumerate(zip(list(items.keys()), colors)):
    x = x_positions[idx]
    
    # 위치 제목
    ax.add_patch(patches.FancyBboxPatch((x-0.7, y_position-0.4), 1.4, 0.5,
                                        boxstyle="round,pad=0.05", 
                                        facecolor=color, edgecolor='black', linewidth=2))
    ax.text(x, y_position-0.15, location, fontsize=18, weight='bold', ha='center', va='center', color='white')
    
    # 항목들
    current_y = y_position - 0.8
    for item in items[location]:
        # 항목 박스
        ax.add_patch(patches.FancyBboxPatch((x-0.65, current_y-0.35), 1.3, 0.4,
                                            boxstyle="round,pad=0.03",
                                            facecolor='white', edgecolor=color, linewidth=1.5))
        ax.text(x, current_y-0.15, item, fontsize=11, ha='center', va='center', weight='bold')
        current_y -= 0.5

# 범례 추가
legend_y = 0.5
ax.text(0.5, legend_y, '📍 장소별 준비물 정리', fontsize=14, weight='bold')
ax.text(0.5, legend_y-0.5, '• 다이소: 일회용품', fontsize=10)
ax.text(0.5, legend_y-0.8, '• 이마트: 식재료', fontsize=10)
ax.text(0.5, legend_y-1.1, '• 편의점: 반찬류', fontsize=10)
ax.text(0.5, legend_y-1.4, '• 정육점: 육류', fontsize=10)
ax.text(0.5, legend_y-1.7, '• 집: 용품 & 준비물', fontsize=10)

plt.tight_layout()
plt.savefig('menu_shopping_list.png', dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
print("Image saved: menu_shopping_list.png")
plt.show()
