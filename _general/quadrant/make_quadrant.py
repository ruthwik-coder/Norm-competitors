"""Builds the Ubanthu competitive quadrant (Gartner-style) from SCORES below.
Edit the scores, then run:  python _general/quadrant/make_quadrant.py
Outputs: _general/quadrant/competitive-quadrant.svg and .png
Scores are internal analysis [INF] on a 0-10 scale; rubric in COMPETITOR_INTELLIGENCE.md."""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))

# name, completeness of vision, ability to execute, style, label dx, label dy, label side
SCORES = [
    ('Hivebotics',          7.8, 7.6, 'company', 0.18, 0.00, 'right'),
    ('Somatic',             6.3, 6.0, 'company', 0.18, 0.00, 'right'),
    ('Wangchao / Octopus',  6.8, 4.7, 'company', 0.18, 0.00, 'right'),
    ('Primech AI',          6.0, 4.1, 'company', 0.18, -0.05, 'right'),
    ('Peanut (defunct)',    5.7, 3.2, 'defunct', 0.18, 0.00, 'right'),
    ('Fonda + A*STAR ALAC', 4.2, 4.2, 'company', -0.18, 0.00, 'left'),
    ('Eternia TCR-H',       4.6, 3.6, 'lowdata', -0.18, 0.00, 'left'),
    ('ZeeqClean',           4.4, 2.8, 'lowdata', -0.18, 0.00, 'left'),
    ('Senxeed WUUMIE',      3.9, 2.3, 'lowdata', -0.18, 0.00, 'left'),
    ('Amrita Sudha',        4.8, 1.3, 'company', 0.18, 0.00, 'right'),
    ('Sketch Robotics',     3.6, 1.4, 'company', -0.18, 0.00, 'left'),
    ('Ubanthu (set by team)', 7.0, 2.0, 'us',    0.20, 0.00, 'right'),
]

BLUE = '#2f6f9f'
fig, ax = plt.subplots(figsize=(8.6, 9.2), dpi=110)
fig.patch.set_facecolor('white')
ax.set_xlim(0, 10); ax.set_ylim(0, 10)
ax.add_patch(plt.Rectangle((5, 5), 5, 5, color='#f4f4f4', zorder=0))
ax.add_patch(plt.Rectangle((0, 0), 5, 5, color='#f4f4f4', zorder=0))
ax.axhline(5, color='#bdbdbd', lw=1); ax.axvline(5, color='#bdbdbd', lw=1)
for s in ax.spines.values():
    s.set_linewidth(2.4); s.set_color('#222')
ax.set_xticks([]); ax.set_yticks([])
for txt, x, y in [('CHALLENGERS', 2.5, 9.62), ('LEADERS', 7.5, 9.62), ('NICHE PLAYERS', 2.5, 0.38), ('VISIONARIES', 7.5, 0.38)]:
    ax.text(x, y, txt, ha='center', va='center', color='white', fontsize=11,
            bbox=dict(boxstyle='square,pad=0.45', fc='#aab7c1', ec='none'))
for name, v, e, style, dx, dy, side in SCORES:
    if style == 'company':
        ax.scatter(v, e, s=170, color=BLUE, edgecolor='white', lw=1.5, zorder=3)
        col = BLUE
    elif style == 'lowdata':
        ax.scatter(v, e, s=150, facecolor='white', edgecolor=BLUE, lw=2, zorder=3)
        col = BLUE
    elif style == 'defunct':
        ax.scatter(v, e, s=150, color='#9e9e9e', edgecolor='white', lw=1.5, zorder=3)
        col = '#7a7a7a'
    else:  # us
        ax.scatter(v, e, s=330, marker='*', facecolor='white', edgecolor='#d9531e', lw=2, zorder=3)
        col = '#d9531e'
    ax.text(v + dx, e + dy, name, color=col, fontsize=11.5, va='center',
            ha='left' if side == 'right' else 'right', fontweight='bold' if style == 'us' else 'normal')
ax.set_xlabel('COMPLETENESS OF VISION  →', fontsize=11, color='#444', loc='left', labelpad=8)
ax.set_ylabel('ABILITY TO EXECUTE  →', fontsize=11, color='#444', loc='bottom', labelpad=8)
ax.set_title('Restroom-Cleaning Robotics: Competitive Quadrant\n(Ubanthu internal analysis, as of Oct 2026)', fontsize=14, loc='left', pad=14)
fig.text(0.13, 0.035, '●  filled = scored from evidence   ○  hollow = thin evidence (low confidence)   ● grey = defunct   ☆ = Ubanthu placeholder',
         fontsize=8.2, color='#555')
fig.text(0.13, 0.015, 'Scores are [INF] judgements on a 0-10 scale; rubric + rationale in COMPETITOR_INTELLIGENCE.md. Not a Gartner product.',
         fontsize=8.2, color='#555')
plt.subplots_adjust(left=0.1, right=0.97, top=0.9, bottom=0.1)
for ext in ('svg', 'png'):
    fig.savefig(os.path.join(HERE, 'competitive-quadrant.' + ext), facecolor='white')
print('saved')
