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
    # style: 'same'  = filled: same problem AND same robot type (mobile manipulator for restrooms)
    #        'diff'  = hollow: same problem, different robot type (fixed / semi-autonomous / arm not confirmed)
    #        'defunct' = grey filled, 'us' = orange filled
    ('Hivebotics',          7.8, 7.6, 'same',    0.18, 0.00, 'right'),
    ('Loki Robotics',       7.2, 5.4, 'same',    0.18, 0.00, 'right'),
    ('Somatic',             6.3, 6.0, 'same',    0.18, 0.00, 'right'),
    ('Wangchao / Octopus',  6.8, 4.7, 'same',    0.18, 0.00, 'right'),
    ('Primech AI',          6.0, 4.1, 'same',    0.18, -0.05, 'right'),
    ('Peanut (defunct)',    5.7, 3.2, 'defunct', 0.18, 0.00, 'right'),
    ('Fonda + A*STAR ALAC', 5.3, 2.9, 'same',    0.18, 0.00, 'right'),
    ('Eternia TCR-H',       4.6, 3.6, 'diff',   -0.18, 0.00, 'left'),
    ('ZeeqClean',           4.4, 2.8, 'diff',   -0.18, 0.00, 'left'),
    ('Senxeed WUUMIE',      3.9, 2.3, 'same',   -0.18, 0.00, 'left'),
    ('Amrita Sudha',        4.8, 1.3, 'same',   -0.18, 0.00, 'left'),
    ('Sketch Robotics',     5.6, 0.9, 'same',    0.18, 0.00, 'right'),
    ('Ubanthu',             6.6, 2.4, 'us',      0.20, 0.00, 'right'),
]

BLUE = '#2f6f9f'
fig, ax = plt.subplots(figsize=(9.6, 10.2), dpi=110)
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
    if style == 'same':
        ax.scatter(v, e, s=200, color=BLUE, edgecolor='white', lw=1.5, zorder=3); col = BLUE
    elif style == 'diff':
        ax.scatter(v, e, s=180, facecolor='white', edgecolor=BLUE, lw=2.2, zorder=3); col = BLUE
    elif style == 'defunct':
        ax.scatter(v, e, s=180, color='#9e9e9e', edgecolor='white', lw=1.5, zorder=3); col = '#7a7a7a'
    else:  # us
        ax.scatter(v, e, s=260, color='#e8641b', edgecolor='white', lw=1.5, zorder=4); col = '#e8641b'
    ax.text(v + dx, e + dy, name, color=col, fontsize=12.5, va='center',
            ha='left' if side == 'right' else 'right', fontweight='bold' if style == 'us' else 'normal')
ax.set_xlabel('COMPLETENESS OF VISION  →', fontsize=11, color='#444', loc='left', labelpad=8)
ax.set_ylabel('ABILITY TO EXECUTE  →', fontsize=11, color='#444', loc='bottom', labelpad=8)
ax.set_title('Restroom-Cleaning Robotics: Competitive Quadrant\n(Ubanthu internal analysis, as of Oct 2026)', fontsize=14, loc='left', pad=14)
fig.text(0.1, 0.05, '●  filled = same problem, same robot type (restroom mobile manipulator)      ○  hollow = same problem, different robot type',
         fontsize=9, color='#555')
fig.text(0.1, 0.032, '●  grey = defunct      ', fontsize=9, color='#7a7a7a')
fig.text(0.24, 0.032, '●  orange = Ubanthu', fontsize=9, color='#e8641b')
fig.text(0.1, 0.012, 'Scores are [INF] judgements on a 0-10 scale; rubric + rationale in COMPETITOR_INTELLIGENCE.md. Not a Gartner product.',
         fontsize=9, color='#555')
plt.subplots_adjust(left=0.1, right=0.97, top=0.9, bottom=0.11)
for ext in ('svg', 'png'):
    fig.savefig(os.path.join(HERE, 'competitive-quadrant.' + ext), facecolor='white')
print('saved')
